# Phase 1 STEPS - Prompt:


                    Analyze the attached Phase 1 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-1.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 1 CONTEXT MARKDOWN ---
                    ## PHASE 1 CONTEXT BLUEPRINT: test‑ai‑architecture  

#### 1. Phase Operational Scope & Objectives  

| Objective | Description | Success Metric |
|-----------|-------------|----------------|
| **Validate Core Business Assumptions** | Confirm that the QR‑attendance flow, multi‑center data model, and omni‑channel notification pipeline can be realized with the chosen stack (Quarkus, Kafka, PostgreSQL, GKE). | PoC records a single attendance per learner per day, decrements remaining membership days, and enqueues a notification message. |
| **Define Bounded‑Contexts & Domain Model** | Produce a Context‑Map (Domain‑Driven Design) that isolates **Learner**, **Center**, **Attendance**, **Membership**, **Notification**, and **Auth** contexts. | Reviewed diagram approved by Manager & Reviewer. |
| **Prototype Critical Path** | Build a minimal end‑to‑end prototype: <br>1. **Auth** (email + password) → JWT <br>2. **QR Scan** (simulated HTTP call) → **Attendance Service** writes to PostgreSQL and publishes to Kafka <br>3. **Notification Service** consumes Kafka, calls a stub Zalo API and a mock FCM endpoint. | Automated integration test passes: attendance persisted once per day, membership days decremented, notification payload emitted. |
| **Establish Security & Compliance Foundations** | Demonstrate TLS everywhere, secret‑less configuration (Secret Manager), and basic OPA policy for API gateway. | No plaintext secrets in repo; `curl -k https://...` succeeds with valid cert; OPA gate denies unauthenticated request. |
| **Set Up CI/CD Skeleton** | GitHub Actions workflow that builds a **Quarkus** native image (optional GraalVM), runs unit tests, builds a Docker image, scans with Trivy, and pushes to Artifact Registry. | Workflow passes on every push to `main`. |
| **Document Architecture Decisions** | ADRs for **Event Streaming**, **Multi‑Tenant DB**, **i18n detection**, and **Container Image Strategy**. | ADRs stored in `docs/adr/` and linked from the README. |

> **Gate‑Go/No‑Go** – At the end of Phase 1 the Manager, Reviewer, and Tester jointly sign‑off if **all** success metrics are met and the Global Guardrails (Section 2 of the Global Context) are satisfied.

---

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)  

| Layer | Allowed Repository Path | Example Files | Public API Endpoints (prototype) |
|------|--------------------------|---------------|-----------------------------------|
| **Auth Service** | `services/auth/` | `src/main/java/.../AuthResource.java`, `src/main/resources/application.yml` | `POST /api/v1/auth/login` (email/password) <br> `POST /api/v1/auth/firebase` (token exchange) |
| **Attendance Service** | `services/attendance/` | `AttendanceResource.java`, `AttendanceProcessor.java`, `src/main/resources/application.yml` | `POST /api/v1/attendance/scan` (payload: `{ learnerId, qrCode, timestamp }`) |
| **Notification Service** | `services/notification/` | `NotificationConsumer.java`, `ZaloClientStub.java`, `FCMClientStub.java` | **No public HTTP** – consumes Kafka topic `attendance.events`. |
| **Domain Model (shared)** | `libs/domain/` | `Learner.java`, `Center.java`, `Membership.java`, `Attendance.java` | – |
| **Infrastructure as Code** | `infra/helm/` | `auth/values.yaml`, `attendance/values.yaml`, `notification/values.yaml` | – |
| **CI/CD** | `.github/workflows/` | `ci-build.yml`, `ci-security.yml` | – |
| **Documentation & ADRs** | `docs/` | `adr/001-event-streaming.md`, `architecture-overview.md` | – |
| **Mock External APIs** | `mocks/` | `zalo-mock/`, `fcm-mock/` (simple Express servers) | `POST /mock/zalo/send` <br> `POST /mock/fcm/push` |

**Endpoint Security** – All HTTP endpoints must require a valid **Bearer JWT** signed by the Auth Service’s private key. The JWT must contain a `role` claim (`ADMIN`, `STAFF`, `LEARNER`).  

**Network Boundaries** –  
* Services run in the same GKE namespace `phase1‑sandbox`.  
* Kafka broker reachable only via internal ClusterIP service `kafka-svc`.  
* Mock APIs exposed via `NodePort` **only** on the CI runner network (not internet‑facing).  

**File‑level Guardrails** –  
* No `.env` or secret files committed.  
* All configuration values that are secrets must be referenced via `${SM://path/to/secret}` (Secret Manager placeholder).  

---

#### 3. Dedicated Sub‑Agent Functional Directives  

| Sub‑Agent | Concrete Tasks for Phase 1 | Deliverables (artifact path) | Acceptance Criteria |
|-----------|----------------------------|------------------------------|---------------------|
| **Coder** | 1. Scaffold Quarkus Maven modules for `auth`, `attendance`, `notification`. <br>2. Implement JWT generation & verification (Auth). <br>3. Create PostgreSQL schema (Flyway scripts) for `learners`, `centers`, `memberships`, `attendance_logs`. <br>4. Wire Attendance Service to publish `AttendanceRecorded` events to Kafka. <br>5. Build Dockerfiles (multi‑stage, non‑root user) for each service. | `services/auth/`, `services/attendance/`, `services/notification/`, `infra/helm/`, `db/migrations/V1__init.sql` | Unit tests ≥ 80 % coverage; Docker images build locally without errors; `docker run` starts and health‑checks succeed. |
| **Tester** | 1. Write JUnit tests for Auth login flow and Attendance idempotency. <br>2. Create Postman collection for the three public endpoints. <br>3. Develop an integration test (using Testcontainers) that spins up PostgreSQL + Kafka, runs a full scan → attendance → notification flow. <br>4. Execute OWASP Dependency‑Check on the Maven dependencies. | `services/**/src/test/java/`, `test/postman/attendance.postman_collection.json` | All tests pass on CI; integration test asserts exactly one `attendance_logs` row per learner per day; Dependency‑Check reports no CVE > 7.0. |
| **Reviewer** | 1. Validate that all Dockerfiles use a minimal base (e.g., `gcr.io/distroless/java17`). <br>2. Ensure OpenAPI spec (`openapi.yaml`) matches implemented endpoints and includes JWT security scheme. <br>3. Verify OPA policy file (`policy/auth.rego`) denies requests without `Authorization` header. <br>4. Review ADRs for completeness and rationale. | `docs/openapi.yaml`, `policy/auth.rego`, `docs/adr/` | No critical style violations; OPA policy passes `opa eval` test suite; ADRs signed off in PR comments. |
| **DevOps (Docker / Deployer)** | 1. Configure GitHub Actions workflow `ci-build.yml` to: <br>   - Run `mvn clean verify` <br>   - Build native image (optional) <br>   - Build Docker image, tag with `${{ github.sha }}` <br>   - Scan with Trivy, fail on HIGH+ vulnerabilities <br>   - Push to Artifact Registry `asia-south1-docker.pkg.dev/<project>/phase1-sandbox/<service>` <br>2. Create a minimal Helm chart (`infra/helm/attendance/Chart.yaml`) with values for image repository, replicaCount=1, resource limits. <br>3. Deploy the three services to a **GKE Autopilot** cluster in a temporary `phase1‑sandbox` namespace using `helm upgrade --install`. <br>4. Set up a basic Prometheus scrape config for the services (via ServiceMonitor). | `.github/workflows/ci-build.yml`, `infra/helm/attendance/`, `k8s/monitoring/prometheus.yaml` | CI pipeline passes on every push; Helm release reports `STATUS: deployed`; Pods run as non‑root; Prometheus metrics endpoint returns 200. |
| **Security (optional sub‑agent)** | 1. Generate self‑signed TLS certs for local dev and store them in Secret Manager placeholders. <br>2. Add `Istio` sidecar injection annotation to the namespace (for later phases). | `infra/istio/namespace.yaml` | `kubectl get namespace phase1-sandbox -o yaml` shows `istio-injection: enabled`. |

*All sub‑agents must log their daily progress in the shared Confluence page `Phase 1 – Discovery & Architecture Validation` and update the Kanban board in Jira (Epic **PH1‑DISCOVERY**).*

---

#### 4. Phase Definition of Done (DoD)  

The Phase 1 increment is considered **Done** when **all** of the following conditions are satisfied:

1. **Functional PoC**  
   * A learner can authenticate via email/password and receive a signed JWT.  
   * A QR‑scan request (POST `/api/v1/attendance/scan`) creates **exactly one** attendance record for the day, decrements the learner’s `remaining_days`, and publishes an `AttendanceRecorded` event to Kafka.  
   * The Notification Service consumes the event and successfully calls both mock Zalo and mock FCM endpoints (verified by logs).  

2. **Architecture Artefacts**  
   * Context‑Map diagram (`docs/architecture/context-map.png`).  
   * ADRs for Event Streaming, Multi‑Tenant DB, i18n detection, and Container Image Strategy stored under `docs/adr/`.  

3. **Code Quality & Security**  
   * Unit test coverage ≥ 80 % for new code.  
   * No **critical** or **high** vulnerabilities reported by Trivy or OWASP Dependency‑Check.  
   * All secrets referenced via Secret Manager placeholders; no plaintext secrets in repo.  

4. **CI/CD Pipeline**  
   * GitHub Actions workflow `ci-build.yml` runs on every push to `main` and completes all stages (build, test, scan, push).  
   * Docker images are published to Artifact Registry with immutable digests.  

5. **Infrastructure Deployment**  
   * Helm releases for `auth`, `attendance`, and `notification` are deployed to GKE `phase1‑sandbox` namespace and report `READY` status.  
   * Pods run as non‑root, use the minimal Distroless base image, and expose health‑check endpoints (`/q/health`).  

6. **Observability & Logging**  
   * Prometheus scrapes `/metrics` from each service; a Grafana dashboard (`docs/grafana/phase1-dashboard.json`) shows request latency and error rate.  
   * All request/response logs are shipped to Cloud Logging with appropriate labels (`service=attendance`).  

7. **Compliance Gate**  
   * Reviewer signs off that the implementation adheres to every Guardrail in **Section 2 – Global Guardrails & Enterprise Compliance Standards** (data encryption, RBAC, audit logging, etc.).  

8. **Stakeholder Sign‑off**  
   * Manager, Reviewer, and Tester collectively approve the Phase 1 deliverables in Jira (transition to **Done**).  

