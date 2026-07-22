# GLOBAL PROJECT CONTEXT: membership-hub
## 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a comprehensive web and mobile application designed to manage and facilitate learning centers. The tech stack includes Java 17, Quarkus, Kafka, Postgres, and Docker, with deployment on GCP and GKE. The application will support authentication via email, password, Firebase, Google, and Facebook, and will have a role-based access control system. The web application will be built using Next.js, with support for multiple languages and SEO optimization. The mobile application will be built using Next.js as well, with support for iOS and Android.

## 2. Global Guardrails & Enterprise Compliance Standards
The project will adhere to the following global guardrails and enterprise compliance standards:
* All Java backend source codes will reside within the corporate package foundation: `org.nlh4j.saas.membership-hub`.
* The project will follow a strict package-to-path mapping, with all physical Java files under `./sources/backend/src/main/java/` or `./sources/backend/src/test/java/` following the exact subdirectory layout matching the package tokens.
* The project will adhere to the absolute workspace boundary rule, with the true repository workspace root permanently fixed at the project root `./`.
* All directory paths generated across all phases will be prefixed with `./sources/backend/` for Java/Spring/Quarkus/Database logic and `./sources/frontend/` for TypeScript/Tailwind/UI views.
* The project will follow strict tester target path syntax, with any component targeted by a Tester Sub-Agent structured as a semi-colon separated pair `<source_component>;<test_suite>`.
* The project will avoid runtime in-memory large dataset loops and will delegate complex multi-dataset processing to native, indexed database relational operations.

## 3. Standardized Sub-Agent Persona Definitions
The project will have the following standardized sub-agent persona definitions:
* **Manager Agent:** Responsible for cross-phase orchestration, task timeline validation, and checking that the total phase count is exactly 5.
* **Coder Agent:** Owns the implementation of components located in `./sources/backend/src/main/` and `./sources/frontend/src/`. Never writes test frameworks.
* **Tester Agent:** Owns code verification. Responsible for emitting the dual-path semi-colon format (`<source>;<test>`) for units, or prefixing with `INTEGRATION_SCOPE` for system integration suites under `./sources/backend/src/test/`.
* **Reviewer Agent:** Performs static analysis, validates compliance against the database-native calculation rule, and rejects any code containing nested loops over massive tables.
* **DevOps Agent:** Owns deployment configurations, multi-stage Dockerfiles, package managers (`./sources/backend/pom.xml`, `./sources/frontend/package.json`), and CI/CD pipelines.

## 4. Multi-Phase Segmentation Strategy Overview
The project will be segmented into exactly 5 phases, with each phase strictly bounded between 1 to 7 days maximum. The phases will be:
* **Phase 1: Project Setup and Planning (Days 1-3)**
	+ Set up the project structure and repository
	+ Define the tech stack and architecture
	+ Create a detailed project plan and timeline
* **Phase 2: Backend Development (Days 4-10)**
	+ Implement the Java backend using Quarkus and Kafka
	+ Develop the database schema and models
	+ Implement authentication and authorization
* **Phase 3: Frontend Development (Days 11-17)**
	+ Implement the web application using Next.js
	+ Develop the mobile application using Next.js
	+ Implement SEO optimization and multi-language support
* **Phase 4: Testing and Quality Assurance (Days 18-24)**
	+ Develop unit tests and integration tests
	+ Perform static analysis and code review
	+ Conduct performance testing and optimization
* **Phase 5: Deployment and Maintenance (Days 25-31)**
	+ Deploy the application to GCP and GKE
	+ Configure CI/CD pipelines and monitoring
	+ Perform maintenance and updates as needed