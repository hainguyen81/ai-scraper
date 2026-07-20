# GLOBAL PROJECT CONTEXT: test-ai-architecture  

## 1. Executive Summary & Tech Stack Blueprint  
**Executive Summary**  
The *membership‑hub* platform is a dual‑mode solution (web + mobile) that enables education centers to manage learners, track attendance via QR codes, monitor membership validity, and communicate through Zalo & push notifications. The system must serve multiple centers concurrently, support multilingual UI/UX, provide SEO‑friendly content, and be fully cloud‑native, scalable, and container‑ready for deployment on Google Cloud Platform (GCP) using Google Kubernetes Engine (GKE).  

**Core Business Capabilities**  
| Capability | Description | Primary Actors |
|------------|-------------|----------------|
| Multi‑center learner registry | Centralized DB storing learners, centers, enrollment, membership periods | Admin, Center staff |
| QR‑based daily attendance | Scan QR → record attendance (idempotent per day) | Learner, Staff |
| Membership day‑counter | Auto‑decrement remaining valid days after each attendance | Learner, Staff |
| Omni‑channel notification | Zalo SMS, Zalo group message, mobile push (FCM/APNs) | System, Learner |
| Multi‑method authentication | Email + password, Firebase, Google, Facebook | Learner, Staff |
| Internationalization & SEO | Multi‑locale UI, locale detection, SEO‑friendly URLs & meta tags | All users |
| Analytics & reporting | Attendance logs, membership health, center‑level KPIs | Admin, Center staff |

**Technology Blueprint**  

| Layer | Technology | Rationale |
|-------|------------|-----------|
| **API / Business Logic** | **Quarkus** (Java, reactive, GraalVM native image optional) | Low‑memory, high‑throughput, native compilation for fast start‑up; excellent Kubernetes integration |
| **Event Streaming** | **Apache Kafka** (Confluent Cloud or self‑managed) | Decouple attendance, notification, and analytics pipelines; guarantee at‑least‑once delivery |
| **Data Store** | **PostgreSQL** (CloudSQL on GCP) + **TimescaleDB extension** (optional for time‑series attendance) | Strong ACID guarantees, relational modeling for learners/centers, time‑series queries for reporting |
| **Message Queue for Outbound** | **Google Pub/Sub** (or Kafka topics) → **Firebase Cloud Messaging** / **Zalo API** | Scalable fan‑out for push & SMS |
| **Containerization** | **Docker** (multi‑stage builds, GraalVM native image optional) | Consistent runtime across dev, CI, prod |
| **Orchestration** | **Google Kubernetes Engine (GKE)** with **Anthos**‑style policies | Auto‑scaling, zero‑downtime deployments, namespace per center (optional) |
| **CI/CD** | **GitHub Actions** / **Cloud Build** → **Argo CD** for GitOps | Automated build, test, container image push, progressive rollout |
| **Web Front‑end** | **Next.js** (React SSR) | SEO‑ready, i18n support, static generation for public pages, API routes for auth |
| **Mobile Front‑end** | **React Native** (Expo) built from same Next.js component library via **React Native for Web** | Single codebase for iOS & Android, shared i18n |
| **Authentication** | **Firebase Auth** (email/password, Google, Facebook) + **Custom JWT** for internal users | Unified auth flow, token refresh, role‑based claims |
| **Observability** | **OpenTelemetry**, **Prometheus**, **Grafana**, **Stackdriver Logging** | End‑to‑end tracing, metrics, alerts |
| **Security** | **Istio** service mesh (mTLS), **OPA** policy enforcement, **Secret Manager** for credentials | Zero‑trust, fine‑grained access control |
| **Internationalization** | **next-i18next**, **react‑i18next**, locale detection middleware | Auto‑detect from user profile → cookie → browser/device locale |
| **SEO** | **Next.js** `getStaticProps`/`getServerSideProps`, dynamic sitemap per locale, structured data (JSON‑LD) | Search engine visibility in all supported languages |

---

## 2. Global Guardrails & Enterprise Compliance Standards  

| Domain | Guardrail | Implementation Detail | Compliance Reference |
|--------|-----------|-----------------------|----------------------|
| **Data Privacy** | Personal data (email, phone, Zalo ID) must be encrypted at rest & in transit. | PostgreSQL Transparent Data Encryption (TDE); TLS 1.3 for all HTTP/gRPC; Vault/Secret Manager for keys. | GDPR, CCPA, Vietnam PDPA |
| **Identity & Access Management** | Principle of least privilege for services & human operators. | IAM roles per GCP service account; OPA policies for API gateway; RBAC in Kubernetes. | NIST 800‑53 AC‑6 |
| **Audit Logging** | Immutable audit trail for authentication, attendance, and notification events. | Cloud Audit Logs + custom audit table in PostgreSQL; log shipping to Cloud Logging with retention ≥ 1 year. | ISO 27001 A.12.4 |
| **Secure Coding** | No hard‑coded secrets; static code analysis mandatory. | Git pre‑commit hooks, SonarQube, Dependabot alerts. | OWASP ASVS L1‑L2 |
| **API Security** | Rate limiting, input validation, JWT signature verification. | Kong/Envoy API gateway with OIDC plugin; schema validation via OpenAPI 3.0. | OWASP API Security Top 10 |
| **Container Hardening** | Minimal base images, non‑root user, vulnerability scanning. | Distroless or Alpine base; Dockerfile `USER app`; Trivy scan in CI. | CIS Docker Benchmark |
| **Kubernetes Hardening** | Pod security standards, network policies, node auto‑upgrade. | PSP replaced by OPA Gatekeeper; Calico network policies; GKE autopilot. | NIST 800‑190 |
| **Business Continuity** | Automated backups, multi‑zone replication, disaster‑recovery drills. | CloudSQL automated backups + cross‑region read replica; Kafka MirrorMaker2; weekly failover test. | ISO 22301 |
| **Localization** | All UI strings externalized; locale fallback hierarchy. | `public/locales/{lang}` JSON files; default locale = user preference → browser → `en-US`. | WCAG 2.1 AA (language of page) |
| **Accessibility** | WCAG 2.1 AA compliance for web & mobile. | Semantic HTML, ARIA labels, color contrast checks in CI. | WCAG 2.1 |
| **Performance SLA** | 99.9% availability, ≤200 ms API latency (95th percentile). | Horizontal pod autoscaling, GKE regional clusters, CDN (Cloud CDN) for static assets. | SLA internal policy |

