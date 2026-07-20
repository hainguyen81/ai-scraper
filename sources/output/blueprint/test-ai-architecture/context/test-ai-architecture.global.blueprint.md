# GLOBAL PROJECT CONTEXT: test-ai-architecture
## 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable, multi-tenant application designed to manage students across various centers. The tech stack consists of Quarkus, Kafka, Postgres, and Docker, deployed on Google Cloud Platform (GCP) using Google Kubernetes Engine (GKE). The application will have a web interface for management and a mobile app for students, built using Next.js, supporting multiple languages and platforms (iOS, Android). The project requires authentication via email/password, Firebase, Google, or Facebook, and features QR code-based attendance tracking, notification systems, and SEO optimization for both web and mobile platforms.

## 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to industry standards, the following guardrails and compliance standards will be implemented:
- **Security**: Implement OAuth 2.0 for authentication, SSL/TLS encryption for data transmission, and follow OWASP guidelines for secure coding practices.
- **Scalability**: Design the system to scale horizontally using Kubernetes, ensuring high availability and performance under heavy loads.
- **Data Privacy**: Comply with GDPR and CCPA regulations, ensuring user data is protected and handled according to legal requirements.
- **Accessibility**: Follow WCAG 2.1 guidelines to ensure the web and mobile applications are accessible to users with disabilities.
- **Quality Assurance**: Establish a continuous integration and continuous deployment (CI/CD) pipeline, with automated testing and code reviews to maintain high-quality code.

## 3. Standardized Sub-Agent Persona Definitions
The following personas will be involved in the project:
- **Manager**: Oversees the project timeline, budget, and resource allocation. Ensures that the project is delivered on time, within budget, and meets the required quality standards.
- **Coder**: Responsible for writing high-quality, scalable, and secure code. Collaborates with the testing team to identify and fix bugs.
- **Tester**: Develops and executes comprehensive test plans to ensure the application meets the required functionality, performance, and security standards.
- **Reviewer**: Conducts code reviews to ensure that the code is maintainable, efficient, and follows industry best practices.
- **Docker**: Responsible for creating and maintaining Docker images, ensuring that the application is properly containerized and ready for deployment.
- **Deployer**: Manages the deployment of the application to the production environment, ensuring that the deployment is smooth, and the application is properly configured.

## 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases:
- **Phase 1: Planning and Design** (Weeks 1-4): Define the project scope, create a detailed design document, and establish the technical requirements.
- **Phase 2: Backend Development** (Weeks 5-12): Develop the backend API using Quarkus, Kafka, and Postgres, and implement authentication and authorization mechanisms.
- **Phase 3: Mobile App Development** (Weeks 13-18): Develop the mobile app using Next.js, implementing features such as QR code scanning, notification systems, and multi-language support.
- **Phase 4: Testing and Quality Assurance** (Weeks 19-22): Conduct thorough testing of the application, including unit testing, integration testing, and user acceptance testing.
- **Phase 5: Deployment and Maintenance** (Weeks 23-26): Deploy the application to the production environment, configure monitoring and logging, and establish a maintenance schedule to ensure the application remains stable and secure.