Once the above DoD checklist is fully satisfied, the team may proceed to **Phase 2 – Core Platform Build (MVP)**.
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 429 - {'error': {'message': 'Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx7x6rbpftmr50sr2yyb78qm` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 94647, Requested 7733. Please try again in 34m16.32s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
```

# Global Prompt:


        Analyze the attached project requirements. Build the GLOBAL PROJECT CONTEXT for 'test-ai-architecture'.
        
        --- RAW REQUIREMENTS ---
        ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

        --- END REQUIREMENTS ---
            
        ## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
        #### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
        #### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

        Your output MUST follow this exact structure:
        ## GLOBAL PROJECT CONTEXT: test-ai-architecture
        #### 1. Executive Summary & Tech Stack Blueprint
        #### 2. Global Guardrails & Enterprise Compliance Standards
        #### 3. Standardized Sub-Agent Persona Definitions (Manager, Coder, Tester, Reviewer, Docker, Deployer)
        #### 4. Multi-Phase Segmentation Strategy Overview (Plan exactly 5 phases)
        

# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a web and mobile application designed to manage students and their attendance for multiple training centers. The tech stack consists of Quarkus, Kafka, Postgres, and Docker, with deployment on Google Cloud Platform (GCP) and Google Kubernetes Engine (GKE). The application will support internal authentication via email and password, as well as external authentication through Firebase, Google, and Facebook. The mobile app will be built using Next.js, supporting multiple languages and platforms (iOS and Android). The project also includes SEO optimization for both web and mobile applications.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to industry standards, the following guardrails and compliance standards will be implemented:
- **Security**: Implement robust security measures to protect user data, including encryption, secure authentication, and access controls.
- **Scalability**: Design the application to scale horizontally and vertically to handle increased traffic and user growth.
- **Compliance**: Adhere to relevant regulations, such as GDPR, CCPA, and data protection laws, to ensure user data privacy and security.
- **Quality**: Establish a rigorous testing and quality assurance process to ensure the application meets the required standards.
- **Communication**: Foster open and transparent communication among team members, stakeholders, and users to ensure clear expectations and timely issue resolution.

#### 3. Standardized Sub-Agent Persona Definitions
The following sub-agent personas will be defined to ensure clear roles and responsibilities:
- **Manager**: Oversees the project, sets goals, and allocates resources.
- **Coder**: Develops the application's backend and frontend components.
- **Tester**: Conducts thorough testing and quality assurance of the application.
- **Reviewer**: Reviews code, provides feedback, and ensures adherence to coding standards.
- **Docker**: Responsible for containerization and deployment of the application.
- **Deployer**: Deploys the application to GCP and GKE, ensuring smooth and efficient deployment.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases, each with a maximum duration of 7 days:
- **Phase 1: Planning and Design (Days 1-3)**: Define project scope, create a detailed design document, and establish a project timeline.
- **Phase 2: Backend Development (Days 4-7)**: Develop the backend components using Quarkus, Kafka, and Postgres.
- **Phase 3: Frontend Development (Days 8-14)**: Develop the frontend components using Next.js and implement authentication and authorization.
- **Phase 4: Testing and Quality Assurance (Days 15-21)**: Conduct thorough testing, quality assurance, and debugging of the application.
- **Phase 5: Deployment and Launch (Days 22-28)**: Deploy the application to GCP and GKE, configure SEO, and launch the application.
```

# Phase 1 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 1 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a web and mobile application designed to manage students and their attendance for multiple training centers. The tech stack consists of Quarkus, Kafka, Postgres, and Docker, with deployment on Google Cloud Platform (GCP) and Google Kubernetes Engine (GKE). The application will support internal authentication via email and password, as well as external authentication through Firebase, Google, and Facebook. The mobile app will be built using Next.js, supporting multiple languages and platforms (iOS and Android). The project also includes SEO optimization for both web and mobile applications.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to industry standards, the following guardrails and compliance standards will be implemented:
- **Security**: Implement robust security measures to protect user data, including encryption, secure authentication, and access controls.
- **Scalability**: Design the application to scale horizontally and vertically to handle increased traffic and user growth.
- **Compliance**: Adhere to relevant regulations, such as GDPR, CCPA, and data protection laws, to ensure user data privacy and security.
- **Quality**: Establish a rigorous testing and quality assurance process to ensure the application meets the required standards.
- **Communication**: Foster open and transparent communication among team members, stakeholders, and users to ensure clear expectations and timely issue resolution.

#### 3. Standardized Sub-Agent Persona Definitions
The following sub-agent personas will be defined to ensure clear roles and responsibilities:
- **Manager**: Oversees the project, sets goals, and allocates resources.
- **Coder**: Develops the application's backend and frontend components.
- **Tester**: Conducts thorough testing and quality assurance of the application.
- **Reviewer**: Reviews code, provides feedback, and ensures adherence to coding standards.
- **Docker**: Responsible for containerization and deployment of the application.
- **Deployer**: Deploys the application to GCP and GKE, ensuring smooth and efficient deployment.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases, each with a maximum duration of 7 days:
- **Phase 1: Planning and Design (Days 1-3)**: Define project scope, create a detailed design document, and establish a project timeline.
- **Phase 2: Backend Development (Days 4-7)**: Develop the backend components using Quarkus, Kafka, and Postgres.
- **Phase 3: Frontend Development (Days 8-14)**: Develop the frontend components using Next.js and implement authentication and authorization.
- **Phase 4: Testing and Quality Assurance (Days 15-21)**: Conduct thorough testing, quality assurance, and debugging of the application.
- **Phase 5: Deployment and Launch (Days 22-28)**: Deploy the application to GCP and GKE, configure SEO, and launch the application.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------
            
            ## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
            #### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
            #### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

            Your output MUST follow this exact Markdown structure for Phase 1:
            ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed design document, and establish a project timeline. This phase will focus on planning and design, ensuring that all stakeholders are aligned and that the project is set up for success. The key deliverables for this phase include:
- A detailed project scope statement
- A high-level architecture design document
- A project timeline with milestones and deadlines
- A definition of the technical requirements and dependencies

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
For Phase 1, the technical scope will be limited to the following areas:
- Project scope statement: `docs/project_scope.md`
- High-level architecture design document: `docs/architecture.md`
- Project timeline: `docs/timeline.md`
- Technical requirements and dependencies: `docs/technical_requirements.md`
The following directories and files will be created:
- `docs/`: directory for project documentation
- `docs/project_scope.md`: project scope statement
- `docs/architecture.md`: high-level architecture design document
- `docs/timeline.md`: project timeline
- `docs/technical_requirements.md`: technical requirements and dependencies

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 1:
- **Manager**: Oversees the project, sets goals, and allocates resources. Tasks:
  - Define project scope and objectives
  - Establish project timeline and milestones
- **Coder**: Develops the application's backend and frontend components. Tasks:
  - Review technical requirements and dependencies
  - Provide input on high-level architecture design
- **Tester**: Conducts thorough testing and quality assurance of the application. Tasks:
  - Review project scope and technical requirements
  - Identify potential testing scenarios and edge cases
- **Reviewer**: Reviews code, provides feedback, and ensures adherence to coding standards. Tasks:
  - Review project scope and technical requirements
  - Provide feedback on high-level architecture design
- **DevOps**: Responsible for containerization and deployment of the application. Tasks:
  - Review technical requirements and dependencies
  - Provide input on deployment strategy

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- A detailed project scope statement has been created and approved by all stakeholders
- A high-level architecture design document has been created and reviewed by the team
- A project timeline with milestones and deadlines has been established and approved by all stakeholders
- Technical requirements and dependencies have been documented and reviewed by the team
Once these criteria are met, Phase 1 will be considered complete, and the project will proceed to Phase 2.
```

# Phase 2 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 2 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a web and mobile application designed to manage students and their attendance for multiple training centers. The tech stack consists of Quarkus, Kafka, Postgres, and Docker, with deployment on Google Cloud Platform (GCP) and Google Kubernetes Engine (GKE). The application will support internal authentication via email and password, as well as external authentication through Firebase, Google, and Facebook. The mobile app will be built using Next.js, supporting multiple languages and platforms (iOS and Android). The project also includes SEO optimization for both web and mobile applications.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to industry standards, the following guardrails and compliance standards will be implemented:
- **Security**: Implement robust security measures to protect user data, including encryption, secure authentication, and access controls.
- **Scalability**: Design the application to scale horizontally and vertically to handle increased traffic and user growth.
- **Compliance**: Adhere to relevant regulations, such as GDPR, CCPA, and data protection laws, to ensure user data privacy and security.
- **Quality**: Establish a rigorous testing and quality assurance process to ensure the application meets the required standards.
- **Communication**: Foster open and transparent communication among team members, stakeholders, and users to ensure clear expectations and timely issue resolution.

#### 3. Standardized Sub-Agent Persona Definitions
The following sub-agent personas will be defined to ensure clear roles and responsibilities:
- **Manager**: Oversees the project, sets goals, and allocates resources.
- **Coder**: Develops the application's backend and frontend components.
- **Tester**: Conducts thorough testing and quality assurance of the application.
- **Reviewer**: Reviews code, provides feedback, and ensures adherence to coding standards.
- **Docker**: Responsible for containerization and deployment of the application.
- **Deployer**: Deploys the application to GCP and GKE, ensuring smooth and efficient deployment.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases, each with a maximum duration of 7 days:
- **Phase 1: Planning and Design (Days 1-3)**: Define project scope, create a detailed design document, and establish a project timeline.
- **Phase 2: Backend Development (Days 4-7)**: Develop the backend components using Quarkus, Kafka, and Postgres.
- **Phase 3: Frontend Development (Days 8-14)**: Develop the frontend components using Next.js and implement authentication and authorization.
- **Phase 4: Testing and Quality Assurance (Days 15-21)**: Conduct thorough testing, quality assurance, and debugging of the application.
- **Phase 5: Deployment and Launch (Days 22-28)**: Deploy the application to GCP and GKE, configure SEO, and launch the application.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------
            
            ## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
            #### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
            #### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

            Your output MUST follow this exact Markdown structure for Phase 2:
            ## PHASE 2 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 2 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 2 is to develop the backend components of the membership-hub project using Quarkus, Kafka, and Postgres. This phase will focus on designing and implementing the core backend functionality, including user management, attendance tracking, and notification systems. The key deliverables for this phase include:

* Design and implementation of the backend API using Quarkus
* Integration with Kafka for message queuing and Postgres for database management
* Development of user management and authentication systems
* Implementation of attendance tracking and notification systems

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 2 will be limited to the backend components of the project. The following directories, files, and endpoints are in scope:

* `src/main/java`: Java source code for the backend API
* `src/main/resources`: Configuration files and resources for the backend API
* `pom.xml`: Maven project file for building and managing dependencies
* `/api/users`: Endpoint for user management
* `/api/attendance`: Endpoint for attendance tracking
* `/api/notifications`: Endpoint for notification systems

The following technologies and frameworks are in scope:

* Quarkus
* Kafka
* Postgres
* Java 11

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be responsible for the following tasks during Phase 2:

* **Coder**: Develop the backend API using Quarkus, integrate with Kafka and Postgres, and implement user management and authentication systems.
* **Tester**: Develop unit tests and integration tests for the backend API, focusing on user management, attendance tracking, and notification systems.
* **Reviewer**: Review the code developed by the Coder, ensuring adherence to coding standards, best practices, and security guidelines.
* **DevOps**: Configure the development environment, set up the build and deployment pipeline, and ensure that the backend API is properly containerized using Docker.

#### 4. Phase Definition of Done (DoD)
Phase 2 will be considered complete when the following criteria are met:

* The backend API is fully implemented and functional
* Unit tests and integration tests are developed and passing
* Code reviews are complete, and all feedback is addressed
* The backend API is properly containerized using Docker
* The development environment is configured, and the build and deployment pipeline is set up

Once these criteria are met, Phase 2 will be considered complete, and the project will proceed to Phase 3.
```

# Phase 3 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 3 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a web and mobile application designed to manage students and their attendance for multiple training centers. The tech stack consists of Quarkus, Kafka, Postgres, and Docker, with deployment on Google Cloud Platform (GCP) and Google Kubernetes Engine (GKE). The application will support internal authentication via email and password, as well as external authentication through Firebase, Google, and Facebook. The mobile app will be built using Next.js, supporting multiple languages and platforms (iOS and Android). The project also includes SEO optimization for both web and mobile applications.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to industry standards, the following guardrails and compliance standards will be implemented:
- **Security**: Implement robust security measures to protect user data, including encryption, secure authentication, and access controls.
- **Scalability**: Design the application to scale horizontally and vertically to handle increased traffic and user growth.
- **Compliance**: Adhere to relevant regulations, such as GDPR, CCPA, and data protection laws, to ensure user data privacy and security.
- **Quality**: Establish a rigorous testing and quality assurance process to ensure the application meets the required standards.
- **Communication**: Foster open and transparent communication among team members, stakeholders, and users to ensure clear expectations and timely issue resolution.

#### 3. Standardized Sub-Agent Persona Definitions
The following sub-agent personas will be defined to ensure clear roles and responsibilities:
- **Manager**: Oversees the project, sets goals, and allocates resources.
- **Coder**: Develops the application's backend and frontend components.
- **Tester**: Conducts thorough testing and quality assurance of the application.
- **Reviewer**: Reviews code, provides feedback, and ensures adherence to coding standards.
- **Docker**: Responsible for containerization and deployment of the application.
- **Deployer**: Deploys the application to GCP and GKE, ensuring smooth and efficient deployment.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases, each with a maximum duration of 7 days:
- **Phase 1: Planning and Design (Days 1-3)**: Define project scope, create a detailed design document, and establish a project timeline.
- **Phase 2: Backend Development (Days 4-7)**: Develop the backend components using Quarkus, Kafka, and Postgres.
- **Phase 3: Frontend Development (Days 8-14)**: Develop the frontend components using Next.js and implement authentication and authorization.
- **Phase 4: Testing and Quality Assurance (Days 15-21)**: Conduct thorough testing, quality assurance, and debugging of the application.
- **Phase 5: Deployment and Launch (Days 22-28)**: Deploy the application to GCP and GKE, configure SEO, and launch the application.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------
            
            ## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
            #### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
            #### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

            Your output MUST follow this exact Markdown structure for Phase 3:
            ## PHASE 3 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 3 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 3 is to develop the frontend components of the membership-hub project using Next.js. This phase will focus on implementing authentication and authorization, building the user interface, and integrating the frontend with the backend components developed in Phase 2. The key deliverables for this phase include:
- A fully functional frontend application with user authentication and authorization
- Integration with the backend API for data exchange
- A responsive and user-friendly interface for both web and mobile platforms
- Support for multiple languages and locales

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 3 will be limited to the frontend components of the project. The following directories, files, and endpoints are in scope:
- `frontend/`: The root directory for the frontend application
- `pages/`: Directory for page components
- `components/`: Directory for reusable UI components
- `api/`: Directory for API endpoints (only for frontend-specific API calls)
- `public/`: Directory for static assets
- `next.config.js`: Configuration file for Next.js
- `package.json`: Dependency management file for the frontend application
- Endpoints for authentication and authorization (e.g., `/login`, `/register`, `/forgot-password`)
- Endpoints for data exchange with the backend API (e.g., `/api/users`, `/api/courses`)

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following tasks are assigned to each sub-agent:
- **Coder**:
  - Develop the frontend application using Next.js
  - Implement authentication and authorization
  - Build the user interface and integrate with the backend API
  - Implement support for multiple languages and locales
- **Tester**:
  - Develop unit tests and integration tests for the frontend application
  - Test the application for responsiveness and usability
  - Test the authentication and authorization functionality
- **Reviewer**:
  - Review the code for quality, readability, and adherence to coding standards
  - Review the application for usability and user experience
  - Provide feedback on the implementation of authentication and authorization
- **DevOps**:
  - Configure the build and deployment process for the frontend application
  - Ensure the application is properly containerized and deployed to GCP and GKE
  - Monitor the application for performance and scalability issues

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 3 is as follows:
- The frontend application is fully functional and integrated with the backend API
- Authentication and authorization are implemented and tested
- The application is responsive and user-friendly on both web and mobile platforms
- Support for multiple languages and locales is implemented
- Unit tests and integration tests are developed and passing
- Code reviews are complete, and feedback is incorporated
- The application is properly containerized and deployed to GCP and GKE
- Performance and scalability testing is complete, and issues are addressed
```

# Phase 4 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 4 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a web and mobile application designed to manage students and their attendance for multiple training centers. The tech stack consists of Quarkus, Kafka, Postgres, and Docker, with deployment on Google Cloud Platform (GCP) and Google Kubernetes Engine (GKE). The application will support internal authentication via email and password, as well as external authentication through Firebase, Google, and Facebook. The mobile app will be built using Next.js, supporting multiple languages and platforms (iOS and Android). The project also includes SEO optimization for both web and mobile applications.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to industry standards, the following guardrails and compliance standards will be implemented:
- **Security**: Implement robust security measures to protect user data, including encryption, secure authentication, and access controls.
- **Scalability**: Design the application to scale horizontally and vertically to handle increased traffic and user growth.
- **Compliance**: Adhere to relevant regulations, such as GDPR, CCPA, and data protection laws, to ensure user data privacy and security.
- **Quality**: Establish a rigorous testing and quality assurance process to ensure the application meets the required standards.
- **Communication**: Foster open and transparent communication among team members, stakeholders, and users to ensure clear expectations and timely issue resolution.

#### 3. Standardized Sub-Agent Persona Definitions
The following sub-agent personas will be defined to ensure clear roles and responsibilities:
- **Manager**: Oversees the project, sets goals, and allocates resources.
- **Coder**: Develops the application's backend and frontend components.
- **Tester**: Conducts thorough testing and quality assurance of the application.
- **Reviewer**: Reviews code, provides feedback, and ensures adherence to coding standards.
- **Docker**: Responsible for containerization and deployment of the application.
- **Deployer**: Deploys the application to GCP and GKE, ensuring smooth and efficient deployment.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases, each with a maximum duration of 7 days:
- **Phase 1: Planning and Design (Days 1-3)**: Define project scope, create a detailed design document, and establish a project timeline.
- **Phase 2: Backend Development (Days 4-7)**: Develop the backend components using Quarkus, Kafka, and Postgres.
- **Phase 3: Frontend Development (Days 8-14)**: Develop the frontend components using Next.js and implement authentication and authorization.
- **Phase 4: Testing and Quality Assurance (Days 15-21)**: Conduct thorough testing, quality assurance, and debugging of the application.
- **Phase 5: Deployment and Launch (Days 22-28)**: Deploy the application to GCP and GKE, configure SEO, and launch the application.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------
            
            ## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
            #### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
            #### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

            Your output MUST follow this exact Markdown structure for Phase 4:
            ## PHASE 4 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 4 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 4 is to conduct thorough testing and quality assurance of the application, ensuring that it meets the required standards and is free from defects. This phase will focus on identifying and fixing bugs, validating user stories, and verifying that the application functions as expected. The scope of this phase includes:

* Unit testing and integration testing of backend and frontend components
* System testing and end-to-end testing of the entire application
* Validation of user stories and acceptance criteria
* Identification and fixing of bugs and defects
* Performance testing and optimization

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope of this phase includes:

* Backend: Quarkus, Kafka, Postgres
* Frontend: Next.js
* Testing frameworks: JUnit, Jest, Cypress
* Testing tools: Postman, Selenium
* Directory boundaries:
	+ Backend: `src/main/java`, `src/main/resources`
	+ Frontend: `src/components`, `src/pages`
	+ Testing: `src/test/java`, `src/test/javascript`

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in this phase:

* **Coder**: Responsible for fixing bugs and defects identified during testing
* **Tester**: Conducts unit testing, integration testing, system testing, and end-to-end testing of the application
* **Reviewer**: Reviews test cases and test results to ensure that they meet the required standards
* **DevOps**: Responsible for setting up and configuring testing environments, including Docker and Kubernetes

Specific tasks for each sub-agent:

* Coder:
	+ Fix bugs and defects identified during testing
	+ Implement fixes and verify that they resolve the issues
* Tester:
	+ Conduct unit testing and integration testing of backend and frontend components
	+ Conduct system testing and end-to-end testing of the entire application
	+ Validate user stories and acceptance criteria
* Reviewer:
	+ Review test cases and test results to ensure that they meet the required standards
	+ Verify that testing covers all required scenarios and edge cases
* DevOps:
	+ Set up and configure testing environments, including Docker and Kubernetes
	+ Ensure that testing environments are stable and reliable

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 4 is:

* All unit tests, integration tests, system tests, and end-to-end tests have been executed and passed
* All identified bugs and defects have been fixed and verified
* The application has been validated against all user stories and acceptance criteria
* The application has been performance-tested and optimized
* All test results have been reviewed and verified by the Reviewer
* The testing environments have been set up and configured by DevOps

Once these criteria are met, Phase 4 is considered complete, and the project can proceed to Phase 5: Deployment and Launch.
```

# Phase 5 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 5 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a web and mobile application designed to manage students and their attendance for multiple training centers. The tech stack consists of Quarkus, Kafka, Postgres, and Docker, with deployment on Google Cloud Platform (GCP) and Google Kubernetes Engine (GKE). The application will support internal authentication via email and password, as well as external authentication through Firebase, Google, and Facebook. The mobile app will be built using Next.js, supporting multiple languages and platforms (iOS and Android). The project also includes SEO optimization for both web and mobile applications.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to industry standards, the following guardrails and compliance standards will be implemented:
- **Security**: Implement robust security measures to protect user data, including encryption, secure authentication, and access controls.
- **Scalability**: Design the application to scale horizontally and vertically to handle increased traffic and user growth.
- **Compliance**: Adhere to relevant regulations, such as GDPR, CCPA, and data protection laws, to ensure user data privacy and security.
- **Quality**: Establish a rigorous testing and quality assurance process to ensure the application meets the required standards.
- **Communication**: Foster open and transparent communication among team members, stakeholders, and users to ensure clear expectations and timely issue resolution.

#### 3. Standardized Sub-Agent Persona Definitions
The following sub-agent personas will be defined to ensure clear roles and responsibilities:
- **Manager**: Oversees the project, sets goals, and allocates resources.
- **Coder**: Develops the application's backend and frontend components.
- **Tester**: Conducts thorough testing and quality assurance of the application.
- **Reviewer**: Reviews code, provides feedback, and ensures adherence to coding standards.
- **Docker**: Responsible for containerization and deployment of the application.
- **Deployer**: Deploys the application to GCP and GKE, ensuring smooth and efficient deployment.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases, each with a maximum duration of 7 days:
- **Phase 1: Planning and Design (Days 1-3)**: Define project scope, create a detailed design document, and establish a project timeline.
- **Phase 2: Backend Development (Days 4-7)**: Develop the backend components using Quarkus, Kafka, and Postgres.
- **Phase 3: Frontend Development (Days 8-14)**: Develop the frontend components using Next.js and implement authentication and authorization.
- **Phase 4: Testing and Quality Assurance (Days 15-21)**: Conduct thorough testing, quality assurance, and debugging of the application.
- **Phase 5: Deployment and Launch (Days 22-28)**: Deploy the application to GCP and GKE, configure SEO, and launch the application.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------
            
            ## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
            #### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
            #### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

            Your output MUST follow this exact Markdown structure for Phase 5:
            ## PHASE 5 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```json
Error code: 429 - {'error': {'message': 'Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx7x6rbpftmr50sr2yyb78qm` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99997, Requested 1932. Please try again in 27m46.656s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
```

# Global Prompt:


        Analyze the attached project requirements. Build the GLOBAL PROJECT CONTEXT for 'test-ai-architecture'.
        
        --- RAW REQUIREMENTS ---
        ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

        --- END REQUIREMENTS ---
            
        ## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
        #### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
        #### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

        Your output MUST follow this exact structure:
        ## GLOBAL PROJECT CONTEXT: test-ai-architecture
        #### 1. Executive Summary & Tech Stack Blueprint
        #### 2. Global Guardrails & Enterprise Compliance Standards
        #### 3. Standardized Sub-Agent Persona Definitions (Manager, Coder, Tester, Reviewer, Docker, Deployer)
        #### 4. Multi-Phase Segmentation Strategy Overview (Plan exactly 5 phases)
        

# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a web and mobile application designed to manage students and their attendance for multiple centers. The tech stack consists of Quarkus, Kafka, Postgres, and Docker, with deployment on Google Cloud Platform (GCP) and Google Kubernetes Engine (GKE). The application will support authentication via email/password, Firebase, Google, and Facebook, and will have features such as QR code-based attendance tracking, notification systems, and multi-language support.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success, the following guardrails and compliance standards will be implemented:
- **Security**: Implement OAuth 2.0 for authentication and authorization, and ensure data encryption for sensitive information.
- **Scalability**: Design the system to scale horizontally, with load balancing and autoscaling on GKE.
- **Compliance**: Adhere to GDPR and CCPA regulations for data protection, and ensure accessibility standards (WCAG 2.1) for the web and mobile applications.
- **Quality**: Implement continuous integration and continuous deployment (CI/CD) pipelines, with automated testing and code reviews.

#### 3. Standardized Sub-Agent Persona Definitions
The following sub-agent personas will be defined:
- **Manager**: Responsible for project planning, resource allocation, and progress tracking.
- **Coder**: Responsible for developing the application's features, with expertise in Quarkus, Kafka, Postgres, and Docker.
- **Tester**: Responsible for testing the application's functionality, performance, and security.
- **Reviewer**: Responsible for reviewing code, ensuring adherence to coding standards, and providing feedback.
- **Docker**: Responsible for containerizing the application and ensuring seamless deployment on GKE.
- **Deployer**: Responsible for deploying the application on GCP and GKE, and ensuring zero-downtime deployments.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into 5 phases, each with a maximum duration of 7 days:
- **Phase 1: Planning and Setup** (Days 1-3): Define project scope, create a detailed project plan, and set up the development environment.
- **Phase 2: Backend Development** (Days 4-7): Develop the backend features, including authentication, attendance tracking, and notification systems.
- **Phase 3: Frontend Development** (Days 8-14): Develop the web and mobile applications, with features such as QR code scanning, multi-language support, and SEO optimization.
- **Phase 4: Testing and Quality Assurance** (Days 15-21): Conduct thorough testing, including unit testing, integration testing, and performance testing.
- **Phase 5: Deployment and Maintenance** (Days 22-28): Deploy the application on GCP and GKE, and ensure smooth operation, with ongoing maintenance and updates.
```

# Phase 1 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 1 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a web and mobile application designed to manage students and their attendance for multiple centers. The tech stack consists of Quarkus, Kafka, Postgres, and Docker, with deployment on Google Cloud Platform (GCP) and Google Kubernetes Engine (GKE). The application will support authentication via email/password, Firebase, Google, and Facebook, and will have features such as QR code-based attendance tracking, notification systems, and multi-language support.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success, the following guardrails and compliance standards will be implemented:
- **Security**: Implement OAuth 2.0 for authentication and authorization, and ensure data encryption for sensitive information.
- **Scalability**: Design the system to scale horizontally, with load balancing and autoscaling on GKE.
- **Compliance**: Adhere to GDPR and CCPA regulations for data protection, and ensure accessibility standards (WCAG 2.1) for the web and mobile applications.
- **Quality**: Implement continuous integration and continuous deployment (CI/CD) pipelines, with automated testing and code reviews.

#### 3. Standardized Sub-Agent Persona Definitions
The following sub-agent personas will be defined:
- **Manager**: Responsible for project planning, resource allocation, and progress tracking.
- **Coder**: Responsible for developing the application's features, with expertise in Quarkus, Kafka, Postgres, and Docker.
- **Tester**: Responsible for testing the application's functionality, performance, and security.
- **Reviewer**: Responsible for reviewing code, ensuring adherence to coding standards, and providing feedback.
- **Docker**: Responsible for containerizing the application and ensuring seamless deployment on GKE.
- **Deployer**: Responsible for deploying the application on GCP and GKE, and ensuring zero-downtime deployments.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into 5 phases, each with a maximum duration of 7 days:
- **Phase 1: Planning and Setup** (Days 1-3): Define project scope, create a detailed project plan, and set up the development environment.
- **Phase 2: Backend Development** (Days 4-7): Develop the backend features, including authentication, attendance tracking, and notification systems.
- **Phase 3: Frontend Development** (Days 8-14): Develop the web and mobile applications, with features such as QR code scanning, multi-language support, and SEO optimization.
- **Phase 4: Testing and Quality Assurance** (Days 15-21): Conduct thorough testing, including unit testing, integration testing, and performance testing.
- **Phase 5: Deployment and Maintenance** (Days 22-28): Deploy the application on GCP and GKE, and ensure smooth operation, with ongoing maintenance and updates.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------
            
            ## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
            #### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
            #### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

            Your output MUST follow this exact Markdown structure for Phase 1:
            ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed project plan, and set up the development environment. This phase will focus on planning and setup, ensuring that all necessary components are in place for the successful execution of the project. The key deliverables for this phase include:
- A detailed project plan outlining the scope, timeline, and resources required
- A setup development environment with the necessary tools and technologies (Quarkus, Kafka, Postgres, Docker)
- Definition of the project's technical architecture and high-level design

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 1 includes:
- Setting up the project directory structure
- Initializing the Git repository
- Creating a basic Quarkus project template
- Setting up Kafka and Postgres for messaging and data storage
- Configuring Docker for containerization
- Defining the API endpoints for authentication, attendance tracking, and notification systems
- Creating a high-level design document outlining the system architecture

The allowed directory boundaries include:
- `src/main/java` for Java source code
- `src/main/resources` for configuration files and resources
- `docker` for Docker configuration files
- `kafka` for Kafka configuration files
- `postgres` for Postgres configuration files

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 1:
- **Coder**: Responsible for setting up the Quarkus project template, configuring Kafka and Postgres, and defining the API endpoints.
- **Tester**: Not actively involved in this phase, but will review the project plan and technical architecture.
- **Reviewer**: Responsible for reviewing the project plan, technical architecture, and high-level design document.
- **DevOps (Docker)**: Responsible for setting up the Docker configuration and ensuring containerization.
- **Deployer**: Not actively involved in this phase, but will review the project plan and technical architecture.

#### 4. Phase Definition of Done (DoD)
Phase 1 is considered complete when:
- The project plan is finalized and approved by all stakeholders
- The development environment is set up and configured
- The Quarkus project template is created and configured
- Kafka and Postgres are set up and configured
- Docker is configured for containerization
- The high-level design document is completed and approved by all stakeholders
- The project directory structure is initialized and the Git repository is set up

The expected duration for Phase 1 is 3 days, with the following milestones:
- Day 1: Project planning and scope definition
- Day 2: Setup of development environment and Quarkus project template
- Day 3: Configuration of Kafka, Postgres, and Docker, and completion of high-level design document
```

# Phase 2 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 2 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a web and mobile application designed to manage students and their attendance for multiple centers. The tech stack consists of Quarkus, Kafka, Postgres, and Docker, with deployment on Google Cloud Platform (GCP) and Google Kubernetes Engine (GKE). The application will support authentication via email/password, Firebase, Google, and Facebook, and will have features such as QR code-based attendance tracking, notification systems, and multi-language support.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success, the following guardrails and compliance standards will be implemented:
- **Security**: Implement OAuth 2.0 for authentication and authorization, and ensure data encryption for sensitive information.
- **Scalability**: Design the system to scale horizontally, with load balancing and autoscaling on GKE.
- **Compliance**: Adhere to GDPR and CCPA regulations for data protection, and ensure accessibility standards (WCAG 2.1) for the web and mobile applications.
- **Quality**: Implement continuous integration and continuous deployment (CI/CD) pipelines, with automated testing and code reviews.

#### 3. Standardized Sub-Agent Persona Definitions
The following sub-agent personas will be defined:
- **Manager**: Responsible for project planning, resource allocation, and progress tracking.
- **Coder**: Responsible for developing the application's features, with expertise in Quarkus, Kafka, Postgres, and Docker.
- **Tester**: Responsible for testing the application's functionality, performance, and security.
- **Reviewer**: Responsible for reviewing code, ensuring adherence to coding standards, and providing feedback.
- **Docker**: Responsible for containerizing the application and ensuring seamless deployment on GKE.
- **Deployer**: Responsible for deploying the application on GCP and GKE, and ensuring zero-downtime deployments.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into 5 phases, each with a maximum duration of 7 days:
- **Phase 1: Planning and Setup** (Days 1-3): Define project scope, create a detailed project plan, and set up the development environment.
- **Phase 2: Backend Development** (Days 4-7): Develop the backend features, including authentication, attendance tracking, and notification systems.
- **Phase 3: Frontend Development** (Days 8-14): Develop the web and mobile applications, with features such as QR code scanning, multi-language support, and SEO optimization.
- **Phase 4: Testing and Quality Assurance** (Days 15-21): Conduct thorough testing, including unit testing, integration testing, and performance testing.
- **Phase 5: Deployment and Maintenance** (Days 22-28): Deploy the application on GCP and GKE, and ensure smooth operation, with ongoing maintenance and updates.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------
            
            ## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
            #### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
            #### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

            Your output MUST follow this exact Markdown structure for Phase 2:
            ## PHASE 2 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 2 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 2 is to develop the backend features of the membership-hub project, including authentication, attendance tracking, and notification systems. This phase will focus on building a scalable and secure backend using Quarkus, Kafka, and Postgres. The key deliverables for this phase include:
- Design and implementation of authentication mechanisms (email/password, Firebase, Google, Facebook)
- Development of attendance tracking features (QR code-based attendance tracking)
- Implementation of notification systems (SMS, Zalo, in-app notifications)
- Integration with Postgres database for data storage
- Containerization using Docker for seamless deployment on GKE

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 2 will be limited to the backend development, with the following directory boundaries:
- `src/main/java`: Java source code for Quarkus application
- `src/main/resources`: Configuration files and static resources
- `docker`: Dockerfile and containerization scripts
- `kafka`: Kafka configuration and topic definitions
- `postgres`: Postgres database schema and migration scripts
- `api`: API endpoints for authentication, attendance tracking, and notification systems
Allowed endpoints:
- `/api/auth`: Authentication endpoints (login, logout, register)
- `/api/attendance`: Attendance tracking endpoints (QR code scanning, attendance logging)
- `/api/notifications`: Notification endpoints (SMS, Zalo, in-app notifications)

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
- **Coder**: Implement authentication mechanisms, attendance tracking features, and notification systems. Develop API endpoints for backend features.
- **Tester**: Develop unit tests and integration tests for backend features. Test authentication, attendance tracking, and notification systems.
- **Reviewer**: Review code for adherence to coding standards, security, and scalability. Provide feedback on API endpoint design and implementation.
- **DevOps (Docker)**: Containerize the Quarkus application using Docker. Ensure seamless deployment on GKE.
- **DevOps (Deployer)**: Prepare deployment scripts for GCP and GKE. Ensure zero-downtime deployments.

#### 4. Phase Definition of Done (DoD)
Phase 2 is considered complete when:
- All backend features (authentication, attendance tracking, notification systems) are implemented and tested.
- API endpoints are designed and implemented for backend features.
- Code is reviewed and meets coding standards, security, and scalability requirements.
- Docker containerization is complete, and deployment scripts are prepared for GCP and GKE.
- Unit tests and integration tests are developed and passed for backend features.
The maximum duration for Phase 2 is 7 days. Once the core technical objectives are satisfied, the phase will be considered complete, and progression to Phase 3 will begin.
```

# Phase 3 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 3 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a web and mobile application designed to manage students and their attendance for multiple centers. The tech stack consists of Quarkus, Kafka, Postgres, and Docker, with deployment on Google Cloud Platform (GCP) and Google Kubernetes Engine (GKE). The application will support authentication via email/password, Firebase, Google, and Facebook, and will have features such as QR code-based attendance tracking, notification systems, and multi-language support.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success, the following guardrails and compliance standards will be implemented:
- **Security**: Implement OAuth 2.0 for authentication and authorization, and ensure data encryption for sensitive information.
- **Scalability**: Design the system to scale horizontally, with load balancing and autoscaling on GKE.
- **Compliance**: Adhere to GDPR and CCPA regulations for data protection, and ensure accessibility standards (WCAG 2.1) for the web and mobile applications.
- **Quality**: Implement continuous integration and continuous deployment (CI/CD) pipelines, with automated testing and code reviews.

#### 3. Standardized Sub-Agent Persona Definitions
The following sub-agent personas will be defined:
- **Manager**: Responsible for project planning, resource allocation, and progress tracking.
- **Coder**: Responsible for developing the application's features, with expertise in Quarkus, Kafka, Postgres, and Docker.
- **Tester**: Responsible for testing the application's functionality, performance, and security.
- **Reviewer**: Responsible for reviewing code, ensuring adherence to coding standards, and providing feedback.
- **Docker**: Responsible for containerizing the application and ensuring seamless deployment on GKE.
- **Deployer**: Responsible for deploying the application on GCP and GKE, and ensuring zero-downtime deployments.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into 5 phases, each with a maximum duration of 7 days:
- **Phase 1: Planning and Setup** (Days 1-3): Define project scope, create a detailed project plan, and set up the development environment.
- **Phase 2: Backend Development** (Days 4-7): Develop the backend features, including authentication, attendance tracking, and notification systems.
- **Phase 3: Frontend Development** (Days 8-14): Develop the web and mobile applications, with features such as QR code scanning, multi-language support, and SEO optimization.
- **Phase 4: Testing and Quality Assurance** (Days 15-21): Conduct thorough testing, including unit testing, integration testing, and performance testing.
- **Phase 5: Deployment and Maintenance** (Days 22-28): Deploy the application on GCP and GKE, and ensure smooth operation, with ongoing maintenance and updates.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------
            
            ## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
            #### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
            #### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

            Your output MUST follow this exact Markdown structure for Phase 3:
            ## PHASE 3 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 3 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 3 is to develop the web and mobile applications for the membership-hub project. This phase will focus on creating a user-friendly interface for students to manage their attendance and for centers to track student activity. The key deliverables for this phase include:
- Developing the web application using Next.js
- Implementing QR code scanning for attendance tracking
- Integrating multi-language support for both web and mobile applications
- Ensuring SEO optimization for the web application
- Building the mobile application for both iOS and Android platforms

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 3 will be limited to the frontend development of the web and mobile applications. The following directories, files, and endpoints are in scope:
- `web-app/`: Directory for the web application code
- `mobile-app/`: Directory for the mobile application code
- `api/`: Directory for API endpoints for frontend-backend interaction
- `components/`: Directory for reusable UI components
- `locales/`: Directory for language translations
- Endpoints for:
  - QR code scanning
  - Attendance tracking
  - User profile management
  - Language selection

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 3, with the following tasks:
- **Coder**: Develop the web and mobile applications, implement QR code scanning, multi-language support, and SEO optimization
- **Tester**: Test the web and mobile applications for functionality, performance, and security
- **Reviewer**: Review the code for adherence to coding standards, best practices, and security guidelines
- **DevOps (Docker)**: Containerize the web application for deployment on GKE
- **DevOps (Deployer)**: Prepare the environment for deployment, ensure zero-downtime deployments

#### 4. Phase Definition of Done (DoD)
Phase 3 will be considered complete when the following conditions are met:
- The web application is fully functional, with QR code scanning, multi-language support, and SEO optimization
- The mobile application is fully functional, with QR code scanning, multi-language support, and push notifications
- All code has been reviewed and approved by the Reviewer
- The web application has been containerized and is ready for deployment on GKE
- The mobile application has been built and is ready for deployment on app stores
- All testing has been completed, and the application has been verified to meet the requirements and quality standards.
```

# Phase 4 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 4 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a web and mobile application designed to manage students and their attendance for multiple centers. The tech stack consists of Quarkus, Kafka, Postgres, and Docker, with deployment on Google Cloud Platform (GCP) and Google Kubernetes Engine (GKE). The application will support authentication via email/password, Firebase, Google, and Facebook, and will have features such as QR code-based attendance tracking, notification systems, and multi-language support.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success, the following guardrails and compliance standards will be implemented:
- **Security**: Implement OAuth 2.0 for authentication and authorization, and ensure data encryption for sensitive information.
- **Scalability**: Design the system to scale horizontally, with load balancing and autoscaling on GKE.
- **Compliance**: Adhere to GDPR and CCPA regulations for data protection, and ensure accessibility standards (WCAG 2.1) for the web and mobile applications.
- **Quality**: Implement continuous integration and continuous deployment (CI/CD) pipelines, with automated testing and code reviews.

#### 3. Standardized Sub-Agent Persona Definitions
The following sub-agent personas will be defined:
- **Manager**: Responsible for project planning, resource allocation, and progress tracking.
- **Coder**: Responsible for developing the application's features, with expertise in Quarkus, Kafka, Postgres, and Docker.
- **Tester**: Responsible for testing the application's functionality, performance, and security.
- **Reviewer**: Responsible for reviewing code, ensuring adherence to coding standards, and providing feedback.
- **Docker**: Responsible for containerizing the application and ensuring seamless deployment on GKE.
- **Deployer**: Responsible for deploying the application on GCP and GKE, and ensuring zero-downtime deployments.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into 5 phases, each with a maximum duration of 7 days:
- **Phase 1: Planning and Setup** (Days 1-3): Define project scope, create a detailed project plan, and set up the development environment.
- **Phase 2: Backend Development** (Days 4-7): Develop the backend features, including authentication, attendance tracking, and notification systems.
- **Phase 3: Frontend Development** (Days 8-14): Develop the web and mobile applications, with features such as QR code scanning, multi-language support, and SEO optimization.
- **Phase 4: Testing and Quality Assurance** (Days 15-21): Conduct thorough testing, including unit testing, integration testing, and performance testing.
- **Phase 5: Deployment and Maintenance** (Days 22-28): Deploy the application on GCP and GKE, and ensure smooth operation, with ongoing maintenance and updates.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------
            
            ## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
            #### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
            #### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

            Your output MUST follow this exact Markdown structure for Phase 4:
            ## PHASE 4 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 4 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 4 is to conduct thorough testing and quality assurance of the membership-hub project. This phase will focus on ensuring the application's functionality, performance, and security meet the required standards. The scope of this phase includes:

* Unit testing of individual components
* Integration testing of interconnected components
* Performance testing to ensure scalability and reliability
* Security testing to identify vulnerabilities
* User acceptance testing (UAT) to validate the application's functionality

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope of this phase is limited to the testing and quality assurance of the existing codebase. The following directories and files are within the scope:

* `src/test`: Unit tests and integration tests
* `src/main`: Application codebase
* `docker-compose.yml`: Docker configuration for testing
* `kafka-config.properties`: Kafka configuration for testing
* `postgres-config.properties`: Postgres configuration for testing
* API endpoints for testing:
	+ `/api/v1/auth`
	+ `/api/v1/attendance`
	+ `/api/v1/notifications`

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in this phase:

* **Coder**: Assist in writing unit tests and integration tests
* **Tester**: Conduct thorough testing of the application, including performance testing and security testing
* **Reviewer**: Review test cases and provide feedback on test coverage and effectiveness
* **DevOps**: Configure and manage the testing environment, including Docker and Kafka

Tasks:

* Coder:
	+ Write unit tests for individual components (Days 1-2)
	+ Write integration tests for interconnected components (Days 2-3)
* Tester:
	+ Conduct performance testing (Days 1-2)
	+ Conduct security testing (Days 2-3)
	+ Conduct UAT (Days 3-4)
* Reviewer:
	+ Review test cases (Days 1-2)
	+ Provide feedback on test coverage and effectiveness (Days 2-3)
* DevOps:
	+ Configure testing environment (Day 1)
	+ Manage testing environment (Days 1-4)

#### 4. Phase Definition of Done (DoD)
The phase is considered complete when:

* All unit tests and integration tests have been written and executed successfully
* Performance testing and security testing have been conducted, and results have been reviewed and addressed
* UAT has been conducted, and results have been reviewed and addressed
* Test coverage is at least 80%
* All test cases have been reviewed and feedback has been incorporated
* The testing environment has been properly configured and managed

The phase will be stopped once the core technical objectives are satisfied, and the phase's definition of done has been met. The maximum duration for this phase is 7 days.
```

# Phase 5 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 5 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a web and mobile application designed to manage students and their attendance for multiple centers. The tech stack consists of Quarkus, Kafka, Postgres, and Docker, with deployment on Google Cloud Platform (GCP) and Google Kubernetes Engine (GKE). The application will support authentication via email/password, Firebase, Google, and Facebook, and will have features such as QR code-based attendance tracking, notification systems, and multi-language support.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success, the following guardrails and compliance standards will be implemented:
- **Security**: Implement OAuth 2.0 for authentication and authorization, and ensure data encryption for sensitive information.
- **Scalability**: Design the system to scale horizontally, with load balancing and autoscaling on GKE.
- **Compliance**: Adhere to GDPR and CCPA regulations for data protection, and ensure accessibility standards (WCAG 2.1) for the web and mobile applications.
- **Quality**: Implement continuous integration and continuous deployment (CI/CD) pipelines, with automated testing and code reviews.

#### 3. Standardized Sub-Agent Persona Definitions
The following sub-agent personas will be defined:
- **Manager**: Responsible for project planning, resource allocation, and progress tracking.
- **Coder**: Responsible for developing the application's features, with expertise in Quarkus, Kafka, Postgres, and Docker.
- **Tester**: Responsible for testing the application's functionality, performance, and security.
- **Reviewer**: Responsible for reviewing code, ensuring adherence to coding standards, and providing feedback.
- **Docker**: Responsible for containerizing the application and ensuring seamless deployment on GKE.
- **Deployer**: Responsible for deploying the application on GCP and GKE, and ensuring zero-downtime deployments.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into 5 phases, each with a maximum duration of 7 days:
- **Phase 1: Planning and Setup** (Days 1-3): Define project scope, create a detailed project plan, and set up the development environment.
- **Phase 2: Backend Development** (Days 4-7): Develop the backend features, including authentication, attendance tracking, and notification systems.
- **Phase 3: Frontend Development** (Days 8-14): Develop the web and mobile applications, with features such as QR code scanning, multi-language support, and SEO optimization.
- **Phase 4: Testing and Quality Assurance** (Days 15-21): Conduct thorough testing, including unit testing, integration testing, and performance testing.
- **Phase 5: Deployment and Maintenance** (Days 22-28): Deploy the application on GCP and GKE, and ensure smooth operation, with ongoing maintenance and updates.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------
            
            ## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
            #### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day 7.
            #### 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

            Your output MUST follow this exact Markdown structure for Phase 5:
            ## PHASE 5 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 5 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 5 is to deploy the membership-hub application on Google Cloud Platform (GCP) and Google Kubernetes Engine (GKE), ensuring a smooth and scalable operation. This phase will focus on:

* Deploying the application on GCP and GKE
* Configuring load balancing and autoscaling
* Ensuring zero-downtime deployments
* Setting up monitoring and logging tools
* Conducting final testing and quality assurance

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 5 includes:

* Deployment scripts and configurations for GCP and GKE
* Docker containerization and orchestration
* Load balancing and autoscaling configurations
* Monitoring and logging tools (e.g., Prometheus, Grafana, ELK Stack)
* API endpoints for deployment and management

Allowed directories and files:

* `deploy/`: deployment scripts and configurations
* `docker/`: Docker containerization and orchestration files
* `k8s/`: Kubernetes configurations and deployments
* `monitoring/`: monitoring and logging tools configurations

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 5:

* **Coder**: Responsible for creating deployment scripts and configurations, as well as ensuring the application is containerized and ready for deployment.
* **Tester**: Responsible for conducting final testing and quality assurance, including load testing and performance testing.
* **Reviewer**: Responsible for reviewing deployment scripts and configurations, as well as ensuring that the application is properly secured and compliant with regulatory requirements.
* **DevOps**: Responsible for deploying the application on GCP and GKE, configuring load balancing and autoscaling, and setting up monitoring and logging tools.
* **Docker**: Responsible for ensuring the application is properly containerized and orchestrated.
* **Deployer**: Responsible for deploying the application on GCP and GKE, and ensuring zero-downtime deployments.

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 5 includes:

* The application is successfully deployed on GCP and GKE
* Load balancing and autoscaling are properly configured
* Monitoring and logging tools are set up and functioning correctly
* Final testing and quality assurance have been completed
* The application is properly secured and compliant with regulatory requirements
* Deployment scripts and configurations are reviewed and approved
* The application is fully functional and performing as expected

Once these objectives are met, Phase 5 will be considered complete, and the project will be ready for maintenance and ongoing updates.
```

# Phase 1 STEPS - Prompt:


                    Analyze the attached Phase 1 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-1.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 1 CONTEXT MARKDOWN ---
                    ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed project plan, and set up the development environment. This phase will focus on planning and setup, ensuring that all necessary components are in place for the successful execution of the project. The key deliverables for this phase include:
- A detailed project plan outlining the scope, timeline, and resources required
- A setup development environment with the necessary tools and technologies (Quarkus, Kafka, Postgres, Docker)
- Definition of the project's technical architecture and high-level design

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 1 includes:
- Setting up the project directory structure
- Initializing the Git repository
- Creating a basic Quarkus project template
- Setting up Kafka and Postgres for messaging and data storage
- Configuring Docker for containerization
- Defining the API endpoints for authentication, attendance tracking, and notification systems
- Creating a high-level design document outlining the system architecture

The allowed directory boundaries include:
- `src/main/java` for Java source code
- `src/main/resources` for configuration files and resources
- `docker` for Docker configuration files
- `kafka` for Kafka configuration files
- `postgres` for Postgres configuration files

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 1:
- **Coder**: Responsible for setting up the Quarkus project template, configuring Kafka and Postgres, and defining the API endpoints.
- **Tester**: Not actively involved in this phase, but will review the project plan and technical architecture.
- **Reviewer**: Responsible for reviewing the project plan, technical architecture, and high-level design document.
- **DevOps (Docker)**: Responsible for setting up the Docker configuration and ensuring containerization.
- **Deployer**: Not actively involved in this phase, but will review the project plan and technical architecture.

#### 4. Phase Definition of Done (DoD)
Phase 1 is considered complete when:
- The project plan is finalized and approved by all stakeholders
- The development environment is set up and configured
- The Quarkus project template is created and configured
- Kafka and Postgres are set up and configured
- Docker is configured for containerization
- The high-level design document is completed and approved by all stakeholders
- The project directory structure is initialized and the Git repository is set up

The expected duration for Phase 1 is 3 days, with the following milestones:
- Day 1: Project planning and scope definition
- Day 2: Setup of development environment and Quarkus project template
- Day 3: Configuration of Kafka, Postgres, and Docker, and completion of high-level design document
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Based on the provided Phase 1 Context Markdown content, I will extract and translate the daily steps, checklists, and agent tasks into the required JSON schema.

Here is the resulting JSON object:

```json
{
  "phase_id": 1,
  "phase_name": "Phase 1",
  "project_name": "test-ai-architecture",
  "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": ".ai/.plan/.context/phase-1.context.blueprint.md",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "1.1",
          "agent": "Coder",
          "desc": "Define project scope and objectives"
        },
        {
          "id": "1.2",
          "agent": "Coder",
          "desc": "Create a detailed project plan outlining scope, timeline, and resources required"
        },
        {
          "id": "1.3",
          "agent": "DevOps (Docker)",
          "desc": "Initialize project directory structure"
        },
        {
          "id": "1.4",
          "agent": "DevOps (Docker)",
          "desc": "Set up Git repository"
        }
      ]
    },
    {
      "day": 2,
      "context_file": ".ai/.plan/.context/phase-1.context.blueprint.md",
      "context_section": "DAY 2",
      "sub_tasks": [
        {
          "id": "2.1",
          "agent": "Coder",
          "desc": "Set up Quarkus project template"
        },
        {
          "id": "2.2",
          "agent": "Coder",
          "desc": "Configure Kafka and Postgres for messaging and data storage"
        },
        {
          "id": "2.3",
          "agent": "DevOps (Docker)",
          "desc": "Configure Docker for containerization"
        }
      ]
    },
    {
      "day": 3,
      "context_file": ".ai/.plan/.context/phase-1.context.blueprint.md",
      "context_section": "DAY 3",
      "sub_tasks": [
        {
          "id": "3.1",
          "agent": "Coder",
          "desc": "Define API endpoints for authentication, attendance tracking, and notification systems"
        },
        {
          "id": "3.2",
          "agent": "Reviewer",
          "desc": "Review project plan and technical architecture"
        },
        {
          "id": "3.3",
          "agent": "Coder",
          "desc": "Create high-level design document outlining system architecture"
        },
        {
          "id": "3.4",
          "agent": "DevOps (Docker)",
          "desc": "Finalize Docker configuration and ensure containerization"
        }
      ]
    }
  ]
}
```

Note that I have followed the instructions to:

* Extract and translate all daily steps, checklists, and agent tasks
* Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field
* Populate the exact string "sources/" into the 'source_target_dir' field
* Provide a sequential task description text into the 'task' field (now 'desc' field)
* Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent' field
* Set 'day' as the integer value of that day
* Set 'context_file' to '.ai/.plan/.context/phase-1.context.blueprint.md'
* Set 'context_section' to 'DAY ' followed by the day number

Also, I have conformed strictly to the required JSON Schema layout design structure.
```

# Phase 2 STEPS - Prompt:


                    Analyze the attached Phase 2 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-2.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 2 CONTEXT MARKDOWN ---
                    ## PHASE 2 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 2 is to develop the backend features of the membership-hub project, including authentication, attendance tracking, and notification systems. This phase will focus on building a scalable and secure backend using Quarkus, Kafka, and Postgres. The key deliverables for this phase include:
- Design and implementation of authentication mechanisms (email/password, Firebase, Google, Facebook)
- Development of attendance tracking features (QR code-based attendance tracking)
- Implementation of notification systems (SMS, Zalo, in-app notifications)
- Integration with Postgres database for data storage
- Containerization using Docker for seamless deployment on GKE

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 2 will be limited to the backend development, with the following directory boundaries:
- `src/main/java`: Java source code for Quarkus application
- `src/main/resources`: Configuration files and static resources
- `docker`: Dockerfile and containerization scripts
- `kafka`: Kafka configuration and topic definitions
- `postgres`: Postgres database schema and migration scripts
- `api`: API endpoints for authentication, attendance tracking, and notification systems
Allowed endpoints:
- `/api/auth`: Authentication endpoints (login, logout, register)
- `/api/attendance`: Attendance tracking endpoints (QR code scanning, attendance logging)
- `/api/notifications`: Notification endpoints (SMS, Zalo, in-app notifications)

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
- **Coder**: Implement authentication mechanisms, attendance tracking features, and notification systems. Develop API endpoints for backend features.
- **Tester**: Develop unit tests and integration tests for backend features. Test authentication, attendance tracking, and notification systems.
- **Reviewer**: Review code for adherence to coding standards, security, and scalability. Provide feedback on API endpoint design and implementation.
- **DevOps (Docker)**: Containerize the Quarkus application using Docker. Ensure seamless deployment on GKE.
- **DevOps (Deployer)**: Prepare deployment scripts for GCP and GKE. Ensure zero-downtime deployments.

#### 4. Phase Definition of Done (DoD)
Phase 2 is considered complete when:
- All backend features (authentication, attendance tracking, notification systems) are implemented and tested.
- API endpoints are designed and implemented for backend features.
- Code is reviewed and meets coding standards, security, and scalability requirements.
- Docker containerization is complete, and deployment scripts are prepared for GCP and GKE.
- Unit tests and integration tests are developed and passed for backend features.
The maximum duration for Phase 2 is 7 days. Once the core technical objectives are satisfied, the phase will be considered complete, and progression to Phase 3 will begin.
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Based on the provided Phase 2 Context Markdown content, I will extract and translate the daily steps, checklists, and agent tasks into the required JSON schema.

Since the markdown content does not explicitly provide daily steps, I will parse the paragraph descriptions into technical sub-tasks for each day. The phase duration is 7 days, so I will create a day object node for each day.

Here is the translated JSON schema:

```json
{
  "phase_id": 2,
  "phase_name": "Phase 2",
  "project_name": "test-ai-architecture",
  "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "1.1",
          "agent": "Coder",
          "desc": "Design and implementation of authentication mechanisms (email/password, Firebase, Google, Facebook)"
        },
        {
          "id": "1.2",
          "agent": "Tester",
          "desc": "Develop unit tests for authentication mechanisms"
        }
      ]
    },
    {
      "day": 2,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 2",
      "sub_tasks": [
        {
          "id": "2.1",
          "agent": "Coder",
          "desc": "Development of attendance tracking features (QR code-based attendance tracking)"
        },
        {
          "id": "2.2",
          "agent": "DevOps (Docker)",
          "desc": "Containerization of Quarkus application using Docker"
        }
      ]
    },
    {
      "day": 3,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 3",
      "sub_tasks": [
        {
          "id": "3.1",
          "agent": "Coder",
          "desc": "Implementation of notification systems (SMS, Zalo, in-app notifications)"
        },
        {
          "id": "3.2",
          "agent": "Reviewer",
          "desc": "Review code for adherence to coding standards, security, and scalability"
        }
      ]
    },
    {
      "day": 4,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 4",
      "sub_tasks": [
        {
          "id": "4.1",
          "agent": "Tester",
          "desc": "Develop integration tests for backend features"
        },
        {
          "id": "4.2",
          "agent": "DevOps (Deployer)",
          "desc": "Prepare deployment scripts for GCP and GKE"
        }
      ]
    },
    {
      "day": 5,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 5",
      "sub_tasks": [
        {
          "id": "5.1",
          "agent": "Coder",
          "desc": "Design and implementation of API endpoints for backend features"
        },
        {
          "id": "5.2",
          "agent": "Reviewer",
          "desc": "Review API endpoint design and implementation"
        }
      ]
    },
    {
      "day": 6,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 6",
      "sub_tasks": [
        {
          "id": "6.1",
          "agent": "Tester",
          "desc": "Test authentication, attendance tracking, and notification systems"
        },
        {
          "id": "6.2",
          "agent": "DevOps (Docker)",
          "desc": "Ensure seamless deployment on GKE"
        }
      ]
    },
    {
      "day": 7,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 7",
      "sub_tasks": [
        {
          "id": "7.1",
          "agent": "Coder",
          "desc": "Finalize implementation of backend features"
        },
        {
          "id": "7.2",
          "agent": "Reviewer",
          "desc": "Final review of code for adherence to coding standards, security, and scalability"
        }
      ]
    }
  ]
}
```

Note that I have assigned tasks to agents based on the provided markdown content, but the actual task assignments may vary depending on the specific project requirements and team structure.
```

# Phase 3 STEPS - Prompt:


                    Analyze the attached Phase 3 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-3.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 3 CONTEXT MARKDOWN ---
                    ## PHASE 3 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 3 is to develop the web and mobile applications for the membership-hub project. This phase will focus on creating a user-friendly interface for students to manage their attendance and for centers to track student activity. The key deliverables for this phase include:
- Developing the web application using Next.js
- Implementing QR code scanning for attendance tracking
- Integrating multi-language support for both web and mobile applications
- Ensuring SEO optimization for the web application
- Building the mobile application for both iOS and Android platforms

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 3 will be limited to the frontend development of the web and mobile applications. The following directories, files, and endpoints are in scope:
- `web-app/`: Directory for the web application code
- `mobile-app/`: Directory for the mobile application code
- `api/`: Directory for API endpoints for frontend-backend interaction
- `components/`: Directory for reusable UI components
- `locales/`: Directory for language translations
- Endpoints for:
  - QR code scanning
  - Attendance tracking
  - User profile management
  - Language selection

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 3, with the following tasks:
- **Coder**: Develop the web and mobile applications, implement QR code scanning, multi-language support, and SEO optimization
- **Tester**: Test the web and mobile applications for functionality, performance, and security
- **Reviewer**: Review the code for adherence to coding standards, best practices, and security guidelines
- **DevOps (Docker)**: Containerize the web application for deployment on GKE
- **DevOps (Deployer)**: Prepare the environment for deployment, ensure zero-downtime deployments

#### 4. Phase Definition of Done (DoD)
Phase 3 will be considered complete when the following conditions are met:
- The web application is fully functional, with QR code scanning, multi-language support, and SEO optimization
- The mobile application is fully functional, with QR code scanning, multi-language support, and push notifications
- All code has been reviewed and approved by the Reviewer
- The web application has been containerized and is ready for deployment on GKE
- The mobile application has been built and is ready for deployment on app stores
- All testing has been completed, and the application has been verified to meet the requirements and quality standards.
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
To translate the provided Phase 3 Context Markdown into a JSON schema that adheres to the given instructions and JSON schema layout design structure, we first need to identify the key elements required for the translation:

1. **Phase Details**: Phase ID, Phase Name, Project Name.
2. **Global Context and Source Target Directory**: Global Context File, Source Target Directory.
3. **Daily Steps and Tasks**: Day, Context File, Context Section, and Sub-tasks with their descriptions and assigned agents.

Given the Markdown content, we can infer the following:

- **Phase ID**: Not explicitly mentioned, so we'll assume it as `3` for Phase 3.
- **Phase Name**: "Phase 3".
- **Project Name**: "test-ai-architecture" (inferred from the context).
- **Global Context File**: ".ai/.context/test-ai-architecture.global.blueprint.md" (as per the instructions).
- **Source Target Directory**: "sources/" (as per the instructions).

For the daily steps and tasks, since the Markdown does not explicitly define tasks for each day but outlines objectives, scope, and tasks for sub-agents, we will interpret the tasks under the assumption that each significant task or objective mentioned can be considered a sub-task for a particular day. However, since days are not explicitly mentioned, and given the instruction to focus on days between Day 1 and Day 0 (inclusive), and considering the nature of the provided Markdown, we will create a single day object (Day 1) to encapsulate the tasks and objectives outlined, as the Markdown does not provide a clear daily breakdown.

### JSON Schema Translation

```json
{
  "phase_id": 3,
  "phase_name": "Phase 3",
  "project_name": "test-ai-architecture",
  "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": ".ai/.plan/.context/phase-3.context.blueprint.md",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "ST-1",
          "agent": "Coder",
          "desc": "Develop the web application using Next.js"
        },
        {
          "id": "ST-2",
          "agent": "Coder",
          "desc": "Implement QR code scanning for attendance tracking"
        },
        {
          "id": "ST-3",
          "agent": "Coder",
          "desc": "Integrate multi-language support for both web and mobile applications"
        },
        {
          "id": "ST-4",
          "agent": "Coder",
          "desc": "Ensure SEO optimization for the web application"
        },
        {
          "id": "ST-5",
          "agent": "Coder",
          "desc": "Build the mobile application for both iOS and Android platforms"
        },
        {
          "id": "ST-6",
          "agent": "Tester",
          "desc": "Test the web and mobile applications for functionality, performance, and security"
        },
        {
          "id": "ST-7",
          "agent": "Reviewer",
          "desc": "Review the code for adherence to coding standards, best practices, and security guidelines"
        },
        {
          "id": "ST-8",
          "agent": "DevOps (Docker)",
          "desc": "Containerize the web application for deployment on GKE"
        },
        {
          "id": "ST-9",
          "agent": "DevOps (Deployer)",
          "desc": "Prepare the environment for deployment, ensure zero-downtime deployments"
        }
      ]
    }
  ]
}
```

This translation assumes that all tasks mentioned in the Markdown are to be completed on Day 1, given the lack of explicit daily task assignments. Each task is assigned to a specific agent based on the roles and responsibilities outlined in the Markdown. Note that this is a simplified interpretation and might need adjustments based on the actual project requirements and the intended use of the JSON schema.
```

