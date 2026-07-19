# GLOBAL PROJECT CONTEXT: test-ai-architecture
## 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable web and mobile application designed to manage students across multiple centers. The tech stack includes Quarkus, Kafka, Postgres, and Docker, with deployment on Google Cloud Platform (GCP) using Google Kubernetes Engine (GKE). The application will support internal authentication via email and password, as well as external authentication through Firebase, Google, and Facebook. The front-end for the mobile app will be built using Next.js, supporting multiple languages and platforms (iOS and Android). Key features include QR code-based attendance tracking, notification systems (SMS, Zalo, and in-app notifications), and SEO optimization for both web and mobile applications.

## 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to best practices, the following global guardrails and compliance standards will be implemented:
- **Security**: Implement OAuth 2.0 for authentication and authorization, ensuring that all data transmitted between the client and server is encrypted (HTTPS).
- **Scalability**: Design the system to scale horizontally, using containerization (Docker) and orchestration (Kubernetes) to manage resources efficiently.
- **Data Privacy**: Comply with GDPR and other relevant data protection regulations, ensuring that user data is handled and stored securely.
- **Accessibility**: Follow WCAG 2.1 guidelines to ensure the application is accessible on various devices and for users with disabilities.
- **Code Quality**: Enforce coding standards, conduct regular code reviews, and use automated testing to maintain high code quality.

## 3. Standardized Sub-Agent Persona Definitions
The following personas will be involved in the project:
- **Manager**: Oversees the project timeline, budget, and resource allocation. Ensures that the project meets the stakeholders' requirements and is delivered on time.
- **Coder**: Responsible for writing clean, efficient, and well-documented code. Participates in code reviews and contributes to the improvement of the codebase.
- **Tester**: Develops and executes comprehensive test plans to ensure the application meets the required standards. Reports and tracks defects until they are resolved.
- **Reviewer**: Conducts thorough reviews of code, documentation, and other project artifacts to ensure they meet the project's quality and compliance standards.
- **Docker**: Responsible for containerizing the application, ensuring it can be efficiently deployed and managed in a containerized environment.
- **Deployer**: Manages the deployment of the application to the production environment, ensuring that it is properly configured and monitored.

## 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases:
- **Phase 1: Planning and Design** (Weeks 1-4): Define project scope, create detailed designs, and plan the architecture.
- **Phase 2: Backend Development** (Weeks 5-12): Develop the backend using Quarkus, Kafka, and Postgres, focusing on core functionalities such as user management and attendance tracking.
- **Phase 3: Frontend Development** (Weeks 13-18): Build the mobile app frontend using Next.js, implementing features such as QR code scanning, notification handling, and multi-language support.
- **Phase 4: Testing and Quality Assurance** (Weeks 19-22): Conduct thorough testing of the application, including unit testing, integration testing, and user acceptance testing (UAT).
- **Phase 5: Deployment and Maintenance** (Weeks 23-26): Deploy the application to GCP, configure monitoring and logging, and plan for post-launch maintenance and updates.