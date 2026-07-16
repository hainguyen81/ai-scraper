# GLOBAL PROJECT CONTEXT: test-ai-architecture
## 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable web and mobile application designed to manage students across multiple centers. The tech stack includes Quarkus, Kafka, Postgres, and Docker, with deployment on GCP and GKE. The application supports internal authentication via email/password, Firebase, Google, and Facebook, and manages user login and registration. The project utilizes Next.js for the mobile frontend, supporting multiple languages and building for both iOS and Android. Key features include QR code-based attendance tracking, notification systems, and SEO optimization for both web and mobile platforms.

## 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to industry standards, the following guardrails and compliance standards will be implemented:
- **Security**: Implement OAuth 2.0 for authentication, SSL/TLS encryption for data transmission, and regular security audits.
- **Scalability**: Design the system to scale horizontally, utilizing load balancers and auto-scaling groups in GKE.
- **Data Management**: Establish data backup and recovery procedures, ensuring data integrity and compliance with relevant regulations (e.g., GDPR, CCPA).
- **Accessibility**: Ensure the application meets Web Content Accessibility Guidelines (WCAG 2.1) and is optimized for multiple languages and locales.
- **Compliance**: Adhere to GCP and GKE compliance standards, as well as industry-specific regulations (e.g., education sector).

## 3. Standardized Sub-Agent Persona Definitions
The following sub-agent personas will be defined to ensure clear roles and responsibilities:
- **Manager**: Oversees project timelines, budgets, and resource allocation.
- **Coder**: Develops the application's backend and frontend, ensuring adherence to coding standards and best practices.
- **Tester**: Conducts thorough testing, including unit testing, integration testing, and user acceptance testing (UAT).
- **Reviewer**: Reviews code, ensuring it meets the project's technical requirements and adheres to industry standards.
- **Docker**: Responsible for containerization, ensuring seamless deployment and scaling.
- **Deployer**: Manages the deployment process, ensuring smooth transitions to production environments.

## 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases:
- **Phase 1: Planning and Design** (Weeks 1-4): Define project scope, create wireframes, and establish the technical architecture.
- **Phase 2: Backend Development** (Weeks 5-12): Develop the Quarkus-based backend, including authentication, user management, and attendance tracking.
- **Phase 3: Frontend Development** (Weeks 13-18): Develop the Next.js-based mobile frontend, supporting multiple languages and building for both iOS and Android.
- **Phase 4: Testing and Quality Assurance** (Weeks 19-22): Conduct thorough testing, including unit testing, integration testing, and UAT.
- **Phase 5: Deployment and Maintenance** (Weeks 23-26): Deploy the application to GCP and GKE, ensuring scalability and performance, and establish a maintenance schedule for future updates and bug fixes.