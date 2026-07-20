# GLOBAL PROJECT CONTEXT: test-ai-architecture
## 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable web and mobile application designed to manage students across multiple centers. The tech stack includes Quarkus, Kafka, Postgres, and Docker, with deployment on GCP and GKE. The application will support internal authentication via email and password, as well as external authentication through Firebase, Google, and Facebook. The project will utilize Next.js for the mobile frontend, supporting multiple languages and building for both iOS and Android. Key features include QR code attendance tracking, notification systems, and SEO optimization for both web and mobile platforms.

## 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to industry standards, the following guardrails and compliance standards will be implemented:
- **Security**: Implement OAuth 2.0 for authentication, SSL/TLS encryption for data transmission, and regular security audits.
- **Scalability**: Design the system to scale horizontally, utilizing cloud services like GCP and GKE to handle increased traffic.
- **Data Management**: Utilize Postgres for relational data storage and Kafka for event-driven data processing, ensuring data consistency and integrity.
- **Compliance**: Adhere to GDPR for user data protection, and ensure accessibility standards (WCAG 2.1) for the web and mobile applications.
- **Quality Assurance**: Implement automated testing (unit, integration, and end-to-end) and conduct regular code reviews.

## 3. Standardized Sub-Agent Persona Definitions
The following personas will be involved in the project:
- **Manager**: Oversees project timelines, budgets, and resource allocation. Ensures compliance with enterprise standards and guardrails.
- **Coder**: Develops the application's backend and frontend, focusing on Quarkus, Kafka, Postgres, and Next.js. Responsible for implementing security and scalability features.
- **Tester**: Designs and executes automated tests, as well as manual testing for critical features. Ensures the application meets quality and accessibility standards.
- **Reviewer**: Conducts code reviews, providing feedback on security, performance, and adherence to coding standards.
- **Docker**: Responsible for containerizing the application, ensuring seamless deployment and scalability.
- **Deployer**: Manages the deployment of the application on GCP and GKE, monitoring performance and addressing any deployment issues.

## 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases:
- **Phase 1: Planning and Design** (Weeks 1-4): Define project scope, create wireframes and prototypes, and establish the tech stack.
- **Phase 2: Backend Development** (Weeks 5-12): Develop the Quarkus backend, implement Kafka and Postgres, and integrate authentication systems.
- **Phase 3: Frontend Development** (Weeks 13-18): Develop the Next.js frontend, implement multi-language support, and design the mobile application.
- **Phase 4: Testing and Quality Assurance** (Weeks 19-22): Conduct automated and manual testing, perform code reviews, and ensure accessibility and security standards are met.
- **Phase 5: Deployment and Maintenance** (Weeks 23-26): Deploy the application on GCP and GKE, monitor performance, and address any issues that arise. Implement a maintenance schedule for updates and security patches.