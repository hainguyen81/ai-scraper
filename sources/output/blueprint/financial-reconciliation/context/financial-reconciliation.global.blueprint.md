# GLOBAL PROJECT CONTEXT: financial-reconciliation
## 1. Executive Summary & Tech Stack Blueprint
**Business Goal** – Deliver a lean, high‑throughput Micro‑SaaS Financial Reconciliation Engine that automatically ingests marketplace (Shopee/TikTok/Lazada) and 3PL (GHN, GHTK, Viettel Post) Excel reports, runs native SQL variance calculations, and surfaces three C‑level KPI dashboards (Leaked Capital, Escrow/Holding Capital, Settled/Safe Capital).  

**Core Architecture** – Single‑jar monolithic Spring Boot 3.x (Java 17/21) leveraging:
- **File Ingestion** – Alibaba EasyExcel (SAX‑based streaming) + Spring Batch + `@Async` background workers.  
- **Data Layer** – PostgreSQL/MySQL with normalized staging tables (`temp_shopee_orders`, `temp_logistics_orders`) and a `reconciliation_sessions` master record.  
- **Computation** – All bulk analytics executed as native, indexed SQL (parameterized JPA `@Query`).  
- **Presentation** – Thymeleaf + Tailwind CSS responsive admin UI with drag‑&‑drop upload, session‑driven views, CSV/Excel export for leakage inventory.  
- **Deployment** – Dockerized JVM images, Git‑ops CI/CD (GitHub Actions → ArgoCD), Prometheus + Grafana monitoring, centralized logging (ELK).  

**Tech Stack Summary**  
| Layer | Technology | Rationale |
|-------|------------|-----------|
| Runtime | Spring Boot 3.x, Java 17/21 LTS | Lightweight, mature ecosystem, fast startup |
| Ingestion | EasyExcel (SAX), Spring Batch, `@Async` | Zero‑heap‑blow‑up streaming, non‑blocking background processing |
| DB | PostgreSQL (or MySQL) | ACID, advanced JSON/JSONB, native set operations |
| Computation | Native SQL (JOIN, aggregation) | Guarantees “zero application‑level loops” guardrail |
| UI | Thymeleaf, Tailwind CSS, Axios/Fetch | Server‑side rendering, responsive, minimal JS bundle |
| DevOps | Docker, Kubernetes, GitHub Actions, ArgoCD, Prometheus, Grafana, ELK | Immutable infrastructure, observable, scalable |
| Security | Spring Security (JWT), RBAC, HTTPS, input validation | Enterprise‑grade access control & data protection |

---

## 2. Global Guardrails & Enterprise Compliance Standards
| Guardrail | Description | Enforcement Mechanism |
|-----------|-------------|-----------------------|
| **Zero Application‑Level Loops** | No Java `for/while` over bulk data sets; all heavy analytics must be delegated to indexed native SQL. | Code review checklist; static analysis rule (e.g., SonarQube) flags loops over `TempShopeeOrder`/`TempLogisticsOrder`. |
| **Non‑Blocking, Sub‑200 ms Upload Response** | Upload endpoint must return immediately with a `SessionId`; heavy parsing runs in isolated Spring Batch jobs. | `@Async` + `CompletableFuture`; monitoring alerts if upload response >200 ms. |
| **Memory‑Efficient Streaming** | Prohibit Apache POI / DOM parsers; mandatory use of EasyExcel SAX streaming. | Dependency check (Maven/Gradle) rejects `poi` >2.0; enforce `easyexcel` version. |
| **Session‑Isolated Staging** | Each reconciliation run writes to session‑partitioned tables; no cross‑session data leakage. | Foreign‑key constraints on `session_id`; DB schema enforces isolation. |
| **Native SQL Computation** | All variance, leakage, escrow, safe‑income calculations must be expressed as native SQL (parameterized). | JPA `@Query` annotations; unit tests verify SQL execution plans. |
| **Enterprise UI Security** | Role‑based access (Admin, Analyst), CSRF protection, input sanitization, audit logs. | Spring Security configuration; OWASP ZAP scans. |
| **Observability & SLA** | 99.9 % uptime target, latency <500 ms for dashboard queries, error‑rate <0.1 %. | Prometheus metrics, Grafana alerts, SLO dashboards. |
| **CI/CD Pipeline Guardrails** | Automated lint, unit, integration, security scans; only passing builds deploy to staging/production. | GitHub Actions workflow with fail‑fast steps. |
| **Data Export Integrity** | CSV/Excel exports must be deterministic, include session metadata, and be audit‑ready. | Export service validates row count against DB totals before streaming. |

---

