# PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
## 1. Phase Operational Scope & Objectives
| # | Objective | Description | Success Indicator |
|---|-----------|-------------|-------------------|
| **1.1** | **Project Charter & Scope Definition** | Produce a concise project charter that captures the business problem, stakeholder expectations, and high‑level functional/non‑functional requirements derived from the raw requirements (membership‑hub web + mobile, Quarkus/Kafka/Postgres backend, Next.js mobile front‑end, multi‑language support, QR‑based attendance, notifications, external auth providers, SEO, GDPR/CCPA compliance, scalability, security). | Signed‑off charter document stored in `docs/PROJECT-CHARTER.md`. |
| **1.2** | **Detailed Requirements Elicitation** | Conduct interviews/workshops with the Manager, end‑users (center admins, learners), and technical leads to capture: <br>• Internal & external authentication flows (email/password, Firebase, Google, Facebook). <br>• Attendance QR generation & validation logic. <br>• Notification channels (Zalo SMS, mobile push, group chat). <br>• Multi‑language locale handling (detect default, browser, device). <br>• SEO metadata per language. <br>• Data retention & privacy controls (GDPR/CCPA). | Completed **Requirements Specification** (`docs/REQUIREMENTS.md`) with acceptance criteria for each user story. |
| **1.3** | **Architecture Blueprint & Technical Standards** | Define the end‑to‑end architecture, including: <br>• Backend service boundaries (Auth Service, Membership Service, Attendance Service, Notification Service). <br>• Kafka topics & schema registry. <br>• Postgres schema & entity relationships. <br>• Containerization strategy (Dockerfiles, multi‑stage builds). <br>• GCP/GKE deployment manifests (Deployment, Service, Ingress). <br>• Security controls (JWT + OAuth2 for external providers, encryption at rest/in‑transit, RBAC). <br>• Monitoring & logging stack (Prometheus, Grafana, ELK). | Architecture diagram (`docs/ARCHITECTURE.md`) and standards checklist (`docs/TECH-STANDARDS.md`) approved by Manager and Reviewer. |
| **1.4** | **Project Plan & Timeline** | Create a 5‑phase Gantt/roadmap (max 7 days per phase) with milestones, dependencies, and resource allocation (Coder, Tester, Reviewer, DevOps). Include risk register, mitigation actions, and communication cadence. | `docs/PROJECT-PLAN.md` with approved timeline and risk log. |
| **1.5** | **Quality & Compliance Baseline** | Establish testing strategy (unit, integration, UI, security), code‑review guidelines, and compliance checkpoints (GDPR data‑processing addendum, CCPA opt‑out flows). Define definition of “Done” for this phase (see Section 4). | `docs/QUALITY-BENCHMARK.md` and `docs/COMPLIANCE-CHECKLIST.md` signed off. |

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
```
project-root/
├─ docs/                     # All phase artefacts (charter, requirements, architecture, plan, quality, compliance)
│   ├─ PROJECT-CHARTER.md
│   ├─ REQUIREMENTS.md
│   ├─ ARCHITECTURE.md
│   ├─ TECH-STANDARDS.md
│   ├─ PROJECT-PLAN.md
│   ├─ QUALITY-BENCHMARK.md
│   └─ COMPLIANCE-CHECKLIST.md
├─ backend/                 # Quarkus micro‑services
│   ├─ src/main/java/com/membership/
│   │   ├─ auth/
│   │   ├─ membership/
│   │   ├─ attendance/
│   │   └─ notification/
│   ├─ src/main/resources/
│   │   ├─ application.yml
│   │   ├─ kafka/
│   │   └─ db/
│   ├─ src/test/java/com/membership/
│   ├─ Dockerfile
│   └─ docker-compose.yml   # Local dev stack (Kafka + Postgres)
├─ frontend/                # Next.js mobile front‑end (multi‑lang)
│   ├─ src/
│   │   ├─ i18n/           # locale files & detection logic
│   │   ├─ components/
│   │   ├─ pages/
│   │   └─ api/            # internal API routes (proxy to backend)
│   ├─ public/
│   ├─ next.config.js
│   └─ package.json
├─ mobile/                  # Native wrappers (optional) – placeholder for iOS/Android builds
│   └─ (to be defined in Phase 3)
├─ tests/                   # Test artefacts
│   ├─ unit/
│   ├─ integration/
│   └─ ui/
├─ infrastructure/          # GCP/GKE manifests
│   ├─ k8s/
│   │   ├─ namespace.yaml
│   │   ├─ deployments/
│   │   ├─ services/
│   │   └─ ingress/
│   ├─ terraform/           # IaC (optional)
│   └─ monitoring/
│       ├─ prometheus/
│       └─ grafana/
└─ ci-cd/                   # GitHub Actions / Cloud Build pipelines
    ├─ backend.yml
    ├─ frontend.yml
    └─ deploy.yml
```
**Allowed file extensions / patterns** (any other files must be explicitly requested in a later phase):
- `.java`, `.yml`, `.yaml`, `.json`, `.md`, `.properties`, `.sql`
- `Dockerfile`, `docker-compose.yml`
- Next.js specific: `.js`, `.jsx`, `.ts`, `.tsx`, `.css`, `.scss`
- Terraform (`.tf`), Helm charts (`Chart.yaml`, `values.yaml`)

**Endpoint conventions (to be defined in Phase 2)**:
- `/api/auth/*` → Auth Service
- `/api/members/*` → Membership Service
- `/api/attendance/*` → Attendance Service
- `/api/notifications/*` → Notification Service