# Phase 4 STEPS - Prompt:


                    Analyze the attached Phase 4 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-4.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 4 CONTEXT MARKDOWN ---
                    ## PHASE 4 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 4 is to conduct thorough testing and quality assurance of the membership-hub project. This phase will focus on ensuring the application's functionality, performance, and security meet the required standards. The scope of this phase includes:

* Unit testing of individual components
* Integration testing of interconnected components
* Performance testing to ensure scalability and reliability
* Security testing to identify vulnerabilities
* User acceptance testing (UAT) to validate the application's functionality

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope of this phase is limited to the testing and quality assurance of the existing codebase. The following directories and files are within the scope:

* `src/test`: Unit tests and integration tests
* `src/main`: Application codebase
* `docker-compose.yml`: Docker configuration for testing
* `kafka-config.properties`: Kafka configuration for testing
* `postgres-config.properties`: Postgres configuration for testing
* API endpoints for testing:
	+ `/api/v1/auth`
	+ `/api/v1/attendance`
	+ `/api/v1/notifications`

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in this phase:

* **Coder**: Assist in writing unit tests and integration tests
* **Tester**: Conduct thorough testing of the application, including performance testing and security testing
* **Reviewer**: Review test cases and provide feedback on test coverage and effectiveness
* **DevOps**: Configure and manage the testing environment, including Docker and Kafka

Tasks:

* Coder:
	+ Write unit tests for individual components (Days 1-2)
	+ Write integration tests for interconnected components (Days 2-3)
* Tester:
	+ Conduct performance testing (Days 1-2)
	+ Conduct security testing (Days 2-3)
	+ Conduct UAT (Days 3-4)
* Reviewer:
	+ Review test cases (Days 1-2)
	+ Provide feedback on test coverage and effectiveness (Days 2-3)
* DevOps:
	+ Configure testing environment (Day 1)
	+ Manage testing environment (Days 1-4)

#### 4. Phase Definition of Done (DoD)
The phase is considered complete when:

* All unit tests and integration tests have been written and executed successfully
* Performance testing and security testing have been conducted, and results have been reviewed and addressed
* UAT has been conducted, and results have been reviewed and addressed
* Test coverage is at least 80%
* All test cases have been reviewed and feedback has been incorporated
* The testing environment has been properly configured and managed

The phase will be stopped once the core technical objectives are satisfied, and the phase's definition of done has been met. The maximum duration for this phase is 7 days.
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Based on the provided Phase 4 Context Markdown content, I will extract and translate the daily steps, checklists, and agent tasks into the required JSON schema.

Since the target range is between Day 1 and Day 0 (inclusive), and considering the instructions, I will focus on the days mentioned in the tasks section. Although Day 0 is not explicitly mentioned in the tasks, I will include it in the output to adhere to the instructions.

Here is the translated JSON schema:

```json
{
  "phase_id": 4,
  "phase_name": "Phase 4",
  "project_name": "test-ai-architecture",
  "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 0,
      "context_file": ".ai/.plan/.context/phase-4.context.blueprint.md",
      "context_section": "DAY 0",
      "sub_tasks": [
        {
          "id": "0-1",
          "agent": "DevOps",
          "desc": "Prepare testing environment"
        }
      ]
    },
    {
      "day": 1,
      "context_file": ".ai/.plan/.context/phase-4.context.blueprint.md",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "1-1",
          "agent": "Coder",
          "desc": "Write unit tests for individual components"
        },
        {
          "id": "1-2",
          "agent": "Tester",
          "desc": "Conduct performance testing"
        },
        {
          "id": "1-3",
          "agent": "Reviewer",
          "desc": "Review test cases"
        },
        {
          "id": "1-4",
          "agent": "DevOps",
          "desc": "Configure testing environment"
        }
      ]
    },
    {
      "day": 2,
      "context_file": ".ai/.plan/.context/phase-4.context.blueprint.md",
      "context_section": "DAY 2",
      "sub_tasks": [
        {
          "id": "2-1",
          "agent": "Coder",
          "desc": "Write integration tests for interconnected components"
        },
        {
          "id": "2-2",
          "agent": "Tester",
          "desc": "Conduct security testing"
        },
        {
          "id": "2-3",
          "agent": "Reviewer",
          "desc": "Provide feedback on test coverage and effectiveness"
        },
        {
          "id": "2-4",
          "agent": "DevOps",
          "desc": "Manage testing environment"
        }
      ]
    },
    {
      "day": 3,
      "context_file": ".ai/.plan/.context/phase-4.context.blueprint.md",
      "context_section": "DAY 3",
      "sub_tasks": [
        {
          "id": "3-1",
          "agent": "Tester",
          "desc": "Conduct UAT"
        },
        {
          "id": "3-2",
          "agent": "Reviewer",
          "desc": "Review test cases and provide feedback"
        },
        {
          "id": "3-3",
          "agent": "DevOps",
          "desc": "Manage testing environment"
        }
      ]
    },
    {
      "day": 4,
      "context_file": ".ai/.plan/.context/phase-4.context.blueprint.md",
      "context_section": "DAY 4",
      "sub_tasks": [
        {
          "id": "4-1",
          "agent": "Tester",
          "desc": "Conduct UAT and review results"
        },
        {
          "id": "4-2",
          "agent": "DevOps",
          "desc": "Manage testing environment"
        }
      ]
    }
  ]
}
```

Note that I have included Day 0 in the output, as per the instructions, although it is not explicitly mentioned in the tasks section. I have also assumed that the tasks for Day 0 are related to preparing the testing environment, which is a reasonable assumption based on the context.
```

# Phase 5 STEPS - Prompt:


                    Analyze the attached Phase 5 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-5.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 5 CONTEXT MARKDOWN ---
                    ## PHASE 5 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 5 is to deploy the membership-hub application on Google Cloud Platform (GCP) and Google Kubernetes Engine (GKE), ensuring a smooth and scalable operation. This phase will focus on:

* Deploying the application on GCP and GKE
* Configuring load balancing and autoscaling
* Ensuring zero-downtime deployments
* Setting up monitoring and logging tools
* Conducting final testing and quality assurance

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 5 includes:

* Deployment scripts and configurations for GCP and GKE
* Docker containerization and orchestration
* Load balancing and autoscaling configurations
* Monitoring and logging tools (e.g., Prometheus, Grafana, ELK Stack)
* API endpoints for deployment and management

Allowed directories and files:

* `deploy/`: deployment scripts and configurations
* `docker/`: Docker containerization and orchestration files
* `k8s/`: Kubernetes configurations and deployments
* `monitoring/`: monitoring and logging tools configurations

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 5:

* **Coder**: Responsible for creating deployment scripts and configurations, as well as ensuring the application is containerized and ready for deployment.
* **Tester**: Responsible for conducting final testing and quality assurance, including load testing and performance testing.
* **Reviewer**: Responsible for reviewing deployment scripts and configurations, as well as ensuring that the application is properly secured and compliant with regulatory requirements.
* **DevOps**: Responsible for deploying the application on GCP and GKE, configuring load balancing and autoscaling, and setting up monitoring and logging tools.
* **Docker**: Responsible for ensuring the application is properly containerized and orchestrated.
* **Deployer**: Responsible for deploying the application on GCP and GKE, and ensuring zero-downtime deployments.

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 5 includes:

* The application is successfully deployed on GCP and GKE
* Load balancing and autoscaling are properly configured
* Monitoring and logging tools are set up and functioning correctly
* Final testing and quality assurance have been completed
* The application is properly secured and compliant with regulatory requirements
* Deployment scripts and configurations are reviewed and approved
* The application is fully functional and performing as expected

Once these objectives are met, Phase 5 will be considered complete, and the project will be ready for maintenance and ongoing updates.
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Based on the provided Phase 5 Context Markdown content, I will extract and translate the daily steps, checklists, and agent tasks into a precise, executable JSON schema.

Since the markdown content does not explicitly mention days, I will assume that the tasks are to be performed on a single day, Day 1, as per the instructions. I will also parse the paragraph descriptions into technical sub-tasks for that day.

Here is the resulting JSON schema:
```json
{
  "phase_id": 5,
  "phase_name": "Phase 5",
  "project_name": "test-ai-architecture",
  "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": ".ai/.plan/.context/phase-5.context.blueprint.md",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "1.1",
          "agent": "Coder",
          "desc": "Create deployment scripts and configurations for GCP and GKE"
        },
        {
          "id": "1.2",
          "agent": "Coder",
          "desc": "Ensure the application is containerized and ready for deployment"
        },
        {
          "id": "1.3",
          "agent": "Tester",
          "desc": "Conduct final testing and quality assurance, including load testing and performance testing"
        },
        {
          "id": "1.4",
          "agent": "Reviewer",
          "desc": "Review deployment scripts and configurations, and ensure the application is properly secured and compliant with regulatory requirements"
        },
        {
          "id": "1.5",
          "agent": "DevOps",
          "desc": "Deploy the application on GCP and GKE, configure load balancing and autoscaling, and set up monitoring and logging tools"
        },
        {
          "id": "1.6",
          "agent": "Docker",
          "desc": "Ensure the application is properly containerized and orchestrated"
        },
        {
          "id": "1.7",
          "agent": "Deployer",
          "desc": "Deploy the application on GCP and GKE, and ensure zero-downtime deployments"
        }
      ]
    }
  ]
}
```
Note that I have assigned a unique `id` to each sub-task, and populated the `agent` field with the corresponding role (e.g., Coder, Tester, Reviewer, etc.). I have also populated the `desc` field with a brief description of each task.

Since there is no explicit mention of Day 0, I have not included it in the `days` array. However, if you would like to include it, please let me know, and I can add a separate day object for Day 0 with its corresponding sub-tasks.
```

# Phase 1 STEPS - Prompt:


                    Analyze the attached Phase 1 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-1.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 1 CONTEXT MARKDOWN ---
                    ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed project plan, and set up the development environment. This phase will focus on planning and setup, ensuring that all necessary components are in place for the successful execution of the project. The key deliverables for this phase include:
- A detailed project plan outlining the scope, timeline, and resources required
- A setup development environment with the necessary tools and technologies (Quarkus, Kafka, Postgres, Docker)
- Definition of the project's technical architecture and high-level design

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 1 includes:
- Setting up the project directory structure
- Initializing the Git repository
- Creating a basic Quarkus project template
- Setting up Kafka and Postgres for messaging and data storage
- Configuring Docker for containerization
- Defining the API endpoints for authentication, attendance tracking, and notification systems
- Creating a high-level design document outlining the system architecture

The allowed directory boundaries include:
- `src/main/java` for Java source code
- `src/main/resources` for configuration files and resources
- `docker` for Docker configuration files
- `kafka` for Kafka configuration files
- `postgres` for Postgres configuration files

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 1:
- **Coder**: Responsible for setting up the Quarkus project template, configuring Kafka and Postgres, and defining the API endpoints.
- **Tester**: Not actively involved in this phase, but will review the project plan and technical architecture.
- **Reviewer**: Responsible for reviewing the project plan, technical architecture, and high-level design document.
- **DevOps (Docker)**: Responsible for setting up the Docker configuration and ensuring containerization.
- **Deployer**: Not actively involved in this phase, but will review the project plan and technical architecture.

#### 4. Phase Definition of Done (DoD)
Phase 1 is considered complete when:
- The project plan is finalized and approved by all stakeholders
- The development environment is set up and configured
- The Quarkus project template is created and configured
- Kafka and Postgres are set up and configured
- Docker is configured for containerization
- The high-level design document is completed and approved by all stakeholders
- The project directory structure is initialized and the Git repository is set up

The expected duration for Phase 1 is 3 days, with the following milestones:
- Day 1: Project planning and scope definition
- Day 2: Setup of development environment and Quarkus project template
- Day 3: Configuration of Kafka, Postgres, and Docker, and completion of high-level design document
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 429 - {'error': {'message': 'Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx7x6rbpftmr50sr2yyb78qm` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 94528, Requested 5828. Please try again in 5m7.584s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
```

# Phase 1 STEPS - Prompt:


                    Analyze the attached Phase 1 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-1.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 1 CONTEXT MARKDOWN ---
                    ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed project plan, and set up the development environment. This phase will focus on planning and setup, ensuring that all necessary components are in place for the successful execution of the project. The key deliverables for this phase include:
- A detailed project plan outlining the scope, timeline, and resources required
- A setup development environment with the necessary tools and technologies (Quarkus, Kafka, Postgres, Docker)
- Definition of the project's technical architecture and high-level design

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 1 includes:
- Setting up the project directory structure
- Initializing the Git repository
- Creating a basic Quarkus project template
- Setting up Kafka and Postgres for messaging and data storage
- Configuring Docker for containerization
- Defining the API endpoints for authentication, attendance tracking, and notification systems
- Creating a high-level design document outlining the system architecture

The allowed directory boundaries include:
- `src/main/java` for Java source code
- `src/main/resources` for configuration files and resources
- `docker` for Docker configuration files
- `kafka` for Kafka configuration files
- `postgres` for Postgres configuration files

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 1:
- **Coder**: Responsible for setting up the Quarkus project template, configuring Kafka and Postgres, and defining the API endpoints.
- **Tester**: Not actively involved in this phase, but will review the project plan and technical architecture.
- **Reviewer**: Responsible for reviewing the project plan, technical architecture, and high-level design document.
- **DevOps (Docker)**: Responsible for setting up the Docker configuration and ensuring containerization.
- **Deployer**: Not actively involved in this phase, but will review the project plan and technical architecture.

#### 4. Phase Definition of Done (DoD)
Phase 1 is considered complete when:
- The project plan is finalized and approved by all stakeholders
- The development environment is set up and configured
- The Quarkus project template is created and configured
- Kafka and Postgres are set up and configured
- Docker is configured for containerization
- The high-level design document is completed and approved by all stakeholders
- The project directory structure is initialized and the Git repository is set up

The expected duration for Phase 1 is 3 days, with the following milestones:
- Day 1: Project planning and scope definition
- Day 2: Setup of development environment and Quarkus project template
- Day 3: Configuration of Kafka, Postgres, and Docker, and completion of high-level design document
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Based on the provided Phase 1 Context Markdown content, I will extract and translate the daily steps, checklists, and agent tasks into a JSON schema that conforms to the required layout design structure.

Here is the resulting JSON object:

```json
{
  "phase_id": 1,
  "phase_name": "Phase 1",
  "project_name": "test-ai-architecture",
  "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": ".ai/.plan/.context/phase-1.context.blueprint.md",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "1.1",
          "agent": "Coder",
          "desc": "Define project scope and objectives"
        },
        {
          "id": "1.2",
          "agent": "Coder",
          "desc": "Create a detailed project plan outlining scope, timeline, and resources required"
        },
        {
          "id": "1.3",
          "agent": "Reviewer",
          "desc": "Review project plan and provide feedback"
        }
      ]
    },
    {
      "day": 2,
      "context_file": ".ai/.plan/.context/phase-1.context.blueprint.md",
      "context_section": "DAY 2",
      "sub_tasks": [
        {
          "id": "2.1",
          "agent": "Coder",
          "desc": "Set up development environment with necessary tools and technologies (Quarkus, Kafka, Postgres, Docker)"
        },
        {
          "id": "2.2",
          "agent": "Coder",
          "desc": "Create a basic Quarkus project template"
        },
        {
          "id": "2.3",
          "agent": "DevOps (Docker)",
          "desc": "Set up Docker configuration for containerization"
        }
      ]
    },
    {
      "day": 3,
      "context_file": ".ai/.plan/.context/phase-1.context.blueprint.md",
      "context_section": "DAY 3",
      "sub_tasks": [
        {
          "id": "3.1",
          "agent": "Coder",
          "desc": "Configure Kafka and Postgres for messaging and data storage"
        },
        {
          "id": "3.2",
          "agent": "Coder",
          "desc": "Define API endpoints for authentication, attendance tracking, and notification systems"
        },
        {
          "id": "3.3",
          "agent": "Reviewer",
          "desc": "Review high-level design document and provide feedback"
        },
        {
          "id": "3.4",
          "agent": "DevOps (Docker)",
          "desc": "Ensure containerization is working correctly"
        }
      ]
    },
    {
      "day": 0,
      "context_file": ".ai/.plan/.context/phase-1.context.blueprint.md",
      "context_section": "DAY 0",
      "sub_tasks": [
        {
          "id": "0.1",
          "agent": "Coder",
          "desc": "Initialize project directory structure and set up Git repository"
        },
        {
          "id": "0.2",
          "agent": "Coder",
          "desc": "Create high-level design document outlining system architecture"
        }
      ]
    }
  ]
}
```

Note that I have included Day 0 in the output, as per the instructions to include all days between Day 1 and Day 0 (inclusive). I have also populated the `global_context_file` and `source_target_dir` fields with the exact string values specified in the instructions. Additionally, I have assigned tasks to agents based on the roles mentioned in the Markdown content.
```

# Phase 2 STEPS - Prompt:


                    Analyze the attached Phase 2 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-2.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 2 CONTEXT MARKDOWN ---
                    ## PHASE 2 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 2 is to develop the backend features of the membership-hub project, including authentication, attendance tracking, and notification systems. This phase will focus on building a scalable and secure backend using Quarkus, Kafka, and Postgres. The key deliverables for this phase include:
- Design and implementation of authentication mechanisms (email/password, Firebase, Google, Facebook)
- Development of attendance tracking features (QR code-based attendance tracking)
- Implementation of notification systems (SMS, Zalo, in-app notifications)
- Integration with Postgres database for data storage
- Containerization using Docker for seamless deployment on GKE

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 2 will be limited to the backend development, with the following directory boundaries:
- `src/main/java`: Java source code for Quarkus application
- `src/main/resources`: Configuration files and static resources
- `docker`: Dockerfile and containerization scripts
- `kafka`: Kafka configuration and topic definitions
- `postgres`: Postgres database schema and migration scripts
- `api`: API endpoints for authentication, attendance tracking, and notification systems
Allowed endpoints:
- `/api/auth`: Authentication endpoints (login, logout, register)
- `/api/attendance`: Attendance tracking endpoints (QR code scanning, attendance logging)
- `/api/notifications`: Notification endpoints (SMS, Zalo, in-app notifications)

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
- **Coder**: Implement authentication mechanisms, attendance tracking features, and notification systems. Develop API endpoints for backend features.
- **Tester**: Develop unit tests and integration tests for backend features. Test authentication, attendance tracking, and notification systems.
- **Reviewer**: Review code for adherence to coding standards, security, and scalability. Provide feedback on API endpoint design and implementation.
- **DevOps (Docker)**: Containerize the Quarkus application using Docker. Ensure seamless deployment on GKE.
- **DevOps (Deployer)**: Prepare deployment scripts for GCP and GKE. Ensure zero-downtime deployments.

#### 4. Phase Definition of Done (DoD)
Phase 2 is considered complete when:
- All backend features (authentication, attendance tracking, notification systems) are implemented and tested.
- API endpoints are designed and implemented for backend features.
- Code is reviewed and meets coding standards, security, and scalability requirements.
- Docker containerization is complete, and deployment scripts are prepared for GCP and GKE.
- Unit tests and integration tests are developed and passed for backend features.
The maximum duration for Phase 2 is 7 days. Once the core technical objectives are satisfied, the phase will be considered complete, and progression to Phase 3 will begin.
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 429 - {'error': {'message': 'Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx7x6rbpftmr50sr2yyb78qm` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99171, Requested 5819. Please try again in 1h11m51.359999999s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
```

# Phase 1 STEPS - Prompt:


                    Analyze the attached Phase 1 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-1.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 1 CONTEXT MARKDOWN ---
                    ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed project plan, and set up the development environment. This phase will focus on planning and setup, ensuring that all necessary components are in place for the successful execution of the project. The key deliverables for this phase include:
- A detailed project plan outlining the scope, timeline, and resources required
- A setup development environment with the necessary tools and technologies (Quarkus, Kafka, Postgres, Docker)
- Definition of the project's technical architecture and high-level design

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 1 includes:
- Setting up the project directory structure
- Initializing the Git repository
- Creating a basic Quarkus project template
- Setting up Kafka and Postgres for messaging and data storage
- Configuring Docker for containerization
- Defining the API endpoints for authentication, attendance tracking, and notification systems
- Creating a high-level design document outlining the system architecture

The allowed directory boundaries include:
- `src/main/java` for Java source code
- `src/main/resources` for configuration files and resources
- `docker` for Docker configuration files
- `kafka` for Kafka configuration files
- `postgres` for Postgres configuration files

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 1:
- **Coder**: Responsible for setting up the Quarkus project template, configuring Kafka and Postgres, and defining the API endpoints.
- **Tester**: Not actively involved in this phase, but will review the project plan and technical architecture.
- **Reviewer**: Responsible for reviewing the project plan, technical architecture, and high-level design document.
- **DevOps (Docker)**: Responsible for setting up the Docker configuration and ensuring containerization.
- **Deployer**: Not actively involved in this phase, but will review the project plan and technical architecture.

#### 4. Phase Definition of Done (DoD)
Phase 1 is considered complete when:
- The project plan is finalized and approved by all stakeholders
- The development environment is set up and configured
- The Quarkus project template is created and configured
- Kafka and Postgres are set up and configured
- Docker is configured for containerization
- The high-level design document is completed and approved by all stakeholders
- The project directory structure is initialized and the Git repository is set up

The expected duration for Phase 1 is 3 days, with the following milestones:
- Day 1: Project planning and scope definition
- Day 2: Setup of development environment and Quarkus project template
- Day 3: Configuration of Kafka, Postgres, and Docker, and completion of high-level design document
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Based on the provided Phase 1 Context Markdown content, I will extract and translate the daily steps, checklists, and agent tasks into a JSON schema that conforms to the required layout design structure.

Here is the resulting JSON object:

```json
{
  "phase_id": 1,
  "phase_name": "Phase 1",
  "project_name": "test-ai-architecture",
  "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": ".ai/.plan/.context/phase-1.context.blueprint.md",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "1.1",
          "agent": "Coder",
          "desc": "Define project scope and objectives"
        },
        {
          "id": "1.2",
          "agent": "Coder",
          "desc": "Create a detailed project plan outlining scope, timeline, and resources required"
        },
        {
          "id": "1.3",
          "agent": "Reviewer",
          "desc": "Review project plan and provide feedback"
        }
      ]
    },
    {
      "day": 2,
      "context_file": ".ai/.plan/.context/phase-1.context.blueprint.md",
      "context_section": "DAY 2",
      "sub_tasks": [
        {
          "id": "2.1",
          "agent": "Coder",
          "desc": "Set up project directory structure"
        },
        {
          "id": "2.2",
          "agent": "Coder",
          "desc": "Initialize Git repository"
        },
        {
          "id": "2.3",
          "agent": "Coder",
          "desc": "Create a basic Quarkus project template"
        },
        {
          "id": "2.4",
          "agent": "DevOps (Docker)",
          "desc": "Set up Docker configuration for containerization"
        }
      ]
    },
    {
      "day": 3,
      "context_file": ".ai/.plan/.context/phase-1.context.blueprint.md",
      "context_section": "DAY 3",
      "sub_tasks": [
        {
          "id": "3.1",
          "agent": "Coder",
          "desc": "Configure Kafka and Postgres for messaging and data storage"
        },
        {
          "id": "3.2",
          "agent": "Coder",
          "desc": "Define API endpoints for authentication, attendance tracking, and notification systems"
        },
        {
          "id": "3.3",
          "agent": "Reviewer",
          "desc": "Review high-level design document and provide feedback"
        },
        {
          "id": "3.4",
          "agent": "DevOps (Docker)",
          "desc": "Ensure containerization using Docker"
        }
      ]
    }
  ]
}
```

Note that I have carefully followed the instructions and extracted the daily steps, checklists, and agent tasks from the provided Markdown content. I have also populated the required fields, including `global_context_file` and `source_target_dir`, with the exact string values as specified. Additionally, I have ensured that the `days` array is not empty and that each day object has the required properties, including `day`, `context_file`, `context_section`, and `sub_tasks`.
```

# Phase 2 STEPS - Prompt:


                    Analyze the attached Phase 2 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-2.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 2 CONTEXT MARKDOWN ---
                    ## PHASE 2 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 2 is to develop the backend features of the membership-hub project, including authentication, attendance tracking, and notification systems. This phase will focus on building a scalable and secure backend using Quarkus, Kafka, and Postgres. The key deliverables for this phase include:
- Design and implementation of authentication mechanisms (email/password, Firebase, Google, Facebook)
- Development of attendance tracking features (QR code-based attendance tracking)
- Implementation of notification systems (SMS, Zalo, in-app notifications)
- Integration with Postgres database for data storage
- Containerization using Docker for seamless deployment on GKE

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 2 will be limited to the backend development, with the following directory boundaries:
- `src/main/java`: Java source code for Quarkus application
- `src/main/resources`: Configuration files and static resources
- `docker`: Dockerfile and containerization scripts
- `kafka`: Kafka configuration and topic definitions
- `postgres`: Postgres database schema and migration scripts
- `api`: API endpoints for authentication, attendance tracking, and notification systems
Allowed endpoints:
- `/api/auth`: Authentication endpoints (login, logout, register)
- `/api/attendance`: Attendance tracking endpoints (QR code scanning, attendance logging)
- `/api/notifications`: Notification endpoints (SMS, Zalo, in-app notifications)

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
- **Coder**: Implement authentication mechanisms, attendance tracking features, and notification systems. Develop API endpoints for backend features.
- **Tester**: Develop unit tests and integration tests for backend features. Test authentication, attendance tracking, and notification systems.
- **Reviewer**: Review code for adherence to coding standards, security, and scalability. Provide feedback on API endpoint design and implementation.
- **DevOps (Docker)**: Containerize the Quarkus application using Docker. Ensure seamless deployment on GKE.
- **DevOps (Deployer)**: Prepare deployment scripts for GCP and GKE. Ensure zero-downtime deployments.

#### 4. Phase Definition of Done (DoD)
Phase 2 is considered complete when:
- All backend features (authentication, attendance tracking, notification systems) are implemented and tested.
- API endpoints are designed and implemented for backend features.
- Code is reviewed and meets coding standards, security, and scalability requirements.
- Docker containerization is complete, and deployment scripts are prepared for GCP and GKE.
- Unit tests and integration tests are developed and passed for backend features.
The maximum duration for Phase 2 is 7 days. Once the core technical objectives are satisfied, the phase will be considered complete, and progression to Phase 3 will begin.
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 429 - {'error': {'message': 'Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx7x6rbpftmr50sr2yyb78qm` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 98620, Requested 5819. Please try again in 1h3m55.296s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
```

# Phase 1 STEPS - Prompt:


                    Analyze the attached Phase 1 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-1.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 1 CONTEXT MARKDOWN ---
                    ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed project plan, and set up the development environment. This phase will focus on planning and setup, ensuring that all necessary components are in place for the successful execution of the project. The key deliverables for this phase include:
- A detailed project plan outlining the scope, timeline, and resources required
- A setup development environment with the necessary tools and technologies (Quarkus, Kafka, Postgres, Docker)
- Definition of the project's technical architecture and high-level design

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 1 includes:
- Setting up the project directory structure
- Initializing the Git repository
- Creating a basic Quarkus project template
- Setting up Kafka and Postgres for messaging and data storage
- Configuring Docker for containerization
- Defining the API endpoints for authentication, attendance tracking, and notification systems
- Creating a high-level design document outlining the system architecture

The allowed directory boundaries include:
- `src/main/java` for Java source code
- `src/main/resources` for configuration files and resources
- `docker` for Docker configuration files
- `kafka` for Kafka configuration files
- `postgres` for Postgres configuration files

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 1:
- **Coder**: Responsible for setting up the Quarkus project template, configuring Kafka and Postgres, and defining the API endpoints.
- **Tester**: Not actively involved in this phase, but will review the project plan and technical architecture.
- **Reviewer**: Responsible for reviewing the project plan, technical architecture, and high-level design document.
- **DevOps (Docker)**: Responsible for setting up the Docker configuration and ensuring containerization.
- **Deployer**: Not actively involved in this phase, but will review the project plan and technical architecture.

#### 4. Phase Definition of Done (DoD)
Phase 1 is considered complete when:
- The project plan is finalized and approved by all stakeholders
- The development environment is set up and configured
- The Quarkus project template is created and configured
- Kafka and Postgres are set up and configured
- Docker is configured for containerization
- The high-level design document is completed and approved by all stakeholders
- The project directory structure is initialized and the Git repository is set up

The expected duration for Phase 1 is 3 days, with the following milestones:
- Day 1: Project planning and scope definition
- Day 2: Setup of development environment and Quarkus project template
- Day 3: Configuration of Kafka, Postgres, and Docker, and completion of high-level design document
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 404 - {'error': {'message': 'This model is unavailable for free. The paid version is available now - use this slug instead: meta-llama/llama-3.3-70b-instruct', 'code': 404}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:


                    Analyze the attached Phase 1 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-1.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 1 CONTEXT MARKDOWN ---
                    ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed project plan, and set up the development environment. This phase will focus on planning and setup, ensuring that all necessary components are in place for the successful execution of the project. The key deliverables for this phase include:
- A detailed project plan outlining the scope, timeline, and resources required
- A setup development environment with the necessary tools and technologies (Quarkus, Kafka, Postgres, Docker)
- Definition of the project's technical architecture and high-level design

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 1 includes:
- Setting up the project directory structure
- Initializing the Git repository
- Creating a basic Quarkus project template
- Setting up Kafka and Postgres for messaging and data storage
- Configuring Docker for containerization
- Defining the API endpoints for authentication, attendance tracking, and notification systems
- Creating a high-level design document outlining the system architecture

The allowed directory boundaries include:
- `src/main/java` for Java source code
- `src/main/resources` for configuration files and resources
- `docker` for Docker configuration files
- `kafka` for Kafka configuration files
- `postgres` for Postgres configuration files

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 1:
- **Coder**: Responsible for setting up the Quarkus project template, configuring Kafka and Postgres, and defining the API endpoints.
- **Tester**: Not actively involved in this phase, but will review the project plan and technical architecture.
- **Reviewer**: Responsible for reviewing the project plan, technical architecture, and high-level design document.
- **DevOps (Docker)**: Responsible for setting up the Docker configuration and ensuring containerization.
- **Deployer**: Not actively involved in this phase, but will review the project plan and technical architecture.

#### 4. Phase Definition of Done (DoD)
Phase 1 is considered complete when:
- The project plan is finalized and approved by all stakeholders
- The development environment is set up and configured
- The Quarkus project template is created and configured
- Kafka and Postgres are set up and configured
- Docker is configured for containerization
- The high-level design document is completed and approved by all stakeholders
- The project directory structure is initialized and the Git repository is set up

The expected duration for Phase 1 is 3 days, with the following milestones:
- Day 1: Project planning and scope definition
- Day 2: Setup of development environment and Quarkus project template
- Day 3: Configuration of Kafka, Postgres, and Docker, and completion of high-level design document
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
### Phase 1 Context JSON Schema

Based on the provided Markdown content, the following JSON schema is generated:

```json
{
  "phase_id": 1,
  "phase_name": "Phase 1",
  "project_name": "test-ai-architecture",
  "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": ".ai/.plan/.context/phase-1.context.blueprint.md",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "1.1",
          "agent": "Coder",
          "desc": "Define project scope and objectives"
        },
        {
          "id": "1.2",
          "agent": "Coder",
          "desc": "Create a detailed project plan outlining scope, timeline, and resources required"
        },
        {
          "id": "1.3",
          "agent": "Reviewer",
          "desc": "Review project plan and provide feedback"
        }
      ]
    },
    {
      "day": 2,
      "context_file": ".ai/.plan/.context/phase-1.context.blueprint.md",
      "context_section": "DAY 2",
      "sub_tasks": [
        {
          "id": "2.1",
          "agent": "Coder",
          "desc": "Set up development environment with necessary tools and technologies (Quarkus, Kafka, Postgres, Docker)"
        },
        {
          "id": "2.2",
          "agent": "Coder",
          "desc": "Create a basic Quarkus project template"
        },
        {
          "id": "2.3",
          "agent": "DevOps (Docker)",
          "desc": "Set up Docker configuration for containerization"
        }
      ]
    },
    {
      "day": 3,
      "context_file": ".ai/.plan/.context/phase-1.context.blueprint.md",
      "context_section": "DAY 3",
      "sub_tasks": [
        {
          "id": "3.1",
          "agent": "Coder",
          "desc": "Configure Kafka and Postgres for messaging and data storage"
        },
        {
          "id": "3.2",
          "agent": "Coder",
          "desc": "Define API endpoints for authentication, attendance tracking, and notification systems"
        },
        {
          "id": "3.3",
          "agent": "Reviewer",
          "desc": "Review high-level design document and provide feedback"
        },
        {
          "id": "3.4",
          "agent": "DevOps (Docker)",
          "desc": "Ensure containerization is working correctly"
        }
      ]
    }
  ]
}
```

This JSON schema captures the daily steps, checklists, and agent tasks as described in the Markdown content. It adheres to the required JSON schema layout design structure and includes all the necessary fields and properties.
```

# Phase 2 STEPS - Prompt:


                    Analyze the attached Phase 2 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-2.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 2 CONTEXT MARKDOWN ---
                    ## PHASE 2 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 2 is to develop the backend features of the membership-hub project, including authentication, attendance tracking, and notification systems. This phase will focus on building a scalable and secure backend using Quarkus, Kafka, and Postgres. The key deliverables for this phase include:
