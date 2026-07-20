# GLOBAL PROJECT CONTEXT: test-ai-architecture
## 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable web and mobile application designed to manage students across multiple centers. The tech stack includes Quarkus, Kafka, Postgres, and Docker, with deployment on GCP and GKE. The application supports internal authentication via email/password, Firebase, Google, and Facebook, and manages user login and registration. The project utilizes Next.js for the mobile frontend, supporting multiple languages and building for both iOS and Android. Key features include QR code-based attendance tracking, notification systems, and SEO optimization for both web and mobile platforms.

## 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to industry standards, the following guardrails and compliance standards will be implemented:
- **Security**: Implement OAuth 2.0 for authentication, use HTTPS for encryption, and follow OWASP guidelines for secure coding practices.
- **Scalability**: Design the system to scale horizontally, utilizing load balancers and auto-scaling groups in GKE.
- **Data Management**: Use Postgres for relational data storage and Kafka for event-driven architecture, ensuring data consistency and integrity.
- **Compliance**: Adhere to GDPR for user data protection, and follow accessibility guidelines (WCAG 2.1) for the web and mobile applications.
- **Monitoring and Logging**: Implement logging and monitoring tools (e.g., Prometheus, Grafana) to track system performance and identify potential issues.

## 3. Standardized Sub-Agent Persona Definitions
The following personas will be involved in the project:
- **Manager**: Oversees the project timeline, budget, and resource allocation. Ensures that the project is delivered on time and within budget.
- **Coder**: Responsible for writing clean, efficient, and well-documented code. Collaborates with the team to implement new features and fix bugs.
- **Tester**: Develops and executes comprehensive test plans to ensure the application meets the required standards. Reports defects and collaborates with the development team to resolve issues.
- **Reviewer**: Conducts code reviews to ensure that the code meets the project's coding standards and best practices. Provides feedback to the development team to improve code quality.
- **Docker**: Responsible for creating and maintaining Docker images for the application, ensuring that the images are optimized for production environments.
- **Deployer**: Manages the deployment of the application to GKE, ensuring that the deployment is smooth and that the application is properly configured for production.

## 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into the following five phases:
- **Phase 1: Planning and Design** (Weeks 1-4): Define the project scope, create a detailed design document, and develop a prototype to validate the project's feasibility.
- **Phase 2: Backend Development** (Weeks 5-12): Develop the backend API using Quarkus, implement authentication and authorization, and integrate with Kafka and Postgres.
- **Phase 3: Mobile Frontend Development** (Weeks 13-18): Develop the mobile frontend using Next.js, implement features such as QR code scanning and notification systems.
- **Phase 4: Testing and Quality Assurance** (Weeks 19-22): Conduct unit testing, integration testing, and UI testing to ensure that the application meets the required standards.
- **Phase 5: Deployment and Maintenance** (Weeks 23-26): Deploy the application to GKE, configure monitoring and logging tools, and ensure that the application is properly maintained and updated to meet changing requirements.