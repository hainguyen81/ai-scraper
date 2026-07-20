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

