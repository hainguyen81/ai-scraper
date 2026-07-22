# GLOBAL PROJECT CONTEXT: membership-hub
## 1. Executive Summary & Tech Stack Blueprint
- **Project Vision** – A unified SaaS platform that empowers training centers to manage students, courses, attendance, promotions, and communications through a web admin console and a native mobile app.  
- **Core Domains** – Center management, user authentication (email/password + OAuth via Firebase/Google/Facebook), role‑based access control (System Admin, Admin, Manager, Teacher, Student), course scheduling, student enrollment, QR‑based attendance, digital student cards with expiry tracking, real‑time notifications (Zalo groups & mobile push), multi‑language SEO‑ready UI, and an AI‑powered chat assistant.  
- **Tech Stack Blueprint**  
  - **Backend** – Java 17, Quarkus (reactive, container‑first), Kafka for event streaming, PostgreSQL with native indexing, Docker multi‑stage images, deployment on GCP GKE, package foundation `org.nlh4j.saas.membership-hub`.  
  - **Frontend / Mobile** – Next.js (React‑based) serving both web admin UI and mobile app (iOS/Android) with shared component library, Tailwind CSS, i18n (detect stored locale → browser fallback), SEO‑optimized pages per language.  
  - **Auth & Identity** – Internal email/password, Firebase Auth, Google/Facebook OAuth, JWT‑based session handling, integrated with Kafka for identity events.  
  - **Communication** – Zalo group messaging API, mobile push notifications (Firebase Cloud Messaging), event‑driven notification service via Kafka.  
  - **AI CSKH** – Float‑button AI chat widget with intent‑recognition for course, teacher, and center queries.  
  - **DevOps** – CI/CD pipelines (GitHub Actions), Docker registries, GKE deployment configs, environment‑driven interval updates (e.g., dashboard refresh every 15 min).  

## 2. Global Guardrails & Enterprise Compliance Standards
- **Package & Path Discipline**  
  - All Java source must reside under `org.nlh4j.saas.membership-hub` → physical path `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/...`.  
  - All test source must mirror the same token hierarchy under `./sources/backend/src/test/java`.  
- **Workspace Boundary Rule**  
  - Backend logic, configs, properties → `./sources/backend/`.  
  - UI, assets, packages → `./sources/frontend/`.  
  - No relative paths assuming a sub‑module root; every emitted path must be prefixed accordingly.  
- **Tester Target Syntax**  
  - Unit tests: `<source_path>;<test_path>` (e.g., `./sources/backend/src/main/java/.../Service.java;./sources/backend/src/test/java/.../ServiceTest.java`).  
  - Integration/E2E: `INTEGRATION_SCOPE;<test_path>`.  
- **Performance & Data Handling**  
  - **No large in‑memory loops** – all bulk processing must be expressed as native SQL JOINs or Kafka stream operations.  
  - **Streaming parsing** – SAX/EasyExcel for file imports; avoid DOM‑heavy libraries.  
  - **Real‑time constraints** – dashboard refresh interval configurable via environment (default 15 min).  
- **Phase Discipline**  
  - **Exact 5 phases** – no more, no less.  
  - **Duration per phase** – 1 – 7 days (hard limit).  
  - **Chronological packing** – every requirement item must be fully covered within the five phases; no post‑phase leftovers.  
- **Security & Role Enforcement**  
  - Role hierarchy enforced at API gateway level; each endpoint declares required roles.  
  - OAuth providers integrated via secure token exchange; passwords never stored in plain text.  
- **Observability & Deployment**  
  - Structured logging, metrics via Micrometer, distributed tracing across Kafka and Quarkus.  
  - Docker images built with minimal layers; GKE deployments use declarative Helm charts.  

