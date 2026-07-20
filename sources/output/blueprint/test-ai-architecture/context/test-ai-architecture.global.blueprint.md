# GLOBAL PROJECT CONTEXT: test‑ai‑architecture  

## 1. Executive Summary & Tech Stack Blueprint  

**Executive Summary**  
The *membership‑hub* platform is a bilingual, multi‑tenant SaaS solution that serves two distinct user‑faces:  

1. **Web portal** – used by administrators, teachers, and center staff to manage learners, attendance, subscriptions, and communications.  
2. **Mobile app** – consumed by learners to check‑in via QR, view remaining membership days, receive notifications, and interact with Zalo groups.  

Key business capabilities:  
- Centralized identity federation (email + password, Firebase, Google, Facebook).  
- Scalable, event‑driven backend (Quarkus + Kafka) with PostgreSQL persistence.  
- Multi‑center tenancy – a single deployment can host unlimited learning centers, each isolated by a tenant identifier.  
- Real‑time attendance logging via QR code scans; idempotent daily check‑in.  
- Automatic decrement of “membership days” and proactive messaging (Zalo SMS, push notifications).  
- Internationalization (i18n) for both web and mobile, SEO‑friendly multilingual URLs, locale detection fallback hierarchy (user preference → browser/device locale).  
- Cloud‑native delivery: Docker images, CI/CD pipelines, deployment to Google Cloud Platform (GCP) – specifically Google Kubernetes Engine (GKE).  

**Tech Stack Blueprint**  

| Layer | Technology | Rationale |
|-------|------------|-----------|
| **API / Business Logic** | **Quarkus** (Java 17) | Reactive, GraalVM native image support, low memory footprint – ideal for high‑throughput Kafka consumers & REST endpoints. |
| **Event Streaming** | **Apache Kafka** (Confluent Cloud or self‑managed on GKE) | Decouples attendance, notification, and analytics pipelines; guarantees ordering & replayability. |
| **Data Store** | **PostgreSQL** (CloudSQL) + **TimescaleDB extension** (optional for time‑series attendance) | Strong ACID guarantees, native JSONB for flexible tenant metadata, time‑series queries for attendance trends. |
| **Authentication / Identity** | **Keycloak** (OIDC) + **Firebase Auth** integration | Centralized user‑store for internal accounts; federation to Google/Facebook via OIDC; supports password‑less flows. |
| **Mobile Front‑end** | **Next.js** (React) with **Expo** for native builds (iOS/Android) | Server‑Side Rendering (SSR) for SEO, built‑in i18n routing, easy OTA updates via Expo. |
| **Web Front‑end** | **Next.js** (React) – same codebase as mobile (React Native Web) | Code reuse, SEO‑ready, locale‑aware routing. |
| **Containerization** | **Docker** (multi‑stage builds → GraalVM native image) | Small runtime images, fast start‑up for autoscaling pods. |
| **Orchestration** | **Google Kubernetes Engine (GKE)** | Managed K8s, auto‑scaling, regional clusters for high availability. |
| **CI/CD** | **GitHub Actions** → **Google Cloud Build** → **Argo CD** (GitOps) | Automated lint, unit/integration tests, image build, Helm chart promotion, progressive delivery. |
| **Observability** | **OpenTelemetry** → **Google Cloud Operations (formerly Stackdriver)** (Tracing, Metrics, Logging) | End‑to‑end visibility across services, Kafka lag monitoring, SLA dashboards. |
| **Messaging / Notification** | **Zalo Business API**, **Firebase Cloud Messaging (FCM)** | Direct SMS to Zalo numbers, push notifications to mobile app. |
| **Internationalization (i18n)** | **next‑i18next**, **react‑intl**, **Locale detection middleware** | Server‑side locale resolution, SEO‑friendly language sub‑paths (`/en/`, `/vi/`). |
| **Infrastructure as Code** | **Terraform** (GCP provider) + **Helm** charts | Reproducible environments, multi‑tenant namespace isolation. |
| **Security** | **Istio** (service mesh) + **Google Cloud Armor** | Mutual TLS, traffic policies, DDoS protection. |
| **Testing** | **JUnit 5**, **RestAssured**, **Cypress**, **Detox** (mobile) | Unit, contract, end‑to‑end UI tests. |

