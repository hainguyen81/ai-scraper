# GLOBAL PROJECT CONTEXT: test‑ai‑architecture  

## 1. Executive Summary & Tech Stack Blueprint  
**Project Vision** – Build a unified **membership‑hub** platform that serves two distinct front‑ends (a web portal for administrators and a cross‑platform mobile app for learners) while supporting **multi‑center tenancy**, **QR‑based attendance**, **real‑time notifications**, and **multilingual SEO**. The solution must be **cloud‑native**, **container‑first**, and **scalable** on Google Cloud Platform (GCP) using GKE.  

### Core Business Capabilities  
| Capability | Description | Primary Actors |
|------------|-------------|----------------|
| **Tenant‑aware user management** | Internal email/password + federated login (Firebase, Google, Facebook). Unified identity store for staff and learners across all centers. | Admins, Learners |
| **QR attendance & validity tracking** | Learners scan a QR code on arrival; system records a single attendance per day, updates remaining membership days, and triggers notifications. | Learners, Staff |
| **Real‑time messaging** | Sends Zalo SMS, Zalo group messages, and push notifications (FCM/APNs) immediately after attendance. | Learners |
| **Multilingual UI & SEO** | Next.js front‑end with i18n (locale detection → stored preference → browser/device locale). SEO‑friendly server‑side rendering for web and mobile‑web. | End‑users, Search engines |
| **Multi‑center tenancy** | One logical application serving many independent training centers, with data isolation per tenant. | Center owners, Admins |
| **Observability & Scalability** | Kafka event streaming, PostgreSQL (partitioned per tenant), Prometheus/Grafana, auto‑scaling GKE. | Ops, DevOps |

### Technical Blueprint  

| Layer | Technology | Rationale |
|-------|------------|-----------|
| **API / Business Logic** | **Quarkus** (Java, GraalVM native image optional) | Reactive, low‑memory, fast startup – ideal for microservices on GKE. |
| **Message Bus** | **Apache Kafka** (Confluent Cloud or self‑managed on GKE) | Decouples attendance, notification, and analytics pipelines; guarantees at‑least‑once delivery. |
| **Data Store** | **PostgreSQL** (CloudSQL or managed AlloyDB) + **Schema per tenant** or **Row‑level security** | ACID guarantees for membership days, mature ecosystem, native JSON support for flexible user profiles. |
| **Authentication / Identity** | **Firebase Auth** (email/password, Google, Facebook) + **Custom JWT bridge** for internal users | Centralized auth, easy social login, token‑based access for Quarkus services. |
| **Containerization** | **Docker** (multi‑stage builds, GraalVM native image optional) | Consistent runtime, fast CI/CD, minimal image size. |
| **Orchestration** | **Google Kubernetes Engine (GKE)** with **Anthos**‑style policies (PodSecurity, NetworkPolicy) | Horizontal scaling, zero‑downtime deployments, regional redundancy. |
| **Front‑end (Web)** | **Next.js** (React, SSR) + **i18next** for localization | SEO‑friendly, universal rendering, easy iOS/Android via React Native Web or separate React‑Native app. |
| **Mobile App** | **React Native** (or Expo) sharing code with Next.js UI components | Single codebase for iOS & Android, push notifications via Firebase Cloud Messaging. |
| **Notification Channels** | **Firebase Cloud Messaging** (FCM) + **Zalo Business API** | Real‑time push + SMS‑like Zalo messages to learners & groups. |
| **CI/CD** | **GitHub Actions / Cloud Build** → Docker → Artifact Registry → GKE (ArgoCD or Flux) | Automated testing, image signing, progressive delivery. |
| **Observability** | **Prometheus + Grafana**, **OpenTelemetry**, **ELK** for logs | End‑to‑end tracing from QR scan to notification. |
| **Security & Compliance** | **OPA Gatekeeper**, **Binary Authorization**, **Secret Manager**, **VPC Service Controls** | Guardrails for data protection, least‑privilege, auditability. |

---

## 2. Global Guardrails & Enterprise Compliance Standards  

| Domain | Guardrail | Implementation Detail | Compliance Reference |
|--------|-----------|-----------------------|----------------------|
| **Identity & Access** | **Zero‑Trust** – all services authenticate via mutual TLS and verify JWT signatures. | Use **Istio** mTLS + **OPA** policies to enforce scopes (`attendance:write`, `notification:send`). | NIST SP 800‑207, ISO‑27001 A.5 |
| **Data Privacy** | **Tenant Isolation** – no cross‑tenant data leakage. | Row‑level security in PostgreSQL + separate Kafka topics per tenant. | GDPR Art. 25, CCPA |
| **Encryption** | **In‑Transit** TLS 1.3 everywhere; **At‑Rest** AES‑256 for DB, GCS, and Docker images. | GKE secrets via **Secret Manager**, CloudSQL encryption, Docker Content Trust. | PCI‑DSS 3.4, ISO‑27001 A.10 |
| **Audit Logging** | Immutable audit trail for authentication, attendance, and notification events. | Write to **Cloud Audit Logs** + append‑only Kafka topic `audit-events`. | SOC 2 CC6, GDPR Art. 30 |
| **API Rate Limiting** | Prevent abuse of attendance endpoint. | Envoy rate‑limit filter (e.g., 5 scans per user per minute). | OWASP API Security Top 10 |
| **CI/CD Security** | **Signed images**, **SAST/DAST**, **dependency scanning**. | Cosign signatures, GitHub Dependabot, Trivy scans in pipeline. | SLSA Level 3 |
| **Observability** | **Full‑stack tracing** for end‑to‑end latency SLA < 200 ms for QR scan → notification. | OpenTelemetry instrumentation in Quarkus & Next.js, Grafana alerts. | ITIL Service Monitoring |
| **Disaster Recovery** | RPO < 5 min, RTO < 30 min for DB and Kafka. | CloudSQL cross‑region replicas, Kafka MirrorMaker, automated GKE node pool recreation. | ISO‑22301 |
| **Internationalization** | **Locale fallback** hierarchy: stored preference → user profile → browser/device → default (en‑US). | i18next config with `fallbackLng`. | WCAG 2.1 AA (language) |
| **SEO Compliance** | Structured data (`schema.org`) for centers, courses, and events. | Next.js `next-seo` plugin, server‑side rendering. | Google SEO Guidelines |

