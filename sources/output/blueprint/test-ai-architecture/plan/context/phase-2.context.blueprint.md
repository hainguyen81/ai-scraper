# PHASE 2 CONTEXT BLUEPRINT: test-ai-architecture
## 1. Phase Operational Scope & Objectives
The primary objective of Phase 2 is to develop the backend features of the membership-hub project, including authentication, attendance tracking, and notification systems. This phase will focus on building a scalable and secure backend using Quarkus, Kafka, and Postgres. The key deliverables for this phase include:
- Design and implementation of authentication mechanisms (email/password, Firebase, Google, Facebook)
- Development of attendance tracking features (QR code-based attendance tracking)
- Implementation of notification systems (SMS, Zalo, in-app notifications)
- Integration with Postgres database for data storage
- Containerization using Docker for seamless deployment on GKE

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 2 will be limited to the backend development, with the following directory boundaries:
- `src/main/java`: Java source code for Quarkus application
- `src/main/resources`: Configuration files and static resources
- `docker`: Dockerfile and containerization scripts
- `kafka`: Kafka configuration and topic definitions
- `postgres`: Postgres database schema and migration scripts
- `api`: API endpoints for authentication, attendance tracking, and notification systems
Allowed endpoints:
- `/api/auth`: Authentication endpoints (login, logout, register)
- `/api/attendance`: Attendance tracking endpoints (QR code scanning, attendance logging)
- `/api/notifications`: Notification endpoints (SMS, Zalo, in-app notifications)

## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
- **Coder**: Implement authentication mechanisms, attendance tracking features, and notification systems. Develop API endpoints for backend features.
- **Tester**: Develop unit tests and integration tests for backend features. Test authentication, attendance tracking, and notification systems.
- **Reviewer**: Review code for adherence to coding standards, security, and scalability. Provide feedback on API endpoint design and implementation.
- **DevOps (Docker)**: Containerize the Quarkus application using Docker. Ensure seamless deployment on GKE.
- **DevOps (Deployer)**: Prepare deployment scripts for GCP and GKE. Ensure zero-downtime deployments.

## 4. Phase Definition of Done (DoD)
Phase 2 is considered complete when:
- All backend features (authentication, attendance tracking, notification systems) are implemented and tested.
- API endpoints are designed and implemented for backend features.
- Code is reviewed and meets coding standards, security, and scalability requirements.
- Docker containerization is complete, and deployment scripts are prepared for GCP and GKE.
- Unit tests and integration tests are developed and passed for backend features.
The maximum duration for Phase 2 is 7 days. Once the core technical objectives are satisfied, the phase will be considered complete, and progression to Phase 3 will begin.