# PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
## 1. Phase Operational Scope & Objectives
| Item | Description |
|------|-------------|
| **Goal** | Establish a complete, actionable plan for the *membership‑hub* platform covering web & mobile front‑ends, Quarkus‑based micro‑services, Kafka event streaming, PostgreSQL persistence, Docker containerisation, and GCP‑GKE deployment. |
| **Key Activities (Days 1‑3)** | • Conduct stakeholder interviews & workshops to capture functional & non‑functional requirements.<br>• Document user stories, acceptance criteria, and edge cases (including QR‑based attendance, multi‑auth, multi‑language, SEO, notifications).<br>• Define technical architecture (service boundaries, data flow, authentication flow, event schema).<br>• Produce a detailed project plan with 5‑phase timeline, sprint‑level tasks, resource allocation, and risk register.<br>• Set up the initial repository structure, CI/CD skeleton, and environment manifests. |
| **Deliverables** | • Requirements Specification Document (RSD).<br>• User Story Map & Acceptance Criteria.<br>• Technical Architecture Diagram (including service contracts, Kafka topics, auth providers, GCP resources).<br>• Project Plan & Gantt (Phase‑level, with Day‑1‑to‑Day‑3 milestones).<br>• Repository with `README`, `CONTRIBUTING`, `ISSUE_TEMPLATE`, and placeholder `Dockerfile`s / `k8s` manifests. |
| **Constraints** | • Strict 7‑day max per phase – Phase 1 must be completed within Days 1‑3.<br>• No code implementation beyond scaffolding; focus on documentation & planning artifacts.<br>• All decisions must align with Global Guardrails (Security, Scalability, Compliance, Quality, Monitoring). |

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
```
membership-hub/
├─ docs/                     # Architecture & design docs
│   ├─ architecture.md
│   └─ requirements.md
├─ src/
│   ├─ backend/              # Quarkus micro‑service skeleton
│   │   ├─ src/main/java/com/hub/
│   │   ├─ src/main/resources/application.yml
│   │   └─ pom.xml
│   ├─ frontend/             # Next.js monorepo (web + mobile web view)
│   │   ├─ web/
│   │   └─ mobile/
│   └─ shared/               # Common models, enums, constants
├─ kafka/
│   └─ topics/               # Event schema definitions (Avro/Protobuf)
├─ db/
│   └─ migrations/           # Flyway/Liquibase scripts for Postgres
├─ docker/
│   ├─ Dockerfile.backend
│   └─ Dockerfile.frontend
├─ k8s/
│   ├─ backend/
│   │   └─ deployment.yaml
│   └─ frontend/
│       └─ deployment.yaml
├─ .github/
│   └─ workflows/
│       └─ ci.yml            # CI pipeline (build, lint, test)
├─ .gitlab-ci.yml (if used)  # CI/CD definitions
├─ README.md
├─ CONTRIBUTING.md
└─ LICENSE
```
**Allowed Endpoints (to be defined in Phase 1)**  
- `POST /api/auth/internal` – email/password sign‑in.  
- `POST /api/auth/firebase`, `POST /api/auth/google`, `POST /api/auth/facebook` – external OAuth flows.  
- `GET/POST /api/students/{id}/attendance` – QR check‑in (idempotent per day).  
- `GET /api/students/{id}/card` – remaining validity days.  
- `POST /api/notifications` – push/Zalo message dispatch.  

All other implementation details (service logic, UI components, Kafka producers/consumers) are **out of scope** for Phase 1.

## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)

| Sub‑Agent | Phase 1 Specific Tasks |
|-----------|------------------------|
| **Manager** | • Schedule and conduct 3 stakeholder workshops (client, product owner, security/compliance).<br>• Capture “must‑have”, “should‑have”, “could‑have” items; map to epics.<br>• Draft the Requirements Specification Document (RSD) with acceptance criteria.<br>• Produce the high‑level technical architecture diagram (service boundaries, data flow, auth providers, GCP resources).<br>• Create the Phase 1 project plan (Day‑1‑to‑Day‑3 tasks, dependencies, owners). |
| **Coder** | • Initialise the Git repository with the directory layout shown above.<br>• Create placeholder `pom.xml` (Quarkus) and `package.json`/`next.config.js` (Next.js) to satisfy build pipelines.<br>• Add basic `Dockerfile`s (backend & frontend) with multi‑stage builds.<br>• Draft Kafka topic definitions (Avro schemas) in `kafka/topics/`.<br>• Add Flyway migration skeleton for core tables (`students`, `attendance`, `cards`, `notifications`). |
| **Tester** | • Define the Test Strategy document (unit, integration, contract, security, performance).<br>• Draft test‑case templates for authentication flows, attendance idempotency, notification delivery, and multi‑language SEO.<br>• Create a lightweight test‑plan checklist aligned with the acceptance criteria.<br>• Set up a shared test‑environment manifest (Docker‑Compose for local dev). |
| **Reviewer** | • Publish Code‑Review Guidelines (Java/Quarkus, TypeScript/Next.js, Docker, YAML).<br>• Define security checklist (JWT handling, OAuth scopes, data encryption, GDPR/CCPA data‑handling).<br>• Review all Phase 1 artifacts (RSD, architecture diagram, code scaffolding) for compliance with guidelines. |
| **DevOps** | • Create the CI workflow (`.github/workflows/ci.yml`) that runs `mvn clean package` and `npm run build`.<br>• Draft Kubernetes manifests (`k8s/backend/deployment.yaml`, `k8s/frontend/deployment.yaml`) with resource limits & autoscaling hints.<br>• Add a `monitoring/` folder with Prometheus/Grafana dashboards skeleton and logging configuration (ELK/Stackdriver).<br>• Document local‑dev setup (Docker‑Compose) and GCP‑GKE deployment steps. |

## 4. Phase Definition of Done (DoD)
- **[RSD Completed]** All functional & non‑functional requirements captured, with acceptance criteria and priority levels.
- **[Architecture Documented]** Technical architecture diagram and service contracts approved by stakeholders.
- **[Project Plan Finalised]** Phase 1 Gantt, task breakdown, owner assignments, and risk register signed off.
- **[Repository Ready]** Git repo initialised with the directory structure, `README`, `CONTRIBUTING`, `ISSUE_TEMPLATE`, and placeholder CI/CD files.
- **[Scaffolding Created]** Maven/Quarkus skeleton, Next.js monorepo skeleton, Dockerfiles, Kafka schema placeholders, Flyway migrations.
- **[Test Strategy Defined]** Test‑plan, test‑case templates, and local‑dev environment manifest ready.
- **[Review Guidelines Issued]** Code‑review checklist, security checklist, and documentation of standards.
- **[CI/CD Skeleton Built]** Automated build pipeline (Maven + Next.js) and Kubernetes deployment manifests prepared.
- **[Monitoring Blueprint]** Basic monitoring and logging configuration (metrics, alerts, logs) documented.
- **[Sign‑off]** All sub‑agents have reviewed and signed off the Phase 1 deliverables; no outstanding tasks remain before moving to Phase 2.