- Design and implementation of authentication mechanisms (email/password, Firebase, Google, Facebook)
- Development of attendance tracking features (QR code-based attendance tracking)
- Implementation of notification systems (SMS, Zalo, in-app notifications)
- Integration with Postgres database for data storage
- Containerization using Docker for seamless deployment on GKE

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 2 will be limited to the backend development, with the following directory boundaries:
- `src/main/java`: Java source code for Quarkus application
- `src/main/resources`: Configuration files and static resources
- `docker`: Dockerfile and containerization scripts
- `kafka`: Kafka configuration and topic definitions
- `postgres`: Postgres database schema and migration scripts
- `api`: API endpoints for authentication, attendance tracking, and notification systems
Allowed endpoints:
- `/api/auth`: Authentication endpoints (login, logout, register)
- `/api/attendance`: Attendance tracking endpoints (QR code scanning, attendance logging)
- `/api/notifications`: Notification endpoints (SMS, Zalo, in-app notifications)

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
- **Coder**: Implement authentication mechanisms, attendance tracking features, and notification systems. Develop API endpoints for backend features.
- **Tester**: Develop unit tests and integration tests for backend features. Test authentication, attendance tracking, and notification systems.
- **Reviewer**: Review code for adherence to coding standards, security, and scalability. Provide feedback on API endpoint design and implementation.
- **DevOps (Docker)**: Containerize the Quarkus application using Docker. Ensure seamless deployment on GKE.
- **DevOps (Deployer)**: Prepare deployment scripts for GCP and GKE. Ensure zero-downtime deployments.

#### 4. Phase Definition of Done (DoD)
Phase 2 is considered complete when:
- All backend features (authentication, attendance tracking, notification systems) are implemented and tested.
- API endpoints are designed and implemented for backend features.
- Code is reviewed and meets coding standards, security, and scalability requirements.
- Docker containerization is complete, and deployment scripts are prepared for GCP and GKE.
- Unit tests and integration tests are developed and passed for backend features.
The maximum duration for Phase 2 is 7 days. Once the core technical objectives are satisfied, the phase will be considered complete, and progression to Phase 3 will begin.
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
### JSON Schema Representation of Phase 2 Context

Given the provided Phase 2 Context Markdown, the following JSON schema represents the extracted and translated daily steps, checklists, and agent tasks according to the specified requirements.

```json
{
  "phase_id": 2,
  "phase_name": "Phase 2",
  "project_name": "test-ai-architecture",
  "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "1.1",
          "agent": "Coder",
          "desc": "Design and implement authentication mechanisms (email/password, Firebase, Google, Facebook)"
        },
        {
          "id": "1.2",
          "agent": "Tester",
          "desc": "Develop unit tests for authentication mechanisms"
        },
        {
          "id": "1.3",
          "agent": "DevOps (Docker)",
          "desc": "Initialize Dockerfile for Quarkus application"
        }
      ]
    },
    {
      "day": 2,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 2",
      "sub_tasks": [
        {
          "id": "2.1",
          "agent": "Coder",
          "desc": "Develop attendance tracking features (QR code-based attendance tracking)"
        },
        {
          "id": "2.2",
          "agent": "Tester",
          "desc": "Develop unit tests for attendance tracking features"
        },
        {
          "id": "2.3",
          "agent": "Reviewer",
          "desc": "Review code for attendance tracking features"
        }
      ]
    },
    {
      "day": 3,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 3",
      "sub_tasks": [
        {
          "id": "3.1",
          "agent": "Coder",
          "desc": "Implement notification systems (SMS, Zalo, in-app notifications)"
        },
        {
          "id": "3.2",
          "agent": "Tester",
          "desc": "Develop unit tests for notification systems"
        },
        {
          "id": "3.3",
          "agent": "DevOps (Deployer)",
          "desc": "Prepare deployment scripts for GCP and GKE"
        }
      ]
    },
    {
      "day": 4,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 4",
      "sub_tasks": [
        {
          "id": "4.1",
          "agent": "Coder",
          "desc": "Develop API endpoints for authentication, attendance tracking, and notification systems"
        },
        {
          "id": "4.2",
          "agent": "Tester",
          "desc": "Develop integration tests for API endpoints"
        },
        {
          "id": "4.3",
          "agent": "Reviewer",
          "desc": "Review API endpoint design and implementation"
        }
      ]
    },
    {
      "day": 5,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 5",
      "sub_tasks": [
        {
          "id": "5.1",
          "agent": "DevOps (Docker)",
          "desc": "Containerize Quarkus application using Docker"
        },
        {
          "id": "5.2",
          "agent": "DevOps (Deployer)",
          "desc": "Ensure seamless deployment on GKE"
        },
        {
          "id": "5.3",
          "agent": "Tester",
          "desc": "Test deployment on GKE"
        }
      ]
    },
    {
      "day": 6,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 6",
      "sub_tasks": [
        {
          "id": "6.1",
          "agent": "Reviewer",
          "desc": "Review code for adherence to coding standards, security, and scalability"
        },
        {
          "id": "6.2",
          "agent": "Coder",
          "desc": "Address feedback and complete any remaining tasks"
        },
        {
          "id": "6.3",
          "agent": "Tester",
          "desc": "Re-test any updated features"
        }
      ]
    },
    {
      "day": 7,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 7",
      "sub_tasks": [
        {
          "id": "7.1",
          "agent": "DevOps (Deployer)",
          "desc": "Finalize deployment scripts and ensure zero-downtime deployments"
        },
        {
          "id": "7.2",
          "agent": "Reviewer",
          "desc": "Verify that all tasks are complete and meet the Definition of Done (DoD)"
        },
        {
          "id": "7.3",
          "agent": "Coder",
          "desc": "Document any remaining technical debt or future improvements"
        }
      ]
    }
  ]
}
```

This JSON schema adheres to the specified requirements, including the extraction of daily steps, checklists, and agent tasks from the provided Phase 2 Context Markdown. Each day is represented as an object within the `days` array, containing the day number, context file, context section, and an array of sub-tasks assigned to specific agents. The sub-tasks include a unique identifier, the assigned agent, and a detailed description of the task.
```

# Phase 3 STEPS - Prompt:


                    Analyze the attached Phase 3 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-3.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 3 CONTEXT MARKDOWN ---
                    ## PHASE 3 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 3 is to develop the web and mobile applications for the membership-hub project. This phase will focus on creating a user-friendly interface for students to manage their attendance and for centers to track student activity. The key deliverables for this phase include:
- Developing the web application using Next.js
- Implementing QR code scanning for attendance tracking
- Integrating multi-language support for both web and mobile applications
- Ensuring SEO optimization for the web application
- Building the mobile application for both iOS and Android platforms

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 3 will be limited to the frontend development of the web and mobile applications. The following directories, files, and endpoints are in scope:
- `web-app/`: Directory for the web application code
- `mobile-app/`: Directory for the mobile application code
- `api/`: Directory for API endpoints for frontend-backend interaction
- `components/`: Directory for reusable UI components
- `locales/`: Directory for language translations
- Endpoints for:
  - QR code scanning
  - Attendance tracking
  - User profile management
  - Language selection

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 3, with the following tasks:
- **Coder**: Develop the web and mobile applications, implement QR code scanning, multi-language support, and SEO optimization
- **Tester**: Test the web and mobile applications for functionality, performance, and security
- **Reviewer**: Review the code for adherence to coding standards, best practices, and security guidelines
- **DevOps (Docker)**: Containerize the web application for deployment on GKE
- **DevOps (Deployer)**: Prepare the environment for deployment, ensure zero-downtime deployments

#### 4. Phase Definition of Done (DoD)
Phase 3 will be considered complete when the following conditions are met:
- The web application is fully functional, with QR code scanning, multi-language support, and SEO optimization
- The mobile application is fully functional, with QR code scanning, multi-language support, and push notifications
- All code has been reviewed and approved by the Reviewer
- The web application has been containerized and is ready for deployment on GKE
- The mobile application has been built and is ready for deployment on app stores
- All testing has been completed, and the application has been verified to meet the requirements and quality standards.
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
### Phase 3 Context JSON Schema

Based on the provided Phase 3 Context Markdown content, the following JSON schema is generated:

```json
{
  "phase_id": 3,
  "phase_name": "Phase 3",
  "project_name": "Membership-Hub Project",
  "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": ".ai/.plan/.context/phase-3.context.blueprint.md",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "1.1",
          "agent": "Coder",
          "desc": "Develop the web application using Next.js"
        },
        {
          "id": "1.2",
          "agent": "Coder",
          "desc": "Implement QR code scanning for attendance tracking"
        },
        {
          "id": "1.3",
          "agent": "Coder",
          "desc": "Integrate multi-language support for the web application"
        },
        {
          "id": "1.4",
          "agent": "DevOps (Docker)",
          "desc": "Containerize the web application for deployment on GKE"
        }
      ]
    },
    {
      "day": 0,
      "context_file": ".ai/.plan/.context/phase-3.context.blueprint.md",
      "context_section": "DAY 0",
      "sub_tasks": [
        {
          "id": "0.1",
          "agent": "Tester",
          "desc": "Test the web and mobile applications for functionality, performance, and security"
        },
        {
          "id": "0.2",
          "agent": "Reviewer",
          "desc": "Review the code for adherence to coding standards, best practices, and security guidelines"
        },
        {
          "id": "0.3",
          "agent": "DevOps (Deployer)",
          "desc": "Prepare the environment for deployment, ensure zero-downtime deployments"
        },
        {
          "id": "0.4",
          "agent": "Coder",
          "desc": "Ensure SEO optimization for the web application"
        }
      ]
    }
  ]
}
```

Note that since there are no explicit daily steps or checklists provided in the Markdown content, the tasks are inferred from the phase objectives, technical scope, and sub-agent functional directives. The tasks are assigned to the corresponding agents based on their roles and responsibilities. The `day` field is set to 1 and 0, respectively, as per the instructions, and the `context_section` field is set to "DAY 1" and "DAY 0", respectively. The `global_context_file` and `source_target_dir` fields are populated with the exact string values as specified in the instructions.
```

# Phase 4 STEPS - Prompt:


                    Analyze the attached Phase 4 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-4.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 4 CONTEXT MARKDOWN ---
                    ## PHASE 4 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 4 is to conduct thorough testing and quality assurance of the membership-hub project. This phase will focus on ensuring the application's functionality, performance, and security meet the required standards. The scope of this phase includes:

* Unit testing of individual components
* Integration testing of interconnected components
* Performance testing to ensure scalability and reliability
* Security testing to identify vulnerabilities
* User acceptance testing (UAT) to validate the application's functionality

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope of this phase is limited to the testing and quality assurance of the existing codebase. The following directories and files are within the scope:

* `src/test`: Unit tests and integration tests
* `src/main`: Application codebase
* `docker-compose.yml`: Docker configuration for testing
* `kafka-config.properties`: Kafka configuration for testing
* `postgres-config.properties`: Postgres configuration for testing
* API endpoints for testing:
	+ `/api/v1/auth`
	+ `/api/v1/attendance`
	+ `/api/v1/notifications`

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in this phase:

* **Coder**: Assist in writing unit tests and integration tests
* **Tester**: Conduct thorough testing of the application, including performance testing and security testing
* **Reviewer**: Review test cases and provide feedback on test coverage and effectiveness
* **DevOps**: Configure and manage the testing environment, including Docker and Kafka

Tasks:

* Coder:
	+ Write unit tests for individual components (Days 1-2)
	+ Write integration tests for interconnected components (Days 2-3)
* Tester:
	+ Conduct performance testing (Days 1-2)
	+ Conduct security testing (Days 2-3)
	+ Conduct UAT (Days 3-4)
* Reviewer:
	+ Review test cases (Days 1-2)
	+ Provide feedback on test coverage and effectiveness (Days 2-3)
* DevOps:
	+ Configure testing environment (Day 1)
	+ Manage testing environment (Days 1-4)

#### 4. Phase Definition of Done (DoD)
The phase is considered complete when:

* All unit tests and integration tests have been written and executed successfully
* Performance testing and security testing have been conducted, and results have been reviewed and addressed
* UAT has been conducted, and results have been reviewed and addressed
* Test coverage is at least 80%
* All test cases have been reviewed and feedback has been incorporated
* The testing environment has been properly configured and managed

The phase will be stopped once the core technical objectives are satisfied, and the phase's definition of done has been met. The maximum duration for this phase is 7 days.
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Based on the provided Phase 4 Context Markdown content, I will extract and translate the daily steps, checklists, and agent tasks into a JSON schema.

Here is the resulting JSON object:

```json
{
  "phase_id": 4,
  "phase_name": "Phase 4",
  "project_name": "test-ai-architecture",
  "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": ".ai/.plan/.context/phase-4.context.blueprint.md",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "1.1",
          "agent": "Coder",
          "desc": "Write unit tests for individual components"
        },
        {
          "id": "1.2",
          "agent": "Tester",
          "desc": "Conduct performance testing"
        },
        {
          "id": "1.3",
          "agent": "Reviewer",
          "desc": "Review test cases"
        },
        {
          "id": "1.4",
          "agent": "DevOps",
          "desc": "Configure testing environment"
        }
      ]
    },
    {
      "day": 2,
      "context_file": ".ai/.plan/.context/phase-4.context.blueprint.md",
      "context_section": "DAY 2",
      "sub_tasks": [
        {
          "id": "2.1",
          "agent": "Coder",
          "desc": "Write unit tests for individual components"
        },
        {
          "id": "2.2",
          "agent": "Tester",
          "desc": "Conduct performance testing"
        },
        {
          "id": "2.3",
          "agent": "Reviewer",
          "desc": "Review test cases"
        },
        {
          "id": "2.4",
          "agent": "DevOps",
          "desc": "Manage testing environment"
        },
        {
          "id": "2.5",
          "agent": "Coder",
          "desc": "Write integration tests for interconnected components"
        },
        {
          "id": "2.6",
          "agent": "Tester",
          "desc": "Conduct security testing"
        }
      ]
    },
    {
      "day": 3,
      "context_file": ".ai/.plan/.context/phase-4.context.blueprint.md",
      "context_section": "DAY 3",
      "sub_tasks": [
        {
          "id": "3.1",
          "agent": "Coder",
          "desc": "Write integration tests for interconnected components"
        },
        {
          "id": "3.2",
          "agent": "Tester",
          "desc": "Conduct security testing"
        },
        {
          "id": "3.3",
          "agent": "Reviewer",
          "desc": "Provide feedback on test coverage and effectiveness"
        },
        {
          "id": "3.4",
          "agent": "DevOps",
          "desc": "Manage testing environment"
        },
        {
          "id": "3.5",
          "agent": "Tester",
          "desc": "Conduct UAT"
        }
      ]
    },
    {
      "day": 4,
      "context_file": ".ai/.plan/.context/phase-4.context.blueprint.md",
      "context_section": "DAY 4",
      "sub_tasks": [
        {
          "id": "4.1",
          "agent": "Tester",
          "desc": "Conduct UAT"
        },
        {
          "id": "4.2",
          "agent": "DevOps",
          "desc": "Manage testing environment"
        }
      ]
    }
  ]
}
```

Note that I've followed the instructions to:

* Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
* Populate the exact string "sources/" into the 'source_target_dir' field.
* Provide a sequential task description text into the 'task' field (now 'desc' field in the SubAgentTask object).
* Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent' field.
* Set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-4.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number for each day object.
* Conform strictly to the required JSON Schema layout design structure.
```

# Phase 5 STEPS - Prompt:


                    Analyze the attached Phase 5 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-5.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 5 CONTEXT MARKDOWN ---
                    ## PHASE 5 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 5 is to deploy the membership-hub application on Google Cloud Platform (GCP) and Google Kubernetes Engine (GKE), ensuring a smooth and scalable operation. This phase will focus on:

* Deploying the application on GCP and GKE
* Configuring load balancing and autoscaling
* Ensuring zero-downtime deployments
* Setting up monitoring and logging tools
* Conducting final testing and quality assurance

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 5 includes:

* Deployment scripts and configurations for GCP and GKE
* Docker containerization and orchestration
* Load balancing and autoscaling configurations
* Monitoring and logging tools (e.g., Prometheus, Grafana, ELK Stack)
* API endpoints for deployment and management

Allowed directories and files:

* `deploy/`: deployment scripts and configurations
* `docker/`: Docker containerization and orchestration files
* `k8s/`: Kubernetes configurations and deployments
* `monitoring/`: monitoring and logging tools configurations

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 5:

* **Coder**: Responsible for creating deployment scripts and configurations, as well as ensuring the application is containerized and ready for deployment.
* **Tester**: Responsible for conducting final testing and quality assurance, including load testing and performance testing.
* **Reviewer**: Responsible for reviewing deployment scripts and configurations, as well as ensuring that the application is properly secured and compliant with regulatory requirements.
* **DevOps**: Responsible for deploying the application on GCP and GKE, configuring load balancing and autoscaling, and setting up monitoring and logging tools.
* **Docker**: Responsible for ensuring the application is properly containerized and orchestrated.
* **Deployer**: Responsible for deploying the application on GCP and GKE, and ensuring zero-downtime deployments.

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 5 includes:

* The application is successfully deployed on GCP and GKE
* Load balancing and autoscaling are properly configured
* Monitoring and logging tools are set up and functioning correctly
* Final testing and quality assurance have been completed
* The application is properly secured and compliant with regulatory requirements
* Deployment scripts and configurations are reviewed and approved
* The application is fully functional and performing as expected

Once these objectives are met, Phase 5 will be considered complete, and the project will be ready for maintenance and ongoing updates.
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Based on the provided Phase 5 Context Markdown content, I will extract and translate the daily steps, checklists, and agent tasks into a JSON schema.

Since the markdown content does not explicitly provide daily steps, I will parse the paragraph descriptions into technical sub-tasks for each day. According to the instructions, I will generate a day object node inside the 'days' array for every single day within the requested range [1 to 0]. However, since the range is from Day 1 to Day 0 (inclusive), I will only generate a day object node for Day 1, as Day 0 is not a valid day.

Here is the translated JSON schema:

```json
{
  "phase_id": 5,
  "phase_name": "Phase 5",
  "project_name": "test-ai-architecture",
  "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": ".ai/.plan/.context/phase-5.context.blueprint.md",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "1.1",
          "agent": "Coder",
          "desc": "Create deployment scripts and configurations for GCP and GKE"
        },
        {
          "id": "1.2",
          "agent": "Coder",
          "desc": "Ensure the application is containerized and ready for deployment"
        },
        {
          "id": "1.3",
          "agent": "Tester",
          "desc": "Conduct final testing and quality assurance, including load testing and performance testing"
        },
        {
          "id": "1.4",
          "agent": "Reviewer",
          "desc": "Review deployment scripts and configurations, and ensure the application is properly secured and compliant with regulatory requirements"
        },
        {
          "id": "1.5",
          "agent": "DevOps",
          "desc": "Deploy the application on GCP and GKE, configure load balancing and autoscaling, and set up monitoring and logging tools"
        },
        {
          "id": "1.6",
          "agent": "Docker",
          "desc": "Ensure the application is properly containerized and orchestrated"
        },
        {
          "id": "1.7",
          "agent": "Deployer",
          "desc": "Deploy the application on GCP and GKE, and ensure zero-downtime deployments"
        }
      ]
    }
  ]
}
```

Note that I have generated sub-tasks for each agent based on the paragraph descriptions in the markdown content. The sub-tasks are assigned to the corresponding agents, and the day object node is generated for Day 1. The `global_context_file` and `source_target_dir` fields are populated with the exact string values as specified in the instructions.
```

# Phase 1 STEPS - Prompt:


                    Analyze the attached Phase 1 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-1.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 1 CONTEXT MARKDOWN ---
                    ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed project plan, and set up the development environment. This phase will focus on planning and setup, ensuring that all necessary components are in place for the successful execution of the project. The key deliverables for this phase include:
- A detailed project plan outlining the scope, timeline, and resources required
- A setup development environment with the necessary tools and technologies (Quarkus, Kafka, Postgres, Docker)
- Definition of the project's technical architecture and high-level design

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 1 includes:
- Setting up the project directory structure
- Initializing the Git repository
- Creating a basic Quarkus project template
- Setting up Kafka and Postgres for messaging and data storage
- Configuring Docker for containerization
- Defining the API endpoints for authentication, attendance tracking, and notification systems
- Creating a high-level design document outlining the system architecture

The allowed directory boundaries include:
- `src/main/java` for Java source code
- `src/main/resources` for configuration files and resources
- `docker` for Docker configuration files
- `kafka` for Kafka configuration files
- `postgres` for Postgres configuration files

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 1:
- **Coder**: Responsible for setting up the Quarkus project template, configuring Kafka and Postgres, and defining the API endpoints.
- **Tester**: Not actively involved in this phase, but will review the project plan and technical architecture.
- **Reviewer**: Responsible for reviewing the project plan, technical architecture, and high-level design document.
- **DevOps (Docker)**: Responsible for setting up the Docker configuration and ensuring containerization.
- **Deployer**: Not actively involved in this phase, but will review the project plan and technical architecture.

#### 4. Phase Definition of Done (DoD)
Phase 1 is considered complete when:
- The project plan is finalized and approved by all stakeholders
- The development environment is set up and configured
- The Quarkus project template is created and configured
- Kafka and Postgres are set up and configured
- Docker is configured for containerization
- The high-level design document is completed and approved by all stakeholders
- The project directory structure is initialized and the Git repository is set up

The expected duration for Phase 1 is 3 days, with the following milestones:
- Day 1: Project planning and scope definition
- Day 2: Setup of development environment and Quarkus project template
- Day 3: Configuration of Kafka, Postgres, and Docker, and completion of high-level design document
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 429 - {'error': {'message': 'Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx7x6rbpftmr50sr2yyb78qm` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 97659, Requested 5828. Please try again in 50m12.768s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
```

# Phase 1 STEPS - Prompt:


                    Analyze the attached Phase 1 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-1.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 1 CONTEXT MARKDOWN ---
                    ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed project plan, and set up the development environment. This phase will focus on planning and setup, ensuring that all necessary components are in place for the successful execution of the project. The key deliverables for this phase include:
- A detailed project plan outlining the scope, timeline, and resources required
- A setup development environment with the necessary tools and technologies (Quarkus, Kafka, Postgres, Docker)
- Definition of the project's technical architecture and high-level design

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 1 includes:
- Setting up the project directory structure
- Initializing the Git repository
- Creating a basic Quarkus project template
- Setting up Kafka and Postgres for messaging and data storage
- Configuring Docker for containerization
- Defining the API endpoints for authentication, attendance tracking, and notification systems
- Creating a high-level design document outlining the system architecture

The allowed directory boundaries include:
- `src/main/java` for Java source code
- `src/main/resources` for configuration files and resources
- `docker` for Docker configuration files
- `kafka` for Kafka configuration files
- `postgres` for Postgres configuration files

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 1:
- **Coder**: Responsible for setting up the Quarkus project template, configuring Kafka and Postgres, and defining the API endpoints.
- **Tester**: Not actively involved in this phase, but will review the project plan and technical architecture.
- **Reviewer**: Responsible for reviewing the project plan, technical architecture, and high-level design document.
- **DevOps (Docker)**: Responsible for setting up the Docker configuration and ensuring containerization.
- **Deployer**: Not actively involved in this phase, but will review the project plan and technical architecture.

#### 4. Phase Definition of Done (DoD)
Phase 1 is considered complete when:
- The project plan is finalized and approved by all stakeholders
- The development environment is set up and configured
- The Quarkus project template is created and configured
- Kafka and Postgres are set up and configured
- Docker is configured for containerization
- The high-level design document is completed and approved by all stakeholders
- The project directory structure is initialized and the Git repository is set up

The expected duration for Phase 1 is 3 days, with the following milestones:
- Day 1: Project planning and scope definition
- Day 2: Setup of development environment and Quarkus project template
- Day 3: Configuration of Kafka, Postgres, and Docker, and completion of high-level design document
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 404 - {'error': {'message': 'This model is unavailable for free. The paid version is available now - use this slug instead: meta-llama/llama-3.3-70b-instruct', 'code': 404}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:


                    Analyze the attached Phase 1 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-1.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 1 CONTEXT MARKDOWN ---
                    ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed project plan, and set up the development environment. This phase will focus on planning and setup, ensuring that all necessary components are in place for the successful execution of the project. The key deliverables for this phase include:
- A detailed project plan outlining the scope, timeline, and resources required
- A setup development environment with the necessary tools and technologies (Quarkus, Kafka, Postgres, Docker)
- Definition of the project's technical architecture and high-level design

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 1 includes:
- Setting up the project directory structure
- Initializing the Git repository
- Creating a basic Quarkus project template
- Setting up Kafka and Postgres for messaging and data storage
- Configuring Docker for containerization
- Defining the API endpoints for authentication, attendance tracking, and notification systems
- Creating a high-level design document outlining the system architecture

The allowed directory boundaries include:
- `src/main/java` for Java source code
- `src/main/resources` for configuration files and resources
- `docker` for Docker configuration files
- `kafka` for Kafka configuration files
- `postgres` for Postgres configuration files

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 1:
- **Coder**: Responsible for setting up the Quarkus project template, configuring Kafka and Postgres, and defining the API endpoints.
- **Tester**: Not actively involved in this phase, but will review the project plan and technical architecture.
- **Reviewer**: Responsible for reviewing the project plan, technical architecture, and high-level design document.
- **DevOps (Docker)**: Responsible for setting up the Docker configuration and ensuring containerization.
- **Deployer**: Not actively involved in this phase, but will review the project plan and technical architecture.

#### 4. Phase Definition of Done (DoD)
Phase 1 is considered complete when:
- The project plan is finalized and approved by all stakeholders
- The development environment is set up and configured
- The Quarkus project template is created and configured
- Kafka and Postgres are set up and configured
- Docker is configured for containerization
- The high-level design document is completed and approved by all stakeholders
- The project directory structure is initialized and the Git repository is set up

The expected duration for Phase 1 is 3 days, with the following milestones:
- Day 1: Project planning and scope definition
- Day 2: Setup of development environment and Quarkus project template
- Day 3: Configuration of Kafka, Postgres, and Docker, and completion of high-level design document
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
### Phase 1 Context JSON Schema

Based on the provided Phase 1 Context Markdown content, the following JSON schema is generated:

```json
{
  "phase_id": 1,
  "phase_name": "Phase 1",
  "project_name": "test-ai-architecture",
  "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": ".ai/.plan/.context/phase-1.context.blueprint.md",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "1.1",
          "agent": "Coder",
          "desc": "Define project scope and objectives"
        },
        {
          "id": "1.2",
          "agent": "Coder",
          "desc": "Create a detailed project plan outlining the scope, timeline, and resources required"
        },
        {
          "id": "1.3",
          "agent": "Reviewer",
          "desc": "Review the project plan and technical architecture"
        }
      ]
    },
    {
      "day": 2,
      "context_file": ".ai/.plan/.context/phase-1.context.blueprint.md",
      "context_section": "DAY 2",
      "sub_tasks": [
        {
          "id": "2.1",
          "agent": "Coder",
          "desc": "Set up the development environment with the necessary tools and technologies (Quarkus, Kafka, Postgres, Docker)"
        },
        {
          "id": "2.2",
          "agent": "Coder",
          "desc": "Create a basic Quarkus project template"
        },
        {
          "id": "2.3",
          "agent": "DevOps (Docker)",
          "desc": "Set up the Docker configuration and ensure containerization"
        }
      ]
    },
    {
      "day": 3,
      "context_file": ".ai/.plan/.context/phase-1.context.blueprint.md",
      "context_section": "DAY 3",
      "sub_tasks": [
        {
          "id": "3.1",
          "agent": "Coder",
          "desc": "Configure Kafka and Postgres for messaging and data storage"
        },
        {
          "id": "3.2",
          "agent": "Coder",
          "desc": "Define the API endpoints for authentication, attendance tracking, and notification systems"
        },
        {
          "id": "3.3",
          "agent": "Reviewer",
          "desc": "Review the high-level design document outlining the system architecture"
        }
      ]
    }
  ]
}
```

This JSON schema captures the daily steps, checklists, and agent tasks as specified in the Phase 1 Context Markdown content. It adheres to the required JSON Schema layout design structure and includes all the necessary fields and values.
```

# Phase 2 STEPS - Prompt:


                    Analyze the attached Phase 2 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-2.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 2 CONTEXT MARKDOWN ---
                    ## PHASE 2 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 2 is to develop the backend features of the membership-hub project, including authentication, attendance tracking, and notification systems. This phase will focus on building a scalable and secure backend using Quarkus, Kafka, and Postgres. The key deliverables for this phase include:
- Design and implementation of authentication mechanisms (email/password, Firebase, Google, Facebook)
- Development of attendance tracking features (QR code-based attendance tracking)
- Implementation of notification systems (SMS, Zalo, in-app notifications)
- Integration with Postgres database for data storage
- Containerization using Docker for seamless deployment on GKE

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 2 will be limited to the backend development, with the following directory boundaries:
- `src/main/java`: Java source code for Quarkus application
- `src/main/resources`: Configuration files and static resources
- `docker`: Dockerfile and containerization scripts
- `kafka`: Kafka configuration and topic definitions
- `postgres`: Postgres database schema and migration scripts
- `api`: API endpoints for authentication, attendance tracking, and notification systems
Allowed endpoints:
- `/api/auth`: Authentication endpoints (login, logout, register)
- `/api/attendance`: Attendance tracking endpoints (QR code scanning, attendance logging)
- `/api/notifications`: Notification endpoints (SMS, Zalo, in-app notifications)

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
- **Coder**: Implement authentication mechanisms, attendance tracking features, and notification systems. Develop API endpoints for backend features.
- **Tester**: Develop unit tests and integration tests for backend features. Test authentication, attendance tracking, and notification systems.
- **Reviewer**: Review code for adherence to coding standards, security, and scalability. Provide feedback on API endpoint design and implementation.
- **DevOps (Docker)**: Containerize the Quarkus application using Docker. Ensure seamless deployment on GKE.
- **DevOps (Deployer)**: Prepare deployment scripts for GCP and GKE. Ensure zero-downtime deployments.

#### 4. Phase Definition of Done (DoD)
Phase 2 is considered complete when:
- All backend features (authentication, attendance tracking, notification systems) are implemented and tested.
- API endpoints are designed and implemented for backend features.
- Code is reviewed and meets coding standards, security, and scalability requirements.
- Docker containerization is complete, and deployment scripts are prepared for GCP and GKE.
- Unit tests and integration tests are developed and passed for backend features.
The maximum duration for Phase 2 is 7 days. Once the core technical objectives are satisfied, the phase will be considered complete, and progression to Phase 3 will begin.
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
### Phase 2 Context JSON Schema

Based on the provided Markdown content, the following JSON schema represents the extracted daily steps, checklists, and agent tasks:

```json
{
  "phase_id": 2,
  "phase_name": "Phase 2",
  "project_name": "test-ai-architecture",
  "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "1.1",
          "agent": "Coder",
          "desc": "Implement authentication mechanisms (email/password, Firebase, Google, Facebook)"
        },
        {
          "id": "1.2",
          "agent": "Tester",
          "desc": "Develop unit tests and integration tests for authentication mechanisms"
        },
        {
          "id": "1.3",
          "agent": "Reviewer",
          "desc": "Review code for adherence to coding standards, security, and scalability"
        }
      ]
    },
    {
      "day": 2,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 2",
      "sub_tasks": [
        {
          "id": "2.1",
          "agent": "Coder",
          "desc": "Develop attendance tracking features (QR code-based attendance tracking)"
        },
        {
          "id": "2.2",
          "agent": "Tester",
          "desc": "Develop unit tests and integration tests for attendance tracking features"
        },
        {
          "id": "2.3",
          "agent": "DevOps (Docker)",
          "desc": "Containerize the Quarkus application using Docker"
        }
      ]
    },
    {
      "day": 3,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 3",
      "sub_tasks": [
        {
          "id": "3.1",
          "agent": "Coder",
          "desc": "Implement notification systems (SMS, Zalo, in-app notifications)"
        },
        {
          "id": "3.2",
          "agent": "Tester",
          "desc": "Develop unit tests and integration tests for notification systems"
        },
        {
          "id": "3.3",
          "agent": "Reviewer",
          "desc": "Review code for adherence to coding standards, security, and scalability"
        }
      ]
    },
    {
      "day": 4,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 4",
      "sub_tasks": [
        {
          "id": "4.1",
          "agent": "Coder",
          "desc": "Develop API endpoints for authentication, attendance tracking, and notification systems"
        },
        {
          "id": "4.2",
          "agent": "Tester",
          "desc": "Develop unit tests and integration tests for API endpoints"
        },
        {
          "id": "4.3",
          "agent": "DevOps (Deployer)",
          "desc": "Prepare deployment scripts for GCP and GKE"
        }
      ]
    },
    {
      "day": 5,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 5",
      "sub_tasks": [
        {
          "id": "5.1",
          "agent": "Coder",
          "desc": "Integrate with Postgres database for data storage"
        },
        {
          "id": "5.2",
          "agent": "Tester",
          "desc": "Develop unit tests and integration tests for database integration"
        },
        {
          "id": "5.3",
          "agent": "Reviewer",
          "desc": "Review code for adherence to coding standards, security, and scalability"
        }
      ]
    },
    {
      "day": 6,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 6",
      "sub_tasks": [
        {
          "id": "6.1",
          "agent": "DevOps (Docker)",
          "desc": "Ensure seamless deployment on GKE"
        },
        {
          "id": "6.2",
          "agent": "DevOps (Deployer)",
          "desc": "Ensure zero-downtime deployments"
        },
        {
          "id": "6.3",
          "agent": "Tester",
          "desc": "Develop unit tests and integration tests for deployment scripts"
        }
      ]
    },
    {
      "day": 7,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 7",
      "sub_tasks": [
        {
          "id": "7.1",
          "agent": "Coder",
          "desc": "Finalize implementation of all backend features"
        },
        {
          "id": "7.2",
          "agent": "Tester",
          "desc": "Finalize unit tests and integration tests for all backend features"
        },
        {
          "id": "7.3",
          "agent": "Reviewer",
          "desc": "Final review of code for adherence to coding standards, security, and scalability"
        }
      ]
    }
  ]
}
```

This JSON schema represents the daily steps, checklists, and agent tasks for Phase 2 of the project. Each day has a set of sub-tasks assigned to specific agents, and the context file and section are specified for each day. The global context file and source target directory are also specified.
```

# Phase 3 STEPS - Prompt:


                    Analyze the attached Phase 3 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-3.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 3 CONTEXT MARKDOWN ---
                    ## PHASE 3 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 3 is to develop the web and mobile applications for the membership-hub project. This phase will focus on creating a user-friendly interface for students to manage their attendance and for centers to track student activity. The key deliverables for this phase include:
- Developing the web application using Next.js
- Implementing QR code scanning for attendance tracking
- Integrating multi-language support for both web and mobile applications
- Ensuring SEO optimization for the web application
- Building the mobile application for both iOS and Android platforms

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 3 will be limited to the frontend development of the web and mobile applications. The following directories, files, and endpoints are in scope:
- `web-app/`: Directory for the web application code
- `mobile-app/`: Directory for the mobile application code
- `api/`: Directory for API endpoints for frontend-backend interaction
- `components/`: Directory for reusable UI components
- `locales/`: Directory for language translations
- Endpoints for:
  - QR code scanning
  - Attendance tracking
  - User profile management
  - Language selection

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 3, with the following tasks:
- **Coder**: Develop the web and mobile applications, implement QR code scanning, multi-language support, and SEO optimization
- **Tester**: Test the web and mobile applications for functionality, performance, and security
- **Reviewer**: Review the code for adherence to coding standards, best practices, and security guidelines
- **DevOps (Docker)**: Containerize the web application for deployment on GKE
- **DevOps (Deployer)**: Prepare the environment for deployment, ensure zero-downtime deployments

#### 4. Phase Definition of Done (DoD)
Phase 3 will be considered complete when the following conditions are met:
- The web application is fully functional, with QR code scanning, multi-language support, and SEO optimization
- The mobile application is fully functional, with QR code scanning, multi-language support, and push notifications
- All code has been reviewed and approved by the Reviewer
- The web application has been containerized and is ready for deployment on GKE
- The mobile application has been built and is ready for deployment on app stores
- All testing has been completed, and the application has been verified to meet the requirements and quality standards.
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
### Phase 3 Context JSON Schema

Based on the provided Phase 3 Context Markdown content, the following JSON schema is generated:

```json
{
  "phase_id": 3,
  "phase_name": "Phase 3",
  "project_name": "Membership-Hub Project",
  "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": ".ai/.plan/.context/phase-3.context.blueprint.md",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "ST-1",
          "agent": "Coder",
          "desc": "Develop the web application using Next.js"
        },
        {
          "id": "ST-2",
          "agent": "Coder",
          "desc": "Implement QR code scanning for attendance tracking"
        },
        {
          "id": "ST-3",
          "agent": "Coder",
          "desc": "Integrate multi-language support for the web application"
        },
        {
          "id": "ST-4",
          "agent": "DevOps (Docker)",
          "desc": "Containerize the web application for deployment on GKE"
        }
      ]
    },
    {
      "day": 0,
      "context_file": ".ai/.plan/.context/phase-3.context.blueprint.md",
      "context_section": "DAY 0",
      "sub_tasks": [
        {
          "id": "ST-5",
          "agent": "Tester",
          "desc": "Test the web and mobile applications for functionality, performance, and security"
        },
        {
          "id": "ST-6",
          "agent": "Reviewer",
          "desc": "Review the code for adherence to coding standards, best practices, and security guidelines"
        },
        {
          "id": "ST-7",
          "agent": "DevOps (Deployer)",
          "desc": "Prepare the environment for deployment, ensure zero-downtime deployments"
        },
        {
          "id": "ST-8",
          "agent": "Coder",
          "desc": "Build the mobile application for both iOS and Android platforms"
        }
      ]
    }
  ]
}
```

Note that the tasks are distributed across the days based on the provided markdown content. The tasks for Day 1 focus on developing the web application, while the tasks for Day 0 focus on testing, reviewing, and deploying the applications. The agents assigned to each task are based on the dedicated sub-agent functional directives provided in the markdown content.
```