## 3. Standardized Sub‑Agent Persona Definitions
| Persona | Core Responsibilities | Decision Authority |
|---------|----------------------|--------------------|
| **Manager** | • Overall project roadmap & phase sequencing.<br>• Resource allocation, risk & stakeholder communication.<br>• Approval of architectural decisions & scope changes. | Final sign‑off on phase deliverables and go/no‑go to next phase. |
| **Coder** | • Implement all Java services, Spring Batch jobs, native SQL queries, UI components.<br>• Write unit & integration tests, adhere to guardrails (no loops, streaming).<br>• Perform code reviews within the team. | Code commits; resolves technical blockers; proposes refactor if guardrails violated. |
| **Tester** | • Design test suites for ingestion pipeline, reconciliation logic, dashboard UI.<br>• Execute performance & load tests (large Excel files).<br>• Validate guardrail compliance (memory, latency). | Test execution results; raises defects; signs off test readiness for each phase. |
| **Reviewer** | • Conduct architectural & security reviews.<br>• Verify compliance with enterprise guardrails, coding standards, and data‑privacy policies.<br>• Approve releases to production. | Approval to promote artifacts; can request rework. |
| **DevOps** | • Containerize application, configure CI/CD pipelines, set up monitoring & logging.<br>• Manage environment provisioning, scaling, and incident response.<br>• Ensure observability meets SLA. | Infrastructure changes, deployment approvals, environment access. |

---

## 4. Multi-Phase Segmentation Strategy Overview (Plan exactly 5 phases)

| Phase | Duration | Primary Objectives (must cover all requirement items) |
|-------|----------|--------------------------------------------------------|
| **Phase 1 – Foundations & Guardrail Setup** | **1‑2 days** | • Define monolithic project skeleton, Spring Boot configuration, and Java version.<br>• Configure PostgreSQL/MySQL schema (`ReconciliationSession`, `TempShopeeOrder`, `TempLogisticsOrder`).<br>• Implement core entities, enums (`SessionStatus`), and JPA repositories.<br>• Set up Docker base image, CI pipeline skeleton, and monitoring stubs.<br>• Establish static‑analysis rules enforcing “zero loops”, “EasyExcel only”, and “sub‑200 ms upload”. |
| **Phase 2 – Async Ingestion Pipeline & Session Management** | **3‑4 days** | • Build REST endpoint (`/upload`) that returns immediate `SessionId` and marks session `PENDING`.<br>• Create Spring Batch job (`EasyExcel` reader → `TempShopeeOrder`/`TempLogisticsOrder` writers) triggered asynchronously.<br>• Implement `@Async` background worker that updates session status (`PROCESSING` → `COMPLETED/FAILED`).<br>• Add UI drag‑&‑drop page (Thymeleaf) for concurrent file selection and real‑time session status polling.<br>• Validate file size limits, MIME types, and enforce memory‑streaming guardrails. |
| **Phase 3 – Native Reconciliation Logic & Metric Computation** | **2‑3 days** | • Write the native SQL variance query (as per requirements) and expose a service method that runs it per `sessionId`.<br>• Implement additional native queries for leakage inventory, escrow holding, and safe income aggregates (populate `ReconciliationSession` fields).<br>• Ensure all calculations are performed **only** via native SQL (guardrail compliance).<br>• Add error‑handling for missing matches, data‑type mismatches, and log anomalies. |
| **Phase 4 – Executive Dashboard & Export Features** | **2‑3 days** | • Develop Thymeleaf dashboard view that reads `ReconciliationSession` metrics and renders the three KPI cards (X, Y, Z).<br>• Build data‑grid tables for leakage inventory (order ID, variance) with inline CSV/Excel export.<br>• Add session‑filtering, refresh intervals, and responsive Tailwind styling.<br>• Integrate session status display (PENDING → PROCESSING → COMPLETED) with real‑time WebSocket or polling. |
| **Phase 5 – Testing, Security Hardening & Production Deployment** | **2‑4 days** | • Unit & integration test suites covering entities, ingestion, SQL calculations, UI pages.<br>• Performance & load tests simulating multi‑megabyte Excel files (verify memory usage & sub‑200 ms upload response).<br>• Security review: OWASP checks, JWT auth, RBAC, CSRF protection, input validation.<br>• Finalize CI/CD pipeline (build, scan, container push, ArgoCD promotion).<br>• Deploy to staging, run end‑to‑end smoke tests, then promote to production.<br>• Set up Prometheus/Grafana dashboards and ELK logging; document run‑books. |

**Phase‑wise Coverage Check** – Every requirement from the PRD (async ingestion, session lifecycle, EasyExcel streaming, native SQL variance, leakage/escrow/safe metrics, UI dashboard, export, guardrails, memory constraints, non‑blocking upload, monolithic architecture, tech stack) is addressed in at least one of the five phases, ensuring no loose ends remain before moving to the next.  

**Progression Rule** – A phase is considered complete only after the designated sub‑agent(s) (Coder, Tester, DevOps) sign off the deliverables, and the Manager approves the transition. No extra phases or day‑extensions are permitted.