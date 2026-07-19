# PHASE 2 CONTEXT BLUEPRINT: test-ai-architecture
## 1. Phase Operational Scope & Objectives
The primary objective of Phase 2 is to develop the backend of the membership-hub project using Quarkus, Kafka, and Postgres. This phase will focus on building the core functionalities of the application, including user management, attendance tracking, and notification systems. The scope of this phase includes:

* Designing and implementing the database schema for user management and attendance tracking
* Developing the backend API for user authentication, registration, and profile management
* Integrating Kafka for real-time notification handling
* Building the attendance tracking system with QR code scanning functionality
* Implementing notification systems for SMS, Zalo, and in-app notifications

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 2 includes:

* Backend development using Quarkus, Kafka, and Postgres
* Containerization using Docker
* API endpoint development for user management and attendance tracking
* Integration with Firebase, Google, and Facebook for external authentication
* Development of notification systems using Kafka

Directory boundaries:

* `src/main/java`: Quarkus backend code
* `src/main/resources`: Database schema and configuration files
* `src/test/java`: Unit tests and integration tests for backend code
* `docker`: Dockerfile and containerization configuration
* `kafka`: Kafka configuration and notification handling code

Endpoints:

* `/api/v1/users`: User management API endpoints
* `/api/v1/attendance`: Attendance tracking API endpoints
* `/api/v1/notifications`: Notification systems API endpoints

## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
* **Coder**:
	+ Develop the backend API for user management and attendance tracking
	+ Implement Kafka integration for real-time notification handling
	+ Build the attendance tracking system with QR code scanning functionality
* **Tester**:
	+ Develop unit tests and integration tests for backend code
	+ Test API endpoints for user management and attendance tracking
	+ Test notification systems for SMS, Zalo, and in-app notifications
* **Reviewer**:
	+ Review backend code for quality and compliance with coding standards
	+ Review database schema and configuration files
	+ Review API endpoint documentation and testing coverage
* **DevOps**:
	+ Configure Docker containerization for backend code
	+ Deploy backend code to GCP using GKE
	+ Configure monitoring and logging for backend code

## 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 2 includes:

* All backend API endpoints are developed and tested
* Kafka integration is complete and functional
* Attendance tracking system with QR code scanning functionality is built and tested
* Notification systems for SMS, Zalo, and in-app notifications are developed and tested
* Backend code is reviewed and meets coding standards
* Docker containerization is configured and deployed to GCP using GKE
* Monitoring and logging are configured for backend code

The phase is considered complete when all the above criteria are met, and the backend code is fully functional and deployable to production.