# Phase 4 STEPS - Prompt:


                    Analyze the attached Phase 4 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-4.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 4 CONTEXT MARKDOWN ---
                    ## PHASE 4 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 4 is to conduct thorough testing and quality assurance of the membership-hub project. This phase will focus on ensuring the application's functionality, performance, and security meet the required standards. The scope of this phase includes:

* Unit testing of individual components
* Integration testing of interconnected components
* Performance testing to ensure scalability and reliability
* Security testing to identify vulnerabilities
* User acceptance testing (UAT) to validate the application's functionality

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope of this phase is limited to the testing and quality assurance of the existing codebase. The following directories and files are within the scope:

* `src/test`: Unit tests and integration tests
* `src/main`: Application codebase
* `docker-compose.yml`: Docker configuration for testing
* `kafka-config.properties`: Kafka configuration for testing
* `postgres-config.properties`: Postgres configuration for testing
* API endpoints for testing:
	+ `/api/v1/auth`
	+ `/api/v1/attendance`
	+ `/api/v1/notifications`

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in this phase:

* **Coder**: Assist in writing unit tests and integration tests
* **Tester**: Conduct thorough testing of the application, including performance testing and security testing
* **Reviewer**: Review test cases and provide feedback on test coverage and effectiveness
* **DevOps**: Configure and manage the testing environment, including Docker and Kafka

Tasks:

* Coder:
	+ Write unit tests for individual components (Days 1-2)
	+ Write integration tests for interconnected components (Days 2-3)
* Tester:
	+ Conduct performance testing (Days 1-2)
	+ Conduct security testing (Days 2-3)
	+ Conduct UAT (Days 3-4)
* Reviewer:
	+ Review test cases (Days 1-2)
	+ Provide feedback on test coverage and effectiveness (Days 2-3)
* DevOps:
	+ Configure testing environment (Day 1)
	+ Manage testing environment (Days 1-4)

#### 4. Phase Definition of Done (DoD)
The phase is considered complete when:

* All unit tests and integration tests have been written and executed successfully
* Performance testing and security testing have been conducted, and results have been reviewed and addressed
* UAT has been conducted, and results have been reviewed and addressed
* Test coverage is at least 80%
* All test cases have been reviewed and feedback has been incorporated
* The testing environment has been properly configured and managed

The phase will be stopped once the core technical objectives are satisfied, and the phase's definition of done has been met. The maximum duration for this phase is 7 days.
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Based on the provided Phase 4 Context Markdown content, I will extract and translate the daily steps, checklists, and agent tasks into the required JSON schema.

Here is the resulting JSON object:

```json
{
  "phase_id": 4,
  "phase_name": "Phase 4",
  "project_name": "test-ai-architecture",
  "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": ".ai/.plan/.context/phase-4.context.blueprint.md",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "1.1",
          "agent": "Coder",
          "desc": "Write unit tests for individual components"
        },
        {
          "id": "1.2",
          "agent": "Tester",
          "desc": "Conduct performance testing"
        },
        {
          "id": "1.3",
          "agent": "Reviewer",
          "desc": "Review test cases"
        },
        {
          "id": "1.4",
          "agent": "DevOps",
          "desc": "Configure testing environment"
        }
      ]
    },
    {
      "day": 2,
      "context_file": ".ai/.plan/.context/phase-4.context.blueprint.md",
      "context_section": "DAY 2",
      "sub_tasks": [
        {
          "id": "2.1",
          "agent": "Coder",
          "desc": "Write integration tests for interconnected components"
        },
        {
          "id": "2.2",
          "agent": "Tester",
          "desc": "Conduct security testing"
        },
        {
          "id": "2.3",
          "agent": "Reviewer",
          "desc": "Provide feedback on test coverage and effectiveness"
        },
        {
          "id": "2.4",
          "agent": "DevOps",
          "desc": "Manage testing environment"
        }
      ]
    },
    {
      "day": 3,
      "context_file": ".ai/.plan/.context/phase-4.context.blueprint.md",
      "context_section": "DAY 3",
      "sub_tasks": [
        {
          "id": "3.1",
          "agent": "Tester",
          "desc": "Conduct UAT"
        },
        {
          "id": "3.2",
          "agent": "Reviewer",
          "desc": "Review test cases"
        },
        {
          "id": "3.3",
          "agent": "DevOps",
          "desc": "Manage testing environment"
        }
      ]
    },
    {
      "day": 0,
      "context_file": ".ai/.plan/.context/phase-4.context.blueprint.md",
      "context_section": "DAY 0",
      "sub_tasks": [
        {
          "id": "0.1",
          "agent": "DevOps",
          "desc": "Finalize testing environment configuration"
        }
      ]
    }
  ]
}
```

Note that I've assumed the following:

* The phase ID is 4, and the phase name is "Phase 4".
* The project name is "test-ai-architecture".
* The global context file is ".ai/.context/test-ai-architecture.global.blueprint.md", and the source target directory is "sources/".
* The days array includes four days: 1, 2, 3, and 0 (as per the instruction to include all days between Day 1 and Day 0 inclusive).
* Each day has a context file and context section as specified in the instructions.
* The sub-tasks for each day are based on the tasks listed in the Markdown content, with the agent and description fields populated accordingly.

Please let me know if this meets your requirements or if you need further modifications.
```

# Phase 5 STEPS - Prompt:


                    Analyze the attached Phase 5 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-5.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 5 CONTEXT MARKDOWN ---
                    ## PHASE 5 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 5 is to deploy the membership-hub application on Google Cloud Platform (GCP) and Google Kubernetes Engine (GKE), ensuring a smooth and scalable operation. This phase will focus on:

* Deploying the application on GCP and GKE
* Configuring load balancing and autoscaling
* Ensuring zero-downtime deployments
* Setting up monitoring and logging tools
* Conducting final testing and quality assurance

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 5 includes:

* Deployment scripts and configurations for GCP and GKE
* Docker containerization and orchestration
* Load balancing and autoscaling configurations
* Monitoring and logging tools (e.g., Prometheus, Grafana, ELK Stack)
* API endpoints for deployment and management

Allowed directories and files:

* `deploy/`: deployment scripts and configurations
* `docker/`: Docker containerization and orchestration files
* `k8s/`: Kubernetes configurations and deployments
* `monitoring/`: monitoring and logging tools configurations

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 5:

* **Coder**: Responsible for creating deployment scripts and configurations, as well as ensuring the application is containerized and ready for deployment.
* **Tester**: Responsible for conducting final testing and quality assurance, including load testing and performance testing.
* **Reviewer**: Responsible for reviewing deployment scripts and configurations, as well as ensuring that the application is properly secured and compliant with regulatory requirements.
* **DevOps**: Responsible for deploying the application on GCP and GKE, configuring load balancing and autoscaling, and setting up monitoring and logging tools.
* **Docker**: Responsible for ensuring the application is properly containerized and orchestrated.
* **Deployer**: Responsible for deploying the application on GCP and GKE, and ensuring zero-downtime deployments.

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 5 includes:

* The application is successfully deployed on GCP and GKE
* Load balancing and autoscaling are properly configured
* Monitoring and logging tools are set up and functioning correctly
* Final testing and quality assurance have been completed
* The application is properly secured and compliant with regulatory requirements
* Deployment scripts and configurations are reviewed and approved
* The application is fully functional and performing as expected

Once these objectives are met, Phase 5 will be considered complete, and the project will be ready for maintenance and ongoing updates.
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Based on the provided Phase 5 Context Markdown content, I will extract and translate the daily steps, checklists, and agent tasks into the required JSON schema.

Since the markdown content does not explicitly provide daily steps, I will parse the paragraph descriptions into technical sub-tasks for each day. According to the instructions, I will generate a day object node inside the 'days' array for every single day within the requested range [1 to 0]. However, since the range is invalid (Day 1 to Day 0), I will assume the range is from Day 1 to Day 1 (a single day).

Here is the resulting JSON object:

```json
{
  "phase_id": 5,
  "phase_name": "Phase 5",
  "project_name": "test-ai-architecture",
  "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": ".ai/.plan/.context/phase-5.context.blueprint.md",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "1.1",
          "agent": "Coder",
          "desc": "Create deployment scripts and configurations for GCP and GKE"
        },
        {
          "id": "1.2",
          "agent": "Coder",
          "desc": "Ensure the application is containerized and ready for deployment"
        },
        {
          "id": "1.3",
          "agent": "Tester",
          "desc": "Conduct final testing and quality assurance, including load testing and performance testing"
        },
        {
          "id": "1.4",
          "agent": "Reviewer",
          "desc": "Review deployment scripts and configurations, and ensure the application is properly secured and compliant with regulatory requirements"
        },
        {
          "id": "1.5",
          "agent": "DevOps",
          "desc": "Deploy the application on GCP and GKE, configure load balancing and autoscaling, and set up monitoring and logging tools"
        },
        {
          "id": "1.6",
          "agent": "Docker",
          "desc": "Ensure the application is properly containerized and orchestrated"
        },
        {
          "id": "1.7",
          "agent": "Deployer",
          "desc": "Deploy the application on GCP and GKE, and ensure zero-downtime deployments"
        }
      ]
    }
  ]
}
```

Note that I have assigned tasks to agents based on the "Dedicated Sub-Agent Functional Directives" section in the markdown content. I have also generated a unique ID for each sub-task. If you need any further modifications or have any questions, please let me know.
```

# Phase 1 STEPS - Prompt:


                    Analyze the attached Phase 1 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-1.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 1 CONTEXT MARKDOWN ---
                    ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed project plan, and set up the development environment. This phase will focus on planning and setup, ensuring that all necessary components are in place for the successful execution of the project. The key deliverables for this phase include:
- A detailed project plan outlining the scope, timeline, and resources required
- A setup development environment with the necessary tools and technologies (Quarkus, Kafka, Postgres, Docker)
- Definition of the project's technical architecture and high-level design

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 1 includes:
- Setting up the project directory structure
- Initializing the Git repository
- Creating a basic Quarkus project template
- Setting up Kafka and Postgres for messaging and data storage
- Configuring Docker for containerization
- Defining the API endpoints for authentication, attendance tracking, and notification systems
- Creating a high-level design document outlining the system architecture

The allowed directory boundaries include:
- `src/main/java` for Java source code
- `src/main/resources` for configuration files and resources
- `docker` for Docker configuration files
- `kafka` for Kafka configuration files
- `postgres` for Postgres configuration files

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 1:
- **Coder**: Responsible for setting up the Quarkus project template, configuring Kafka and Postgres, and defining the API endpoints.
- **Tester**: Not actively involved in this phase, but will review the project plan and technical architecture.
- **Reviewer**: Responsible for reviewing the project plan, technical architecture, and high-level design document.
- **DevOps (Docker)**: Responsible for setting up the Docker configuration and ensuring containerization.
- **Deployer**: Not actively involved in this phase, but will review the project plan and technical architecture.

#### 4. Phase Definition of Done (DoD)
Phase 1 is considered complete when:
- The project plan is finalized and approved by all stakeholders
- The development environment is set up and configured
- The Quarkus project template is created and configured
- Kafka and Postgres are set up and configured
- Docker is configured for containerization
- The high-level design document is completed and approved by all stakeholders
- The project directory structure is initialized and the Git repository is set up

The expected duration for Phase 1 is 3 days, with the following milestones:
- Day 1: Project planning and scope definition
- Day 2: Setup of development environment and Quarkus project template
- Day 3: Configuration of Kafka, Postgres, and Docker, and completion of high-level design document
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 429 - {'error': {'message': 'Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx7x6rbpftmr50sr2yyb78qm` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 96664, Requested 5828. Please try again in 35m53.088s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
```

# Phase 1 STEPS - Prompt:


                    Analyze the attached Phase 1 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-1.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 1 CONTEXT MARKDOWN ---
                    ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed project plan, and set up the development environment. This phase will focus on planning and setup, ensuring that all necessary components are in place for the successful execution of the project. The key deliverables for this phase include:
- A detailed project plan outlining the scope, timeline, and resources required
- A setup development environment with the necessary tools and technologies (Quarkus, Kafka, Postgres, Docker)
- Definition of the project's technical architecture and high-level design

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 1 includes:
- Setting up the project directory structure
- Initializing the Git repository
- Creating a basic Quarkus project template
- Setting up Kafka and Postgres for messaging and data storage
- Configuring Docker for containerization
- Defining the API endpoints for authentication, attendance tracking, and notification systems
- Creating a high-level design document outlining the system architecture

The allowed directory boundaries include:
- `src/main/java` for Java source code
- `src/main/resources` for configuration files and resources
- `docker` for Docker configuration files
- `kafka` for Kafka configuration files
- `postgres` for Postgres configuration files

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 1:
- **Coder**: Responsible for setting up the Quarkus project template, configuring Kafka and Postgres, and defining the API endpoints.
- **Tester**: Not actively involved in this phase, but will review the project plan and technical architecture.
- **Reviewer**: Responsible for reviewing the project plan, technical architecture, and high-level design document.
- **DevOps (Docker)**: Responsible for setting up the Docker configuration and ensuring containerization.
- **Deployer**: Not actively involved in this phase, but will review the project plan and technical architecture.

#### 4. Phase Definition of Done (DoD)
Phase 1 is considered complete when:
- The project plan is finalized and approved by all stakeholders
- The development environment is set up and configured
- The Quarkus project template is created and configured
- Kafka and Postgres are set up and configured
- Docker is configured for containerization
- The high-level design document is completed and approved by all stakeholders
- The project directory structure is initialized and the Git repository is set up

The expected duration for Phase 1 is 3 days, with the following milestones:
- Day 1: Project planning and scope definition
- Day 2: Setup of development environment and Quarkus project template
- Day 3: Configuration of Kafka, Postgres, and Docker, and completion of high-level design document
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 404 - {'error': {'message': 'This model is unavailable for free. The paid version is available now - use this slug instead: meta-llama/llama-3.3-70b-instruct', 'code': 404}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:


                    Analyze the attached Phase 1 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-1.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 1 CONTEXT MARKDOWN ---
                    ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed project plan, and set up the development environment. This phase will focus on planning and setup, ensuring that all necessary components are in place for the successful execution of the project. The key deliverables for this phase include:
- A detailed project plan outlining the scope, timeline, and resources required
- A setup development environment with the necessary tools and technologies (Quarkus, Kafka, Postgres, Docker)
- Definition of the project's technical architecture and high-level design

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 1 includes:
- Setting up the project directory structure
- Initializing the Git repository
- Creating a basic Quarkus project template
- Setting up Kafka and Postgres for messaging and data storage
- Configuring Docker for containerization
- Defining the API endpoints for authentication, attendance tracking, and notification systems
- Creating a high-level design document outlining the system architecture

The allowed directory boundaries include:
- `src/main/java` for Java source code
- `src/main/resources` for configuration files and resources
- `docker` for Docker configuration files
- `kafka` for Kafka configuration files
- `postgres` for Postgres configuration files

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 1:
- **Coder**: Responsible for setting up the Quarkus project template, configuring Kafka and Postgres, and defining the API endpoints.
- **Tester**: Not actively involved in this phase, but will review the project plan and technical architecture.
- **Reviewer**: Responsible for reviewing the project plan, technical architecture, and high-level design document.
- **DevOps (Docker)**: Responsible for setting up the Docker configuration and ensuring containerization.
- **Deployer**: Not actively involved in this phase, but will review the project plan and technical architecture.

#### 4. Phase Definition of Done (DoD)
Phase 1 is considered complete when:
- The project plan is finalized and approved by all stakeholders
- The development environment is set up and configured
- The Quarkus project template is created and configured
- Kafka and Postgres are set up and configured
- Docker is configured for containerization
- The high-level design document is completed and approved by all stakeholders
- The project directory structure is initialized and the Git repository is set up

The expected duration for Phase 1 is 3 days, with the following milestones:
- Day 1: Project planning and scope definition
- Day 2: Setup of development environment and Quarkus project template
- Day 3: Configuration of Kafka, Postgres, and Docker, and completion of high-level design document
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Based on the provided Phase 1 Context Markdown content, I will extract and translate the daily steps, checklists, and agent tasks into a JSON schema.

Here is the resulting JSON object:

```json
{
  "phase_id": 1,
  "phase_name": "Phase 1",
  "project_name": "test-ai-architecture",
  "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": ".ai/.plan/.context/phase-1.context.blueprint.md",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "1.1",
          "agent": "Coder",
          "desc": "Define project scope and objectives"
        },
        {
          "id": "1.2",
          "agent": "Coder",
          "desc": "Create a detailed project plan outlining scope, timeline, and resources required"
        },
        {
          "id": "1.3",
          "agent": "Reviewer",
          "desc": "Review project plan and provide feedback"
        }
      ]
    },
    {
      "day": 2,
      "context_file": ".ai/.plan/.context/phase-1.context.blueprint.md",
      "context_section": "DAY 2",
      "sub_tasks": [
        {
          "id": "2.1",
          "agent": "Coder",
          "desc": "Set up development environment with necessary tools and technologies (Quarkus, Kafka, Postgres, Docker)"
        },
        {
          "id": "2.2",
          "agent": "Coder",
          "desc": "Create a basic Quarkus project template"
        },
        {
          "id": "2.3",
          "agent": "DevOps (Docker)",
          "desc": "Set up Docker configuration for containerization"
        }
      ]
    },
    {
      "day": 3,
      "context_file": ".ai/.plan/.context/phase-1.context.blueprint.md",
      "context_section": "DAY 3",
      "sub_tasks": [
        {
          "id": "3.1",
          "agent": "Coder",
          "desc": "Configure Kafka and Postgres for messaging and data storage"
        },
        {
          "id": "3.2",
          "agent": "Coder",
          "desc": "Define API endpoints for authentication, attendance tracking, and notification systems"
        },
        {
          "id": "3.3",
          "agent": "Reviewer",
          "desc": "Review high-level design document and provide feedback"
        },
        {
          "id": "3.4",
          "agent": "DevOps (Docker)",
          "desc": "Ensure containerization is complete and functional"
        }
      ]
    }
  ]
}
```

Note that I've followed the provided JSON schema layout design structure and populated the required fields accordingly. I've also extracted the daily steps, checklists, and agent tasks from the Phase 1 Context Markdown content and translated them into the corresponding JSON objects.
```

# Phase 2 STEPS - Prompt:


                    Analyze the attached Phase 2 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-2.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 2 CONTEXT MARKDOWN ---
                    ## PHASE 2 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 2 is to develop the backend features of the membership-hub project, including authentication, attendance tracking, and notification systems. This phase will focus on building a scalable and secure backend using Quarkus, Kafka, and Postgres. The key deliverables for this phase include:
- Design and implementation of authentication mechanisms (email/password, Firebase, Google, Facebook)
- Development of attendance tracking features (QR code-based attendance tracking)
- Implementation of notification systems (SMS, Zalo, in-app notifications)
- Integration with Postgres database for data storage
- Containerization using Docker for seamless deployment on GKE

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 2 will be limited to the backend development, with the following directory boundaries:
- `src/main/java`: Java source code for Quarkus application
- `src/main/resources`: Configuration files and static resources
- `docker`: Dockerfile and containerization scripts
- `kafka`: Kafka configuration and topic definitions
- `postgres`: Postgres database schema and migration scripts
- `api`: API endpoints for authentication, attendance tracking, and notification systems
Allowed endpoints:
- `/api/auth`: Authentication endpoints (login, logout, register)
- `/api/attendance`: Attendance tracking endpoints (QR code scanning, attendance logging)
- `/api/notifications`: Notification endpoints (SMS, Zalo, in-app notifications)

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
- **Coder**: Implement authentication mechanisms, attendance tracking features, and notification systems. Develop API endpoints for backend features.
- **Tester**: Develop unit tests and integration tests for backend features. Test authentication, attendance tracking, and notification systems.
- **Reviewer**: Review code for adherence to coding standards, security, and scalability. Provide feedback on API endpoint design and implementation.
- **DevOps (Docker)**: Containerize the Quarkus application using Docker. Ensure seamless deployment on GKE.
- **DevOps (Deployer)**: Prepare deployment scripts for GCP and GKE. Ensure zero-downtime deployments.

#### 4. Phase Definition of Done (DoD)
Phase 2 is considered complete when:
- All backend features (authentication, attendance tracking, notification systems) are implemented and tested.
- API endpoints are designed and implemented for backend features.
- Code is reviewed and meets coding standards, security, and scalability requirements.
- Docker containerization is complete, and deployment scripts are prepared for GCP and GKE.
- Unit tests and integration tests are developed and passed for backend features.
The maximum duration for Phase 2 is 7 days. Once the core technical objectives are satisfied, the phase will be considered complete, and progression to Phase 3 will begin.
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
### Translated JSON Schema

Based on the provided Phase 2 Context Markdown, the following JSON schema is generated:

```json
{
  "phase_id": 2,
  "phase_name": "Phase 2",
  "project_name": "test-ai-architecture",
  "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "1.1",
          "agent": "Coder",
          "desc": "Implement authentication mechanisms (email/password, Firebase, Google, Facebook)"
        },
        {
          "id": "1.2",
          "agent": "Tester",
          "desc": "Develop unit tests and integration tests for authentication mechanisms"
        },
        {
          "id": "1.3",
          "agent": "Reviewer",
          "desc": "Review code for adherence to coding standards, security, and scalability"
        }
      ]
    },
    {
      "day": 2,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 2",
      "sub_tasks": [
        {
          "id": "2.1",
          "agent": "Coder",
          "desc": "Develop attendance tracking features (QR code-based attendance tracking)"
        },
        {
          "id": "2.2",
          "agent": "Tester",
          "desc": "Develop unit tests and integration tests for attendance tracking features"
        },
        {
          "id": "2.3",
          "agent": "DevOps (Docker)",
          "desc": "Containerize the Quarkus application using Docker"
        }
      ]
    },
    {
      "day": 3,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 3",
      "sub_tasks": [
        {
          "id": "3.1",
          "agent": "Coder",
          "desc": "Implement notification systems (SMS, Zalo, in-app notifications)"
        },
        {
          "id": "3.2",
          "agent": "Tester",
          "desc": "Develop unit tests and integration tests for notification systems"
        },
        {
          "id": "3.3",
          "agent": "Reviewer",
          "desc": "Review code for adherence to coding standards, security, and scalability"
        }
      ]
    },
    {
      "day": 4,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 4",
      "sub_tasks": [
        {
          "id": "4.1",
          "agent": "Coder",
          "desc": "Develop API endpoints for backend features"
        },
        {
          "id": "4.2",
          "agent": "Tester",
          "desc": "Develop unit tests and integration tests for API endpoints"
        },
        {
          "id": "4.3",
          "agent": "DevOps (Deployer)",
          "desc": "Prepare deployment scripts for GCP and GKE"
        }
      ]
    },
    {
      "day": 5,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 5",
      "sub_tasks": [
        {
          "id": "5.1",
          "agent": "Coder",
          "desc": "Integrate with Postgres database for data storage"
        },
        {
          "id": "5.2",
          "agent": "Tester",
          "desc": "Develop unit tests and integration tests for database integration"
        },
        {
          "id": "5.3",
          "agent": "Reviewer",
          "desc": "Review code for adherence to coding standards, security, and scalability"
        }
      ]
    },
    {
      "day": 6,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 6",
      "sub_tasks": [
        {
          "id": "6.1",
          "agent": "DevOps (Docker)",
          "desc": "Ensure seamless deployment on GKE"
        },
        {
          "id": "6.2",
          "agent": "DevOps (Deployer)",
          "desc": "Ensure zero-downtime deployments"
        },
        {
          "id": "6.3",
          "agent": "Tester",
          "desc": "Develop unit tests and integration tests for deployment scripts"
        }
      ]
    },
    {
      "day": 7,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 7",
      "sub_tasks": [
        {
          "id": "7.1",
          "agent": "Coder",
          "desc": "Finalize implementation of backend features"
        },
        {
          "id": "7.2",
          "agent": "Tester",
          "desc": "Finalize unit tests and integration tests for backend features"
        },
        {
          "id": "7.3",
          "agent": "Reviewer",
          "desc": "Final review of code for adherence to coding standards, security, and scalability"
        }
      ]
    }
  ]
}
```

Note that the tasks are assigned to agents based on the Phase 2 Context Markdown, and the sub-tasks are generated based on the technical objectives and deliverables mentioned in the markdown. The days are numbered from 1 to 7, and each day has a set of sub-tasks assigned to different agents. The context file, context section, and global context file are populated as per the instructions.
```

# Phase 3 STEPS - Prompt:


                    Analyze the attached Phase 3 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-3.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 3 CONTEXT MARKDOWN ---
                    ## PHASE 3 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 3 is to develop the web and mobile applications for the membership-hub project. This phase will focus on creating a user-friendly interface for students to manage their attendance and for centers to track student activity. The key deliverables for this phase include:
- Developing the web application using Next.js
- Implementing QR code scanning for attendance tracking
- Integrating multi-language support for both web and mobile applications
- Ensuring SEO optimization for the web application
- Building the mobile application for both iOS and Android platforms

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 3 will be limited to the frontend development of the web and mobile applications. The following directories, files, and endpoints are in scope:
- `web-app/`: Directory for the web application code
- `mobile-app/`: Directory for the mobile application code
- `api/`: Directory for API endpoints for frontend-backend interaction
- `components/`: Directory for reusable UI components
- `locales/`: Directory for language translations
- Endpoints for:
  - QR code scanning
  - Attendance tracking
  - User profile management
  - Language selection

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 3, with the following tasks:
- **Coder**: Develop the web and mobile applications, implement QR code scanning, multi-language support, and SEO optimization
- **Tester**: Test the web and mobile applications for functionality, performance, and security
- **Reviewer**: Review the code for adherence to coding standards, best practices, and security guidelines
- **DevOps (Docker)**: Containerize the web application for deployment on GKE
- **DevOps (Deployer)**: Prepare the environment for deployment, ensure zero-downtime deployments

#### 4. Phase Definition of Done (DoD)
Phase 3 will be considered complete when the following conditions are met:
- The web application is fully functional, with QR code scanning, multi-language support, and SEO optimization
- The mobile application is fully functional, with QR code scanning, multi-language support, and push notifications
- All code has been reviewed and approved by the Reviewer
- The web application has been containerized and is ready for deployment on GKE
- The mobile application has been built and is ready for deployment on app stores
- All testing has been completed, and the application has been verified to meet the requirements and quality standards.
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Based on the provided Phase 3 Context Markdown content, I will extract and translate the daily steps, checklists, and agent tasks into the required JSON schema.

Since the markdown content does not explicitly provide daily steps, I will parse the paragraph descriptions into technical sub-tasks for each day. According to the instructions, I will generate a day object node inside the 'days' array for every single day within the requested range [1 to 0]. However, since the range is from Day 1 to Day 0 (inclusive), I will assume that there is only one day, which is Day 1, and Day 0 is not a valid day.

Here is the translated JSON schema:

```json
{
  "phase_id": 3,
  "phase_name": "Phase 3",
  "project_name": "test-ai-architecture",
  "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": ".ai/.plan/.context/phase-3.context.blueprint.md",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "1.1",
          "agent": "Coder",
          "desc": "Develop the web application using Next.js"
        },
        {
          "id": "1.2",
          "agent": "Coder",
          "desc": "Implement QR code scanning for attendance tracking"
        },
        {
          "id": "1.3",
          "agent": "Coder",
          "desc": "Integrate multi-language support for both web and mobile applications"
        },
        {
          "id": "1.4",
          "agent": "Coder",
          "desc": "Ensure SEO optimization for the web application"
        },
        {
          "id": "1.5",
          "agent": "Coder",
          "desc": "Build the mobile application for both iOS and Android platforms"
        },
        {
          "id": "1.6",
          "agent": "Tester",
          "desc": "Test the web and mobile applications for functionality, performance, and security"
        },
        {
          "id": "1.7",
          "agent": "Reviewer",
          "desc": "Review the code for adherence to coding standards, best practices, and security guidelines"
        },
        {
          "id": "1.8",
          "agent": "DevOps (Docker)",
          "desc": "Containerize the web application for deployment on GKE"
        },
        {
          "id": "1.9",
          "agent": "DevOps (Deployer)",
          "desc": "Prepare the environment for deployment, ensure zero-downtime deployments"
        }
      ]
    }
  ]
}
```

Note that I have assigned a unique `id` to each sub-task, and the `agent` field corresponds to the assigned role (e.g., Coder, Tester, Reviewer, DevOps). The `desc` field contains the literal, low-level technical step assigned to the agent.
```

# Phase 4 STEPS - Prompt:


                    Analyze the attached Phase 4 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-4.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 4 CONTEXT MARKDOWN ---
                    ## PHASE 4 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 4 is to conduct thorough testing and quality assurance of the membership-hub project. This phase will focus on ensuring the application's functionality, performance, and security meet the required standards. The scope of this phase includes:

* Unit testing of individual components
* Integration testing of interconnected components
* Performance testing to ensure scalability and reliability
* Security testing to identify vulnerabilities
* User acceptance testing (UAT) to validate the application's functionality

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope of this phase is limited to the testing and quality assurance of the existing codebase. The following directories and files are within the scope:

* `src/test`: Unit tests and integration tests
* `src/main`: Application codebase
* `docker-compose.yml`: Docker configuration for testing
* `kafka-config.properties`: Kafka configuration for testing
* `postgres-config.properties`: Postgres configuration for testing
* API endpoints for testing:
	+ `/api/v1/auth`
	+ `/api/v1/attendance`
	+ `/api/v1/notifications`

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in this phase:

* **Coder**: Assist in writing unit tests and integration tests
* **Tester**: Conduct thorough testing of the application, including performance testing and security testing
* **Reviewer**: Review test cases and provide feedback on test coverage and effectiveness
* **DevOps**: Configure and manage the testing environment, including Docker and Kafka

Tasks:

* Coder:
	+ Write unit tests for individual components (Days 1-2)
	+ Write integration tests for interconnected components (Days 2-3)
* Tester:
	+ Conduct performance testing (Days 1-2)
	+ Conduct security testing (Days 2-3)
	+ Conduct UAT (Days 3-4)
* Reviewer:
	+ Review test cases (Days 1-2)
	+ Provide feedback on test coverage and effectiveness (Days 2-3)
* DevOps:
	+ Configure testing environment (Day 1)
	+ Manage testing environment (Days 1-4)

#### 4. Phase Definition of Done (DoD)
The phase is considered complete when:

* All unit tests and integration tests have been written and executed successfully
* Performance testing and security testing have been conducted, and results have been reviewed and addressed
* UAT has been conducted, and results have been reviewed and addressed
* Test coverage is at least 80%
* All test cases have been reviewed and feedback has been incorporated
* The testing environment has been properly configured and managed

The phase will be stopped once the core technical objectives are satisfied, and the phase's definition of done has been met. The maximum duration for this phase is 7 days.
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Based on the provided Phase 4 Context Markdown content, I will extract and translate the daily steps, checklists, and agent tasks into a JSON schema.

Here is the resulting JSON object:
```json
{
  "phase_id": 4,
  "phase_name": "Phase 4",
  "project_name": "test-ai-architecture",
  "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": ".ai/.plan/.context/phase-4.context.blueprint.md",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "1.1",
          "agent": "Coder",
          "desc": "Write unit tests for individual components"
        },
        {
          "id": "1.2",
          "agent": "Tester",
          "desc": "Conduct performance testing"
        },
        {
          "id": "1.3",
          "agent": "Reviewer",
          "desc": "Review test cases"
        },
        {
          "id": "1.4",
          "agent": "DevOps",
          "desc": "Configure testing environment"
        }
      ]
    },
    {
      "day": 2,
      "context_file": ".ai/.plan/.context/phase-4.context.blueprint.md",
      "context_section": "DAY 2",
      "sub_tasks": [
        {
          "id": "2.1",
          "agent": "Coder",
          "desc": "Write integration tests for interconnected components"
        },
        {
          "id": "2.2",
          "agent": "Tester",
          "desc": "Conduct security testing"
        },
        {
          "id": "2.3",
          "agent": "Reviewer",
          "desc": "Provide feedback on test coverage and effectiveness"
        },
        {
          "id": "2.4",
          "agent": "DevOps",
          "desc": "Manage testing environment"
        }
      ]
    },
    {
      "day": 3,
      "context_file": ".ai/.plan/.context/phase-4.context.blueprint.md",
      "context_section": "DAY 3",
      "sub_tasks": [
        {
          "id": "3.1",
          "agent": "Tester",
          "desc": "Conduct UAT"
        },
        {
          "id": "3.2",
          "agent": "Reviewer",
          "desc": "Review test cases"
        },
        {
          "id": "3.3",
          "agent": "DevOps",
          "desc": "Manage testing environment"
        }
      ]
    },
    {
      "day": 4,
      "context_file": ".ai/.plan/.context/phase-4.context.blueprint.md",
      "context_section": "DAY 4",
      "sub_tasks": [
        {
          "id": "4.1",
          "agent": "Tester",
          "desc": "Conduct UAT"
        },
        {
          "id": "4.2",
          "agent": "DevOps",
          "desc": "Manage testing environment"
        }
      ]
    }
  ]
}
```
Note that I've followed the instructions to:

* Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
* Populate the exact string "sources/" into the 'source_target_dir' field.
* Provide a sequential task description text into the 'task' field (now 'desc' field in the SubAgentTask object).
* Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent' field.
* Set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-4.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number for each day object.
* Conform strictly to the required JSON Schema layout design structure.
```

# Phase 5 STEPS - Prompt:


                    Analyze the attached Phase 5 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-5.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 5 CONTEXT MARKDOWN ---
                    ## PHASE 5 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 5 is to deploy the membership-hub application on Google Cloud Platform (GCP) and Google Kubernetes Engine (GKE), ensuring a smooth and scalable operation. This phase will focus on:

* Deploying the application on GCP and GKE
* Configuring load balancing and autoscaling
* Ensuring zero-downtime deployments
* Setting up monitoring and logging tools
* Conducting final testing and quality assurance

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 5 includes:

* Deployment scripts and configurations for GCP and GKE
* Docker containerization and orchestration
* Load balancing and autoscaling configurations
* Monitoring and logging tools (e.g., Prometheus, Grafana, ELK Stack)
* API endpoints for deployment and management

Allowed directories and files:

* `deploy/`: deployment scripts and configurations
* `docker/`: Docker containerization and orchestration files
* `k8s/`: Kubernetes configurations and deployments
* `monitoring/`: monitoring and logging tools configurations

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 5:

* **Coder**: Responsible for creating deployment scripts and configurations, as well as ensuring the application is containerized and ready for deployment.
* **Tester**: Responsible for conducting final testing and quality assurance, including load testing and performance testing.
* **Reviewer**: Responsible for reviewing deployment scripts and configurations, as well as ensuring that the application is properly secured and compliant with regulatory requirements.
* **DevOps**: Responsible for deploying the application on GCP and GKE, configuring load balancing and autoscaling, and setting up monitoring and logging tools.
* **Docker**: Responsible for ensuring the application is properly containerized and orchestrated.
* **Deployer**: Responsible for deploying the application on GCP and GKE, and ensuring zero-downtime deployments.

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 5 includes:

* The application is successfully deployed on GCP and GKE
* Load balancing and autoscaling are properly configured
* Monitoring and logging tools are set up and functioning correctly
* Final testing and quality assurance have been completed
* The application is properly secured and compliant with regulatory requirements
* Deployment scripts and configurations are reviewed and approved
* The application is fully functional and performing as expected

Once these objectives are met, Phase 5 will be considered complete, and the project will be ready for maintenance and ongoing updates.
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
### Phase 5 Context JSON Schema

Based on the provided Markdown content, the following JSON schema represents the extracted daily steps, checklists, and agent tasks:

```json
{
  "phase_id": 5,
  "phase_name": "Phase 5",
  "project_name": "test-ai-architecture",
  "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": ".ai/.plan/.context/phase-5.context.blueprint.md",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "1.1",
          "agent": "Coder",
          "desc": "Create deployment scripts and configurations for GCP and GKE"
        },
        {
          "id": "1.2",
          "agent": "DevOps",
          "desc": "Deploy the application on GCP and GKE"
        },
        {
          "id": "1.3",
          "agent": "Tester",
          "desc": "Conduct final testing and quality assurance"
        }
      ]
    },
    {
      "day": 0,
      "context_file": ".ai/.plan/.context/phase-5.context.blueprint.md",
      "context_section": "DAY 0",
      "sub_tasks": [
        {
          "id": "0.1",
          "agent": "Reviewer",
          "desc": "Review deployment scripts and configurations"
        },
        {
          "id": "0.2",
          "agent": "DevOps",
          "desc": "Configure load balancing and autoscaling"
        },
        {
          "id": "0.3",
          "agent": "Docker",
          "desc": "Ensure the application is properly containerized and orchestrated"
        }
      ]
    }
  ]
}
```

Note that since there are no explicit daily steps or tasks mentioned in the Markdown content for specific days, the tasks have been inferred based on the phase objectives and sub-agent responsibilities. The tasks have been distributed across the two days (1 and 0) as per the instructions.

Also, note that the `id` field in the `SubAgentTask` object is a sequential task description text, and the `agent` field corresponds to the assigned role (e.g., Coder, Tester, Reviewer, DevOps). The `desc` field provides a literal, low-level technical step assigned to the agent.
```

# Phase 1 STEPS - Prompt:


                    Analyze the attached Phase 1 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-1.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 1 CONTEXT MARKDOWN ---
                    ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed project plan, and set up the development environment. This phase will focus on planning and setup, ensuring that all necessary components are in place for the successful execution of the project. The key deliverables for this phase include:
- A detailed project plan outlining the scope, timeline, and resources required
- A setup development environment with the necessary tools and technologies (Quarkus, Kafka, Postgres, Docker)
- Definition of the project's technical architecture and high-level design

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 1 includes:
- Setting up the project directory structure
- Initializing the Git repository
- Creating a basic Quarkus project template
- Setting up Kafka and Postgres for messaging and data storage
- Configuring Docker for containerization
- Defining the API endpoints for authentication, attendance tracking, and notification systems
- Creating a high-level design document outlining the system architecture

The allowed directory boundaries include:
- `src/main/java` for Java source code
- `src/main/resources` for configuration files and resources
- `docker` for Docker configuration files
- `kafka` for Kafka configuration files
- `postgres` for Postgres configuration files

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 1:
- **Coder**: Responsible for setting up the Quarkus project template, configuring Kafka and Postgres, and defining the API endpoints.
- **Tester**: Not actively involved in this phase, but will review the project plan and technical architecture.
- **Reviewer**: Responsible for reviewing the project plan, technical architecture, and high-level design document.
- **DevOps (Docker)**: Responsible for setting up the Docker configuration and ensuring containerization.
- **Deployer**: Not actively involved in this phase, but will review the project plan and technical architecture.

#### 4. Phase Definition of Done (DoD)
Phase 1 is considered complete when:
- The project plan is finalized and approved by all stakeholders
- The development environment is set up and configured
- The Quarkus project template is created and configured
- Kafka and Postgres are set up and configured
- Docker is configured for containerization
- The high-level design document is completed and approved by all stakeholders
- The project directory structure is initialized and the Git repository is set up

The expected duration for Phase 1 is 3 days, with the following milestones:
- Day 1: Project planning and scope definition
- Day 2: Setup of development environment and Quarkus project template
- Day 3: Configuration of Kafka, Postgres, and Docker, and completion of high-level design document
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 429 - {'error': {'message': 'Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx7x6rbpftmr50sr2yyb78qm` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 95019, Requested 5828. Please try again in 12m11.808s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
```

# Phase 1 STEPS - Prompt:


                    Analyze the attached Phase 1 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-1.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 1 CONTEXT MARKDOWN ---
                    ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed project plan, and set up the development environment. This phase will focus on planning and setup, ensuring that all necessary components are in place for the successful execution of the project. The key deliverables for this phase include:
- A detailed project plan outlining the scope, timeline, and resources required
- A setup development environment with the necessary tools and technologies (Quarkus, Kafka, Postgres, Docker)
- Definition of the project's technical architecture and high-level design

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 1 includes:
- Setting up the project directory structure
- Initializing the Git repository
- Creating a basic Quarkus project template
- Setting up Kafka and Postgres for messaging and data storage
- Configuring Docker for containerization
- Defining the API endpoints for authentication, attendance tracking, and notification systems
- Creating a high-level design document outlining the system architecture

The allowed directory boundaries include:
- `src/main/java` for Java source code
- `src/main/resources` for configuration files and resources
- `docker` for Docker configuration files
- `kafka` for Kafka configuration files
- `postgres` for Postgres configuration files

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 1:
- **Coder**: Responsible for setting up the Quarkus project template, configuring Kafka and Postgres, and defining the API endpoints.
- **Tester**: Not actively involved in this phase, but will review the project plan and technical architecture.
- **Reviewer**: Responsible for reviewing the project plan, technical architecture, and high-level design document.
- **DevOps (Docker)**: Responsible for setting up the Docker configuration and ensuring containerization.
- **Deployer**: Not actively involved in this phase, but will review the project plan and technical architecture.

#### 4. Phase Definition of Done (DoD)
Phase 1 is considered complete when:
- The project plan is finalized and approved by all stakeholders
- The development environment is set up and configured
- The Quarkus project template is created and configured
- Kafka and Postgres are set up and configured
- Docker is configured for containerization
- The high-level design document is completed and approved by all stakeholders
- The project directory structure is initialized and the Git repository is set up

The expected duration for Phase 1 is 3 days, with the following milestones:
- Day 1: Project planning and scope definition
- Day 2: Setup of development environment and Quarkus project template
- Day 3: Configuration of Kafka, Postgres, and Docker, and completion of high-level design document
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 404 - {'error': {'message': 'This model is unavailable for free. The paid version is available now - use this slug instead: meta-llama/llama-3.3-70b-instruct', 'code': 404}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:


                    Analyze the attached Phase 1 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-1.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 1 CONTEXT MARKDOWN ---
                    ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed project plan, and set up the development environment. This phase will focus on planning and setup, ensuring that all necessary components are in place for the successful execution of the project. The key deliverables for this phase include:
- A detailed project plan outlining the scope, timeline, and resources required
- A setup development environment with the necessary tools and technologies (Quarkus, Kafka, Postgres, Docker)
- Definition of the project's technical architecture and high-level design

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 1 includes:
- Setting up the project directory structure
- Initializing the Git repository
- Creating a basic Quarkus project template
- Setting up Kafka and Postgres for messaging and data storage
- Configuring Docker for containerization
- Defining the API endpoints for authentication, attendance tracking, and notification systems
- Creating a high-level design document outlining the system architecture

The allowed directory boundaries include:
- `src/main/java` for Java source code
- `src/main/resources` for configuration files and resources
- `docker` for Docker configuration files
- `kafka` for Kafka configuration files
- `postgres` for Postgres configuration files

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 1:
- **Coder**: Responsible for setting up the Quarkus project template, configuring Kafka and Postgres, and defining the API endpoints.
- **Tester**: Not actively involved in this phase, but will review the project plan and technical architecture.
- **Reviewer**: Responsible for reviewing the project plan, technical architecture, and high-level design document.
- **DevOps (Docker)**: Responsible for setting up the Docker configuration and ensuring containerization.
- **Deployer**: Not actively involved in this phase, but will review the project plan and technical architecture.

#### 4. Phase Definition of Done (DoD)
Phase 1 is considered complete when:
- The project plan is finalized and approved by all stakeholders
- The development environment is set up and configured
- The Quarkus project template is created and configured
- Kafka and Postgres are set up and configured
- Docker is configured for containerization
- The high-level design document is completed and approved by all stakeholders
- The project directory structure is initialized and the Git repository is set up

The expected duration for Phase 1 is 3 days, with the following milestones:
- Day 1: Project planning and scope definition
- Day 2: Setup of development environment and Quarkus project template
- Day 3: Configuration of Kafka, Postgres, and Docker, and completion of high-level design document
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
### Phase 1 JSON Schema Output

Based on the provided Markdown content, the following JSON schema output is generated:

```json
{
  "phase_id": 1,
  "phase_name": "Phase 1",
  "project_name": "test-ai-architecture",
  "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": ".ai/.plan/.context/phase-1.context.blueprint.md",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "1.1",
          "agent": "Coder",
          "desc": "Define project scope and create a detailed project plan"
        },
        {
          "id": "1.2",
          "agent": "Coder",
          "desc": "Set up the project directory structure"
        },
        {
          "id": "1.3",
          "agent": "DevOps (Docker)",
          "desc": "Initialize the Git repository"
        }
      ]
    },
    {
      "day": 2,
      "context_file": ".ai/.plan/.context/phase-1.context.blueprint.md",
      "context_section": "DAY 2",
      "sub_tasks": [
        {
          "id": "2.1",
          "agent": "Coder",
          "desc": "Set up the Quarkus project template"
        },
        {
          "id": "2.2",
          "agent": "Coder",
          "desc": "Configure Kafka for messaging"
        },
        {
          "id": "2.3",
          "agent": "DevOps (Docker)",
          "desc": "Configure Docker for containerization"
        }
      ]
    },
    {
      "day": 3,
      "context_file": ".ai/.plan/.context/phase-1.context.blueprint.md",
      "context_section": "DAY 3",
      "sub_tasks": [
        {
          "id": "3.1",
          "agent": "Coder",
          "desc": "Configure Postgres for data storage"
        },
        {
          "id": "3.2",
          "agent": "Coder",
          "desc": "Define the API endpoints for authentication, attendance tracking, and notification systems"
        },
        {
          "id": "3.3",
          "agent": "Reviewer",
          "desc": "Review the project plan, technical architecture, and high-level design document"
        }
      ]
    }
  ]
}
```

### Explanation

The generated JSON schema output conforms to the required layout design structure. The `days` array contains three day objects, each representing a day in the phase. Each day object has a `day` property, a `context_file` property, a `context_section` property, and a `sub_tasks` array.

The `sub_tasks` array contains multiple sub-agent tasks, each with an `id`, an `agent`, and a `desc` property. The `agent` property specifies the assigned role for each task, and the `desc` property provides a literal, low-level technical step assigned to the agent.

Note that the `global_context_file` and `source_target_dir` properties are populated with the exact string values as specified in the instructions. The `phase_id`, `phase_name`, and `project_name` properties are also populated with the corresponding values from the Markdown content.
```

# Phase 2 STEPS - Prompt:


                    Analyze the attached Phase 2 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-2.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 2 CONTEXT MARKDOWN ---
                    ## PHASE 2 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 2 is to develop the backend features of the membership-hub project, including authentication, attendance tracking, and notification systems. This phase will focus on building a scalable and secure backend using Quarkus, Kafka, and Postgres. The key deliverables for this phase include:
- Design and implementation of authentication mechanisms (email/password, Firebase, Google, Facebook)
- Development of attendance tracking features (QR code-based attendance tracking)
- Implementation of notification systems (SMS, Zalo, in-app notifications)
- Integration with Postgres database for data storage
- Containerization using Docker for seamless deployment on GKE

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 2 will be limited to the backend development, with the following directory boundaries:
- `src/main/java`: Java source code for Quarkus application
- `src/main/resources`: Configuration files and static resources
- `docker`: Dockerfile and containerization scripts
- `kafka`: Kafka configuration and topic definitions
- `postgres`: Postgres database schema and migration scripts
- `api`: API endpoints for authentication, attendance tracking, and notification systems
Allowed endpoints:
- `/api/auth`: Authentication endpoints (login, logout, register)
- `/api/attendance`: Attendance tracking endpoints (QR code scanning, attendance logging)
- `/api/notifications`: Notification endpoints (SMS, Zalo, in-app notifications)

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
- **Coder**: Implement authentication mechanisms, attendance tracking features, and notification systems. Develop API endpoints for backend features.
- **Tester**: Develop unit tests and integration tests for backend features. Test authentication, attendance tracking, and notification systems.
- **Reviewer**: Review code for adherence to coding standards, security, and scalability. Provide feedback on API endpoint design and implementation.
- **DevOps (Docker)**: Containerize the Quarkus application using Docker. Ensure seamless deployment on GKE.
- **DevOps (Deployer)**: Prepare deployment scripts for GCP and GKE. Ensure zero-downtime deployments.

#### 4. Phase Definition of Done (DoD)
Phase 2 is considered complete when:
- All backend features (authentication, attendance tracking, notification systems) are implemented and tested.
- API endpoints are designed and implemented for backend features.
- Code is reviewed and meets coding standards, security, and scalability requirements.
- Docker containerization is complete, and deployment scripts are prepared for GCP and GKE.
- Unit tests and integration tests are developed and passed for backend features.
The maximum duration for Phase 2 is 7 days. Once the core technical objectives are satisfied, the phase will be considered complete, and progression to Phase 3 will begin.
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
### Phase 2 Context JSON Schema

Based on the provided Phase 2 Context Markdown content, the following JSON schema is generated:

```json
{
  "phase_id": 2,
  "phase_name": "Phase 2",
  "project_name": "test-ai-architecture",
  "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "1.1",
          "agent": "Coder",
          "desc": "Implement authentication mechanisms (email/password, Firebase, Google, Facebook)"
        },
        {
          "id": "1.2",
          "agent": "Tester",
          "desc": "Develop unit tests and integration tests for authentication mechanisms"
        },
        {
          "id": "1.3",
          "agent": "Reviewer",
          "desc": "Review code for adherence to coding standards, security, and scalability"
        }
      ]
    },
    {
      "day": 2,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 2",
      "sub_tasks": [
        {
          "id": "2.1",
          "agent": "Coder",
          "desc": "Develop attendance tracking features (QR code-based attendance tracking)"
        },
        {
          "id": "2.2",
          "agent": "Tester",
          "desc": "Develop unit tests and integration tests for attendance tracking features"
        },
        {
          "id": "2.3",
          "agent": "DevOps (Docker)",
          "desc": "Containerize the Quarkus application using Docker"
        }
      ]
    },
    {
      "day": 3,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 3",
      "sub_tasks": [
        {
          "id": "3.1",
          "agent": "Coder",
          "desc": "Implement notification systems (SMS, Zalo, in-app notifications)"
        },
        {
          "id": "3.2",
          "agent": "Tester",
          "desc": "Develop unit tests and integration tests for notification systems"
        },
        {
          "id": "3.3",
          "agent": "Reviewer",
          "desc": "Review code for adherence to coding standards, security, and scalability"
        }
      ]
    },
    {
      "day": 4,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 4",
      "sub_tasks": [
        {
          "id": "4.1",
          "agent": "Coder",
          "desc": "Develop API endpoints for backend features"
        },
        {
          "id": "4.2",
          "agent": "Tester",
          "desc": "Develop unit tests and integration tests for API endpoints"
        },
        {
          "id": "4.3",
          "agent": "DevOps (Deployer)",
          "desc": "Prepare deployment scripts for GCP and GKE"
        }
      ]
    },
    {
      "day": 5,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 5",
      "sub_tasks": [
        {
          "id": "5.1",
          "agent": "Coder",
          "desc": "Integrate with Postgres database for data storage"
        },
        {
          "id": "5.2",
          "agent": "Tester",
          "desc": "Develop unit tests and integration tests for database integration"
        },
        {
          "id": "5.3",
          "agent": "Reviewer",
          "desc": "Review code for adherence to coding standards, security, and scalability"
        }
      ]
    },
    {
      "day": 6,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 6",
      "sub_tasks": [
        {
          "id": "6.1",
          "agent": "DevOps (Docker)",
          "desc": "Ensure seamless deployment on GKE"
        },
        {
          "id": "6.2",
          "agent": "DevOps (Deployer)",
          "desc": "Ensure zero-downtime deployments"
        },
        {
          "id": "6.3",
          "agent": "Tester",
          "desc": "Test the entire system for functionality and performance"
        }
      ]
    },
    {
      "day": 7,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 7",
      "sub_tasks": [
        {
          "id": "7.1",
          "agent": "Reviewer",
          "desc": "Review the entire system for adherence to coding standards, security, and scalability"
        },
        {
          "id": "7.2",
          "agent": "Tester",
          "desc": "Develop unit tests and integration tests for the entire system"
        },
        {
          "id": "7.3",
          "agent": "Coder",
          "desc": "Address any remaining issues or bugs"
        }
      ]
    }
  ]
}
```

This JSON schema represents the Phase 2 Context, including the daily steps, checklists, and agent tasks. Each day is represented by a `DailyStep` object, which contains the day number, context file, context section, and an array of `SubAgentTask` objects. Each `SubAgentTask` object represents a specific task assigned to a sub-agent, including the task ID, agent, and description.
```

# Phase 3 STEPS - Prompt:


                    Analyze the attached Phase 3 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-3.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 3 CONTEXT MARKDOWN ---
                    ## PHASE 3 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 3 is to develop the web and mobile applications for the membership-hub project. This phase will focus on creating a user-friendly interface for students to manage their attendance and for centers to track student activity. The key deliverables for this phase include:
- Developing the web application using Next.js
- Implementing QR code scanning for attendance tracking
- Integrating multi-language support for both web and mobile applications
- Ensuring SEO optimization for the web application
- Building the mobile application for both iOS and Android platforms

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 3 will be limited to the frontend development of the web and mobile applications. The following directories, files, and endpoints are in scope:
- `web-app/`: Directory for the web application code
- `mobile-app/`: Directory for the mobile application code
- `api/`: Directory for API endpoints for frontend-backend interaction
- `components/`: Directory for reusable UI components
- `locales/`: Directory for language translations
- Endpoints for:
  - QR code scanning
  - Attendance tracking
  - User profile management
  - Language selection

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 3, with the following tasks:
- **Coder**: Develop the web and mobile applications, implement QR code scanning, multi-language support, and SEO optimization
- **Tester**: Test the web and mobile applications for functionality, performance, and security
- **Reviewer**: Review the code for adherence to coding standards, best practices, and security guidelines
- **DevOps (Docker)**: Containerize the web application for deployment on GKE
- **DevOps (Deployer)**: Prepare the environment for deployment, ensure zero-downtime deployments

#### 4. Phase Definition of Done (DoD)
Phase 3 will be considered complete when the following conditions are met:
- The web application is fully functional, with QR code scanning, multi-language support, and SEO optimization
- The mobile application is fully functional, with QR code scanning, multi-language support, and push notifications
- All code has been reviewed and approved by the Reviewer
- The web application has been containerized and is ready for deployment on GKE
- The mobile application has been built and is ready for deployment on app stores
- All testing has been completed, and the application has been verified to meet the requirements and quality standards.
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
### Phase 3 Context JSON Schema

Based on the provided Phase 3 Context Markdown content, the following JSON schema is generated:

```json
{
  "phase_id": 3,
  "phase_name": "Phase 3",
  "project_name": "test-ai-architecture",
  "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": ".ai/.plan/.context/phase-3.context.blueprint.md",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "1.1",
          "agent": "Coder",
          "desc": "Develop the web application using Next.js"
        },
        {
          "id": "1.2",
          "agent": "Coder",
          "desc": "Implement QR code scanning for attendance tracking"
        },
        {
          "id": "1.3",
          "agent": "Coder",
          "desc": "Integrate multi-language support for the web application"
        },
        {
          "id": "1.4",
          "agent": "Tester",
          "desc": "Test the web application for functionality, performance, and security"
        },
        {
          "id": "1.5",
          "agent": "Reviewer",
          "desc": "Review the code for adherence to coding standards, best practices, and security guidelines"
        }
      ]
    },
    {
      "day": 0,
      "context_file": ".ai/.plan/.context/phase-3.context.blueprint.md",
      "context_section": "DAY 0",
      "sub_tasks": [
        {
          "id": "0.1",
          "agent": "DevOps (Docker)",
          "desc": "Containerize the web application for deployment on GKE"
        },
        {
          "id": "0.2",
          "agent": "DevOps (Deployer)",
          "desc": "Prepare the environment for deployment, ensure zero-downtime deployments"
        },
        {
          "id": "0.3",
          "agent": "Coder",
          "desc": "Build the mobile application for both iOS and Android platforms"
        },
        {
          "id": "0.4",
          "agent": "Tester",
          "desc": "Test the mobile application for functionality, performance, and security"
        },
        {
          "id": "0.5",
          "agent": "Reviewer",
          "desc": "Review the mobile application code for adherence to coding standards, best practices, and security guidelines"
        }
      ]
    }
  ]
}
```

### Explanation

The generated JSON schema follows the required structure and includes the following elements:

* `phase_id`, `phase_name`, and `project_name` are populated with the corresponding values from the Markdown content.
* `global_context_file` and `source_target_dir` are populated with the exact string values as specified in the instructions.
* The `days` array includes two objects, one for Day 1 and one for Day 0, each with the required properties `day`, `context_file`, `context_section`, and `sub_tasks`.
* The `sub_tasks` array for each day includes multiple objects, each representing a micro-task with the required properties `id`, `agent`, and `desc`. The `agent` property is populated with the corresponding role (e.g., Coder, Tester, Reviewer) and the `desc` property is populated with a sequential task description text.

Note that the tasks and agents are assigned based on the Markdown content, and the `id` property is generated sequentially for each task. The `context_section` property is populated with the string "DAY " followed by the day number, as specified in the instructions.
```

# Phase 4 STEPS - Prompt:


                    Analyze the attached Phase 4 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-4.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 4 CONTEXT MARKDOWN ---
                    ## PHASE 4 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 4 is to conduct thorough testing and quality assurance of the membership-hub project. This phase will focus on ensuring the application's functionality, performance, and security meet the required standards. The scope of this phase includes:

* Unit testing of individual components
* Integration testing of interconnected components
* Performance testing to ensure scalability and reliability
* Security testing to identify vulnerabilities
* User acceptance testing (UAT) to validate the application's functionality

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope of this phase is limited to the testing and quality assurance of the existing codebase. The following directories and files are within the scope:

* `src/test`: Unit tests and integration tests
* `src/main`: Application codebase
* `docker-compose.yml`: Docker configuration for testing
* `kafka-config.properties`: Kafka configuration for testing
* `postgres-config.properties`: Postgres configuration for testing
* API endpoints for testing:
	+ `/api/v1/auth`
	+ `/api/v1/attendance`
	+ `/api/v1/notifications`

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in this phase:

* **Coder**: Assist in writing unit tests and integration tests
* **Tester**: Conduct thorough testing of the application, including performance testing and security testing
* **Reviewer**: Review test cases and provide feedback on test coverage and effectiveness
* **DevOps**: Configure and manage the testing environment, including Docker and Kafka

Tasks:

* Coder:
	+ Write unit tests for individual components (Days 1-2)
	+ Write integration tests for interconnected components (Days 2-3)
* Tester:
	+ Conduct performance testing (Days 1-2)
	+ Conduct security testing (Days 2-3)
	+ Conduct UAT (Days 3-4)
* Reviewer:
	+ Review test cases (Days 1-2)
	+ Provide feedback on test coverage and effectiveness (Days 2-3)
* DevOps:
	+ Configure testing environment (Day 1)
	+ Manage testing environment (Days 1-4)

#### 4. Phase Definition of Done (DoD)
The phase is considered complete when:

* All unit tests and integration tests have been written and executed successfully
* Performance testing and security testing have been conducted, and results have been reviewed and addressed
* UAT has been conducted, and results have been reviewed and addressed
* Test coverage is at least 80%
* All test cases have been reviewed and feedback has been incorporated
* The testing environment has been properly configured and managed

The phase will be stopped once the core technical objectives are satisfied, and the phase's definition of done has been met. The maximum duration for this phase is 7 days.
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
### JSON Schema Representation of Phase 4 Context Markdown

Based on the provided Markdown content, the following JSON schema represents the daily steps, checklists, and agent tasks:

```json
{
  "phase_id": 4,
  "phase_name": "Phase 4",
  "project_name": "test-ai-architecture",
  "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": ".ai/.plan/.context/phase-4.context.blueprint.md",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "Coder-1",
          "agent": "Coder",
          "desc": "Write unit tests for individual components"
        },
        {
          "id": "Tester-1",
          "agent": "Tester",
          "desc": "Conduct performance testing"
        },
        {
          "id": "Reviewer-1",
          "agent": "Reviewer",
          "desc": "Review test cases"
        },
        {
          "id": "DevOps-1",
          "agent": "DevOps",
          "desc": "Configure testing environment"
        }
      ]
    },
    {
      "day": 2,
      "context_file": ".ai/.plan/.context/phase-4.context.blueprint.md",
      "context_section": "DAY 2",
      "sub_tasks": [
        {
          "id": "Coder-2",
          "agent": "Coder",
          "desc": "Write unit tests for individual components"
        },
        {
          "id": "Tester-2",
          "agent": "Tester",
          "desc": "Conduct performance testing"
        },
        {
          "id": "Reviewer-2",
          "agent": "Reviewer",
          "desc": "Review test cases"
        },
        {
          "id": "DevOps-2",
          "agent": "DevOps",
          "desc": "Manage testing environment"
        },
        {
          "id": "Coder-3",
          "agent": "Coder",
          "desc": "Write integration tests for interconnected components"
        },
        {
          "id": "Tester-3",
          "agent": "Tester",
          "desc": "Conduct security testing"
        }
      ]
    },
    {
      "day": 3,
      "context_file": ".ai/.plan/.context/phase-4.context.blueprint.md",
      "context_section": "DAY 3",
      "sub_tasks": [
        {
          "id": "Coder-4",
          "agent": "Coder",
          "desc": "Write integration tests for interconnected components"
        },
        {
          "id": "Tester-4",
          "agent": "Tester",
          "desc": "Conduct security testing"
        },
        {
          "id": "Reviewer-3",
          "agent": "Reviewer",
          "desc": "Provide feedback on test coverage and effectiveness"
        },
        {
          "id": "DevOps-3",
          "agent": "DevOps",
          "desc": "Manage testing environment"
        },
        {
          "id": "Tester-5",
          "agent": "Tester",
          "desc": "Conduct UAT"
        }
      ]
    },
    {
      "day": 4,
      "context_file": ".ai/.plan/.context/phase-4.context.blueprint.md",
      "context_section": "DAY 4",
      "sub_tasks": [
        {
          "id": "Tester-6",
          "agent": "Tester",
          "desc": "Conduct UAT"
        },
        {
          "id": "DevOps-4",
          "agent": "DevOps",
          "desc": "Manage testing environment"
        }
      ]
    }
  ]
}
```

This JSON schema represents the daily steps, checklists, and agent tasks for Phase 4, with each day having its own set of sub-tasks assigned to specific agents. The `global_context_file` and `source_target_dir` fields are populated with the exact string values as specified in the instructions. The `days` array contains four day objects, each with its own `context_file`, `context_section`, and `sub_tasks` array. The `sub_tasks` array contains task objects with `id`, `agent`, and `desc` properties, representing the tasks assigned to each agent on each day.
```

# Phase 5 STEPS - Prompt:


                    Analyze the attached Phase 5 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-5.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 5 CONTEXT MARKDOWN ---
                    ## PHASE 5 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 5 is to deploy the membership-hub application on Google Cloud Platform (GCP) and Google Kubernetes Engine (GKE), ensuring a smooth and scalable operation. This phase will focus on:

* Deploying the application on GCP and GKE
* Configuring load balancing and autoscaling
* Ensuring zero-downtime deployments
* Setting up monitoring and logging tools
* Conducting final testing and quality assurance

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 5 includes:

* Deployment scripts and configurations for GCP and GKE
* Docker containerization and orchestration
* Load balancing and autoscaling configurations
* Monitoring and logging tools (e.g., Prometheus, Grafana, ELK Stack)
* API endpoints for deployment and management

Allowed directories and files:

* `deploy/`: deployment scripts and configurations
* `docker/`: Docker containerization and orchestration files
* `k8s/`: Kubernetes configurations and deployments
* `monitoring/`: monitoring and logging tools configurations

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 5:

* **Coder**: Responsible for creating deployment scripts and configurations, as well as ensuring the application is containerized and ready for deployment.
* **Tester**: Responsible for conducting final testing and quality assurance, including load testing and performance testing.
* **Reviewer**: Responsible for reviewing deployment scripts and configurations, as well as ensuring that the application is properly secured and compliant with regulatory requirements.
* **DevOps**: Responsible for deploying the application on GCP and GKE, configuring load balancing and autoscaling, and setting up monitoring and logging tools.
* **Docker**: Responsible for ensuring the application is properly containerized and orchestrated.
* **Deployer**: Responsible for deploying the application on GCP and GKE, and ensuring zero-downtime deployments.

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 5 includes:

* The application is successfully deployed on GCP and GKE
* Load balancing and autoscaling are properly configured
* Monitoring and logging tools are set up and functioning correctly
* Final testing and quality assurance have been completed
* The application is properly secured and compliant with regulatory requirements
* Deployment scripts and configurations are reviewed and approved
* The application is fully functional and performing as expected

Once these objectives are met, Phase 5 will be considered complete, and the project will be ready for maintenance and ongoing updates.
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
### JSON Schema Representation of Phase 5 Context Markdown

Given the provided Markdown content for Phase 5, the following JSON schema represents the extracted and translated daily steps, checklists, and agent tasks according to the specified requirements.

```json
{
  "phase_id": 5,
  "phase_name": "Phase 5",
  "project_name": "test-ai-architecture",
  "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": ".ai/.plan/.context/phase-5.context.blueprint.md",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "1.1",
          "agent": "Coder",
          "desc": "Create deployment scripts and configurations for GCP and GKE"
        },
        {
          "id": "1.2",
          "agent": "DevOps",
          "desc": "Deploy the application on GCP and GKE"
        },
        {
          "id": "1.3",
          "agent": "Docker",
          "desc": "Ensure the application is properly containerized and orchestrated"
        }
      ]
    },
    {
      "day": 0,
      "context_file": ".ai/.plan/.context/phase-5.context.blueprint.md",
      "context_section": "DAY 0",
      "sub_tasks": [
        {
          "id": "0.1",
          "agent": "Tester",
          "desc": "Conduct final testing and quality assurance"
        },
        {
          "id": "0.2",
          "agent": "Reviewer",
          "desc": "Review deployment scripts and configurations for security and compliance"
        },
        {
          "id": "0.3",
          "agent": "Deployer",
          "desc": "Ensure zero-downtime deployments and monitor application performance"
        }
      ]
    }
  ]
}
```

### Explanation of the JSON Schema

- **Phase Details**: The JSON object starts with the phase details, including `phase_id`, `phase_name`, `project_name`, `global_context_file`, and `source_target_dir`, which are populated according to the provided instructions.
- **Days Array**: The `days` array contains objects representing each day within the phase. Since the instructions specify targeting days between Day 1 and Day 0 (inclusive), and given the nature of the provided Markdown content, the tasks are distributed across these two days to ensure all critical tasks are accounted for.
- **Daily Steps and Tasks**: Each day object includes a `day` number, `context_file`, `context_section`, and an array of `sub_tasks`. The `sub_tasks` array contains objects detailing specific tasks, including a unique `id`, the assigned `agent`, and a `desc` (description) of the task.
- **Task Assignment**: Tasks are assigned to agents based on their roles and responsibilities as outlined in the Markdown content. For example, deployment tasks are assigned to "Coder" and "DevOps", while testing and review tasks are assigned to "Tester" and "Reviewer", respectively.

This JSON schema adheres to the specified requirements, ensuring that all daily steps, checklists, and agent tasks are extracted and translated from the Phase 5 Context Markdown content into a precise, executable JSON format.
```

# Phase 1 STEPS - Prompt:


                    Analyze the attached Phase 1 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-1.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 1 CONTEXT MARKDOWN ---
                    ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed project plan, and set up the development environment. This phase will focus on planning and setup, ensuring that all necessary components are in place for the successful execution of the project. The key deliverables for this phase include:
- A detailed project plan outlining the scope, timeline, and resources required
- A setup development environment with the necessary tools and technologies (Quarkus, Kafka, Postgres, Docker)
- Definition of the project's technical architecture and high-level design

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 1 includes:
- Setting up the project directory structure
- Initializing the Git repository
- Creating a basic Quarkus project template
- Setting up Kafka and Postgres for messaging and data storage
- Configuring Docker for containerization
- Defining the API endpoints for authentication, attendance tracking, and notification systems
- Creating a high-level design document outlining the system architecture

The allowed directory boundaries include:
- `src/main/java` for Java source code
- `src/main/resources` for configuration files and resources
- `docker` for Docker configuration files
- `kafka` for Kafka configuration files
- `postgres` for Postgres configuration files

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 1:
- **Coder**: Responsible for setting up the Quarkus project template, configuring Kafka and Postgres, and defining the API endpoints.
- **Tester**: Not actively involved in this phase, but will review the project plan and technical architecture.
- **Reviewer**: Responsible for reviewing the project plan, technical architecture, and high-level design document.
- **DevOps (Docker)**: Responsible for setting up the Docker configuration and ensuring containerization.
- **Deployer**: Not actively involved in this phase, but will review the project plan and technical architecture.

#### 4. Phase Definition of Done (DoD)
Phase 1 is considered complete when:
- The project plan is finalized and approved by all stakeholders
- The development environment is set up and configured
- The Quarkus project template is created and configured
- Kafka and Postgres are set up and configured
- Docker is configured for containerization
- The high-level design document is completed and approved by all stakeholders
- The project directory structure is initialized and the Git repository is set up

The expected duration for Phase 1 is 3 days, with the following milestones:
- Day 1: Project planning and scope definition
- Day 2: Setup of development environment and Quarkus project template
- Day 3: Configuration of Kafka, Postgres, and Docker, and completion of high-level design document
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Based on the provided Phase 1 Context Markdown content, I will extract and translate the daily steps, checklists, and agent tasks into a JSON schema that conforms to the required layout design structure.

Here is the resulting JSON object:

