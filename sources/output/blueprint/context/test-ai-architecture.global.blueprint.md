# GLOBAL PROJECT CONTEXT: test-ai-architecture
## 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable web and mobile application designed to manage students across multiple centers. The tech stack consists of Quarkus, Kafka, Postgres, and Docker, with deployment on Google Cloud Platform (GCP) and Google Kubernetes Engine (GKE). The application supports internal authentication via email and password, as well as external authentication through Firebase, Google, and Facebook. The project utilizes Next.js for the mobile frontend, supporting multiple languages and building for both iOS and Android. Key features include QR code-based attendance tracking, notification systems, and SEO optimization for both web and mobile platforms.

## 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to industry standards, the following global guardrails and compliance standards will be implemented:
- **Security**: Implement OAuth 2.0 for authentication, SSL/TLS encryption for data transmission, and regular security audits.
- **Scalability**: Design the system to scale horizontally, utilizing load balancers and auto-scaling groups in GCP.
- **Data Management**: Establish data backup and recovery procedures, ensuring data integrity and compliance with relevant regulations (e.g., GDPR, CCPA).
- **Accessibility**: Ensure the application meets Web Content Accessibility Guidelines (WCAG 2.1) and is optimized for users with disabilities.
- **Compliance**: Adhere to GCP's compliance framework, ensuring alignment with industry standards such as HIPAA, PCI-DSS, and ISO 27001.

## 3. Standardized Sub-Agent Persona Definitions
The following sub-agent personas will be defined to ensure clear roles and responsibilities:
- **Manager**: Oversees project timelines, budgets, and resource allocation. Ensures compliance with global guardrails and enterprise standards.
- **Coder**: Develops the application's backend and frontend, focusing on scalability, security, and performance.
- **Tester**: Conducts unit testing, integration testing, and user acceptance testing (UAT) to ensure the application meets requirements.
- **Reviewer**: Performs code reviews, ensuring adherence to coding standards, best practices, and security guidelines.
- **Docker**: Responsible for containerization, creating and managing Docker images for deployment.
- **Deployer**: Handles deployment to GCP and GKE, ensuring smooth rollout and minimal downtime.

## 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases:
- **Phase 1: Planning and Design** (Weeks 1-4): Define project scope, create wireframes, and establish the tech stack.
- **Phase 2: Backend Development** (Weeks 5-12): Develop the Quarkus backend, Kafka integration, and Postgres database.
- **Phase 3: Frontend Development** (Weeks 13-20): Build the Next.js mobile frontend, supporting multiple languages and platforms.
- **Phase 4: Testing and Quality Assurance** (Weeks 21-24): Conduct unit testing, integration testing, UAT, and code reviews.
- **Phase 5: Deployment and Maintenance** (Weeks 24-30): Deploy the application to GCP and GKE, ensuring scalability and performance, and provide ongoing maintenance and support.