---

## 2. Global Guardrails & Enterprise Compliance Standards  

| Domain | Guardrail | Implementation Detail | Compliance Reference |
|--------|-----------|-----------------------|----------------------|
| **Data Privacy** | **GDPR / CCPA** – personal data must be pseudonymized & stored with consent logs. | Store only hashed email/phone, keep consent flag in `users.consent_at`. Enable data‑subject‑access‑request (DSAR) API. | GDPR Art. 5‑7, CCPA §1798.100 |
| **Tenant Isolation** | **Logical isolation** – each center’s data scoped by `tenant_id`. | Row‑level security (RLS) policies in PostgreSQL; K8s namespace per tenant for optional dedicated resources. | ISO 27001 A.9.2 |
| **Authentication** | **Zero‑trust** – MFA for admin accounts, short‑lived access tokens. | Keycloak MFA (TOTP), OAuth2 access token ≤15 min, refresh token rotation. | NIST SP 800‑63B |
| **API Security** | **OWASP Top 10** mitigation. | Input validation via Bean Validation, rate limiting via Istio, CSP headers, secure cookies, CSRF tokens for web. | OWASP ASVS L2 |
| **Secrets Management** | **No secrets in code**. | Google Secret Manager + K8s secrets injected at pod start; CI pipelines fetch via IAM. | SOC 2 CC6.1 |
| **Logging & Auditing** | **Immutable audit trail** for attendance & membership changes. | Write‑once audit table, Cloud Logging with retention ≥ 1 year, log integrity via Cloud KMS signatures. | PCI‑DSS 10.2 |
| **CI/CD Governance** | **Gate‑controlled promotions** – only after automated tests & security scans. | GitHub Actions runs: lint → unit → integration → SAST (SonarQube) → container scan (Trivy) → manual approval before prod. | NIST SP 800‑64 |
| **Disaster Recovery** | **RPO ≤ 5 min, RTO ≤ 30 min**. | Automated cross‑region CloudSQL replicas, GKE multi‑zone node pools, Helm rollback scripts. | BCDR best practice |
| **Accessibility** | **WCAG 2.1 AA** for web & mobile UI. | Automated axe-core scans, manual review checklist. | WCAG 2.1 |
| **Internationalization** | **Locale fallback hierarchy** must be deterministic. | Middleware: `userPref → cookie → Accept‑Language → default (en)`. SEO hreflang tags on every page. | W3C i18n Best Practices |
| **Resource Quotas** | **Prevent noisy neighbor** across tenants. | K8s ResourceQuota per namespace, Kafka consumer group throttling. | Cloud‑native best practice |

All agents must enforce these guardrails automatically; any deviation must raise a blocking CI/CD failure or runtime alert.

---

## 3. Standardized Sub‑Agent Persona Definitions  

