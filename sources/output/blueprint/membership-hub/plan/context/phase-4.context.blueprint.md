# PHASE 4 CONTEXT BLUEPRINT: membership-hub

## 1. Phase Operational Scope & Objectives
- Implement end‑to‑end deployment infrastructure using Docker containers, Google Cloud Platform (GCP) services, and Google Kubernetes Engine (GKE).  
- Harden the cluster with security policies, encryption, IAM controls, and OWASP‑aligned hardening.  
- Establish automated orchestration for multi‑tenant isolation, secret management, and production‑grade validation.  

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
- `./sources/backend/docker/` – Dockerfile definitions for Quarkus services.  
- `./sources/infrastructure/docker/` – Docker Compose and image‑push scripts.  
- `./sources/infrastructure/gcp/` – Terraform and YAML configs for GCP projects, IAM, KMS, and Artifact Registry.  
- `./sources/infrastructure/gke/` – GKE cluster, node‑pool, PodSecurityPolicy, NetworkPolicy manifests.  
- `./sources/infrastructure/orchestration/` – Manager configuration, validation, and compliance artifacts.  
- `./sources/infrastructure/security/` – OWASP scanning configs and encryption policies.  

## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Docker, GCP, GKE, Manager)
- **Docker Agent:** Build multi‑stage images, define Compose topology, and automate image push to Artifact Registry with tenant‑aware tagging.  
- **GCP Agent:** Provision GCP resources (GKE cluster, KMS keys, IAM roles), configure service accounts, and enforce encryption‑at‑rest policies.  
- **GKE Agent:** Create and secure the GKE cluster (private mode, autoscaling), apply PodSecurityPolicy and NetworkPolicy, and enforce tenant isolation.  
- **Manager Agent:** Orchestrate the overall deployment pipeline, store high‑level configuration, validate health, and produce compliance reports.  

## 4. Phase Definition of Done (DoD)
- All Docker images built, tagged with tenant_id, and pushed to GCP Artifact Registry.  
- GKE cluster provisioned with private networking, autoscaling, and security policies applied.  
- GCP IAM and KMS configured for least‑privilege access and encryption‑at‑rest with rotation.  
- OWASP compliance verified (ZAP scan) and security policies documented in compliance report.  
- End‑to‑end health checks pass; manager validation confirms all components ready for production.  

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: Establish Container Images and GCP Project Foundations
#### SUB‑TASK 1.1: Build and Configure Backend Docker Image
##### Assigned Sub-Agent: Docker
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/docker/Dockerfile
    * **Architectural Requirements:**
        * Use multi‑stage build with openjdk:17-jdk-alpine for Quarkus app.
        * Include health‑check endpoint and expose port 8080.
        * Embed OWASP validation for request size and CSRF tokens.
* **Target Path:** ./sources/infrastructure/docker/docker-compose.yml
    * **Architectural Requirements:**
        * Define services for backend (quarkus) and postgres, kafka.
        * Use environment variables for multi‑tenancy tenant_id.
        * Ensure network isolation for each tenant via separate containers.

#### SUB‑TASK 1.2: Provision GCP Project and Service Accounts
##### Assigned Sub-Agent: GCP
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/infrastructure/gcp/terraform/gke-cluster.tf
    * **Architectural Requirements:**
        * Create GKE cluster with autoscaling.
        * Enable Binary Authorization for security.
        * Tag cluster with project identifier and tenant isolation label.
* **Target Path:** ./sources/infrastructure/gcp/iam/service-account.yaml
    * **Architectural Requirements:**
        * Define service account with roles: Cloud Build, Container Developer, Security Admin.
        * Attach encrypted credentials using KMS.

#### SUB‑TASK 1.3: High‑Level Deployment Orchestration
##### Assigned Sub-Agent: Manager
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/infrastructure/orchestration/manager-config.yaml
    * **Architectural Requirements:**
        * Store deployment pipeline URLs, tenant_id scopes, and rollback policies.
        * Include validation steps for OWASP compliance before promotion.

### DAY 2: GKE Cluster Setup and Manifest Deployment
#### SUB‑TASK 2.1: Create GKE Cluster and Node Pools
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/infrastructure/gke/cluster.yaml
    * **Architectural Requirements:**
        * Define GKE cluster version 1.28+.
        * Enable Network Policy and PodSecurityPolicy.
        * Set private cluster mode for tenant isolation.
* **Target Path:** ./sources/infrastructure/gke/node-pool.yaml
    * **Architectural Requirements:**
        * Configure auto‑scaling node pools with minimum 2 nodes.
        * Apply security tags for inbound/outbound traffic control.

#### SUB‑TASK 2.2: Push Built Images to Artifact Registry
##### Assigned Sub-Agent: Docker
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/docker/Dockerfile
    * **Architectural Requirements:**
        * Add final stage copying built jar to `/app.jar`.
        * Include JMX metrics exporter for monitoring.
* **Target Path:** ./sources/infrastructure/docker/push-to-gcr.sh
    * **Architectural Requirements:**
        * Script to authenticate with GCP and push image to Artifact Registry.
        * Tag images with tenant_id and version.

#### SUB‑TASK 2.3: Deployment Orchestration Validation
##### Assigned Sub-Agent: Manager
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/infrastructure/orchestration/validation.yaml
    * **Architectural Requirements:**
        * Define health‑check endpoints for backend services.
        * Include automated rollback triggers on pod failures.

### DAY 3: Security Hardening and Production Readiness
#### SUB‑TASK 3.1: Apply Security Policies in GKE
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/infrastructure/gke/pod-security-policy.yaml
    * **Architectural Requirements:**
        * Enforce restricted pod security standards (non‑root users, read‑only root FS).
        * Include tenant_id label validation.
* **Target Path:** ./sources/infrastructure/gke/network-policy.yaml
    * **Architectural Requirements:**
        * Isolate tenant namespaces, allow only required ingress/egress.
        * Enforce mTLS where applicable.

#### SUB‑TASK 3.2: Configure Encryption and IAM Controls
##### Assigned Sub-Agent: GCP
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/infrastructure/gcp/kms/encryption-key.yaml
    * **Architectural Requirements:**
        * Create KMS key ring and symmetric encryption key with rotation policy (90 days).
        * Attach to service accounts for secret management.
* **Target Path:** ./sources/infrastructure/gcp/iam/security-policy.yaml
    * **Architectural Requirements:**
        * Define IAM roles per tenant (Admin, Manager, Teacher, Student).
        * Enforce principle of least privilege and multi‑tenancy isolation.

#### SUB‑TASK 3.3: Final Production Validation and OWASP Sign‑off
##### Assigned Sub-Agent: Manager
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/infrastructure/orchestration/production-checklist.yaml
    * **Architectural Requirements:**
        * Verify all required services are deployed and healthy.
        * Run OWASP ZAP scan against exposed endpoints, ensure no high‑risk findings.
* **Target Path:** ./sources/infrastructure/orchestration/compliance-report.json
    * **Architectural Requirements:**
        * Capture tenant_id scopes, encryption status, and security policy compliance.
        * Archive report for audit.