---

## 3. Standardized Sub‑Agent Persona Definitions  

| Persona | Core Responsibility | Primary Tools / APIs | Success Metrics |
|---------|----------------------|----------------------|-----------------|
| **Manager** | Oversees product backlog, defines milestones, aligns stakeholders. | Jira, Confluence, Roadmap Planner. | On‑time delivery of phase gates, stakeholder satisfaction > 90 %. |
| **Coder** | Implements services, UI components, infrastructure as code. | Quarkus, Java, Kotlin, TypeScript, Next.js, Docker, Terraform. | Code coverage ≥ 80 %, PR merge time ≤ 24 h, no critical lint violations. |
| **Tester** | Designs & runs automated unit, integration, contract, and UI tests. | JUnit, RestAssured, Cypress, Playwright, Pact. | Test pass rate ≥ 95 %, defect leakage < 5 %. |
| **Reviewer** | Conducts code reviews, security reviews, and architecture compliance checks. | GitHub PR reviews, SonarQube, OPA policy checks. | Review turnaround ≤ 12 h, no high‑severity findings post‑merge. |
| **Docker** | Crafts optimal container images, ensures reproducibility and security. | Dockerfile multi‑stage, Buildpacks, Cosign, Trivy. | Image size ≤ 150 MB (native) or ≤ 300 MB (JVM), 0 critical CVEs. |
| **Deployer** | Automates CI/CD pipelines, manages releases to GKE, monitors roll‑backs. | GitHub Actions, Cloud Build, ArgoCD/Flux, Helm, Kustomize. | Deployment success rate ≥ 99 %, mean time to recovery (MTTR) < 10 min. |

*All agents operate under the global guardrails defined in Section 2 and report status to the Manager.*

---

## 4. Multi‑Phase Segmentation Strategy Overview (5 Phases)

| Phase | Goal | Key Deliverables | Duration (weeks) | Primary Agents |
|-------|------|------------------|------------------|----------------|
| **1️⃣ Discovery & Architecture Foundations** | Validate requirements, define multi‑tenant data model, set up baseline infra. | • Requirement traceability matrix<br>• High‑level architecture diagram<br>• GCP project & IAM baseline<br>• PoC: Quarkus service + Kafka + Postgres on GKE | 4 | Manager, Coder, Reviewer, Deployer |
| **2️⃣ Core Backend & Identity Service** | Implement tenant‑aware authentication, user CRUD, JWT issuance, and basic attendance API. | • Firebase‑Auth bridge service<br>• Quarkus microservice `attendance-service` (REST + Kafka producer)<br>• DB schema with row‑level security<br>• Unit & contract tests | 6 | Coder, Tester, Reviewer, Docker |
| **3️⃣ Front‑end & QR Attendance Flow** | Build web portal (Next.js) and mobile UI (React Native) with QR scanning, locale detection, and SSR SEO. | • Next.js web app with i18n, SEO tags<br>• React‑Native app (Expo) with QR scanner<br>• Integration tests (Cypress/Playwright)<br>• CI pipeline for front‑end builds | 6 | Coder, Tester, Reviewer, Docker |
| **4️⃣ Notification Engine & Zalo Integration** | Real‑time push + Zalo messaging after attendance, implement idempotent attendance logic. | • Kafka consumer `notification-service` (Quarkus)<br>• FCM integration<br>• Zalo Business API wrapper<br>• End‑to‑end test harness | 5 | Coder, Tester, Reviewer, Deployer |
| **5️⃣ Scaling, Observability & Production Roll‑out** | Harden security, enable auto‑scaling, implement monitoring, conduct load‑test, and go live. | • OPA Gatekeeper policies, Binary Authorization<br>• Prometheus/Grafana dashboards, OpenTelemetry tracing<br>• Chaos‑engineered load test (k6)<br>• Production deployment with blue‑green strategy | 5 | Manager, Deployer, Reviewer, Tester |

**Milestone Gates** – At the end of each phase, the Manager conducts a **Phase Review** (demo, compliance checklist, risk assessment). Only upon sign‑off does the project proceed to the next phase.

--- 

*This GLOBAL PROJECT CONTEXT provides a unified, enterprise‑grade blueprint that aligns technical decisions, compliance guardrails, and coordinated multi‑agent execution for the **membership‑hub** solution.*