All other endpoints will be defined during backend development.

## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)

| Sub‑Agent | Core Deliverables for Phase 1 | Detailed Tasks & Artifacts |
|-----------|------------------------------|----------------------------|
| **Manager** | • Signed‑off Project Charter <br>• Approved Project Plan | 1. Convene kickoff meeting with all stakeholders. <br>2. Capture high‑level business goals and constraints. <br>3. Validate scope against raw requirements. <br>4. Draft `PROJECT-CHARTER.md` and circulate for approval. <br>5. Produce `PROJECT-PLAN.md` with 5‑phase timeline, resource allocation, and risk register. |
| **Coder** (Backend focus) | • Initial service skeleton & schema definitions | 1. Create basic Quarkus project structure under `backend/src/main/java/com/membership/`. <br>2. Define JPA entities for `User`, `Center`, `Member`, `AttendanceRecord`. <br>3. Draft Kafka topic definitions (`attendance.created`, `notification.sent`) in `backend/src/main/resources/kafka/`. <br>4. Write placeholder REST resources (controllers) with OpenAPI annotations. <br>5. Add Dockerignore and a minimal `Dockerfile` (multi‑stage). |
| **Coder** (Frontend focus) | • Next.js project scaffold with i18n support | 1. Initialize Next.js app (`frontend/`). <br>2. Install `i18next` and `next-i18next` plugins. <br>3. Create `src/i18n/locales/` (en, vi, zh for example). <br>4. Add locale detection middleware (browser → default → fallback). <br>5. Scaffold basic pages: `Login`, `Dashboard`, `Attendance`, `Profile`. |
| **Tester** | • Test strategy & baseline test suite | 1. Review `QUALITY-BENCHMARK.md` and map to raw requirements. <br>2. Draft unit‑test templates for JPA entities and service beans (using JUnit5 + Mockito). <br>3. Draft integration‑test plan for Kafka message flow (using Testcontainers). <br>4. Draft UI‑test scenarios (Cypress) for login flows, QR scanning mock, notification display. <br>5. Store all test templates in `tests/` directory. |
| **Reviewer** | • Code & artefact review checklist | 1. Establish a checklist covering: security (JWT handling, input validation), coding standards (SonarQube rules), documentation (README, API contracts), and compliance (GDPR data‑mapping). <br>2. Perform peer review of `PROJECT-CHARTER.md`, `REQUIREMENTS.md`, `ARCHITECTURE.md`. <br>3. Approve `TECH-STANDARDS.md` and `COMPLIANCE-CHECKLIST.md`. |
| **DevOps** | • CI/CD pipeline skeleton & infrastructure manifests | 1. Create GitHub Actions workflows under `ci-cd/` for: <br>   - Backend lint, unit test, Docker build. <br>   - Frontend lint, test, static export. <br>   - Deploy to GKE (helm or raw manifests). <br>2. Draft K8s manifests (`namespace.yaml`, Deployment, Service, Ingress) under `infrastructure/k8s/`. <br>3. Define monitoring configs (Prometheus ServiceMonitors, Grafana dashboards) in `infrastructure/monitoring/`. |
| **All Agents (Collaborative)** | • Documentation & Artefact Storage | 1. Ensure every deliverable is placed under `docs/` with version control. <br>2. Use a shared markdown table for traceability (requirement ↔ artefact ↔ owner). <br>3. Update `PROJECT-PLAN.md` progress log after each sub‑agent completes its tasks. |

## 4. Phase Definition of Done (DoD)

1. **Deliverables Completed**
   - `docs/PROJECT-CHARTER.md` – approved by Manager & Reviewer.  
   - `docs/REQUIREMENTS.md` – all raw requirements captured with acceptance criteria.  
   - `docs/ARCHITECTURE.md` – service boundaries, data flows, Kafka topics, Postgres schema, security model, GCP/GKE deployment overview.  
   - `docs/TECH-STANDARDS.md` – coding, security, naming, and containerization standards.  
   - `docs/PROJECT-PLAN.md` – 5‑phase timeline, resource allocation, risk register, and milestone definitions.  
   - `docs/QUALITY-BENCHMARK.md` – testing strategy, coverage goals, and toolchains.  
   - `docs/COMPLIANCE-CHECKLIST.md` – GDPR/CCPA controls mapped to data entities.  

2. **Code & Configuration**
   - Minimal Quarkus project skeleton with JPA entities and placeholder REST resources.  
   - Next.js project scaffold with i18n plugin, locale detection middleware, and basic page shells.  
   - Dockerfile (multi‑stage) and docker‑compose for local Kafka + Postgres stack.  
   - K8s manifests for a single namespace, one backend Deployment/Service/Ingress.  
   - CI/CD workflow files (backend, frontend, deploy) that at least trigger on push.  

3. **Testing Baseline**
   - Unit‑test templates for core domain classes.  
   - Integration‑test plan for Kafka message flow (Testcontainers).  
   - UI‑test scenarios (Cypress) for login and navigation.  

4. **Review & Approval**
   - All artefacts reviewed and signed off by the designated Reviewer.  
   - Manager confirms scope alignment with raw requirements.  
   - DevOps validates CI/CD pipeline syntax and K8s manifest formatting.  

5. **Traceability & Documentation**
   - A single traceability matrix (`docs/TRACEABILITY.md`) linking each requirement to its artefact and owner.  
   - Updated `README.md` in the repository describing how to run local dev stack (`docker‑compose up`).  

**When every item above is present, verified, and approved, Phase 1 is complete and the team may proceed to Phase 2 (Backend Development) without further iteration.**