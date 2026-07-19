# GLOBAL PROJECT CONTEXT: test-ai-architecture
## 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable, multi-tenant application designed to manage students across various centers. The tech stack includes Quarkus, Kafka, Postgres, and Docker, with deployment on GCP and GKE. The application will have both web and mobile interfaces, with the mobile app built using Next.js, supporting multiple languages and platforms (iOS, Android). The project requires internal authentication, as well as integration with Firebase, Google, and Facebook for external authentication. Key features include QR code-based attendance tracking, notification systems (SMS, Zalo, and in-app notifications), and SEO optimization for both web and mobile applications.

## 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to best practices, the following global guardrails and enterprise compliance standards will be implemented:
- **Security**: Implement OAuth 2.0 for authentication, SSL/TLS for encryption, and follow OWASP guidelines for secure coding practices.
- **Scalability**: Design the system to scale horizontally, using containerization (Docker) and orchestration (Kubernetes on GKE).
- **Data Privacy**: Comply with GDPR and CCPA regulations, ensuring user data is protected and handled according to legal requirements.
- **Accessibility**: Follow WCAG 2.1 guidelines to ensure the application is accessible on various devices and for users with disabilities.
- **Quality Assurance**: Implement automated testing (unit, integration, and UI tests) and continuous integration/continuous deployment (CI/CD) pipelines.

## 3. Standardized Sub-Agent Persona Definitions
The following personas will be involved in the project:
- **Manager**: Oversees the project timeline, budget, and resource allocation. Ensures that the project meets the stakeholders' requirements and is delivered on time.
- **Coder**: Responsible for writing clean, efficient, and well-documented code. Participates in code reviews and ensures that the codebase is scalable and maintainable.
- **Tester**: Designs and executes tests to ensure the application meets the required standards. Reports bugs and works with the development team to resolve issues.
- **Reviewer**: Conducts code reviews, ensuring that the code adheres to the project's standards and best practices. Provides feedback to improve code quality.
- **Docker**: Responsible for containerizing the application, ensuring it is properly packaged and ready for deployment.
- **Deployer**: Manages the deployment of the application to the production environment, ensuring that it is properly configured and running smoothly.

## 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases:
- **Phase 1: Planning and Design (Weeks 1-4)**: Define the project scope, create a detailed design document, and plan the architecture.
- **Phase 2: Backend Development (Weeks 5-12)**: Develop the backend using Quarkus, Kafka, and Postgres. Implement authentication and authorization mechanisms.
- **Phase 3: Mobile App Development (Weeks 13-18)**: Build the mobile app using Next.js, implementing features such as QR code scanning, notification systems, and multi-language support.
- **Phase 4: Testing and Quality Assurance (Weeks 19-22)**: Conduct thorough testing of the application, including unit tests, integration tests, and UI tests. Ensure the application meets the defined quality standards.
- **Phase 5: Deployment and Maintenance (Weeks 23-26)**: Deploy the application to GCP and GKE, configure monitoring and logging, and ensure the application is running smoothly. Plan for future maintenance and updates.