| Persona | Core Responsibilities | Primary Tools / Artifacts | Success Metrics |
|---------|-----------------------|---------------------------|-----------------|
| **Manager** | Owns product vision, backlog grooming, sprint planning, stakeholder communication. | Jira (Epics/Stories), Confluence, Roadmap board. | On‑time delivery of Phase milestones, stakeholder NPS ≥ 8. |
| **Coder** | Implements features, writes unit & integration tests, adheres to coding standards. | IntelliJ, Quarkus, Next.js, Git, Prettier/ESLint, JUnit, Cypress. | Code coverage ≥ 80 %, PR merge time ≤ 24 h, static analysis score ≥ A. |
| **Tester** | Designs & executes functional, performance, security, and accessibility test suites. | Postman, Karate, JMeter, OWASP ZAP, axe‑core, Detox. | Defect leakage ≤ 5 %, test automation pass rate ≥ 95 %. |
| **Reviewer** | Conducts peer reviews, enforces architectural consistency, validates guardrail compliance. | GitHub PR reviews, SonarQube, Checkov (IaC), Trivy (container). | Review turnaround ≤ 12 h, no critical findings post‑merge. |
| **Docker** | Crafts multi‑stage Dockerfiles, optimizes image size, ensures reproducible builds. | Docker CLI, BuildKit, GraalVM native-image, Dockerfile linter (hadolint). | Image size ≤ 150 MB (native), build success rate 100 % in CI. |
| **Deployer** | Manages Helm charts, Terraform modules, CI/CD pipelines, monitors rollouts. | Helm, Terraform, Argo CD, Cloud Build, GKE, Prometheus/Grafana. | Zero‑downtime deployments, rollback < 5 min, deployment success rate ≥ 99 %. |

All personas share a **common “Guardrail‑Aware” mindset**: every artifact (code, config, pipeline) must be validated against the Global Guardrails (Section 2) before promotion.

---

## 4. Multi‑Phase Segmentation Strategy Overview (5 Phases)  

| Phase | Objective | Key Deliverables | Primary Agents Involved | Timeline (Weeks) |
|-------|-----------|------------------|--------------------------|------------------|
| **1️⃣ Discovery & Architecture Foundations** | Validate requirements, define multi‑tenant model, set up baseline infra. | • Requirement traceability matrix<br>• High‑level architecture diagram<br>• Terraform base module (VPC, GKE cluster, CloudSQL)<br>• CI/CD skeleton (GitHub Actions + Argo CD) | Manager, Coder (infra), Reviewer, Deployer | 2 |
| **2️⃣ Core Backend & Identity Service** | Build authentication, tenant isolation, attendance API, Kafka pipelines. | • Quarkus microservice (auth, attendance)<br>• Keycloak realm + federation config<br>• Kafka topics & consumer groups<br>• Unit & contract tests<br>• Docker image (native) | Coder, Tester, Docker, Reviewer, Deployer | 4 |
| **3️⃣ Front‑End & Mobile Experience** | Deliver multilingual web portal & React‑Native mobile app with QR check‑in flow. | • Next.js shared codebase (web + RN Web)<br>• i18n routing & SEO hreflang tags<br>• QR scanner integration (Expo Camera)<br>• Push notification setup (FCM) <br>• End‑to‑end Cypress/Detox suites | Coder, Tester, Reviewer, Docker | 5 |
| **4️⃣ Notification Engine & Business Rules** | Implement Zalo messaging, membership day decrement, tenant‑specific branding. | • Notification microservice (Kafka consumer) <br>• Zalo Business API connector<br>• Membership‑day calculation service<br>• Configurable tenant templates (email/SMS) | Coder, Tester, Reviewer, Deployer | 3 |
| **5️⃣ Productionization & Compliance Hardening** | Harden security, performance tune, launch MVP to pilot centers, establish monitoring. | • Istio mTLS + Cloud Armor policies<br>• RLS policies & audit logging<br>• Load‑test results (JMeter)<br>• Documentation (runbooks, GDPR DSAR API)<br>• Go‑live checklist & pilot rollout | Manager, Coder, Tester, Reviewer, Deployer | 3 |

**Milestone Gates** – At the end of each phase, a **Phase Gate Review** (Manager + Reviewer) must certify that:  

1. All guardrails are passed (static analysis, security scans, compliance checks).  
2. Test coverage & quality gates are met.  
3. Documentation is up‑to‑date.  

Only then does the pipeline promote artifacts to the next environment (dev → staging → prod).  

---  

*Prepared by the Elite Solution Architecture team to guide the end‑to‑end delivery of the **membership‑hub** SaaS platform under the global project identifier **test‑ai‑architecture**.*