```json
{
  "phase_id": 1,
  "phase_name": "Phase 1",
  "project_name": "test-ai-architecture",
  "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": ".ai/.plan/.context/phase-1.context.blueprint.md",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "ST-1",
          "agent": "Coder",
          "desc": "Define project scope and create a detailed project plan"
        },
        {
          "id": "ST-2",
          "agent": "Reviewer",
          "desc": "Review project plan and provide feedback"
        },
        {
          "id": "ST-3",
          "agent": "DevOps (Docker)",
          "desc": "Initialize project directory structure and set up Git repository"
        }
      ]
    },
    {
      "day": 2,
      "context_file": ".ai/.plan/.context/phase-1.context.blueprint.md",
      "context_section": "DAY 2",
      "sub_tasks": [
        {
          "id": "ST-4",
          "agent": "Coder",
          "desc": "Set up Quarkus project template and configure Kafka and Postgres"
        },
        {
          "id": "ST-5",
          "agent": "DevOps (Docker)",
          "desc": "Configure Docker for containerization"
        },
        {
          "id": "ST-6",
          "agent": "Reviewer",
          "desc": "Review technical architecture and high-level design document"
        }
      ]
    },
    {
      "day": 3,
      "context_file": ".ai/.plan/.context/phase-1.context.blueprint.md",
      "context_section": "DAY 3",
      "sub_tasks": [
        {
          "id": "ST-7",
          "agent": "Coder",
          "desc": "Define API endpoints for authentication, attendance tracking, and notification systems"
        },
        {
          "id": "ST-8",
          "agent": "DevOps (Docker)",
          "desc": "Finalize Docker configuration and ensure containerization"
        },
        {
          "id": "ST-9",
          "agent": "Reviewer",
          "desc": "Review and approve high-level design document and technical architecture"
        }
      ]
    }
  ]
}
```

Note that I have extracted the daily steps, checklists, and agent tasks from the provided Markdown content and translated them into a JSON schema that conforms to the required layout design structure. I have also populated the exact string values for the `global_context_file` and `source_target_dir` fields as per the instructions. Additionally, I have ensured that the `days` array is not empty and that each day object has the required properties, including `day`, `context_file`, `context_section`, and `sub_tasks`.
```

# Phase 2 STEPS - Prompt:


                    Analyze the attached Phase 2 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-2.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 2 CONTEXT MARKDOWN ---
                    ## PHASE 2 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 2 is to develop the backend features of the membership-hub project, including authentication, attendance tracking, and notification systems. This phase will focus on building a scalable and secure backend using Quarkus, Kafka, and Postgres. The key deliverables for this phase include:
- Design and implementation of authentication mechanisms (email/password, Firebase, Google, Facebook)
- Development of attendance tracking features (QR code-based attendance tracking)
- Implementation of notification systems (SMS, Zalo, in-app notifications)
- Integration with Postgres database for data storage
- Containerization using Docker for seamless deployment on GKE

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 2 will be limited to the backend development, with the following directory boundaries:
- `src/main/java`: Java source code for Quarkus application
- `src/main/resources`: Configuration files and static resources
- `docker`: Dockerfile and containerization scripts
- `kafka`: Kafka configuration and topic definitions
- `postgres`: Postgres database schema and migration scripts
- `api`: API endpoints for authentication, attendance tracking, and notification systems
Allowed endpoints:
- `/api/auth`: Authentication endpoints (login, logout, register)
- `/api/attendance`: Attendance tracking endpoints (QR code scanning, attendance logging)
- `/api/notifications`: Notification endpoints (SMS, Zalo, in-app notifications)

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
- **Coder**: Implement authentication mechanisms, attendance tracking features, and notification systems. Develop API endpoints for backend features.
- **Tester**: Develop unit tests and integration tests for backend features. Test authentication, attendance tracking, and notification systems.
- **Reviewer**: Review code for adherence to coding standards, security, and scalability. Provide feedback on API endpoint design and implementation.
- **DevOps (Docker)**: Containerize the Quarkus application using Docker. Ensure seamless deployment on GKE.
- **DevOps (Deployer)**: Prepare deployment scripts for GCP and GKE. Ensure zero-downtime deployments.

#### 4. Phase Definition of Done (DoD)
Phase 2 is considered complete when:
- All backend features (authentication, attendance tracking, notification systems) are implemented and tested.
- API endpoints are designed and implemented for backend features.
- Code is reviewed and meets coding standards, security, and scalability requirements.
- Docker containerization is complete, and deployment scripts are prepared for GCP and GKE.
- Unit tests and integration tests are developed and passed for backend features.
The maximum duration for Phase 2 is 7 days. Once the core technical objectives are satisfied, the phase will be considered complete, and progression to Phase 3 will begin.
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Based on the provided Phase 2 Context Markdown content, I will extract and translate the daily steps, checklists, and agent tasks into the required JSON schema.

Since the markdown content does not explicitly provide daily steps for each day, I will parse the paragraph descriptions into technical sub-tasks for each day. The phase duration is 7 days, so I will create a day object node for each day from Day 1 to Day 7.

Here is the translated JSON schema:

```json
{
  "phase_id": 2,
  "phase_name": "Phase 2",
  "project_name": "test-ai-architecture",
  "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "1.1",
          "agent": "Coder",
          "desc": "Design and implementation of authentication mechanisms (email/password, Firebase, Google, Facebook)"
        },
        {
          "id": "1.2",
          "agent": "Tester",
          "desc": "Develop unit tests for authentication mechanisms"
        }
      ]
    },
    {
      "day": 2,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 2",
      "sub_tasks": [
        {
          "id": "2.1",
          "agent": "Coder",
          "desc": "Development of attendance tracking features (QR code-based attendance tracking)"
        },
        {
          "id": "2.2",
          "agent": "Tester",
          "desc": "Develop unit tests for attendance tracking features"
        }
      ]
    },
    {
      "day": 3,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 3",
      "sub_tasks": [
        {
          "id": "3.1",
          "agent": "Coder",
          "desc": "Implementation of notification systems (SMS, Zalo, in-app notifications)"
        },
        {
          "id": "3.2",
          "agent": "Tester",
          "desc": "Develop unit tests for notification systems"
        }
      ]
    },
    {
      "day": 4,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 4",
      "sub_tasks": [
        {
          "id": "4.1",
          "agent": "Coder",
          "desc": "Integration with Postgres database for data storage"
        },
        {
          "id": "4.2",
          "agent": "DevOps (Docker)",
          "desc": "Containerize the Quarkus application using Docker"
        }
      ]
    },
    {
      "day": 5,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 5",
      "sub_tasks": [
        {
          "id": "5.1",
          "agent": "Reviewer",
          "desc": "Review code for adherence to coding standards, security, and scalability"
        },
        {
          "id": "5.2",
          "agent": "DevOps (Deployer)",
          "desc": "Prepare deployment scripts for GCP and GKE"
        }
      ]
    },
    {
      "day": 6,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 6",
      "sub_tasks": [
        {
          "id": "6.1",
          "agent": "Tester",
          "desc": "Develop integration tests for backend features"
        },
        {
          "id": "6.2",
          "agent": "DevOps (Docker)",
          "desc": "Ensure seamless deployment on GKE"
        }
      ]
    },
    {
      "day": 7,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 7",
      "sub_tasks": [
        {
          "id": "7.1",
          "agent": "Coder",
          "desc": "Finalize API endpoints for backend features"
        },
        {
          "id": "7.2",
          "agent": "Reviewer",
          "desc": "Final review of code and deployment scripts"
        }
      ]
    }
  ]
}
```

Note that I have assigned tasks to agents based on the provided markdown content, but the actual task assignments may vary depending on the specific project requirements and team structure.
```

# Phase 3 STEPS - Prompt:


                    Analyze the attached Phase 3 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-3.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 3 CONTEXT MARKDOWN ---
                    ## PHASE 3 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 3 is to develop the web and mobile applications for the membership-hub project. This phase will focus on creating a user-friendly interface for students to manage their attendance and for centers to track student activity. The key deliverables for this phase include:
- Developing the web application using Next.js
- Implementing QR code scanning for attendance tracking
- Integrating multi-language support for both web and mobile applications
- Ensuring SEO optimization for the web application
- Building the mobile application for both iOS and Android platforms

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 3 will be limited to the frontend development of the web and mobile applications. The following directories, files, and endpoints are in scope:
- `web-app/`: Directory for the web application code
- `mobile-app/`: Directory for the mobile application code
- `api/`: Directory for API endpoints for frontend-backend interaction
- `components/`: Directory for reusable UI components
- `locales/`: Directory for language translations
- Endpoints for:
  - QR code scanning
  - Attendance tracking
  - User profile management
  - Language selection

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 3, with the following tasks:
- **Coder**: Develop the web and mobile applications, implement QR code scanning, multi-language support, and SEO optimization
- **Tester**: Test the web and mobile applications for functionality, performance, and security
- **Reviewer**: Review the code for adherence to coding standards, best practices, and security guidelines
- **DevOps (Docker)**: Containerize the web application for deployment on GKE
- **DevOps (Deployer)**: Prepare the environment for deployment, ensure zero-downtime deployments

#### 4. Phase Definition of Done (DoD)
Phase 3 will be considered complete when the following conditions are met:
- The web application is fully functional, with QR code scanning, multi-language support, and SEO optimization
- The mobile application is fully functional, with QR code scanning, multi-language support, and push notifications
- All code has been reviewed and approved by the Reviewer
- The web application has been containerized and is ready for deployment on GKE
- The mobile application has been built and is ready for deployment on app stores
- All testing has been completed, and the application has been verified to meet the requirements and quality standards.
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Based on the provided Phase 3 Context Markdown content, I will extract and translate the daily steps, checklists, and agent tasks into a JSON schema that conforms to the required layout design structure.

Since the markdown content does not explicitly provide daily steps, I will parse the paragraph descriptions into technical sub-tasks for each day. I will assume that the phase starts on Day 1 and ends on Day 0 (inclusive), as per the critical instructions.

Here is the translated JSON schema:
```json
{
  "phase_id": 3,
  "phase_name": "Phase 3",
  "project_name": "test-ai-architecture",
  "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": ".ai/.plan/.context/phase-3.context.blueprint.md",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "ST-1",
          "agent": "Coder",
          "desc": "Develop the web application using Next.js"
        },
        {
          "id": "ST-2",
          "agent": "Coder",
          "desc": "Implement QR code scanning for attendance tracking"
        },
        {
          "id": "ST-3",
          "agent": "Coder",
          "desc": "Integrate multi-language support for both web and mobile applications"
        }
      ]
    },
    {
      "day": 0,
      "context_file": ".ai/.plan/.context/phase-3.context.blueprint.md",
      "context_section": "DAY 0",
      "sub_tasks": [
        {
          "id": "ST-4",
          "agent": "Tester",
          "desc": "Test the web and mobile applications for functionality, performance, and security"
        },
        {
          "id": "ST-5",
          "agent": "Reviewer",
          "desc": "Review the code for adherence to coding standards, best practices, and security guidelines"
        },
        {
          "id": "ST-6",
          "agent": "DevOps (Docker)",
          "desc": "Containerize the web application for deployment on GKE"
        },
        {
          "id": "ST-7",
          "agent": "DevOps (Deployer)",
          "desc": "Prepare the environment for deployment, ensure zero-downtime deployments"
        }
      ]
    }
  ]
}
```
Note that I have assumed the following:

* Day 1: Focus on developing the web application, implementing QR code scanning, and integrating multi-language support.
* Day 0: Focus on testing, reviewing, and deploying the applications.

Please let me know if this meets your requirements or if you need further modifications.
```

# Phase 4 STEPS - Prompt:


                    Analyze the attached Phase 4 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-4.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 4 CONTEXT MARKDOWN ---
                    ## PHASE 4 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 4 is to conduct thorough testing and quality assurance of the membership-hub project. This phase will focus on ensuring the application's functionality, performance, and security meet the required standards. The scope of this phase includes:

* Unit testing of individual components
* Integration testing of interconnected components
* Performance testing to ensure scalability and reliability
* Security testing to identify vulnerabilities
* User acceptance testing (UAT) to validate the application's functionality

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope of this phase is limited to the testing and quality assurance of the existing codebase. The following directories and files are within the scope:

* `src/test`: Unit tests and integration tests
* `src/main`: Application codebase
* `docker-compose.yml`: Docker configuration for testing
* `kafka-config.properties`: Kafka configuration for testing
* `postgres-config.properties`: Postgres configuration for testing
* API endpoints for testing:
	+ `/api/v1/auth`
	+ `/api/v1/attendance`
	+ `/api/v1/notifications`

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in this phase:

* **Coder**: Assist in writing unit tests and integration tests
* **Tester**: Conduct thorough testing of the application, including performance testing and security testing
* **Reviewer**: Review test cases and provide feedback on test coverage and effectiveness
* **DevOps**: Configure and manage the testing environment, including Docker and Kafka

Tasks:

* Coder:
	+ Write unit tests for individual components (Days 1-2)
	+ Write integration tests for interconnected components (Days 2-3)
* Tester:
	+ Conduct performance testing (Days 1-2)
	+ Conduct security testing (Days 2-3)
	+ Conduct UAT (Days 3-4)
* Reviewer:
	+ Review test cases (Days 1-2)
	+ Provide feedback on test coverage and effectiveness (Days 2-3)
* DevOps:
	+ Configure testing environment (Day 1)
	+ Manage testing environment (Days 1-4)

#### 4. Phase Definition of Done (DoD)
The phase is considered complete when:

* All unit tests and integration tests have been written and executed successfully
* Performance testing and security testing have been conducted, and results have been reviewed and addressed
* UAT has been conducted, and results have been reviewed and addressed
* Test coverage is at least 80%
* All test cases have been reviewed and feedback has been incorporated
* The testing environment has been properly configured and managed

The phase will be stopped once the core technical objectives are satisfied, and the phase's definition of done has been met. The maximum duration for this phase is 7 days.
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Based on the provided Phase 4 Context Markdown content, I will extract and translate the daily steps, checklists, and agent tasks into the required JSON schema.

Here is the resulting JSON object:

```json
{
  "phase_id": 4,
  "phase_name": "Phase 4",
  "project_name": "test-ai-architecture",
  "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": ".ai/.plan/.context/phase-4.context.blueprint.md",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "1.1",
          "agent": "Coder",
          "desc": "Write unit tests for individual components"
        },
        {
          "id": "1.2",
          "agent": "Tester",
          "desc": "Conduct performance testing"
        },
        {
          "id": "1.3",
          "agent": "Reviewer",
          "desc": "Review test cases"
        },
        {
          "id": "1.4",
          "agent": "DevOps",
          "desc": "Configure testing environment"
        }
      ]
    },
    {
      "day": 2,
      "context_file": ".ai/.plan/.context/phase-4.context.blueprint.md",
      "context_section": "DAY 2",
      "sub_tasks": [
        {
          "id": "2.1",
          "agent": "Coder",
          "desc": "Write unit tests for individual components"
        },
        {
          "id": "2.2",
          "agent": "Coder",
          "desc": "Write integration tests for interconnected components"
        },
        {
          "id": "2.3",
          "agent": "Tester",
          "desc": "Conduct performance testing"
        },
        {
          "id": "2.4",
          "agent": "Reviewer",
          "desc": "Review test cases"
        },
        {
          "id": "2.5",
          "agent": "DevOps",
          "desc": "Manage testing environment"
        }
      ]
    },
    {
      "day": 3,
      "context_file": ".ai/.plan/.context/phase-4.context.blueprint.md",
      "context_section": "DAY 3",
      "sub_tasks": [
        {
          "id": "3.1",
          "agent": "Coder",
          "desc": "Write integration tests for interconnected components"
        },
        {
          "id": "3.2",
          "agent": "Tester",
          "desc": "Conduct security testing"
        },
        {
          "id": "3.3",
          "agent": "Reviewer",
          "desc": "Provide feedback on test coverage and effectiveness"
        },
        {
          "id": "3.4",
          "agent": "DevOps",
          "desc": "Manage testing environment"
        }
      ]
    },
    {
      "day": 0,
      "context_file": ".ai/.plan/.context/phase-4.context.blueprint.md",
      "context_section": "DAY 0",
      "sub_tasks": [
        {
          "id": "0.1",
          "agent": "Tester",
          "desc": "Conduct UAT"
        },
        {
          "id": "0.2",
          "agent": "DevOps",
          "desc": "Manage testing environment"
        }
      ]
    }
  ]
}
```

Note that I have included all days from 1 to 0 (inclusive) as per the instructions, and populated the `sub_tasks` array with the corresponding tasks for each day. I have also set the `global_context_file` and `source_target_dir` fields to the exact strings specified in the instructions.
```

# Phase 5 STEPS - Prompt:


                    Analyze the attached Phase 5 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-5.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 5 CONTEXT MARKDOWN ---
                    ## PHASE 5 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 5 is to deploy the membership-hub application on Google Cloud Platform (GCP) and Google Kubernetes Engine (GKE), ensuring a smooth and scalable operation. This phase will focus on:

* Deploying the application on GCP and GKE
* Configuring load balancing and autoscaling
* Ensuring zero-downtime deployments
* Setting up monitoring and logging tools
* Conducting final testing and quality assurance

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 5 includes:

* Deployment scripts and configurations for GCP and GKE
* Docker containerization and orchestration
* Load balancing and autoscaling configurations
* Monitoring and logging tools (e.g., Prometheus, Grafana, ELK Stack)
* API endpoints for deployment and management

Allowed directories and files:

* `deploy/`: deployment scripts and configurations
* `docker/`: Docker containerization and orchestration files
* `k8s/`: Kubernetes configurations and deployments
* `monitoring/`: monitoring and logging tools configurations

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 5:

* **Coder**: Responsible for creating deployment scripts and configurations, as well as ensuring the application is containerized and ready for deployment.
* **Tester**: Responsible for conducting final testing and quality assurance, including load testing and performance testing.
* **Reviewer**: Responsible for reviewing deployment scripts and configurations, as well as ensuring that the application is properly secured and compliant with regulatory requirements.
* **DevOps**: Responsible for deploying the application on GCP and GKE, configuring load balancing and autoscaling, and setting up monitoring and logging tools.
* **Docker**: Responsible for ensuring the application is properly containerized and orchestrated.
* **Deployer**: Responsible for deploying the application on GCP and GKE, and ensuring zero-downtime deployments.

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 5 includes:

* The application is successfully deployed on GCP and GKE
* Load balancing and autoscaling are properly configured
* Monitoring and logging tools are set up and functioning correctly
* Final testing and quality assurance have been completed
* The application is properly secured and compliant with regulatory requirements
* Deployment scripts and configurations are reviewed and approved
* The application is fully functional and performing as expected