## 3. Standardized Sub-Agent Persona Definitions
| Persona | Core Mandate | Key Deliverables |
|---------|--------------|------------------|
| **Manager** | Cross‑phase orchestration, timeline validation, phase‑count enforcement, dependency mapping, risk mitigation. | Phase schedules, dependency graphs, compliance checkpoints, final project synopsis. |
| **Coder** | Implement all backend services (`./sources/backend/src/main/java`) and frontend/mobile components (`./sources/frontend/src`). Writes production‑ready code, adheres to package & path rules, integrates Kafka, auth, and DB layers. | Functional modules, API contracts, UI components, shared libraries. |
| **Tester** | Verify correctness via unit & integration tests. Emits dual‑path syntax `<source>;<test>` for units; uses `INTEGRATION_SCOPE` for system suites. | Test suites, coverage reports, validation of business rules (attendance, enrollment, notifications). |
| **Reviewer** | Static analysis, compliance audit against guardrails (no large loops, native DB calculations, path correctness). Rejects non‑compliant code. | Review comments, compliance sign‑off, remediation requests. |
| **DevOps** | Build CI/CD pipelines, multi‑stage Dockerfiles, `pom.xml`/`package.json` management, GKE deployment configs, environment variables, monitoring setup. | Docker images, GitHub Actions workflows, Helm charts, infra‑as‑code snippets. |

## 4. Multi-Phase Segmentation Strategy Overview (Plan exactly 5 phases)
| Phase | Duration (Days) | Backend Core Components (touched) | Frontend / Mobile Core Components (touched) | Phase Objective Summary |
|-------|-----------------|-----------------------------------|---------------------------------------------|--------------------------|
| **Phase 1** | 1‑3 | • Project scaffolding (`org.nlh4j.saas.membershiphub`) <br>• Quarkus runtime, Kafka broker connection, PostgreSQL datasource <br>• Core domain entities: Center, User, Role, Course, Enrollment, Attendance, StudentCard <br>• Basic CRUD repositories & JPA entities | • Next.js project init, i18n middleware (locale detection), shared UI library (Tailwind) <br>• Login/Auth page (email/password + OAuth buttons) <br>• Role‑based routing guard | Establish the foundational architecture, data model, and authentication scaffold. |
| **Phase 2** | 2‑4 | • User service with JWT issuance, role mapping, password hashing <br>• OAuth integration adapters (Firebase, Google, Facebook) <br>• Kafka producers/consumers for user & enrollment events <br>• Notification service (Zalo API, FCM) <br>• Authorization filter & security config | • Admin web layout (sidebar, header, role‑specific menus) <br>• Mobile app shell (React‑Native/Next.js hybrid) <br>• Multi‑language support (locale storage, fallback) <br>• Responsive dashboard skeleton | Implement identity & access, event streaming, and notification backbone; deliver UI shell for both web and mobile. |
| **Phase 3** | 3‑5 | • Course, Teacher, Student management services <br>• Enrollment & registration logic (auto‑create Student/Teacher accounts) <br>• QR attendance capture (Kafka event, atomic daily flag) <br>• StudentCard expiry calculation (native DB function) <br>• Promotion & Announcement services | • Center Management screens (list/add/edit centers) <br>• Course Management UI (list, schedule, assign teachers) <br>• Student enrollment forms & search <br>• Mobile app screens mirroring web (profile, card view, enrollment) | Build core business logic, enrollment workflow, attendance tracking, and corresponding UI forms. |
| **Phase 4** | 4‑6 | • Role‑based access control enforcement (System Admin, Admin, Manager, Teacher, Student) <br>• Advanced reporting & dashboard APIs (real‑time stats, interval refresh) <br>• AI CSKH integration (REST endpoint for chat queries) <br>• CI/CD pipeline stubs, Docker multi‑stage builds | • Full admin dashboards (overview, course schedule, teacher assignments) <br>• Mobile push notification handling, offline‑first service workers <br>• SEO‑optimized multilingual pages (course listings, center info) <br>• AI chat widget embed | Harden security, deliver analytics & AI chat, and complete responsive UI with SEO readiness. |
| **Phase 5** | 5‑7 | • End‑to‑end integration testing (unit + integration suites) <br>• Performance tuning (native SQL, Kafka backpressure) <br>• Production‑grade Docker images & GKE deployment scripts <br>• Monitoring & logging configuration | • Polished mobile app (iOS/Android builds), final UI refinements <br>• End‑user documentation & rollout checklist <br>• Final QA sign‑off and hypercare preparation | Close the loop with comprehensive testing, deployment readiness, and final delivery. |

**Phase Discipline Recap**  
- Each phase is bounded 1‑7 days; no phase exceeds Day 7.  
- All requirement items (QR attendance, student cards, notifications, multi‑language SEO, role screens, AI chat, etc.) are fully addressed within these five phases.  
- No scheduling logs or extra phases are generated; work stops as soon as a phase’s core objectives are satisfied.