---

## 3. Standardized Sub‑Agent Persona Definitions  

| Persona | Core Responsibilities | Primary Tools / Artifacts | Interaction Model |
|---------|-----------------------|---------------------------|-------------------|
| **Manager** | Owns product vision, backlog prioritization, stakeholder alignment. | Confluence, Jira, Roadmap, OKRs | Reviews deliverables from Coder, Tester, Reviewer; approves releases. |
| **Coder** | Implements features, writes micro‑services, UI components, IaC. | VS Code, Quarkus, Java, TypeScript, Docker, Git | Pull‑request author; collaborates with Reviewer; runs unit tests locally. |
| **Tester** | Designs & executes automated & manual test suites, performance testing. | JUnit, Cypress, Postman, k6, TestRail | Consumes build artifacts; raises defects; validates against Acceptance Criteria. |
| **Reviewer** | Conducts code reviews, enforces style, security, and architectural guidelines. | GitHub PR reviews, SonarQube, OPA policies | Approves/rejects PRs; provides feedback to Coder; ensures Guardrails compliance. |
| **Docker** | Builds, tags, scans, and pushes container images; maintains base image catalog. | Dockerfile, BuildKit, Trivy, GitHub Packages/Artifact Registry | Triggered by CI; outputs immutable image digest for Deployer. |
| **Deployer** | Manages CI/CD pipelines, Helm releases, rollbacks, environment promotion. | GitHub Actions, Cloud Build, Argo CD, Helm, Kustomize | Deploys Docker images to GKE; monitors health; enforces canary/blue‑green strategies. |

*All agents operate under the global guardrails defined in Section 2 and report status to the Manager via daily stand‑ups and automated dashboards.*

---

## 4. Multi‑Phase Segmentation Strategy Overview (5 Phases)  

| Phase | Goal | Key Deliverables | Success Criteria |
|-------|------|------------------|------------------|
| **1️⃣ Discovery & Architecture Validation** | Validate assumptions, define domain model, prototype critical flows. | • Context diagram, bounded‑context map<br>• PoC: QR attendance → Kafka → PostgreSQL<br>• i18n detection middleware demo<br>• Security threat model | PoC passes functional test (attendance recorded once per day) and security review (no plaintext secrets). |
| **2️⃣ Core Platform Build (MVP)** | Implement core backend services, authentication, and basic web UI. | • Quarkus micro‑services (Auth, Learner, Attendance, Notification)<br>• Kafka topics & consumers<br>• PostgreSQL schema + migrations (Flyway)<br>• Next.js web portal (login, dashboard, QR scanner)<br>• CI pipeline (build → Docker → unit tests) | End‑to‑end flow: user logs in → scans QR → attendance stored → notification queued. Load test ≥ 500 RPS with <200 ms latency. |
| **3️⃣ Mobile Extension & Multi‑Center Scaling** | Add React Native app, multi‑tenant isolation, and scaling mechanisms. | • Expo React Native app (iOS/Android) sharing i18n assets<br>• Multi‑tenant DB schema (center_id foreign key) + optional namespace per center in GKE<br>• Horizontal pod autoscaling rules, Kafka partition strategy<br>• Zalo API integration & push notification service | Mobile app passes device‑farm tests; system sustains 5 k concurrent users across 3 centers without degradation. |
| **4️⃣ SEO, Internationalization & Compliance Hardening** | Make the platform globally discoverable and audit‑ready. | • Server‑side rendering with locale‑specific routes, sitemap per language<br>• Structured data (JSON‑LD) for centers & courses<br>• OPA policies, Istio mTLS, secret rotation automation<br>• GDPR/PDPA data‑subject request endpoints | SEO score ≥ 80 (Google Lighthouse) for all locales; security scan (Snyk) reports zero critical findings. |
| **5️⃣ Productionization & Continuous Improvement** | Deploy to GKE regional cluster, establish monitoring, and set up governance. | • Helm charts + Argo CD GitOps repo<br>• Prometheus/Grafana dashboards, alerting policies<br>• Disaster‑recovery runbooks, backup verification<br>• Automated canary releases, feature flag framework | 99.9% uptime SLA met for 30 days; incident response time < 15 min; feature flag rollout success rate ≥ 95%. |

*Each phase ends with a **Go/No‑Go** gate reviewed by the Manager, Reviewer, and Tester, ensuring alignment with the Global Guardrails before proceeding.*