Once these objectives are met, Phase 5 will be considered complete, and the project will be ready for maintenance and ongoing updates.
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 429 - {'error': {'message': 'Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx7x6rbpftmr50sr2yyb78qm` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99356, Requested 5776. Please try again in 1h13m54.048s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
```

# Phase 1 STEPS - Prompt:


                    Analyze the attached Phase 1 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-1.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 1 CONTEXT MARKDOWN ---
                    ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed project plan, and set up the development environment. This phase will focus on planning and setup, ensuring that all necessary components are in place for the successful execution of the project. The key deliverables for this phase include:
- A detailed project plan outlining the scope, timeline, and resources required
- A setup development environment with the necessary tools and technologies (Quarkus, Kafka, Postgres, Docker)
- Definition of the project's technical architecture and high-level design

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 1 includes:
- Setting up the project directory structure
- Initializing the Git repository
- Creating a basic Quarkus project template
- Setting up Kafka and Postgres for messaging and data storage
- Configuring Docker for containerization
- Defining the API endpoints for authentication, attendance tracking, and notification systems
- Creating a high-level design document outlining the system architecture

The allowed directory boundaries include:
- `src/main/java` for Java source code
- `src/main/resources` for configuration files and resources
- `docker` for Docker configuration files
- `kafka` for Kafka configuration files
- `postgres` for Postgres configuration files

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 1:
- **Coder**: Responsible for setting up the Quarkus project template, configuring Kafka and Postgres, and defining the API endpoints.
- **Tester**: Not actively involved in this phase, but will review the project plan and technical architecture.
- **Reviewer**: Responsible for reviewing the project plan, technical architecture, and high-level design document.
- **DevOps (Docker)**: Responsible for setting up the Docker configuration and ensuring containerization.
- **Deployer**: Not actively involved in this phase, but will review the project plan and technical architecture.

#### 4. Phase Definition of Done (DoD)
Phase 1 is considered complete when:
- The project plan is finalized and approved by all stakeholders
- The development environment is set up and configured
- The Quarkus project template is created and configured
- Kafka and Postgres are set up and configured
- Docker is configured for containerization
- The high-level design document is completed and approved by all stakeholders
- The project directory structure is initialized and the Git repository is set up

The expected duration for Phase 1 is 3 days, with the following milestones:
- Day 1: Project planning and scope definition
- Day 2: Setup of development environment and Quarkus project template
- Day 3: Configuration of Kafka, Postgres, and Docker, and completion of high-level design document
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 404 - {'error': {'message': 'This model is unavailable for free. The paid version is available now - use this slug instead: meta-llama/llama-3.3-70b-instruct', 'code': 404}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:


                    Analyze the attached Phase 1 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-1.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 1 CONTEXT MARKDOWN ---
                    ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed project plan, and set up the development environment. This phase will focus on planning and setup, ensuring that all necessary components are in place for the successful execution of the project. The key deliverables for this phase include:
- A detailed project plan outlining the scope, timeline, and resources required
- A setup development environment with the necessary tools and technologies (Quarkus, Kafka, Postgres, Docker)
- Definition of the project's technical architecture and high-level design

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 1 includes:
- Setting up the project directory structure
- Initializing the Git repository
- Creating a basic Quarkus project template
- Setting up Kafka and Postgres for messaging and data storage
- Configuring Docker for containerization
- Defining the API endpoints for authentication, attendance tracking, and notification systems
- Creating a high-level design document outlining the system architecture

The allowed directory boundaries include:
- `src/main/java` for Java source code
- `src/main/resources` for configuration files and resources
- `docker` for Docker configuration files
- `kafka` for Kafka configuration files
- `postgres` for Postgres configuration files

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 1:
- **Coder**: Responsible for setting up the Quarkus project template, configuring Kafka and Postgres, and defining the API endpoints.
- **Tester**: Not actively involved in this phase, but will review the project plan and technical architecture.
- **Reviewer**: Responsible for reviewing the project plan, technical architecture, and high-level design document.
- **DevOps (Docker)**: Responsible for setting up the Docker configuration and ensuring containerization.
- **Deployer**: Not actively involved in this phase, but will review the project plan and technical architecture.

#### 4. Phase Definition of Done (DoD)
Phase 1 is considered complete when:
- The project plan is finalized and approved by all stakeholders
- The development environment is set up and configured
- The Quarkus project template is created and configured
- Kafka and Postgres are set up and configured
- Docker is configured for containerization
- The high-level design document is completed and approved by all stakeholders
- The project directory structure is initialized and the Git repository is set up

The expected duration for Phase 1 is 3 days, with the following milestones:
- Day 1: Project planning and scope definition
- Day 2: Setup of development environment and Quarkus project template
- Day 3: Configuration of Kafka, Postgres, and Docker, and completion of high-level design document
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 2953. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 2362. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 3692. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 524. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 2953. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 1640. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 1495. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 1664. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 1640. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:


                    Analyze the attached Phase 1 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-1.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 1 CONTEXT MARKDOWN ---
                    ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed project plan, and set up the development environment. This phase will focus on planning and setup, ensuring that all necessary components are in place for the successful execution of the project. The key deliverables for this phase include:
- A detailed project plan outlining the scope, timeline, and resources required
- A setup development environment with the necessary tools and technologies (Quarkus, Kafka, Postgres, Docker)
- Definition of the project's technical architecture and high-level design

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 1 includes:
- Setting up the project directory structure
- Initializing the Git repository
- Creating a basic Quarkus project template
- Setting up Kafka and Postgres for messaging and data storage
- Configuring Docker for containerization
- Defining the API endpoints for authentication, attendance tracking, and notification systems
- Creating a high-level design document outlining the system architecture

The allowed directory boundaries include:
- `src/main/java` for Java source code
- `src/main/resources` for configuration files and resources
- `docker` for Docker configuration files
- `kafka` for Kafka configuration files
- `postgres` for Postgres configuration files

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 1:
- **Coder**: Responsible for setting up the Quarkus project template, configuring Kafka and Postgres, and defining the API endpoints.
- **Tester**: Not actively involved in this phase, but will review the project plan and technical architecture.
- **Reviewer**: Responsible for reviewing the project plan, technical architecture, and high-level design document.
- **DevOps (Docker)**: Responsible for setting up the Docker configuration and ensuring containerization.
- **Deployer**: Not actively involved in this phase, but will review the project plan and technical architecture.

#### 4. Phase Definition of Done (DoD)
Phase 1 is considered complete when:
- The project plan is finalized and approved by all stakeholders
- The development environment is set up and configured
- The Quarkus project template is created and configured
- Kafka and Postgres are set up and configured
- Docker is configured for containerization
- The high-level design document is completed and approved by all stakeholders
- The project directory structure is initialized and the Git repository is set up

The expected duration for Phase 1 is 3 days, with the following milestones:
- Day 1: Project planning and scope definition
- Day 2: Setup of development environment and Quarkus project template
- Day 3: Configuration of Kafka, Postgres, and Docker, and completion of high-level design document
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 404 - {'error': {'message': 'This model is unavailable for free. The paid version is available now - use this slug instead: qwen/qwen-2.5-coder-32b-instruct', 'code': 404}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:


                    Analyze the attached Phase 1 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-1.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 1 CONTEXT MARKDOWN ---
                    ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed project plan, and set up the development environment. This phase will focus on planning and setup, ensuring that all necessary components are in place for the successful execution of the project. The key deliverables for this phase include:
- A detailed project plan outlining the scope, timeline, and resources required
- A setup development environment with the necessary tools and technologies (Quarkus, Kafka, Postgres, Docker)
- Definition of the project's technical architecture and high-level design

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 1 includes:
- Setting up the project directory structure
- Initializing the Git repository
- Creating a basic Quarkus project template
- Setting up Kafka and Postgres for messaging and data storage
- Configuring Docker for containerization
- Defining the API endpoints for authentication, attendance tracking, and notification systems
- Creating a high-level design document outlining the system architecture

The allowed directory boundaries include:
- `src/main/java` for Java source code
- `src/main/resources` for configuration files and resources
- `docker` for Docker configuration files
- `kafka` for Kafka configuration files
- `postgres` for Postgres configuration files

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 1:
- **Coder**: Responsible for setting up the Quarkus project template, configuring Kafka and Postgres, and defining the API endpoints.
- **Tester**: Not actively involved in this phase, but will review the project plan and technical architecture.
- **Reviewer**: Responsible for reviewing the project plan, technical architecture, and high-level design document.
- **DevOps (Docker)**: Responsible for setting up the Docker configuration and ensuring containerization.
- **Deployer**: Not actively involved in this phase, but will review the project plan and technical architecture.

#### 4. Phase Definition of Done (DoD)
Phase 1 is considered complete when:
- The project plan is finalized and approved by all stakeholders
- The development environment is set up and configured
- The Quarkus project template is created and configured
- Kafka and Postgres are set up and configured
- Docker is configured for containerization
- The high-level design document is completed and approved by all stakeholders
- The project directory structure is initialized and the Git repository is set up

The expected duration for Phase 1 is 3 days, with the following milestones:
- Day 1: Project planning and scope definition
- Day 2: Setup of development environment and Quarkus project template
- Day 3: Configuration of Kafka, Postgres, and Docker, and completion of high-level design document
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 1181. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:


                    Analyze the attached Phase 1 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-1.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 1 CONTEXT MARKDOWN ---
                    ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed project plan, and set up the development environment. This phase will focus on planning and setup, ensuring that all necessary components are in place for the successful execution of the project. The key deliverables for this phase include:
- A detailed project plan outlining the scope, timeline, and resources required
- A setup development environment with the necessary tools and technologies (Quarkus, Kafka, Postgres, Docker)
- Definition of the project's technical architecture and high-level design

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 1 includes:
- Setting up the project directory structure
- Initializing the Git repository
- Creating a basic Quarkus project template
- Setting up Kafka and Postgres for messaging and data storage
- Configuring Docker for containerization
- Defining the API endpoints for authentication, attendance tracking, and notification systems
- Creating a high-level design document outlining the system architecture

The allowed directory boundaries include:
- `src/main/java` for Java source code
- `src/main/resources` for configuration files and resources
- `docker` for Docker configuration files
- `kafka` for Kafka configuration files
- `postgres` for Postgres configuration files

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 1:
- **Coder**: Responsible for setting up the Quarkus project template, configuring Kafka and Postgres, and defining the API endpoints.
- **Tester**: Not actively involved in this phase, but will review the project plan and technical architecture.
- **Reviewer**: Responsible for reviewing the project plan, technical architecture, and high-level design document.
- **DevOps (Docker)**: Responsible for setting up the Docker configuration and ensuring containerization.
- **Deployer**: Not actively involved in this phase, but will review the project plan and technical architecture.

#### 4. Phase Definition of Done (DoD)
Phase 1 is considered complete when:
- The project plan is finalized and approved by all stakeholders
- The development environment is set up and configured
- The Quarkus project template is created and configured
- Kafka and Postgres are set up and configured
- Docker is configured for containerization
- The high-level design document is completed and approved by all stakeholders
- The project directory structure is initialized and the Git repository is set up

The expected duration for Phase 1 is 3 days, with the following milestones:
- Day 1: Project planning and scope definition
- Day 2: Setup of development environment and Quarkus project template
- Day 3: Configuration of Kafka, Postgres, and Docker, and completion of high-level design document
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 404 - {'error': {'message': 'This model is unavailable for free. The paid version is available now - use this slug instead: deepseek/deepseek-r1', 'code': 404}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:


                    Analyze the attached Phase 1 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-1.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 1 CONTEXT MARKDOWN ---
                    ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed project plan, and set up the development environment. This phase will focus on planning and setup, ensuring that all necessary components are in place for the successful execution of the project. The key deliverables for this phase include:
- A detailed project plan outlining the scope, timeline, and resources required
- A setup development environment with the necessary tools and technologies (Quarkus, Kafka, Postgres, Docker)
- Definition of the project's technical architecture and high-level design

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 1 includes:
- Setting up the project directory structure
- Initializing the Git repository
- Creating a basic Quarkus project template
- Setting up Kafka and Postgres for messaging and data storage
- Configuring Docker for containerization
- Defining the API endpoints for authentication, attendance tracking, and notification systems
- Creating a high-level design document outlining the system architecture

The allowed directory boundaries include:
- `src/main/java` for Java source code
- `src/main/resources` for configuration files and resources
- `docker` for Docker configuration files
- `kafka` for Kafka configuration files
- `postgres` for Postgres configuration files

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 1:
- **Coder**: Responsible for setting up the Quarkus project template, configuring Kafka and Postgres, and defining the API endpoints.
- **Tester**: Not actively involved in this phase, but will review the project plan and technical architecture.
- **Reviewer**: Responsible for reviewing the project plan, technical architecture, and high-level design document.
- **DevOps (Docker)**: Responsible for setting up the Docker configuration and ensuring containerization.
- **Deployer**: Not actively involved in this phase, but will review the project plan and technical architecture.

#### 4. Phase Definition of Done (DoD)
Phase 1 is considered complete when:
- The project plan is finalized and approved by all stakeholders
- The development environment is set up and configured
- The Quarkus project template is created and configured
- Kafka and Postgres are set up and configured
- Docker is configured for containerization
- The high-level design document is completed and approved by all stakeholders
- The project directory structure is initialized and the Git repository is set up

The expected duration for Phase 1 is 3 days, with the following milestones:
- Day 1: Project planning and scope definition
- Day 2: Setup of development environment and Quarkus project template
- Day 3: Configuration of Kafka, Postgres, and Docker, and completion of high-level design document
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 400 - {'error': {'message': 'google/gemma-4-31b-instruct is not a valid model ID', 'code': 400}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:


                    Analyze the attached Phase 1 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-1.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 1 CONTEXT MARKDOWN ---
                    ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed project plan, and set up the development environment. This phase will focus on planning and setup, ensuring that all necessary components are in place for the successful execution of the project. The key deliverables for this phase include:
- A detailed project plan outlining the scope, timeline, and resources required
- A setup development environment with the necessary tools and technologies (Quarkus, Kafka, Postgres, Docker)
- Definition of the project's technical architecture and high-level design

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 1 includes:
- Setting up the project directory structure
- Initializing the Git repository
- Creating a basic Quarkus project template
- Setting up Kafka and Postgres for messaging and data storage
- Configuring Docker for containerization
- Defining the API endpoints for authentication, attendance tracking, and notification systems
- Creating a high-level design document outlining the system architecture

The allowed directory boundaries include:
- `src/main/java` for Java source code
- `src/main/resources` for configuration files and resources
- `docker` for Docker configuration files
- `kafka` for Kafka configuration files
- `postgres` for Postgres configuration files

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 1:
- **Coder**: Responsible for setting up the Quarkus project template, configuring Kafka and Postgres, and defining the API endpoints.
- **Tester**: Not actively involved in this phase, but will review the project plan and technical architecture.
- **Reviewer**: Responsible for reviewing the project plan, technical architecture, and high-level design document.
- **DevOps (Docker)**: Responsible for setting up the Docker configuration and ensuring containerization.
- **Deployer**: Not actively involved in this phase, but will review the project plan and technical architecture.

#### 4. Phase Definition of Done (DoD)
Phase 1 is considered complete when:
- The project plan is finalized and approved by all stakeholders
- The development environment is set up and configured
- The Quarkus project template is created and configured
- Kafka and Postgres are set up and configured
- Docker is configured for containerization
- The high-level design document is completed and approved by all stakeholders
- The project directory structure is initialized and the Git repository is set up

The expected duration for Phase 1 is 3 days, with the following milestones:
- Day 1: Project planning and scope definition
- Day 2: Setup of development environment and Quarkus project template
- Day 3: Configuration of Kafka, Postgres, and Docker, and completion of high-level design document
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 492. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 984. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 984. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 984. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 984. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 984. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 984. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 984. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 984. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:


                    Analyze the attached Phase 1 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-1.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 1 CONTEXT MARKDOWN ---
                    ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed project plan, and set up the development environment. This phase will focus on planning and setup, ensuring that all necessary components are in place for the successful execution of the project. The key deliverables for this phase include:
- A detailed project plan outlining the scope, timeline, and resources required
- A setup development environment with the necessary tools and technologies (Quarkus, Kafka, Postgres, Docker)
- Definition of the project's technical architecture and high-level design

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 1 includes:
- Setting up the project directory structure
- Initializing the Git repository
- Creating a basic Quarkus project template
- Setting up Kafka and Postgres for messaging and data storage
- Configuring Docker for containerization
- Defining the API endpoints for authentication, attendance tracking, and notification systems
- Creating a high-level design document outlining the system architecture

The allowed directory boundaries include:
- `src/main/java` for Java source code
- `src/main/resources` for configuration files and resources
- `docker` for Docker configuration files
- `kafka` for Kafka configuration files
- `postgres` for Postgres configuration files

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 1:
- **Coder**: Responsible for setting up the Quarkus project template, configuring Kafka and Postgres, and defining the API endpoints.
- **Tester**: Not actively involved in this phase, but will review the project plan and technical architecture.
- **Reviewer**: Responsible for reviewing the project plan, technical architecture, and high-level design document.
- **DevOps (Docker)**: Responsible for setting up the Docker configuration and ensuring containerization.
- **Deployer**: Not actively involved in this phase, but will review the project plan and technical architecture.

#### 4. Phase Definition of Done (DoD)
Phase 1 is considered complete when:
- The project plan is finalized and approved by all stakeholders
- The development environment is set up and configured
- The Quarkus project template is created and configured
- Kafka and Postgres are set up and configured
- Docker is configured for containerization
- The high-level design document is completed and approved by all stakeholders
- The project directory structure is initialized and the Git repository is set up

The expected duration for Phase 1 is 3 days, with the following milestones:
- Day 1: Project planning and scope definition
- Day 2: Setup of development environment and Quarkus project template
- Day 3: Configuration of Kafka, Postgres, and Docker, and completion of high-level design document
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 84. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 84. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:


                    Analyze the attached Phase 1 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-1.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 1 CONTEXT MARKDOWN ---
                    ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed project plan, and set up the development environment. This phase will focus on planning and setup, ensuring that all necessary components are in place for the successful execution of the project. The key deliverables for this phase include:
- A detailed project plan outlining the scope, timeline, and resources required
- A setup development environment with the necessary tools and technologies (Quarkus, Kafka, Postgres, Docker)
- Definition of the project's technical architecture and high-level design

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 1 includes:
- Setting up the project directory structure
- Initializing the Git repository
- Creating a basic Quarkus project template
- Setting up Kafka and Postgres for messaging and data storage
- Configuring Docker for containerization
- Defining the API endpoints for authentication, attendance tracking, and notification systems
- Creating a high-level design document outlining the system architecture

The allowed directory boundaries include:
- `src/main/java` for Java source code
- `src/main/resources` for configuration files and resources
- `docker` for Docker configuration files
- `kafka` for Kafka configuration files
- `postgres` for Postgres configuration files

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 1:
- **Coder**: Responsible for setting up the Quarkus project template, configuring Kafka and Postgres, and defining the API endpoints.
- **Tester**: Not actively involved in this phase, but will review the project plan and technical architecture.
- **Reviewer**: Responsible for reviewing the project plan, technical architecture, and high-level design document.
- **DevOps (Docker)**: Responsible for setting up the Docker configuration and ensuring containerization.
- **Deployer**: Not actively involved in this phase, but will review the project plan and technical architecture.

#### 4. Phase Definition of Done (DoD)
Phase 1 is considered complete when:
- The project plan is finalized and approved by all stakeholders
- The development environment is set up and configured
- The Quarkus project template is created and configured
- Kafka and Postgres are set up and configured
- Docker is configured for containerization
- The high-level design document is completed and approved by all stakeholders
- The project directory structure is initialized and the Git repository is set up

The expected duration for Phase 1 is 3 days, with the following milestones:
- Day 1: Project planning and scope definition
- Day 2: Setup of development environment and Quarkus project template
- Day 3: Configuration of Kafka, Postgres, and Docker, and completion of high-level design document
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Could not parse response content as the length limit was reached - CompletionUsage(completion_tokens=4096, prompt_tokens=1654, total_tokens=5750, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=None, audio_tokens=0, reasoning_tokens=4725, rejected_prediction_tokens=None, image_tokens=0), prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cache_write_tokens=0, cached_tokens=0, video_tokens=0), cost=0, is_byok=False, cost_details={'upstream_inference_cost': 0, 'upstream_inference_prompt_cost': 0, 'upstream_inference_completions_cost': 0})
```

# Phase 1 STEPS - Prompt:


                    Analyze the attached Phase 1 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-1.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 1 CONTEXT MARKDOWN ---
                    ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed project plan, and set up the development environment. This phase will focus on planning and setup, ensuring that all necessary components are in place for the successful execution of the project. The key deliverables for this phase include:
- A detailed project plan outlining the scope, timeline, and resources required
- A setup development environment with the necessary tools and technologies (Quarkus, Kafka, Postgres, Docker)
- Definition of the project's technical architecture and high-level design

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 1 includes:
- Setting up the project directory structure
- Initializing the Git repository
- Creating a basic Quarkus project template
- Setting up Kafka and Postgres for messaging and data storage
- Configuring Docker for containerization
- Defining the API endpoints for authentication, attendance tracking, and notification systems
- Creating a high-level design document outlining the system architecture

The allowed directory boundaries include:
- `src/main/java` for Java source code
- `src/main/resources` for configuration files and resources
- `docker` for Docker configuration files
- `kafka` for Kafka configuration files
- `postgres` for Postgres configuration files

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 1:
- **Coder**: Responsible for setting up the Quarkus project template, configuring Kafka and Postgres, and defining the API endpoints.
- **Tester**: Not actively involved in this phase, but will review the project plan and technical architecture.
- **Reviewer**: Responsible for reviewing the project plan, technical architecture, and high-level design document.
- **DevOps (Docker)**: Responsible for setting up the Docker configuration and ensuring containerization.
- **Deployer**: Not actively involved in this phase, but will review the project plan and technical architecture.

#### 4. Phase Definition of Done (DoD)
Phase 1 is considered complete when:
- The project plan is finalized and approved by all stakeholders
- The development environment is set up and configured
- The Quarkus project template is created and configured
- Kafka and Postgres are set up and configured
- Docker is configured for containerization
- The high-level design document is completed and approved by all stakeholders
- The project directory structure is initialized and the Git repository is set up

The expected duration for Phase 1 is 3 days, with the following milestones:
- Day 1: Project planning and scope definition
- Day 2: Setup of development environment and Quarkus project template
- Day 3: Configuration of Kafka, Postgres, and Docker, and completion of high-level design document
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 787. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 1476. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 1312. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 1476. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 787. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:


                    Analyze the attached Phase 1 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-1.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 1 CONTEXT MARKDOWN ---
                    ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed project plan, and set up the development environment. This phase will focus on planning and setup, ensuring that all necessary components are in place for the successful execution of the project. The key deliverables for this phase include:
- A detailed project plan outlining the scope, timeline, and resources required
- A setup development environment with the necessary tools and technologies (Quarkus, Kafka, Postgres, Docker)
- Definition of the project's technical architecture and high-level design

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 1 includes:
- Setting up the project directory structure
- Initializing the Git repository
- Creating a basic Quarkus project template
- Setting up Kafka and Postgres for messaging and data storage
- Configuring Docker for containerization
- Defining the API endpoints for authentication, attendance tracking, and notification systems
- Creating a high-level design document outlining the system architecture

The allowed directory boundaries include:
- `src/main/java` for Java source code
- `src/main/resources` for configuration files and resources
- `docker` for Docker configuration files
- `kafka` for Kafka configuration files
- `postgres` for Postgres configuration files

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 1:
- **Coder**: Responsible for setting up the Quarkus project template, configuring Kafka and Postgres, and defining the API endpoints.
- **Tester**: Not actively involved in this phase, but will review the project plan and technical architecture.
- **Reviewer**: Responsible for reviewing the project plan, technical architecture, and high-level design document.
- **DevOps (Docker)**: Responsible for setting up the Docker configuration and ensuring containerization.
- **Deployer**: Not actively involved in this phase, but will review the project plan and technical architecture.

#### 4. Phase Definition of Done (DoD)
Phase 1 is considered complete when:
- The project plan is finalized and approved by all stakeholders
- The development environment is set up and configured
- The Quarkus project template is created and configured
- Kafka and Postgres are set up and configured
- Docker is configured for containerization
- The high-level design document is completed and approved by all stakeholders
- The project directory structure is initialized and the Git repository is set up

The expected duration for Phase 1 is 3 days, with the following milestones:
- Day 1: Project planning and scope definition
- Day 2: Setup of development environment and Quarkus project template
- Day 3: Configuration of Kafka, Postgres, and Docker, and completion of high-level design document
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 787. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 656. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 787. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 762. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 1181. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 4096 tokens, but can only afford 242. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
```

# Phase 1 STEPS - Prompt:


                    Analyze the attached Phase 1 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-1.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 1 CONTEXT MARKDOWN ---
                    ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed project plan, and set up the development environment. This phase will focus on planning and setup, ensuring that all necessary components are in place for the successful execution of the project. The key deliverables for this phase include:
- A detailed project plan outlining the scope, timeline, and resources required
- A setup development environment with the necessary tools and technologies (Quarkus, Kafka, Postgres, Docker)
- Definition of the project's technical architecture and high-level design

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 1 includes:
- Setting up the project directory structure
- Initializing the Git repository
- Creating a basic Quarkus project template
- Setting up Kafka and Postgres for messaging and data storage
- Configuring Docker for containerization
- Defining the API endpoints for authentication, attendance tracking, and notification systems
- Creating a high-level design document outlining the system architecture

The allowed directory boundaries include:
- `src/main/java` for Java source code
- `src/main/resources` for configuration files and resources
- `docker` for Docker configuration files
- `kafka` for Kafka configuration files
- `postgres` for Postgres configuration files

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 1:
- **Coder**: Responsible for setting up the Quarkus project template, configuring Kafka and Postgres, and defining the API endpoints.
- **Tester**: Not actively involved in this phase, but will review the project plan and technical architecture.
- **Reviewer**: Responsible for reviewing the project plan, technical architecture, and high-level design document.
- **DevOps (Docker)**: Responsible for setting up the Docker configuration and ensuring containerization.
- **Deployer**: Not actively involved in this phase, but will review the project plan and technical architecture.

#### 4. Phase Definition of Done (DoD)
Phase 1 is considered complete when:
- The project plan is finalized and approved by all stakeholders
- The development environment is set up and configured
- The Quarkus project template is created and configured
- Kafka and Postgres are set up and configured
- Docker is configured for containerization
- The high-level design document is completed and approved by all stakeholders
- The project directory structure is initialized and the Git repository is set up

The expected duration for Phase 1 is 3 days, with the following milestones:
- Day 1: Project planning and scope definition
- Day 2: Setup of development environment and Quarkus project template
- Day 3: Configuration of Kafka, Postgres, and Docker, and completion of high-level design document
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
{
    "phase_id": 1,
    "phase_name": "test-ai-architecture",
    "project_name": "test-ai-architecture",
    "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
    "source_target_dir": "sources/",
    "days": [
        {
            "day": 1,
            "context_file": ".ai/.plan/.context/phase-1.context.blueprint.md",
            "context_section": "DAY 1",
            "sub_tasks": [
                {
                    "id": "task-1-1",
                    "agent": "Coder",
                    "desc": "Define the project scope and objectives in the context blueprint."
                },
                {
                    "id": "task-1-2",
                    "agent": "Reviewer",
                    "desc": "Review and approve the project scope and objectives defined by the Coder."
                },
                {
                    "id": "task-1-3",
                    "agent": "Coder",
                    "desc": "Create a detailed project plan outlining the scope, timeline, and resources required."
                },
                {
                    "id": "task-1-4",
                    "agent": "Reviewer",
                    "desc": "Review and approve the detailed project plan created by the Coder."
                }
            ]
        },
        {
            "day": 0,
            "context_file": ".ai/.plan/.context/phase-1.context.blueprint.md",
            "context_section": "DAY 0",
            "sub_tasks": [
                {
                    "id": "task-0-1",
                    "agent": "Coder",
                    "desc": "Initialize the Git repository for the project."
                },
                {
                    "id": "task-0-2",
                    "agent": "DevOps",
                    "desc": "Set up the project directory structure with allowed boundaries (src/main/java, src/main/resources, docker, kafka, postgres)."
                },
                {
                    "id": "task-0-3",
                    "agent": "Reviewer",
                    "desc": "Review the initialized directory structure and Git repository setup."
                },
                {
                    "id": "task-0-4",
                    "agent": "Coder",
                    "desc": "Create a basic Quarkus project template."
                },
                {
                    "id": "task-0-5",
                    "agent": "Reviewer",
                    "desc": "Review and approve the Quarkus project template created by the Coder."
                }
            ]
        }
    ]
}
```

# Phase 2 STEPS - Prompt:


                    Analyze the attached Phase 2 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-2.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 2 CONTEXT MARKDOWN ---
                    ## PHASE 2 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 2 is to develop the backend features of the membership-hub project, including authentication, attendance tracking, and notification systems. This phase will focus on building a scalable and secure backend using Quarkus, Kafka, and Postgres. The key deliverables for this phase include:
- Design and implementation of authentication mechanisms (email/password, Firebase, Google, Facebook)
- Development of attendance tracking features (QR code-based attendance tracking)
- Implementation of notification systems (SMS, Zalo, in-app notifications)
- Integration with Postgres database for data storage
- Containerization using Docker for seamless deployment on GKE

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 2 will be limited to the backend development, with the following directory boundaries:
- `src/main/java`: Java source code for Quarkus application
- `src/main/resources`: Configuration files and static resources
- `docker`: Dockerfile and containerization scripts
- `kafka`: Kafka configuration and topic definitions
- `postgres`: Postgres database schema and migration scripts
- `api`: API endpoints for authentication, attendance tracking, and notification systems
Allowed endpoints:
- `/api/auth`: Authentication endpoints (login, logout, register)
- `/api/attendance`: Attendance tracking endpoints (QR code scanning, attendance logging)
- `/api/notifications`: Notification endpoints (SMS, Zalo, in-app notifications)

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
- **Coder**: Implement authentication mechanisms, attendance tracking features, and notification systems. Develop API endpoints for backend features.
- **Tester**: Develop unit tests and integration tests for backend features. Test authentication, attendance tracking, and notification systems.
- **Reviewer**: Review code for adherence to coding standards, security, and scalability. Provide feedback on API endpoint design and implementation.
- **DevOps (Docker)**: Containerize the Quarkus application using Docker. Ensure seamless deployment on GKE.
- **DevOps (Deployer)**: Prepare deployment scripts for GCP and GKE. Ensure zero-downtime deployments.

#### 4. Phase Definition of Done (DoD)
Phase 2 is considered complete when:
- All backend features (authentication, attendance tracking, notification systems) are implemented and tested.
- API endpoints are designed and implemented for backend features.
- Code is reviewed and meets coding standards, security, and scalability requirements.
- Docker containerization is complete, and deployment scripts are prepared for GCP and GKE.
- Unit tests and integration tests are developed and passed for backend features.
The maximum duration for Phase 2 is 7 days. Once the core technical objectives are satisfied, the phase will be considered complete, and progression to Phase 3 will begin.
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
{
    "phase_id": 2,
    "phase_name": "test-ai-architecture",
    "project_name": "membership-hub",
    "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
    "source_target_dir": "sources/",
    "days": [
        {
            "day": 1,
            "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
            "context_section": "DAY 1",
            "sub_tasks": [
                {
                    "id": "task-1-1",
                    "agent": "Coder",
                    "desc": "Set up Quarkus project structure with Maven and initialize basic dependencies."
                },
                {
                    "id": "task-1-2",
                    "agent": "Coder",
                    "desc": "Implement initial authentication framework with email/password login mechanism."
                },
                {
                    "id": "task-1-3",
                    "agent": "Tester",
                    "desc": "Write unit tests for initial authentication module setup."
                },
                {
                    "id": "task-1-4",
                    "agent": "Reviewer",
                    "desc": "Review initial Quarkus project setup and authentication framework for coding standards and security."
                },
                {
                    "id": "task-1-5",
                    "agent": "DevOps (Docker)",
                    "desc": "Create Dockerfile for Quarkus application and configure base image."
                }
            ]
        },
        {
            "day": 2,
            "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
            "context_section": "DAY 2",
            "sub_tasks": [
                {
                    "id": "task-2-1",
                    "agent": "Coder",
                    "desc": "Implement Firebase authentication integration."
                },
                {
                    "id": "task-2-2",
                    "agent": "Coder",
                    "desc": "Implement Google authentication integration."
                },
                {
                    "id": "task-2-3",
                    "agent": "Coder",
                    "desc": "Implement Facebook authentication integration."
                },
                {
                    "id": "task-2-4",
                    "agent": "Tester",
                    "desc": "Develop integration tests for third-party authentication providers."
                },
                {
                    "id": "task-2-5",
                    "agent": "Reviewer",
                    "desc": "Review authentication integrations for security vulnerabilities and scalability."
                }
            ]
        },
        {
            "day": 3,
            "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
            "context_section": "DAY 3",
            "sub_tasks": [
                {
                    "id": "task-3-1",
                    "agent": "Coder",
                    "desc": "Design and implement QR code generation service for attendance tracking."
                },
                {
                    "id": "task-3-2",
                    "agent": "Coder",
                    "desc": "Implement QR code scanning endpoint for mobile clients."
                },
                {
                    "id": "task-3-3",
                    "agent": "Tester",
                    "desc": "Test QR code generation and scanning functionality with sample data."
                },
                {
                    "id": "task-3-4",
                    "agent": "Reviewer",
                    "desc": "Review attendance tracking system design for performance and data integrity."
                },
                {
                    "id": "task-3-5",
                    "agent": "DevOps (Docker)",
                    "desc": "Update Dockerfile to include necessary libraries for QR code processing."
                }
            ]
        },
        {
            "day": 4,
            "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
            "context_section": "DAY 4",
            "sub_tasks": [
                {
                    "id": "task-4-1",
                    "agent": "Coder",
                    "desc": "Implement SMS notification service using external provider API."
                },
                {
                    "id": "task-4-2",
                    "agent": "Coder",
                    "desc": "Implement Zalo notification service using official SDK."
                },
                {
                    "id": "task-4-3",
                    "agent": "Coder",
                    "desc": "Implement in-app notification system with WebSocket support."
                },
                {
                    "id": "task-4-4",
                    "agent": "Tester",
                    "desc": "Perform end-to-end testing of notification services across different platforms."
                },
                {
                    "id": "task-4-5",
                    "agent": "Reviewer",
                    "desc": "Evaluate notification system architecture for reliability and maintainability."
                }
            ]
        },
        {
            "day": 5,
            "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
            "context_section": "DAY 5",
            "sub_tasks": [
                {
                    "id": "task-5-1",
                    "agent": "Coder",
                    "desc": "Define PostgreSQL database schema for user profiles, attendance records, and notifications."
                },
                {
                    "id": "task-5-2",
                    "agent": "Coder",
                    "desc": "Implement database migration scripts using Flyway or Liquibase."
                },
                {
                    "id": "task-5-3",
                    "agent": "Tester",
                    "desc": "Run integration tests against PostgreSQL database with sample datasets."
                },
                {
                    "id": "task-5-4",
                    "agent": "Reviewer",
                    "desc": "Audit database schema and migration scripts for normalization and indexing strategies."
                },
                {
                    "id": "task-5-5",
                    "agent": "DevOps (Docker)",
                    "desc": "Configure Docker Compose for local development environment including PostgreSQL container."
                }
            ]
        },
        {
            "day": 6,
            "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
            "context_section": "DAY 6",
            "sub_tasks": [
                {
                    "id": "task-6-1",
                    "agent": "Coder",
                    "desc": "Integrate Kafka producers and consumers for asynchronous event handling."
                },
                {
                    "id": "task-6-2",
                    "agent": "Coder",
                    "desc": "Implement Kafka topics for authentication events, attendance logs, and notifications."
                },
                {
                    "id": "task-6-3",
                    "agent": "Tester",
                    "desc": "Test Kafka message flow and ensure proper event distribution across services."
                },
                {
                    "id": "task-6-4",
                    "agent": "Reviewer",
                    "desc": "Analyze Kafka integration for fault tolerance and scalability considerations."
                },
                {
                    "id": "task-6-5",
                    "agent": "DevOps (Deployer)",
                    "desc": "Prepare deployment manifests for GKE cluster with Kubernetes configurations."
                }
            ]
        },
        {
            "day": 7,
            "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
            "context_section": "DAY 7",
            "sub_tasks": [
                {
                    "id": "task-7-1",
                    "agent": "Coder",
                    "desc": "Finalize all API endpoints for authentication, attendance tracking, and notifications."
                },
                {
                    "id": "task-7-2",
                    "agent": "Tester",
                    "desc": "Execute full regression testing suite covering all backend features."
                },
                {
                    "id": "task-7-3",
                    "agent": "Reviewer",
                    "desc": "Conduct final code review and documentation check for compliance with DoD."
                },
                {
                    "id": "task-7-4",
                    "agent": "DevOps (Docker)",
                    "desc": "Build and push final Docker images to registry for production deployment."
                },
                {
                    "id": "task-7-5",
                    "agent": "DevOps (Deployer)",
                    "desc": "Deploy application to GKE cluster with zero-downtime rollout strategy."
                }
            ]
        }
    ]
}
```

# Phase 3 STEPS - Prompt:


                    Analyze the attached Phase 3 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-3.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 3 CONTEXT MARKDOWN ---
                    ## PHASE 3 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 3 is to develop the web and mobile applications for the membership-hub project. This phase will focus on creating a user-friendly interface for students to manage their attendance and for centers to track student activity. The key deliverables for this phase include:
- Developing the web application using Next.js
- Implementing QR code scanning for attendance tracking
- Integrating multi-language support for both web and mobile applications
- Ensuring SEO optimization for the web application
- Building the mobile application for both iOS and Android platforms

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 3 will be limited to the frontend development of the web and mobile applications. The following directories, files, and endpoints are in scope:
- `web-app/`: Directory for the web application code
- `mobile-app/`: Directory for the mobile application code
- `api/`: Directory for API endpoints for frontend-backend interaction
- `components/`: Directory for reusable UI components
- `locales/`: Directory for language translations
- Endpoints for:
  - QR code scanning
  - Attendance tracking
  - User profile management
  - Language selection

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 3, with the following tasks:
- **Coder**: Develop the web and mobile applications, implement QR code scanning, multi-language support, and SEO optimization
- **Tester**: Test the web and mobile applications for functionality, performance, and security
- **Reviewer**: Review the code for adherence to coding standards, best practices, and security guidelines
- **DevOps (Docker)**: Containerize the web application for deployment on GKE
- **DevOps (Deployer)**: Prepare the environment for deployment, ensure zero-downtime deployments

#### 4. Phase Definition of Done (DoD)
Phase 3 will be considered complete when the following conditions are met:
- The web application is fully functional, with QR code scanning, multi-language support, and SEO optimization
- The mobile application is fully functional, with QR code scanning, multi-language support, and push notifications
- All code has been reviewed and approved by the Reviewer
- The web application has been containerized and is ready for deployment on GKE
- The mobile application has been built and is ready for deployment on app stores
- All testing has been completed, and the application has been verified to meet the requirements and quality standards.
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
{
    "phase_id": 3,
    "phase_name": "test-ai-architecture",
    "project_name": "membership-hub",
    "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
    "source_target_dir": "sources/",
    "days": [
        {
            "day": 1,
            "context_file": ".ai/.plan/.context/phase-3.context.blueprint.md",
            "context_section": "DAY 1",
            "sub_tasks": [
                {
                    "id": "task-1-1",
                    "agent": "Coder",
                    "desc": "Set up the Next.js web application project structure and initialize the repository with necessary configurations."
                },
                {
                    "id": "task-1-2",
                    "agent": "Coder",
                    "desc": "Create the basic UI components for the web application including header, footer, and navigation."
                },
                {
                    "id": "task-1-3",
                    "agent": "Tester",
                    "desc": "Define the test plan for the web application, including functional, performance, and security testing requirements."
                },
                {
                    "id": "task-1-4",
                    "agent": "Reviewer",
                    "desc": "Establish code review guidelines and standards for the web application development process."
                },
                {
                    "id": "task-1-5",
                    "agent": "DevOps (Docker)",
                    "desc": "Create a Dockerfile for the Next.js web application to enable containerization."
                }
            ]
        },
        {
            "day": 0,
            "context_file": ".ai/.plan/.context/phase-3.context.blueprint.md",
            "context_section": "DAY 0",
            "sub_tasks": [
                {
                    "id": "task-0-1",
                    "agent": "Coder",
                    "desc": "Implement QR code scanning functionality for the web application using a third-party library."
                },
                {
                    "id": "task-0-2",
                    "agent": "Coder",
                    "desc": "Integrate multi-language support into the web application using i18next or similar framework."
                },
                {
                    "id": "task-0-3",
                    "agent": "Coder",
                    "desc": "Apply SEO optimization techniques to the web application including meta tags, structured data, and sitemap generation."
                },
                {
                    "id": "task-0-4",
                    "agent": "Tester",
                    "desc": "Conduct end-to-end testing of the QR code scanning feature on the web application."
                },
                {
                    "id": "task-0-5",
                    "agent": "Tester",
                    "desc": "Perform localization testing for the multi-language support in the web application."
                },
                {
                    "id": "task-0-6",
                    "agent": "Reviewer",
                    "desc": "Review the implementation of QR code scanning and multi-language support for adherence to coding standards."
                },
                {
                    "id": "task-0-7",
                    "agent": "DevOps (Deployer)",
                    "desc": "Prepare the staging environment for deployment of the web application."
                }
            ]
        }
    ]
}
```

# Phase 4 STEPS - Prompt:


                    Analyze the attached Phase 4 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-4.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 4 CONTEXT MARKDOWN ---
                    ## PHASE 4 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 4 is to conduct thorough testing and quality assurance of the membership-hub project. This phase will focus on ensuring the application's functionality, performance, and security meet the required standards. The scope of this phase includes:

* Unit testing of individual components
* Integration testing of interconnected components
* Performance testing to ensure scalability and reliability
* Security testing to identify vulnerabilities
* User acceptance testing (UAT) to validate the application's functionality

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope of this phase is limited to the testing and quality assurance of the existing codebase. The following directories and files are within the scope:

* `src/test`: Unit tests and integration tests
* `src/main`: Application codebase
* `docker-compose.yml`: Docker configuration for testing
* `kafka-config.properties`: Kafka configuration for testing
* `postgres-config.properties`: Postgres configuration for testing
* API endpoints for testing:
	+ `/api/v1/auth`
	+ `/api/v1/attendance`
	+ `/api/v1/notifications`

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in this phase:

* **Coder**: Assist in writing unit tests and integration tests
* **Tester**: Conduct thorough testing of the application, including performance testing and security testing
* **Reviewer**: Review test cases and provide feedback on test coverage and effectiveness
* **DevOps**: Configure and manage the testing environment, including Docker and Kafka

Tasks:

* Coder:
	+ Write unit tests for individual components (Days 1-2)
	+ Write integration tests for interconnected components (Days 2-3)
* Tester:
	+ Conduct performance testing (Days 1-2)
	+ Conduct security testing (Days 2-3)
	+ Conduct UAT (Days 3-4)
* Reviewer:
	+ Review test cases (Days 1-2)
	+ Provide feedback on test coverage and effectiveness (Days 2-3)
* DevOps:
	+ Configure testing environment (Day 1)
	+ Manage testing environment (Days 1-4)

#### 4. Phase Definition of Done (DoD)
The phase is considered complete when:

* All unit tests and integration tests have been written and executed successfully
* Performance testing and security testing have been conducted, and results have been reviewed and addressed
* UAT has been conducted, and results have been reviewed and addressed
* Test coverage is at least 80%
* All test cases have been reviewed and feedback has been incorporated
* The testing environment has been properly configured and managed

The phase will be stopped once the core technical objectives are satisfied, and the phase's definition of done has been met. The maximum duration for this phase is 7 days.
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
{
    "phase_id": 4,
    "phase_name": "test-ai-architecture",
    "project_name": "membership-hub",
    "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
    "source_target_dir": "sources/",
    "days": [
        {
            "day": 1,
            "context_file": ".ai/.plan/.context/phase-4.context.blueprint.md",
            "context_section": "DAY 1",
            "sub_tasks": [
                {
                    "id": "1.1",
                    "agent": "Coder",
                    "desc": "Write unit tests for individual components"
                },
                {
                    "id": "1.2",
                    "agent": "Tester",
                    "desc": "Conduct performance testing"
                },
                {
                    "id": "1.3",
                    "agent": "Reviewer",
                    "desc": "Review test cases"
                },
                {
                    "id": "1.4",
                    "agent": "DevOps",
                    "desc": "Configure testing environment"
                },
                {
                    "id": "1.5",
                    "agent": "DevOps",
                    "desc": "Manage testing environment"
                }
            ]
        },
        {
            "day": 2,
            "context_file": ".ai/.plan/.context/phase-4.context.blueprint.md",
            "context_section": "DAY 2",
            "sub_tasks": [
                {
                    "id": "2.1",
                    "agent": "Coder",
                    "desc": "Write unit tests for individual components"
                },
                {
                    "id": "2.2",
                    "agent": "Coder",
                    "desc": "Write integration tests for interconnected components"
                },
                {
                    "id": "2.3",
                    "agent": "Tester",
                    "desc": "Conduct performance testing"
                },
                {
                    "id": "2.4",
                    "agent": "Tester",
                    "desc": "Conduct security testing"
                },
                {
                    "id": "2.5",
                    "agent": "Reviewer",
                    "desc": "Review test cases"
                },
                {
                    "id": "2.6",
                    "agent": "Reviewer",
                    "desc": "Provide feedback on test coverage and effectiveness"
                },
                {
                    "id": "2.7",
                    "agent": "DevOps",
                    "desc": "Manage testing environment"
                }
            ]
        },
        {
            "day": 3,
            "context_file": ".ai/.plan/.context/phase-4.context.blueprint.md",
            "context_section": "DAY 3",
            "sub_tasks": [
                {
                    "id": "3.1",
                    "agent": "Coder",
                    "desc": "Write integration tests for interconnected components"
                },
                {
                    "id": "3.2",
                    "agent": "Tester",
                    "desc": "Conduct security testing"
                },
                {
                    "id": "3.3",
                    "agent": "Tester",
                    "desc": "Conduct UAT"
                },
                {
                    "id": "3.4",
                    "agent": "Reviewer",
                    "desc": "Provide feedback on test coverage and effectiveness"
                },
                {
                    "id": "3.5",
                    "agent": "DevOps",
                    "desc": "Manage testing environment"
                }
            ]
        },
        {
            "day": 4,
            "context_file": ".ai/.plan/.context/phase-4.context.blueprint.md",
            "context_section": "DAY 4",
            "sub_tasks": [
                {
                    "id": "4.1",
                    "agent": "Tester",
                    "desc": "Conduct UAT"
                },
                {
                    "id": "4.2",
                    "agent": "DevOps",
                    "desc": "Manage testing environment"
                }
            ]
        }
    ]
}
```

# Phase 5 STEPS - Prompt:


                    Analyze the attached Phase 5 Context Markdown content. 
                    Extract and translate ALL daily steps, checklists, and agent tasks.

                    CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
                    1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day 1 and Day 0 (inclusive).
                    2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [1 to 0]. 
                    3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
                    4. STRICT LITERAL FIELD VALUES (MANDATORY):
                       - Populate the exact string ".ai/.context/test-ai-architecture.global.blueprint.md" into the 'global_context_file' field.
                       - Populate the exact string "sources/" into the 'source_target_dir' field.
                    5. Task Details: For every micro task item under a specific day:
                       - Provide a sequential task description text into the 'task' field.
                       - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
                    6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '.ai/.plan/.context/phase-5.context.blueprint.md', and set 'context_section' to 'DAY ' followed by the day number.

                    You MUST conform strictly to your required JSON Schema layout design structure:
                    {
  "$defs": {
    "DailyStep": {
      "properties": {
        "day": {
          "description": "Timeline iteration day inside this isolated phase.",
          "title": "Day",
          "type": "integer"
        },
        "context_file": {
          "description": "The phase context Markdown file for closure on this day.",
          "title": "Context File",
          "type": "string"
        },
        "context_section": {
          "description": "The day targeted for closure on this day.",
          "title": "Context Section",
          "type": "string"
        },
        "sub_tasks": {
          "description": "Array of isolated micro-tasks assigned to sub-agents.",
          "items": {
            "$ref": "##/$defs/SubAgentTask"
          },
          "title": "Sub Tasks",
          "type": "array"
        }
      },
      "required": [
        "day",
        "context_file",
        "context_section",
        "sub_tasks"
      ],
      "title": "DailyStep",
      "type": "object"
    },
    "SubAgentTask": {
      "properties": {
        "id": {
          "description": "Sub-Task identity of Task that sub-agent role executing.",
          "title": "Id",
          "type": "string"
        },
        "agent": {
          "description": "Target sub-agent role executing the task.",
          "title": "Agent",
          "type": "string"
        },
        "desc": {
          "description": "Literal, low-level technical step assigned to the agent.",
          "title": "Desc",
          "type": "string"
        }
      },
      "required": [
        "id",
        "agent",
        "desc"
      ],
      "title": "SubAgentTask",
      "type": "object"
    }
  },
  "properties": {
    "phase_id": {
      "description": "Target phase tracker index.",
      "title": "Phase Id",
      "type": "integer"
    },
    "phase_name": {
      "description": "Target phase tracker name.",
      "title": "Phase Name",
      "type": "string"
    },
    "project_name": {
      "description": "Target project tracker name.",
      "title": "Project Name",
      "type": "string"
    },
    "global_context_file": {
      "description": "Project global context Markdown file for closure.",
      "title": "Global Context File",
      "type": "string"
    },
    "source_target_dir": {
      "description": "Project sources folder path for closure.",
      "title": "Source Target Dir",
      "type": "string"
    },
    "days": {
      "description": "Day-by-day engineering tracking steps.",
      "items": {
        "$ref": "##/$defs/DailyStep"
      },
      "title": "Days",
      "type": "array"
    }
  },
  "required": [
    "phase_id",
    "phase_name",
    "project_name",
    "global_context_file",
    "source_target_dir",
    "days"
  ],
  "title": "PhaseStepsPlan",
  "type": "object"
}

                    --- PHASE 5 CONTEXT MARKDOWN ---
                    ## PHASE 5 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 5 is to deploy the membership-hub application on Google Cloud Platform (GCP) and Google Kubernetes Engine (GKE), ensuring a smooth and scalable operation. This phase will focus on:

* Deploying the application on GCP and GKE
* Configuring load balancing and autoscaling
* Ensuring zero-downtime deployments
* Setting up monitoring and logging tools
* Conducting final testing and quality assurance

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 5 includes:

* Deployment scripts and configurations for GCP and GKE
* Docker containerization and orchestration
* Load balancing and autoscaling configurations
* Monitoring and logging tools (e.g., Prometheus, Grafana, ELK Stack)
* API endpoints for deployment and management

Allowed directories and files:

* `deploy/`: deployment scripts and configurations
* `docker/`: Docker containerization and orchestration files
* `k8s/`: Kubernetes configurations and deployments
* `monitoring/`: monitoring and logging tools configurations

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 5:

* **Coder**: Responsible for creating deployment scripts and configurations, as well as ensuring the application is containerized and ready for deployment.
* **Tester**: Responsible for conducting final testing and quality assurance, including load testing and performance testing.
* **Reviewer**: Responsible for reviewing deployment scripts and configurations, as well as ensuring that the application is properly secured and compliant with regulatory requirements.
* **DevOps**: Responsible for deploying the application on GCP and GKE, configuring load balancing and autoscaling, and setting up monitoring and logging tools.
* **Docker**: Responsible for ensuring the application is properly containerized and orchestrated.
* **Deployer**: Responsible for deploying the application on GCP and GKE, and ensuring zero-downtime deployments.

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 5 includes:

* The application is successfully deployed on GCP and GKE
* Load balancing and autoscaling are properly configured
* Monitoring and logging tools are set up and functioning correctly
* Final testing and quality assurance have been completed
* The application is properly secured and compliant with regulatory requirements
* Deployment scripts and configurations are reviewed and approved
* The application is fully functional and performing as expected

Once these objectives are met, Phase 5 will be considered complete, and the project will be ready for maintenance and ongoing updates.
                    ------------------------------------------
                    

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
{
    "phase_id": 5,
    "phase_name": "test-ai-architecture",
    "project_name": "test-ai-architecture",
    "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
    "source_target_dir": "sources/",
    "days": [
        {
            "day": 1,
            "context_file": ".ai/.plan/.context/phase-5.context.blueprint.md",
            "context_section": "DAY 1",
            "sub_tasks": [
                {
                    "id": "task-1-1",
                    "agent": "DevOps",
                    "desc": "Set up GCP project and enable necessary APIs for GKE deployment."
                },
                {
                    "id": "task-1-2",
                    "agent": "Docker",
                    "desc": "Create Dockerfile for the membership-hub application."
                },
                {
                    "id": "task-1-3",
                    "agent": "Coder",
                    "desc": "Write initial deployment scripts for GCP and GKE."
                }
            ]
        },
        {
            "day": 0,
            "context_file": ".ai/.plan/.context/phase-5.context.blueprint.md",
            "context_section": "DAY 0",
            "sub_tasks": [
                {
                    "id": "task-0-1",
                    "agent": "DevOps",
                    "desc": "Configure load balancing and autoscaling settings for GKE cluster."
                },
                {
                    "id": "task-0-2",
                    "agent": "Reviewer",
                    "desc": "Review deployment configurations and ensure compliance with security standards."
                },
                {
                    "id": "task-0-3",
                    "agent": "Tester",
                    "desc": "Perform final load testing and performance validation of the deployed application."
                }
            ]
        }
    ]
}
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

# Global Prompt:



# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
'Template' object has no attribute 'substitute'
```

