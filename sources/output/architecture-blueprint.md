# Global Prompt:


        Analyze the attached project requirements. Build the GLOBAL PROJECT CONTEXT for 'test-ai-architecture'.
        
        --- RAW REQUIREMENTS ---
        ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

        --- END REQUIREMENTS ---

        Your output MUST follow this exact structure:
        ## GLOBAL PROJECT CONTEXT: test-ai-architecture
        #### 1. Executive Summary & Tech Stack Blueprint
        #### 2. Global Guardrails & Enterprise Compliance Standards
        #### 3. Standardized Sub-Agent Persona Definitions (Manager, Coder, Tester, Reviewer, Docker, Deployer)
        #### 4. Multi-Phase Segmentation Strategy Overview (Plan exactly 5 phases)
        

# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable, multi-tenant application designed to manage students across various centers. The tech stack includes Quarkus, Kafka, Postgres, and Docker, with deployment on GCP and GKE. The application will have both web and mobile interfaces, with the mobile app built using Next.js, supporting multiple languages and platforms (iOS, Android). The project requires internal authentication, as well as integration with Firebase, Google, and Facebook for external authentication. Key features include QR code-based attendance tracking, notification systems (SMS, Zalo, and in-app notifications), and SEO optimization for both web and mobile applications.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to best practices, the following global guardrails and enterprise compliance standards will be implemented:
- **Security**: Implement OAuth 2.0 for authentication, SSL/TLS for encryption, and follow OWASP guidelines for secure coding practices.
- **Scalability**: Design the system to scale horizontally, using containerization (Docker) and orchestration (Kubernetes on GKE).
- **Data Privacy**: Comply with GDPR and CCPA regulations, ensuring user data is protected and handled according to legal requirements.
- **Accessibility**: Follow WCAG 2.1 guidelines to ensure the application is accessible on various devices and for users with disabilities.
- **Quality Assurance**: Implement automated testing (unit, integration, and UI tests) and continuous integration/continuous deployment (CI/CD) pipelines.

#### 3. Standardized Sub-Agent Persona Definitions
The following personas will be involved in the project:
- **Manager**: Oversees the project timeline, budget, and resource allocation. Ensures that the project meets the stakeholders' requirements and is delivered on time.
- **Coder**: Responsible for writing clean, efficient, and well-documented code. Participates in code reviews and ensures that the codebase is scalable and maintainable.
- **Tester**: Designs and executes tests to ensure the application meets the required standards. Reports bugs and works with the development team to resolve issues.
- **Reviewer**: Conducts code reviews, ensuring that the code adheres to the project's standards and best practices. Provides feedback to improve code quality.
- **Docker**: Responsible for containerizing the application, ensuring it is properly packaged and ready for deployment.
- **Deployer**: Manages the deployment of the application to the production environment, ensuring that it is properly configured and running smoothly.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases:
- **Phase 1: Planning and Design (Weeks 1-4)**: Define the project scope, create a detailed design document, and plan the architecture.
- **Phase 2: Backend Development (Weeks 5-12)**: Develop the backend using Quarkus, Kafka, and Postgres. Implement authentication and authorization mechanisms.
- **Phase 3: Mobile App Development (Weeks 13-18)**: Build the mobile app using Next.js, implementing features such as QR code scanning, notification systems, and multi-language support.
- **Phase 4: Testing and Quality Assurance (Weeks 19-22)**: Conduct thorough testing of the application, including unit tests, integration tests, and UI tests. Ensure the application meets the defined quality standards.
- **Phase 5: Deployment and Maintenance (Weeks 23-26)**: Deploy the application to GCP and GKE, configure monitoring and logging, and ensure the application is running smoothly. Plan for future maintenance and updates.
```

# Phase 1 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 1 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable, multi-tenant application designed to manage students across various centers. The tech stack includes Quarkus, Kafka, Postgres, and Docker, with deployment on GCP and GKE. The application will have both web and mobile interfaces, with the mobile app built using Next.js, supporting multiple languages and platforms (iOS, Android). The project requires internal authentication, as well as integration with Firebase, Google, and Facebook for external authentication. Key features include QR code-based attendance tracking, notification systems (SMS, Zalo, and in-app notifications), and SEO optimization for both web and mobile applications.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to best practices, the following global guardrails and enterprise compliance standards will be implemented:
- **Security**: Implement OAuth 2.0 for authentication, SSL/TLS for encryption, and follow OWASP guidelines for secure coding practices.
- **Scalability**: Design the system to scale horizontally, using containerization (Docker) and orchestration (Kubernetes on GKE).
- **Data Privacy**: Comply with GDPR and CCPA regulations, ensuring user data is protected and handled according to legal requirements.
- **Accessibility**: Follow WCAG 2.1 guidelines to ensure the application is accessible on various devices and for users with disabilities.
- **Quality Assurance**: Implement automated testing (unit, integration, and UI tests) and continuous integration/continuous deployment (CI/CD) pipelines.

#### 3. Standardized Sub-Agent Persona Definitions
The following personas will be involved in the project:
- **Manager**: Oversees the project timeline, budget, and resource allocation. Ensures that the project meets the stakeholders' requirements and is delivered on time.
- **Coder**: Responsible for writing clean, efficient, and well-documented code. Participates in code reviews and ensures that the codebase is scalable and maintainable.
- **Tester**: Designs and executes tests to ensure the application meets the required standards. Reports bugs and works with the development team to resolve issues.
- **Reviewer**: Conducts code reviews, ensuring that the code adheres to the project's standards and best practices. Provides feedback to improve code quality.
- **Docker**: Responsible for containerizing the application, ensuring it is properly packaged and ready for deployment.
- **Deployer**: Manages the deployment of the application to the production environment, ensuring that it is properly configured and running smoothly.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases:
- **Phase 1: Planning and Design (Weeks 1-4)**: Define the project scope, create a detailed design document, and plan the architecture.
- **Phase 2: Backend Development (Weeks 5-12)**: Develop the backend using Quarkus, Kafka, and Postgres. Implement authentication and authorization mechanisms.
- **Phase 3: Mobile App Development (Weeks 13-18)**: Build the mobile app using Next.js, implementing features such as QR code scanning, notification systems, and multi-language support.
- **Phase 4: Testing and Quality Assurance (Weeks 19-22)**: Conduct thorough testing of the application, including unit tests, integration tests, and UI tests. Ensure the application meets the defined quality standards.
- **Phase 5: Deployment and Maintenance (Weeks 23-26)**: Deploy the application to GCP and GKE, configure monitoring and logging, and ensure the application is running smoothly. Plan for future maintenance and updates.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------

            Your output MUST follow this exact Markdown structure for Phase 1:
            ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed design document, and plan the architecture for the membership-hub project. This phase will focus on gathering and analyzing requirements, identifying potential technical challenges, and outlining the overall system design. The key deliverables for this phase include:
- A detailed project scope statement
- A high-level system architecture design
- A comprehensive requirements document
- An initial project timeline and resource allocation plan

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
For Phase 1, the technical scope will be limited to the following areas:
- Project scope definition: Defining the project's objectives, deliverables, and key performance indicators (KPIs)
- System architecture design: Outlining the overall system architecture, including the backend, frontend, and database components
- Requirements gathering: Collecting and analyzing the raw requirements for the project, including functional and non-functional requirements
- Directory boundaries:
  - `docs/`: For storing project documentation, including the project scope statement, system architecture design, and requirements document
  - `design/`: For storing design-related files, including wireframes, prototypes, and system architecture diagrams
  - `src/`: For storing source code, including backend, frontend, and database components (initially empty, to be populated in later phases)

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversees the project timeline, budget, and resource allocation. Ensures that the project meets the stakeholders' requirements and is delivered on time.
- **Coder**: Assists in defining the system architecture and outlining the technical requirements for the project. Begins designing the database schema and backend components.
- **Tester**: Reviews the requirements document and begins outlining the testing strategy for the project.
- **Reviewer**: Reviews the project scope statement, system architecture design, and requirements document to ensure they meet the project's standards and best practices.
- **Docker**: Not directly involved in Phase 1, but will be responsible for containerizing the application in later phases.
- **Deployer**: Not directly involved in Phase 1, but will be responsible for deploying the application to the production environment in later phases.

#### 4. Phase Definition of Done (DoD)
The Definition of Done (DoD) for Phase 1 is as follows:
- A detailed project scope statement has been created and approved by stakeholders
- A high-level system architecture design has been outlined and reviewed by the team
- A comprehensive requirements document has been created and reviewed by the team
- An initial project timeline and resource allocation plan have been created and approved by stakeholders
- All documents and designs have been stored in the designated directories (`docs/`, `design/`, etc.)
- The project scope, system architecture, and requirements have been reviewed and approved by the Manager, Coder, Tester, Reviewer, and other relevant stakeholders.
```

# Phase 2 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 2 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable, multi-tenant application designed to manage students across various centers. The tech stack includes Quarkus, Kafka, Postgres, and Docker, with deployment on GCP and GKE. The application will have both web and mobile interfaces, with the mobile app built using Next.js, supporting multiple languages and platforms (iOS, Android). The project requires internal authentication, as well as integration with Firebase, Google, and Facebook for external authentication. Key features include QR code-based attendance tracking, notification systems (SMS, Zalo, and in-app notifications), and SEO optimization for both web and mobile applications.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to best practices, the following global guardrails and enterprise compliance standards will be implemented:
- **Security**: Implement OAuth 2.0 for authentication, SSL/TLS for encryption, and follow OWASP guidelines for secure coding practices.
- **Scalability**: Design the system to scale horizontally, using containerization (Docker) and orchestration (Kubernetes on GKE).
- **Data Privacy**: Comply with GDPR and CCPA regulations, ensuring user data is protected and handled according to legal requirements.
- **Accessibility**: Follow WCAG 2.1 guidelines to ensure the application is accessible on various devices and for users with disabilities.
- **Quality Assurance**: Implement automated testing (unit, integration, and UI tests) and continuous integration/continuous deployment (CI/CD) pipelines.

#### 3. Standardized Sub-Agent Persona Definitions
The following personas will be involved in the project:
- **Manager**: Oversees the project timeline, budget, and resource allocation. Ensures that the project meets the stakeholders' requirements and is delivered on time.
- **Coder**: Responsible for writing clean, efficient, and well-documented code. Participates in code reviews and ensures that the codebase is scalable and maintainable.
- **Tester**: Designs and executes tests to ensure the application meets the required standards. Reports bugs and works with the development team to resolve issues.
- **Reviewer**: Conducts code reviews, ensuring that the code adheres to the project's standards and best practices. Provides feedback to improve code quality.
- **Docker**: Responsible for containerizing the application, ensuring it is properly packaged and ready for deployment.
- **Deployer**: Manages the deployment of the application to the production environment, ensuring that it is properly configured and running smoothly.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases:
- **Phase 1: Planning and Design (Weeks 1-4)**: Define the project scope, create a detailed design document, and plan the architecture.
- **Phase 2: Backend Development (Weeks 5-12)**: Develop the backend using Quarkus, Kafka, and Postgres. Implement authentication and authorization mechanisms.
- **Phase 3: Mobile App Development (Weeks 13-18)**: Build the mobile app using Next.js, implementing features such as QR code scanning, notification systems, and multi-language support.
- **Phase 4: Testing and Quality Assurance (Weeks 19-22)**: Conduct thorough testing of the application, including unit tests, integration tests, and UI tests. Ensure the application meets the defined quality standards.
- **Phase 5: Deployment and Maintenance (Weeks 23-26)**: Deploy the application to GCP and GKE, configure monitoring and logging, and ensure the application is running smoothly. Plan for future maintenance and updates.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------

            Your output MUST follow this exact Markdown structure for Phase 2:
            ## PHASE 2 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 2 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 2 is to develop the backend of the membership-hub project using Quarkus, Kafka, and Postgres. This phase will focus on implementing authentication and authorization mechanisms, designing the database schema, and building the core backend functionality. The scope of this phase includes:

* Designing and implementing the database schema for user management, attendance tracking, and notification systems
* Developing the backend API using Quarkus, including endpoints for user registration, login, attendance tracking, and notification systems
* Implementing authentication and authorization mechanisms using OAuth 2.0, including internal authentication and integration with Firebase, Google, and Facebook
* Building the core backend functionality for attendance tracking, including QR code generation and scanning, and notification systems

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope of this phase includes:

* Backend development using Quarkus, Kafka, and Postgres
* Database schema design and implementation
* API endpoint development for user management, attendance tracking, and notification systems
* Authentication and authorization mechanism implementation
* Directory boundaries:
	+ `src/main/java`: Java source code for the backend
	+ `src/main/resources`: Configuration files and resources for the backend
	+ `src/test/java`: Java source code for unit tests and integration tests
	+ `src/test/resources`: Configuration files and resources for testing
	+ API endpoints:
		- `/api/v1/users`: User management endpoints
		- `/api/v1/attendance`: Attendance tracking endpoints
		- `/api/v1/notifications`: Notification system endpoints

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in this phase:

* **Coder**: Responsible for developing the backend API, implementing authentication and authorization mechanisms, and building the core backend functionality
* **Tester**: Responsible for designing and executing unit tests, integration tests, and UI tests for the backend API and core functionality
* **Reviewer**: Responsible for conducting code reviews, ensuring that the code adheres to the project's standards and best practices, and providing feedback to improve code quality
* **DevOps**: Responsible for containerizing the backend application using Docker, configuring the deployment environment, and ensuring that the application is properly packaged and ready for deployment

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 2 includes:

* The backend API is fully implemented, including all required endpoints and functionality
* Authentication and authorization mechanisms are fully implemented and tested
* The database schema is designed and implemented, and all required data models are in place
* Unit tests, integration tests, and UI tests are written and passing for all backend functionality
* Code reviews have been conducted, and all code changes have been approved and merged into the main branch
* The backend application is containerized using Docker, and the deployment environment is configured and ready for deployment.
```

# Phase 3 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 3 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable, multi-tenant application designed to manage students across various centers. The tech stack includes Quarkus, Kafka, Postgres, and Docker, with deployment on GCP and GKE. The application will have both web and mobile interfaces, with the mobile app built using Next.js, supporting multiple languages and platforms (iOS, Android). The project requires internal authentication, as well as integration with Firebase, Google, and Facebook for external authentication. Key features include QR code-based attendance tracking, notification systems (SMS, Zalo, and in-app notifications), and SEO optimization for both web and mobile applications.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to best practices, the following global guardrails and enterprise compliance standards will be implemented:
- **Security**: Implement OAuth 2.0 for authentication, SSL/TLS for encryption, and follow OWASP guidelines for secure coding practices.
- **Scalability**: Design the system to scale horizontally, using containerization (Docker) and orchestration (Kubernetes on GKE).
- **Data Privacy**: Comply with GDPR and CCPA regulations, ensuring user data is protected and handled according to legal requirements.
- **Accessibility**: Follow WCAG 2.1 guidelines to ensure the application is accessible on various devices and for users with disabilities.
- **Quality Assurance**: Implement automated testing (unit, integration, and UI tests) and continuous integration/continuous deployment (CI/CD) pipelines.

#### 3. Standardized Sub-Agent Persona Definitions
The following personas will be involved in the project:
- **Manager**: Oversees the project timeline, budget, and resource allocation. Ensures that the project meets the stakeholders' requirements and is delivered on time.
- **Coder**: Responsible for writing clean, efficient, and well-documented code. Participates in code reviews and ensures that the codebase is scalable and maintainable.
- **Tester**: Designs and executes tests to ensure the application meets the required standards. Reports bugs and works with the development team to resolve issues.
- **Reviewer**: Conducts code reviews, ensuring that the code adheres to the project's standards and best practices. Provides feedback to improve code quality.
- **Docker**: Responsible for containerizing the application, ensuring it is properly packaged and ready for deployment.
- **Deployer**: Manages the deployment of the application to the production environment, ensuring that it is properly configured and running smoothly.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases:
- **Phase 1: Planning and Design (Weeks 1-4)**: Define the project scope, create a detailed design document, and plan the architecture.
- **Phase 2: Backend Development (Weeks 5-12)**: Develop the backend using Quarkus, Kafka, and Postgres. Implement authentication and authorization mechanisms.
- **Phase 3: Mobile App Development (Weeks 13-18)**: Build the mobile app using Next.js, implementing features such as QR code scanning, notification systems, and multi-language support.
- **Phase 4: Testing and Quality Assurance (Weeks 19-22)**: Conduct thorough testing of the application, including unit tests, integration tests, and UI tests. Ensure the application meets the defined quality standards.
- **Phase 5: Deployment and Maintenance (Weeks 23-26)**: Deploy the application to GCP and GKE, configure monitoring and logging, and ensure the application is running smoothly. Plan for future maintenance and updates.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------

            Your output MUST follow this exact Markdown structure for Phase 3:
            ## PHASE 3 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 3 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 3 is to develop the mobile app for the membership-hub project using Next.js. This phase will focus on implementing features such as QR code scanning, notification systems, and multi-language support. The mobile app will be designed to work seamlessly with the backend developed in Phase 2, ensuring a cohesive user experience. Key deliverables for this phase include:

* A fully functional mobile app with QR code scanning capabilities
* Integration with the backend for user authentication and authorization
* Implementation of notification systems (SMS, Zalo, and in-app notifications)
* Support for multiple languages and platforms (iOS, Android)
* Detection of default locale and language settings for users

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 3 will be limited to the mobile app development using Next.js. The following directories, files, and endpoints will be within the scope of this phase:

* `mobile-app/`: The root directory for the mobile app codebase
* `components/`: Directory for reusable UI components
* `pages/`: Directory for page-level components
* `api/`: Directory for API endpoints and integrations
* `utils/`: Directory for utility functions and helpers
* `locales/`: Directory for language and locale settings
* Endpoints:
	+ `/api/qr-code`: Endpoint for QR code scanning and processing
	+ `/api/notifications`: Endpoint for sending notifications (SMS, Zalo, and in-app)
	+ `/api/auth`: Endpoint for user authentication and authorization

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 3, with specific tasks and responsibilities:

* **Coder**: Develop the mobile app using Next.js, implementing features such as QR code scanning, notification systems, and multi-language support. Ensure the app is optimized for performance and follows best practices for coding and security.
* **Tester**: Design and execute tests for the mobile app, ensuring it meets the required standards for functionality, usability, and performance. Report bugs and work with the development team to resolve issues.
* **Reviewer**: Conduct code reviews for the mobile app, ensuring it adheres to the project's standards and best practices. Provide feedback to improve code quality and suggest optimizations.
* **DevOps**: Ensure the mobile app is properly packaged and ready for deployment. Configure the build process and automate testing and deployment scripts.

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 3 will be considered complete when the following criteria are met:

* The mobile app is fully functional and meets all the requirements outlined in the phase objectives
* The app has been thoroughly tested and validated by the testing team
* Code reviews have been completed, and all feedback has been addressed
* The app has been properly packaged and is ready for deployment
* All necessary documentation and guides have been updated to reflect the changes made during this phase
* The phase has been reviewed and approved by the project manager and stakeholders.
```

# Phase 4 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 4 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable, multi-tenant application designed to manage students across various centers. The tech stack includes Quarkus, Kafka, Postgres, and Docker, with deployment on GCP and GKE. The application will have both web and mobile interfaces, with the mobile app built using Next.js, supporting multiple languages and platforms (iOS, Android). The project requires internal authentication, as well as integration with Firebase, Google, and Facebook for external authentication. Key features include QR code-based attendance tracking, notification systems (SMS, Zalo, and in-app notifications), and SEO optimization for both web and mobile applications.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to best practices, the following global guardrails and enterprise compliance standards will be implemented:
- **Security**: Implement OAuth 2.0 for authentication, SSL/TLS for encryption, and follow OWASP guidelines for secure coding practices.
- **Scalability**: Design the system to scale horizontally, using containerization (Docker) and orchestration (Kubernetes on GKE).
- **Data Privacy**: Comply with GDPR and CCPA regulations, ensuring user data is protected and handled according to legal requirements.
- **Accessibility**: Follow WCAG 2.1 guidelines to ensure the application is accessible on various devices and for users with disabilities.
- **Quality Assurance**: Implement automated testing (unit, integration, and UI tests) and continuous integration/continuous deployment (CI/CD) pipelines.

#### 3. Standardized Sub-Agent Persona Definitions
The following personas will be involved in the project:
- **Manager**: Oversees the project timeline, budget, and resource allocation. Ensures that the project meets the stakeholders' requirements and is delivered on time.
- **Coder**: Responsible for writing clean, efficient, and well-documented code. Participates in code reviews and ensures that the codebase is scalable and maintainable.
- **Tester**: Designs and executes tests to ensure the application meets the required standards. Reports bugs and works with the development team to resolve issues.
- **Reviewer**: Conducts code reviews, ensuring that the code adheres to the project's standards and best practices. Provides feedback to improve code quality.
- **Docker**: Responsible for containerizing the application, ensuring it is properly packaged and ready for deployment.
- **Deployer**: Manages the deployment of the application to the production environment, ensuring that it is properly configured and running smoothly.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases:
- **Phase 1: Planning and Design (Weeks 1-4)**: Define the project scope, create a detailed design document, and plan the architecture.
- **Phase 2: Backend Development (Weeks 5-12)**: Develop the backend using Quarkus, Kafka, and Postgres. Implement authentication and authorization mechanisms.
- **Phase 3: Mobile App Development (Weeks 13-18)**: Build the mobile app using Next.js, implementing features such as QR code scanning, notification systems, and multi-language support.
- **Phase 4: Testing and Quality Assurance (Weeks 19-22)**: Conduct thorough testing of the application, including unit tests, integration tests, and UI tests. Ensure the application meets the defined quality standards.
- **Phase 5: Deployment and Maintenance (Weeks 23-26)**: Deploy the application to GCP and GKE, configure monitoring and logging, and ensure the application is running smoothly. Plan for future maintenance and updates.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------

            Your output MUST follow this exact Markdown structure for Phase 4:
            ## PHASE 4 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 4 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 4 is to conduct thorough testing and quality assurance of the membership-hub application. This phase will ensure that the application meets the defined quality standards, is stable, and functions as expected. The scope of this phase includes:

* Conducting unit tests, integration tests, and UI tests for the web and mobile applications
* Testing the application's authentication and authorization mechanisms
* Verifying the application's scalability and performance
* Ensuring the application's compliance with security, data privacy, and accessibility standards
* Identifying and resolving bugs and defects

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope of Phase 4 includes:

* Testing the API endpoints for the backend application
* Verifying the functionality of the mobile app's features, such as QR code scanning and notification systems
* Testing the application's integration with Firebase, Google, and Facebook for external authentication
* Reviewing the codebase to ensure adherence to security, data privacy, and accessibility standards
* Utilizing testing frameworks and tools, such as JUnit, TestNG, and Selenium, to automate testing

The directory boundaries for Phase 4 include:

* `src/test/java` for unit tests and integration tests
* `src/test/resources` for test data and configuration files
* `mobile-app/tests` for mobile app tests
* `api-docs` for API documentation and testing

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 4:

* **Coder**: Responsible for writing unit tests, integration tests, and UI tests for the application
* **Tester**: Conducts testing of the application, including manual and automated testing
* **Reviewer**: Reviews the codebase to ensure adherence to security, data privacy, and accessibility standards
* **DevOps**: Responsible for configuring and managing the testing environment, including setting up test data and configuring testing frameworks

The specific tasks for each sub-agent include:

* Coder: Write unit tests for the backend application, write integration tests for the mobile app
* Tester: Conduct manual testing of the application, automate testing using Selenium
* Reviewer: Review the codebase for security vulnerabilities, review the application's compliance with data privacy regulations
* DevOps: Configure the testing environment, set up test data, manage testing frameworks

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 4 includes:

* All unit tests, integration tests, and UI tests have been written and executed
* The application has been tested for security, data privacy, and accessibility compliance
* All bugs and defects have been identified and resolved
* The application's performance and scalability have been verified
* The testing environment has been configured and managed
* The codebase has been reviewed for adherence to security, data privacy, and accessibility standards

The acceptance criteria for Phase 4 include:

* The application passes all unit tests, integration tests, and UI tests
* The application meets the defined security, data privacy, and accessibility standards
* The application's performance and scalability meet the defined requirements
* The testing environment is properly configured and managed
* The codebase is reviewed and approved by the Reviewer sub-agent
```

# Phase 5 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 5 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable, multi-tenant application designed to manage students across various centers. The tech stack includes Quarkus, Kafka, Postgres, and Docker, with deployment on GCP and GKE. The application will have both web and mobile interfaces, with the mobile app built using Next.js, supporting multiple languages and platforms (iOS, Android). The project requires internal authentication, as well as integration with Firebase, Google, and Facebook for external authentication. Key features include QR code-based attendance tracking, notification systems (SMS, Zalo, and in-app notifications), and SEO optimization for both web and mobile applications.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to best practices, the following global guardrails and enterprise compliance standards will be implemented:
- **Security**: Implement OAuth 2.0 for authentication, SSL/TLS for encryption, and follow OWASP guidelines for secure coding practices.
- **Scalability**: Design the system to scale horizontally, using containerization (Docker) and orchestration (Kubernetes on GKE).
- **Data Privacy**: Comply with GDPR and CCPA regulations, ensuring user data is protected and handled according to legal requirements.
- **Accessibility**: Follow WCAG 2.1 guidelines to ensure the application is accessible on various devices and for users with disabilities.
- **Quality Assurance**: Implement automated testing (unit, integration, and UI tests) and continuous integration/continuous deployment (CI/CD) pipelines.

#### 3. Standardized Sub-Agent Persona Definitions
The following personas will be involved in the project:
- **Manager**: Oversees the project timeline, budget, and resource allocation. Ensures that the project meets the stakeholders' requirements and is delivered on time.
- **Coder**: Responsible for writing clean, efficient, and well-documented code. Participates in code reviews and ensures that the codebase is scalable and maintainable.
- **Tester**: Designs and executes tests to ensure the application meets the required standards. Reports bugs and works with the development team to resolve issues.
- **Reviewer**: Conducts code reviews, ensuring that the code adheres to the project's standards and best practices. Provides feedback to improve code quality.
- **Docker**: Responsible for containerizing the application, ensuring it is properly packaged and ready for deployment.
- **Deployer**: Manages the deployment of the application to the production environment, ensuring that it is properly configured and running smoothly.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases:
- **Phase 1: Planning and Design (Weeks 1-4)**: Define the project scope, create a detailed design document, and plan the architecture.
- **Phase 2: Backend Development (Weeks 5-12)**: Develop the backend using Quarkus, Kafka, and Postgres. Implement authentication and authorization mechanisms.
- **Phase 3: Mobile App Development (Weeks 13-18)**: Build the mobile app using Next.js, implementing features such as QR code scanning, notification systems, and multi-language support.
- **Phase 4: Testing and Quality Assurance (Weeks 19-22)**: Conduct thorough testing of the application, including unit tests, integration tests, and UI tests. Ensure the application meets the defined quality standards.
- **Phase 5: Deployment and Maintenance (Weeks 23-26)**: Deploy the application to GCP and GKE, configure monitoring and logging, and ensure the application is running smoothly. Plan for future maintenance and updates.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------

            Your output MUST follow this exact Markdown structure for Phase 5:
            ## PHASE 5 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 5 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 5 is to deploy the membership-hub application to Google Cloud Platform (GCP) and Google Kubernetes Engine (GKE), ensuring a smooth and scalable operation. This phase involves configuring monitoring and logging, setting up continuous integration and continuous deployment (CI/CD) pipelines, and planning for future maintenance and updates. The key deliverables include:
- A fully deployed and functional application on GCP and GKE.
- Configured monitoring and logging to ensure the application's performance and health.
- Established CI/CD pipelines for automated testing and deployment.
- A plan for future maintenance, updates, and potential scalability adjustments.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 5 includes:
- Deployment scripts and configurations for GCP and GKE.
- CI/CD pipeline definitions for automated testing and deployment.
- Monitoring and logging configurations using tools like Prometheus, Grafana, and ELK Stack.
- Security configurations to ensure the application's compliance with OWASP guidelines and GDPR/CCPA regulations.
- Directory boundaries:
  - `/deploy`: Contains deployment scripts and configurations.
  - `/ci-cd`: Holds CI/CD pipeline definitions.
  - `/monitoring`: Includes monitoring and logging configurations.
  - `/security`: Contains security configurations and compliance documents.
- Endpoints:
  - `/healthcheck`: For monitoring the application's health.
  - `/metrics`: Exposes application metrics for monitoring.
  - `/logs`: Provides access to application logs.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
- **Coder**: Focus on finalizing deployment scripts, ensuring CI/CD pipelines are correctly configured, and addressing any last-minute code fixes.
- **Tester**: Conduct thorough testing of the deployed application, including performance testing, security testing, and user acceptance testing (UAT).
- **Reviewer**: Review deployment configurations, CI/CD pipelines, and security setups to ensure they meet the project's standards and best practices.
- **Docker**: Ensure the Docker image is properly optimized for deployment on GKE.
- **Deployer (DevOps)**: Manage the deployment process, configure monitoring and logging, and set up CI/CD pipelines.

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 5 includes:
- The application is fully deployed on GCP and GKE.
- Monitoring and logging are configured and functional.
- CI/CD pipelines are set up and automated testing is in place.
- Security configurations are compliant with OWASP guidelines and GDPR/CCPA regulations.
- Performance and security testing have been successfully conducted.
- The application is accessible and functional for both web and mobile interfaces.
- Documentation for deployment, monitoring, and maintenance is updated and available.
- A plan for future maintenance and updates is in place and approved by stakeholders.
```

# Phase 1 STEPS - Prompt:


            Analyze the attached Phase 1 Context Markdown content. 
            Translate every directive, objective, and daily task mentioned inside it into a structured day-by-day JSON map.
            
            --- PHASE 1 CONTEXT MARKDOWN ---
            ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed design document, and plan the architecture for the membership-hub project. This phase will focus on gathering and analyzing requirements, identifying potential technical challenges, and outlining the overall system design. The key deliverables for this phase include:
- A detailed project scope statement
- A high-level system architecture design
- A comprehensive requirements document
- An initial project timeline and resource allocation plan

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
For Phase 1, the technical scope will be limited to the following areas:
- Project scope definition: Defining the project's objectives, deliverables, and key performance indicators (KPIs)
- System architecture design: Outlining the overall system architecture, including the backend, frontend, and database components
- Requirements gathering: Collecting and analyzing the raw requirements for the project, including functional and non-functional requirements
- Directory boundaries:
  - `docs/`: For storing project documentation, including the project scope statement, system architecture design, and requirements document
  - `design/`: For storing design-related files, including wireframes, prototypes, and system architecture diagrams
  - `src/`: For storing source code, including backend, frontend, and database components (initially empty, to be populated in later phases)

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversees the project timeline, budget, and resource allocation. Ensures that the project meets the stakeholders' requirements and is delivered on time.
- **Coder**: Assists in defining the system architecture and outlining the technical requirements for the project. Begins designing the database schema and backend components.
- **Tester**: Reviews the requirements document and begins outlining the testing strategy for the project.
- **Reviewer**: Reviews the project scope statement, system architecture design, and requirements document to ensure they meet the project's standards and best practices.
- **Docker**: Not directly involved in Phase 1, but will be responsible for containerizing the application in later phases.
- **Deployer**: Not directly involved in Phase 1, but will be responsible for deploying the application to the production environment in later phases.

#### 4. Phase Definition of Done (DoD)
The Definition of Done (DoD) for Phase 1 is as follows:
- A detailed project scope statement has been created and approved by stakeholders
- A high-level system architecture design has been outlined and reviewed by the team
- A comprehensive requirements document has been created and reviewed by the team
- An initial project timeline and resource allocation plan have been created and approved by stakeholders
- All documents and designs have been stored in the designated directories (`docs/`, `design/`, etc.)
- The project scope, system architecture, and requirements have been reviewed and approved by the Manager, Coder, Tester, Reviewer, and other relevant stakeholders.
            ------------------------------------------

            Map your response strictly to the requested PhaseStepsPlan JSON structure.
            

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```text
Expecting value: line 1 column 1 (char 0)
```

# Global Prompt:


        Analyze the attached project requirements. Build the GLOBAL PROJECT CONTEXT for 'test-ai-architecture'.
        
        --- RAW REQUIREMENTS ---
        ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

        --- END REQUIREMENTS ---

        Your output MUST follow this exact structure:
        ## GLOBAL PROJECT CONTEXT: test-ai-architecture
        #### 1. Executive Summary & Tech Stack Blueprint
        #### 2. Global Guardrails & Enterprise Compliance Standards
        #### 3. Standardized Sub-Agent Persona Definitions (Manager, Coder, Tester, Reviewer, Docker, Deployer)
        #### 4. Multi-Phase Segmentation Strategy Overview (Plan exactly 5 phases)
        

# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable web and mobile application designed to manage students across multiple centers. The tech stack includes Quarkus, Kafka, Postgres, and Docker, with deployment on GCP and GKE. The application will support internal authentication via email/password, Firebase, Google, and Facebook, as well as QR code-based attendance tracking. The frontend will be built using Next.js, supporting multiple languages and platforms (iOS, Android). The project also includes SEO optimization for both web and mobile applications.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to industry standards, the following guardrails will be implemented:
* Security: Implement OAuth 2.0 for authentication, SSL/TLS encryption for data transmission, and regular security audits.
* Scalability: Design the system to handle increased traffic and user growth, with automated scaling on GCP and GKE.
* Compliance: Adhere to GDPR, CCPA, and other relevant data protection regulations, ensuring user data is handled and stored securely.
* Quality: Establish a continuous integration and delivery (CI/CD) pipeline, with automated testing and code reviews.
* Performance: Monitor and optimize application performance, with a focus on latency, throughput, and user experience.

#### 3. Standardized Sub-Agent Persona Definitions
The following sub-agent personas will be defined to ensure clear roles and responsibilities:
* **Manager**: Oversees project scope, timeline, and budget, ensuring alignment with business objectives.
* **Coder**: Develops the application's backend and frontend, focusing on quality, scalability, and performance.
* **Tester**: Designs and executes tests to ensure the application meets requirements and functions as expected.
* **Reviewer**: Conducts code reviews, providing feedback on quality, security, and best practices.
* **Docker**: Responsible for containerization, ensuring seamless deployment and scaling of the application.
* **Deployer**: Manages the deployment process, ensuring smooth transitions to production and minimizing downtime.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases:
* **Phase 1: Planning and Design** (Weeks 1-4): Define project scope, create a detailed design document, and establish the tech stack.
* **Phase 2: Backend Development** (Weeks 5-12): Develop the backend using Quarkus, Kafka, and Postgres, with a focus on scalability and security.
* **Phase 3: Frontend Development** (Weeks 13-18): Build the frontend using Next.js, with support for multiple languages and platforms.
* **Phase 4: Testing and Quality Assurance** (Weeks 19-22): Conduct thorough testing, including unit tests, integration tests, and user acceptance testing (UAT).
* **Phase 5: Deployment and Maintenance** (Weeks 23-26): Deploy the application to GCP and GKE, with ongoing monitoring, maintenance, and optimization to ensure high performance and user satisfaction.
```

# Phase 1 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 1 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable web and mobile application designed to manage students across multiple centers. The tech stack includes Quarkus, Kafka, Postgres, and Docker, with deployment on GCP and GKE. The application will support internal authentication via email/password, Firebase, Google, and Facebook, as well as QR code-based attendance tracking. The frontend will be built using Next.js, supporting multiple languages and platforms (iOS, Android). The project also includes SEO optimization for both web and mobile applications.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to industry standards, the following guardrails will be implemented:
* Security: Implement OAuth 2.0 for authentication, SSL/TLS encryption for data transmission, and regular security audits.
* Scalability: Design the system to handle increased traffic and user growth, with automated scaling on GCP and GKE.
* Compliance: Adhere to GDPR, CCPA, and other relevant data protection regulations, ensuring user data is handled and stored securely.
* Quality: Establish a continuous integration and delivery (CI/CD) pipeline, with automated testing and code reviews.
* Performance: Monitor and optimize application performance, with a focus on latency, throughput, and user experience.

#### 3. Standardized Sub-Agent Persona Definitions
The following sub-agent personas will be defined to ensure clear roles and responsibilities:
* **Manager**: Oversees project scope, timeline, and budget, ensuring alignment with business objectives.
* **Coder**: Develops the application's backend and frontend, focusing on quality, scalability, and performance.
* **Tester**: Designs and executes tests to ensure the application meets requirements and functions as expected.
* **Reviewer**: Conducts code reviews, providing feedback on quality, security, and best practices.
* **Docker**: Responsible for containerization, ensuring seamless deployment and scaling of the application.
* **Deployer**: Manages the deployment process, ensuring smooth transitions to production and minimizing downtime.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases:
* **Phase 1: Planning and Design** (Weeks 1-4): Define project scope, create a detailed design document, and establish the tech stack.
* **Phase 2: Backend Development** (Weeks 5-12): Develop the backend using Quarkus, Kafka, and Postgres, with a focus on scalability and security.
* **Phase 3: Frontend Development** (Weeks 13-18): Build the frontend using Next.js, with support for multiple languages and platforms.
* **Phase 4: Testing and Quality Assurance** (Weeks 19-22): Conduct thorough testing, including unit tests, integration tests, and user acceptance testing (UAT).
* **Phase 5: Deployment and Maintenance** (Weeks 23-26): Deploy the application to GCP and GKE, with ongoing monitoring, maintenance, and optimization to ensure high performance and user satisfaction.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------

            Your output MUST follow this exact Markdown structure for Phase 1:
            ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed design document, and establish the tech stack for the membership-hub project. This phase will focus on planning and design, ensuring that all stakeholders are aligned and that the project is set up for success. The key deliverables for this phase include:
* A detailed project scope statement
* A comprehensive design document outlining the architecture and components of the system
* A defined tech stack, including tools and technologies for backend, frontend, and infrastructure
* A high-level project timeline and milestones

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 1 includes:
* Defining the project directory structure and organization
* Establishing the backend technology stack, including Quarkus, Kafka, and Postgres
* Defining the frontend technology stack, including Next.js
* Identifying the infrastructure requirements, including Docker, GCP, and GKE
* Establishing the API endpoints and data models for the system
* Defining the database schema and data storage requirements
The following directories and files are in scope for this phase:
* `docs/`: design documents and project scope statement
* `src/`: source code for the project, including backend and frontend components
* `infra/`: infrastructure configuration files, including Docker and GCP configurations
* `api/`: API endpoint definitions and data models

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents have specific tasks and responsibilities during Phase 1:
* **Coder**: Develop a high-level design document, define the tech stack, and establish the project directory structure
* **Tester**: Review the design document and provide feedback on testability and potential issues
* **Reviewer**: Conduct a review of the design document and provide feedback on architecture, scalability, and security
* **Docker**: Establish the Docker configuration and ensure that the application can be containerized
* **Deployer**: Define the deployment process and ensure that the application can be deployed to GCP and GKE

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 1 includes:
* A completed project scope statement
* A comprehensive design document outlining the architecture and components of the system
* A defined tech stack, including tools and technologies for backend, frontend, and infrastructure
* A high-level project timeline and milestones
* A reviewed and approved design document by all stakeholders
* A established project directory structure and organization
* A defined API endpoint and data model
* A established infrastructure configuration, including Docker and GCP configurations
```

# Phase 2 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 2 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable web and mobile application designed to manage students across multiple centers. The tech stack includes Quarkus, Kafka, Postgres, and Docker, with deployment on GCP and GKE. The application will support internal authentication via email/password, Firebase, Google, and Facebook, as well as QR code-based attendance tracking. The frontend will be built using Next.js, supporting multiple languages and platforms (iOS, Android). The project also includes SEO optimization for both web and mobile applications.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to industry standards, the following guardrails will be implemented:
* Security: Implement OAuth 2.0 for authentication, SSL/TLS encryption for data transmission, and regular security audits.
* Scalability: Design the system to handle increased traffic and user growth, with automated scaling on GCP and GKE.
* Compliance: Adhere to GDPR, CCPA, and other relevant data protection regulations, ensuring user data is handled and stored securely.
* Quality: Establish a continuous integration and delivery (CI/CD) pipeline, with automated testing and code reviews.
* Performance: Monitor and optimize application performance, with a focus on latency, throughput, and user experience.

#### 3. Standardized Sub-Agent Persona Definitions
The following sub-agent personas will be defined to ensure clear roles and responsibilities:
* **Manager**: Oversees project scope, timeline, and budget, ensuring alignment with business objectives.
* **Coder**: Develops the application's backend and frontend, focusing on quality, scalability, and performance.
* **Tester**: Designs and executes tests to ensure the application meets requirements and functions as expected.
* **Reviewer**: Conducts code reviews, providing feedback on quality, security, and best practices.
* **Docker**: Responsible for containerization, ensuring seamless deployment and scaling of the application.
* **Deployer**: Manages the deployment process, ensuring smooth transitions to production and minimizing downtime.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases:
* **Phase 1: Planning and Design** (Weeks 1-4): Define project scope, create a detailed design document, and establish the tech stack.
* **Phase 2: Backend Development** (Weeks 5-12): Develop the backend using Quarkus, Kafka, and Postgres, with a focus on scalability and security.
* **Phase 3: Frontend Development** (Weeks 13-18): Build the frontend using Next.js, with support for multiple languages and platforms.
* **Phase 4: Testing and Quality Assurance** (Weeks 19-22): Conduct thorough testing, including unit tests, integration tests, and user acceptance testing (UAT).
* **Phase 5: Deployment and Maintenance** (Weeks 23-26): Deploy the application to GCP and GKE, with ongoing monitoring, maintenance, and optimization to ensure high performance and user satisfaction.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------

            Your output MUST follow this exact Markdown structure for Phase 2:
            ## PHASE 2 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 2 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 2 is to develop the backend of the membership-hub project using Quarkus, Kafka, and Postgres, with a focus on scalability and security. This phase will cover the design and implementation of the backend architecture, including the development of APIs, database schema, and integration with Kafka for messaging. The scope of this phase includes:

* Designing and implementing the backend architecture
* Developing APIs for user management, attendance tracking, and notification systems
* Integrating Kafka for messaging and notification purposes
* Implementing authentication and authorization using OAuth 2.0
* Ensuring scalability and security of the backend system

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope of this phase includes:

* Backend directory: `src/main/java`
* API endpoints: `/api/v1/users`, `/api/v1/attendance`, `/api/v1/notifications`
* Database schema: `membership_hub_db`
* Kafka topics: `attendance_topic`, `notification_topic`
* Authentication and authorization: `oauth2`
* Allowed dependencies: Quarkus, Kafka, Postgres, OAuth 2.0

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in this phase:

* **Coder**: Develop the backend APIs, integrate Kafka, and implement authentication and authorization
* **Tester**: Develop unit tests and integration tests for the backend APIs and Kafka integration
* **Reviewer**: Review the code for quality, security, and best practices
* **DevOps (Docker)**: Containerize the backend application and ensure seamless deployment and scaling
* **DevOps (Deployer)**: Deploy the backend application to GCP and GKE, ensuring smooth transitions to production and minimizing downtime

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 2 includes:

* All backend APIs are developed and tested
* Kafka integration is complete and tested
* Authentication and authorization are implemented and tested
* Backend application is containerized and deployed to GCP and GKE
* All unit tests and integration tests pass
* Code review is complete and all feedback is addressed
* Deployment to production is successful and verified
```

# Phase 3 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 3 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable web and mobile application designed to manage students across multiple centers. The tech stack includes Quarkus, Kafka, Postgres, and Docker, with deployment on GCP and GKE. The application will support internal authentication via email/password, Firebase, Google, and Facebook, as well as QR code-based attendance tracking. The frontend will be built using Next.js, supporting multiple languages and platforms (iOS, Android). The project also includes SEO optimization for both web and mobile applications.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to industry standards, the following guardrails will be implemented:
* Security: Implement OAuth 2.0 for authentication, SSL/TLS encryption for data transmission, and regular security audits.
* Scalability: Design the system to handle increased traffic and user growth, with automated scaling on GCP and GKE.
* Compliance: Adhere to GDPR, CCPA, and other relevant data protection regulations, ensuring user data is handled and stored securely.
* Quality: Establish a continuous integration and delivery (CI/CD) pipeline, with automated testing and code reviews.
* Performance: Monitor and optimize application performance, with a focus on latency, throughput, and user experience.

#### 3. Standardized Sub-Agent Persona Definitions
The following sub-agent personas will be defined to ensure clear roles and responsibilities:
* **Manager**: Oversees project scope, timeline, and budget, ensuring alignment with business objectives.
* **Coder**: Develops the application's backend and frontend, focusing on quality, scalability, and performance.
* **Tester**: Designs and executes tests to ensure the application meets requirements and functions as expected.
* **Reviewer**: Conducts code reviews, providing feedback on quality, security, and best practices.
* **Docker**: Responsible for containerization, ensuring seamless deployment and scaling of the application.
* **Deployer**: Manages the deployment process, ensuring smooth transitions to production and minimizing downtime.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases:
* **Phase 1: Planning and Design** (Weeks 1-4): Define project scope, create a detailed design document, and establish the tech stack.
* **Phase 2: Backend Development** (Weeks 5-12): Develop the backend using Quarkus, Kafka, and Postgres, with a focus on scalability and security.
* **Phase 3: Frontend Development** (Weeks 13-18): Build the frontend using Next.js, with support for multiple languages and platforms.
* **Phase 4: Testing and Quality Assurance** (Weeks 19-22): Conduct thorough testing, including unit tests, integration tests, and user acceptance testing (UAT).
* **Phase 5: Deployment and Maintenance** (Weeks 23-26): Deploy the application to GCP and GKE, with ongoing monitoring, maintenance, and optimization to ensure high performance and user satisfaction.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------

            Your output MUST follow this exact Markdown structure for Phase 3:
            ## PHASE 3 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 3 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 3 is to develop the frontend of the membership-hub application using Next.js, supporting multiple languages and platforms (iOS, Android). This phase will focus on creating a user-friendly and responsive interface for students to interact with the application. The scope of this phase includes:

* Designing and implementing the frontend architecture
* Developing features for student management, including QR code-based attendance tracking and notification systems
* Integrating the frontend with the backend API developed in Phase 2
* Ensuring support for multiple languages and platforms (iOS, Android)

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 3 includes:

* Frontend framework: Next.js
* Programming languages: JavaScript, TypeScript
* Directory boundaries:
	+ `frontend/`: root directory for frontend code
	+ `frontend/pages/`: directory for page components
	+ `frontend/components/`: directory for reusable components
	+ `frontend/api/`: directory for API endpoints
* Endpoints:
	+ `/api/attendance`: endpoint for attendance tracking
	+ `/api/notification`: endpoint for notification systems
* Files:
	+ `frontend/package.json`: file for managing dependencies and scripts
	+ `frontend/next.config.js`: file for configuring Next.js

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 3:

* **Coder**: Responsible for developing the frontend code, including page components, reusable components, and API endpoints.
* **Tester**: Responsible for designing and executing tests for the frontend code, including unit tests, integration tests, and user acceptance testing (UAT).
* **Reviewer**: Responsible for conducting code reviews, providing feedback on quality, security, and best practices.
* **DevOps**: Responsible for ensuring the frontend code is properly containerized and deployed to the production environment.

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 3 includes:

* All frontend code is complete, reviewed, and tested
* The frontend is integrated with the backend API
* The application is deployed to the production environment
* All tests, including unit tests, integration tests, and UAT, have been executed and passed
* The application is functional and meets the requirements outlined in the Raw Requirements Reference
* The code is properly documented and follows best practices for maintainability and scalability.
```

# Phase 4 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 4 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable web and mobile application designed to manage students across multiple centers. The tech stack includes Quarkus, Kafka, Postgres, and Docker, with deployment on GCP and GKE. The application will support internal authentication via email/password, Firebase, Google, and Facebook, as well as QR code-based attendance tracking. The frontend will be built using Next.js, supporting multiple languages and platforms (iOS, Android). The project also includes SEO optimization for both web and mobile applications.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to industry standards, the following guardrails will be implemented:
* Security: Implement OAuth 2.0 for authentication, SSL/TLS encryption for data transmission, and regular security audits.
* Scalability: Design the system to handle increased traffic and user growth, with automated scaling on GCP and GKE.
* Compliance: Adhere to GDPR, CCPA, and other relevant data protection regulations, ensuring user data is handled and stored securely.
* Quality: Establish a continuous integration and delivery (CI/CD) pipeline, with automated testing and code reviews.
* Performance: Monitor and optimize application performance, with a focus on latency, throughput, and user experience.

#### 3. Standardized Sub-Agent Persona Definitions
The following sub-agent personas will be defined to ensure clear roles and responsibilities:
* **Manager**: Oversees project scope, timeline, and budget, ensuring alignment with business objectives.
* **Coder**: Develops the application's backend and frontend, focusing on quality, scalability, and performance.
* **Tester**: Designs and executes tests to ensure the application meets requirements and functions as expected.
* **Reviewer**: Conducts code reviews, providing feedback on quality, security, and best practices.
* **Docker**: Responsible for containerization, ensuring seamless deployment and scaling of the application.
* **Deployer**: Manages the deployment process, ensuring smooth transitions to production and minimizing downtime.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases:
* **Phase 1: Planning and Design** (Weeks 1-4): Define project scope, create a detailed design document, and establish the tech stack.
* **Phase 2: Backend Development** (Weeks 5-12): Develop the backend using Quarkus, Kafka, and Postgres, with a focus on scalability and security.
* **Phase 3: Frontend Development** (Weeks 13-18): Build the frontend using Next.js, with support for multiple languages and platforms.
* **Phase 4: Testing and Quality Assurance** (Weeks 19-22): Conduct thorough testing, including unit tests, integration tests, and user acceptance testing (UAT).
* **Phase 5: Deployment and Maintenance** (Weeks 23-26): Deploy the application to GCP and GKE, with ongoing monitoring, maintenance, and optimization to ensure high performance and user satisfaction.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------

            Your output MUST follow this exact Markdown structure for Phase 4:
            ## PHASE 4 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 4 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
In Phase 4, the primary objective is to conduct thorough testing and quality assurance of the membership-hub project. This phase will ensure that the application meets the required standards, is free from defects, and functions as expected. The scope of this phase includes:
* Unit testing: Testing individual components and units of code to ensure they function correctly.
* Integration testing: Testing how different components interact with each other to ensure seamless integration.
* User Acceptance Testing (UAT): Testing the application from a user's perspective to ensure it meets the requirements and is easy to use.
* Performance testing: Testing the application's performance under various loads to ensure it can handle increased traffic and user growth.
* Security testing: Testing the application's security features to ensure they are effective and protect user data.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 4 includes:
* Testing frameworks: JUnit, TestNG, or other relevant testing frameworks for unit and integration testing.
* Testing tools: Postman, Selenium, or other relevant tools for API and UI testing.
* Test data: Sample data will be created to simulate real-world scenarios and test the application's functionality.
* Directory boundaries:
	+ `src/test/java`: Unit tests and integration tests will be written in this directory.
	+ `src/test/resources`: Test data and configuration files will be stored in this directory.
	+ `src/main/java`: The application's source code will be used for testing.
	+ `src/main/resources`: The application's configuration files and static resources will be used for testing.
* Endpoints:
	+ `/api/v1/users`: Endpoint for user management.
	+ `/api/v1/centers`: Endpoint for center management.
	+ `/api/v1/attendance`: Endpoint for attendance tracking.
	+ `/api/v1/notifications`: Endpoint for notification management.

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 4:
* **Coder**: Will assist in writing unit tests and integration tests, and provide support for testing.
* **Tester**: Will design and execute tests, including unit tests, integration tests, and UAT.
* **Reviewer**: Will review test cases and provide feedback on test coverage and effectiveness.
* **DevOps**: Will assist in setting up the testing environment, including test data and configuration.

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 4 includes:
* All unit tests and integration tests have been written and executed.
* UAT has been completed, and the application meets the required standards.
* Performance testing has been completed, and the application can handle increased traffic and user growth.
* Security testing has been completed, and the application's security features are effective.
* All test cases have been reviewed, and feedback has been incorporated.
* The testing environment has been set up, and test data has been created.
* The application has been tested on multiple platforms, including web and mobile.
* All defects and issues have been resolved, and the application is stable and functional.
```

# Phase 5 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 5 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable web and mobile application designed to manage students across multiple centers. The tech stack includes Quarkus, Kafka, Postgres, and Docker, with deployment on GCP and GKE. The application will support internal authentication via email/password, Firebase, Google, and Facebook, as well as QR code-based attendance tracking. The frontend will be built using Next.js, supporting multiple languages and platforms (iOS, Android). The project also includes SEO optimization for both web and mobile applications.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to industry standards, the following guardrails will be implemented:
* Security: Implement OAuth 2.0 for authentication, SSL/TLS encryption for data transmission, and regular security audits.
* Scalability: Design the system to handle increased traffic and user growth, with automated scaling on GCP and GKE.
* Compliance: Adhere to GDPR, CCPA, and other relevant data protection regulations, ensuring user data is handled and stored securely.
* Quality: Establish a continuous integration and delivery (CI/CD) pipeline, with automated testing and code reviews.
* Performance: Monitor and optimize application performance, with a focus on latency, throughput, and user experience.

#### 3. Standardized Sub-Agent Persona Definitions
The following sub-agent personas will be defined to ensure clear roles and responsibilities:
* **Manager**: Oversees project scope, timeline, and budget, ensuring alignment with business objectives.
* **Coder**: Develops the application's backend and frontend, focusing on quality, scalability, and performance.
* **Tester**: Designs and executes tests to ensure the application meets requirements and functions as expected.
* **Reviewer**: Conducts code reviews, providing feedback on quality, security, and best practices.
* **Docker**: Responsible for containerization, ensuring seamless deployment and scaling of the application.
* **Deployer**: Manages the deployment process, ensuring smooth transitions to production and minimizing downtime.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases:
* **Phase 1: Planning and Design** (Weeks 1-4): Define project scope, create a detailed design document, and establish the tech stack.
* **Phase 2: Backend Development** (Weeks 5-12): Develop the backend using Quarkus, Kafka, and Postgres, with a focus on scalability and security.
* **Phase 3: Frontend Development** (Weeks 13-18): Build the frontend using Next.js, with support for multiple languages and platforms.
* **Phase 4: Testing and Quality Assurance** (Weeks 19-22): Conduct thorough testing, including unit tests, integration tests, and user acceptance testing (UAT).
* **Phase 5: Deployment and Maintenance** (Weeks 23-26): Deploy the application to GCP and GKE, with ongoing monitoring, maintenance, and optimization to ensure high performance and user satisfaction.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------

            Your output MUST follow this exact Markdown structure for Phase 5:
            ## PHASE 5 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 5 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
In Phase 5, the primary objective is to deploy the membership-hub application to Google Cloud Platform (GCP) and Google Kubernetes Engine (GKE), ensuring a seamless and scalable deployment process. The scope of this phase includes:
* Configuring and setting up the production environment on GCP and GKE
* Deploying the Dockerized application to the production environment
* Conducting final testing and quality assurance to ensure the application meets the required standards
* Implementing monitoring, logging, and alerting mechanisms to ensure high performance and user satisfaction
* Ensuring compliance with security, scalability, and compliance guardrails established in earlier phases

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 5 includes:
* Deployment scripts and configuration files for GCP and GKE (e.g., `deployment.yaml`, `cluster.yaml`)
* Docker image configuration and build files (e.g., `Dockerfile`, `docker-compose.yml`)
* Environment-specific configuration files (e.g., `application.properties`, `config.js`)
* Monitoring and logging configuration files (e.g., `prometheus.yml`, `logging.json`)
* API endpoints for deployment, scaling, and management (e.g., `/deploy`, `/scale`, `/healthcheck`)
* Directory boundaries:
	+ `deploy`: contains deployment scripts and configuration files
	+ `docker`: contains Docker image configuration and build files
	+ `config`: contains environment-specific configuration files
	+ `monitoring`: contains monitoring and logging configuration files

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 5:
* **Coder**: Responsible for creating deployment scripts, configuring environment-specific settings, and ensuring the application is properly packaged for deployment
* **Tester**: Conducts final testing and quality assurance to ensure the application meets the required standards
* **Reviewer**: Reviews deployment scripts, configuration files, and environment-specific settings to ensure they meet security, scalability, and compliance requirements
* **Docker**: Responsible for building and configuring Docker images for deployment
* **Deployer**: Manages the deployment process, ensuring smooth transitions to production and minimizing downtime
* **DevOps**: Responsible for setting up and configuring monitoring, logging, and alerting mechanisms

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 5 includes:
* The application is successfully deployed to the production environment on GCP and GKE
* All deployment scripts and configuration files are reviewed and approved
* Final testing and quality assurance are completed, and the application meets the required standards
* Monitoring, logging, and alerting mechanisms are set up and configured
* The application is properly secured, scalable, and compliant with established guardrails
* All sub-agents have completed their tasks and have approved the deployment
* The application is available for use by end-users, and all features are functioning as expected
```

# Phase 1 STEPS - Prompt:


            Analyze the attached Phase 1 Context Markdown content. 
            Translate every directive, objective, and daily task mentioned inside it into a structured day-by-day JSON map.
            
            --- PHASE 1 CONTEXT MARKDOWN ---
            ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed design document, and establish the tech stack for the membership-hub project. This phase will focus on planning and design, ensuring that all stakeholders are aligned and that the project is set up for success. The key deliverables for this phase include:
* A detailed project scope statement
* A comprehensive design document outlining the architecture and components of the system
* A defined tech stack, including tools and technologies for backend, frontend, and infrastructure
* A high-level project timeline and milestones

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 1 includes:
* Defining the project directory structure and organization
* Establishing the backend technology stack, including Quarkus, Kafka, and Postgres
* Defining the frontend technology stack, including Next.js
* Identifying the infrastructure requirements, including Docker, GCP, and GKE
* Establishing the API endpoints and data models for the system
* Defining the database schema and data storage requirements
The following directories and files are in scope for this phase:
* `docs/`: design documents and project scope statement
* `src/`: source code for the project, including backend and frontend components
* `infra/`: infrastructure configuration files, including Docker and GCP configurations
* `api/`: API endpoint definitions and data models

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents have specific tasks and responsibilities during Phase 1:
* **Coder**: Develop a high-level design document, define the tech stack, and establish the project directory structure
* **Tester**: Review the design document and provide feedback on testability and potential issues
* **Reviewer**: Conduct a review of the design document and provide feedback on architecture, scalability, and security
* **Docker**: Establish the Docker configuration and ensure that the application can be containerized
* **Deployer**: Define the deployment process and ensure that the application can be deployed to GCP and GKE

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 1 includes:
* A completed project scope statement
* A comprehensive design document outlining the architecture and components of the system
* A defined tech stack, including tools and technologies for backend, frontend, and infrastructure
* A high-level project timeline and milestones
* A reviewed and approved design document by all stakeholders
* A established project directory structure and organization
* A defined API endpoint and data model
* A established infrastructure configuration, including Docker and GCP configurations
            ------------------------------------------

            Map your response strictly to the requested PhaseStepsPlan JSON structure.
            

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
```json
{
  "phase": "Phase 1",
  "context": "test-ai-architecture",
  "objectives": [
    "Define project scope",
    "Create detailed design document",
    "Establish tech stack for membership-hub project"
  ],
  "deliverables": [
    "Detailed project scope statement",
    "Comprehensive design document",
    "Defined tech stack",
    "High-level project timeline and milestones"
  ],
  "technicalScope": {
    "directoryStructure": "Define project directory structure and organization",
    "backendTechStack": "Quarkus, Kafka, and Postgres",
    "frontendTechStack": "Next.js",
    "infrastructureRequirements": "Docker, GCP, and GKE",
    "apiEndpoints": "Establish API endpoints and data models",
    "databaseSchema": "Define database schema and data storage requirements"
  },
  "directoriesAndFiles": [
    "docs/: design documents and project scope statement",
    "src/: source code for the project",
    "infra/: infrastructure configuration files",
    "api/: API endpoint definitions and data models"
  ],
  "subAgentDirectives": {
    "Coder": [
      "Develop high-level design document",
      "Define tech stack",
      "Establish project directory structure"
    ],
    "Tester": [
      "Review design document",
      "Provide feedback on testability and potential issues"
    ],
    "Reviewer": [
      "Conduct review of design document",
      "Provide feedback on architecture, scalability, and security"
    ],
    "Docker": [
      "Establish Docker configuration",
      "Ensure application can be containerized"
    ],
    "Deployer": [
      "Define deployment process",
      "Ensure application can be deployed to GCP and GKE"
    ]
  },
  "definitionOfDone": [
    "Completed project scope statement",
    "Comprehensive design document",
    "Defined tech stack",
    "High-level project timeline and milestones",
    "Reviewed and approved design document",
    "Established project directory structure and organization",
    "Defined API endpoint and data model",
    "Established infrastructure configuration"
  ],
  "dayByDayPlan": [
    {
      "day": 1,
      "tasks": [
        "Define project scope",
        "Establish project directory structure"
      ],
      "subAgent": "Coder"
    },
    {
      "day": 2,
      "tasks": [
        "Develop high-level design document",
        "Define tech stack"
      ],
      "subAgent": "Coder"
    },
    {
      "day": 3,
      "tasks": [
        "Review design document",
        "Provide feedback on testability and potential issues"
      ],
      "subAgent": "Tester"
    },
    {
      "day": 4,
      "tasks": [
        "Conduct review of design document",
        "Provide feedback on architecture, scalability, and security"
      ],
      "subAgent": "Reviewer"
    },
    {
      "day": 5,
      "tasks": [
        "Establish Docker configuration",
        "Ensure application can be containerized"
      ],
      "subAgent": "Docker"
    },
    {
      "day": 6,
      "tasks": [
        "Define deployment process",
        "Ensure application can be deployed to GCP and GKE"
      ],
      "subAgent": "Deployer"
    },
    {
      "day": 7,
      "tasks": [
        "Review and approve design document",
        "Establish project directory structure and organization"
      ],
      "subAgent": "All"
    }
  ]
}
```
```

# Phase 1 STEPS - Prompt:


            Analyze the attached Phase 1 Context Markdown content. 
            Translate every directive, objective, and daily task mentioned inside it into a structured day-by-day JSON map.
            
            --- PHASE 1 CONTEXT MARKDOWN ---
            ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed design document, and establish the tech stack for the membership-hub project. This phase will focus on planning and design, ensuring that all stakeholders are aligned and that the project is set up for success. The key deliverables for this phase include:
* A detailed project scope statement
* A comprehensive design document outlining the architecture and components of the system
* A defined tech stack, including tools and technologies for backend, frontend, and infrastructure
* A high-level project timeline and milestones

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 1 includes:
* Defining the project directory structure and organization
* Establishing the backend technology stack, including Quarkus, Kafka, and Postgres
* Defining the frontend technology stack, including Next.js
* Identifying the infrastructure requirements, including Docker, GCP, and GKE
* Establishing the API endpoints and data models for the system
* Defining the database schema and data storage requirements
The following directories and files are in scope for this phase:
* `docs/`: design documents and project scope statement
* `src/`: source code for the project, including backend and frontend components
* `infra/`: infrastructure configuration files, including Docker and GCP configurations
* `api/`: API endpoint definitions and data models

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents have specific tasks and responsibilities during Phase 1:
* **Coder**: Develop a high-level design document, define the tech stack, and establish the project directory structure
* **Tester**: Review the design document and provide feedback on testability and potential issues
* **Reviewer**: Conduct a review of the design document and provide feedback on architecture, scalability, and security
* **Docker**: Establish the Docker configuration and ensure that the application can be containerized
* **Deployer**: Define the deployment process and ensure that the application can be deployed to GCP and GKE

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 1 includes:
* A completed project scope statement
* A comprehensive design document outlining the architecture and components of the system
* A defined tech stack, including tools and technologies for backend, frontend, and infrastructure
* A high-level project timeline and milestones
* A reviewed and approved design document by all stakeholders
* A established project directory structure and organization
* A defined API endpoint and data model
* A established infrastructure configuration, including Docker and GCP configurations
            ------------------------------------------

            Map your response strictly to the requested PhaseStepsPlan JSON structure.
            

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```text
cannot access local variable 'out_path' where it is not associated with a value
```

# Global Prompt:


        Analyze the attached project requirements. Build the GLOBAL PROJECT CONTEXT for 'test-ai-architecture'.
        
        --- RAW REQUIREMENTS ---
        ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

        --- END REQUIREMENTS ---

        Your output MUST follow this exact structure:
        ## GLOBAL PROJECT CONTEXT: test-ai-architecture
        #### 1. Executive Summary & Tech Stack Blueprint
        #### 2. Global Guardrails & Enterprise Compliance Standards
        #### 3. Standardized Sub-Agent Persona Definitions (Manager, Coder, Tester, Reviewer, Docker, Deployer)
        #### 4. Multi-Phase Segmentation Strategy Overview (Plan exactly 5 phases)
        

# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable web and mobile application designed to manage students across multiple centers. The tech stack includes Quarkus, Kafka, Postgres, and Docker, with deployment on Google Cloud Platform (GCP) using Google Kubernetes Engine (GKE). The application will support internal authentication via email and password, as well as external authentication through Firebase, Google, and Facebook. The front-end for the mobile app will be built using Next.js, supporting multiple languages and platforms (iOS and Android). Key features include QR code-based attendance tracking, notification systems (SMS, Zalo, and in-app notifications), and SEO optimization for both web and mobile applications.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to best practices, the following global guardrails and compliance standards will be implemented:
- **Security**: Implement OAuth 2.0 for authentication and authorization, ensuring that all data transmitted between the client and server is encrypted (HTTPS).
- **Scalability**: Design the system to scale horizontally, using containerization (Docker) and orchestration (Kubernetes) to manage resources efficiently.
- **Data Privacy**: Comply with GDPR and other relevant data protection regulations, ensuring that user data is handled and stored securely.
- **Accessibility**: Follow WCAG 2.1 guidelines to ensure the application is accessible on various devices and for users with disabilities.
- **Code Quality**: Enforce coding standards, conduct regular code reviews, and use automated testing to maintain high code quality.

#### 3. Standardized Sub-Agent Persona Definitions
The following personas will be involved in the project:
- **Manager**: Oversees the project timeline, budget, and resource allocation. Ensures that the project meets the stakeholders' requirements and is delivered on time.
- **Coder**: Responsible for writing clean, efficient, and well-documented code. Participates in code reviews and contributes to the improvement of the codebase.
- **Tester**: Develops and executes comprehensive test plans to ensure the application meets the required standards. Reports and tracks defects until they are resolved.
- **Reviewer**: Conducts thorough reviews of code, documentation, and other project artifacts to ensure they meet the project's quality and compliance standards.
- **Docker**: Responsible for containerizing the application, ensuring it can be efficiently deployed and managed in a containerized environment.
- **Deployer**: Manages the deployment of the application to the production environment, ensuring that it is properly configured and monitored.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases:
- **Phase 1: Planning and Design** (Weeks 1-4): Define project scope, create detailed designs, and plan the architecture.
- **Phase 2: Backend Development** (Weeks 5-12): Develop the backend using Quarkus, Kafka, and Postgres, focusing on core functionalities such as user management and attendance tracking.
- **Phase 3: Frontend Development** (Weeks 13-18): Build the mobile app frontend using Next.js, implementing features such as QR code scanning, notification handling, and multi-language support.
- **Phase 4: Testing and Quality Assurance** (Weeks 19-22): Conduct thorough testing of the application, including unit testing, integration testing, and user acceptance testing (UAT).
- **Phase 5: Deployment and Maintenance** (Weeks 23-26): Deploy the application to GCP, configure monitoring and logging, and plan for post-launch maintenance and updates.
```

# Phase 1 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 1 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable web and mobile application designed to manage students across multiple centers. The tech stack includes Quarkus, Kafka, Postgres, and Docker, with deployment on Google Cloud Platform (GCP) using Google Kubernetes Engine (GKE). The application will support internal authentication via email and password, as well as external authentication through Firebase, Google, and Facebook. The front-end for the mobile app will be built using Next.js, supporting multiple languages and platforms (iOS and Android). Key features include QR code-based attendance tracking, notification systems (SMS, Zalo, and in-app notifications), and SEO optimization for both web and mobile applications.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to best practices, the following global guardrails and compliance standards will be implemented:
- **Security**: Implement OAuth 2.0 for authentication and authorization, ensuring that all data transmitted between the client and server is encrypted (HTTPS).
- **Scalability**: Design the system to scale horizontally, using containerization (Docker) and orchestration (Kubernetes) to manage resources efficiently.
- **Data Privacy**: Comply with GDPR and other relevant data protection regulations, ensuring that user data is handled and stored securely.
- **Accessibility**: Follow WCAG 2.1 guidelines to ensure the application is accessible on various devices and for users with disabilities.
- **Code Quality**: Enforce coding standards, conduct regular code reviews, and use automated testing to maintain high code quality.

#### 3. Standardized Sub-Agent Persona Definitions
The following personas will be involved in the project:
- **Manager**: Oversees the project timeline, budget, and resource allocation. Ensures that the project meets the stakeholders' requirements and is delivered on time.
- **Coder**: Responsible for writing clean, efficient, and well-documented code. Participates in code reviews and contributes to the improvement of the codebase.
- **Tester**: Develops and executes comprehensive test plans to ensure the application meets the required standards. Reports and tracks defects until they are resolved.
- **Reviewer**: Conducts thorough reviews of code, documentation, and other project artifacts to ensure they meet the project's quality and compliance standards.
- **Docker**: Responsible for containerizing the application, ensuring it can be efficiently deployed and managed in a containerized environment.
- **Deployer**: Manages the deployment of the application to the production environment, ensuring that it is properly configured and monitored.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases:
- **Phase 1: Planning and Design** (Weeks 1-4): Define project scope, create detailed designs, and plan the architecture.
- **Phase 2: Backend Development** (Weeks 5-12): Develop the backend using Quarkus, Kafka, and Postgres, focusing on core functionalities such as user management and attendance tracking.
- **Phase 3: Frontend Development** (Weeks 13-18): Build the mobile app frontend using Next.js, implementing features such as QR code scanning, notification handling, and multi-language support.
- **Phase 4: Testing and Quality Assurance** (Weeks 19-22): Conduct thorough testing of the application, including unit testing, integration testing, and user acceptance testing (UAT).
- **Phase 5: Deployment and Maintenance** (Weeks 23-26): Deploy the application to GCP, configure monitoring and logging, and plan for post-launch maintenance and updates.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------

            Your output MUST follow this exact Markdown structure for Phase 1:
            ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create detailed designs, and plan the architecture for the membership-hub project. This phase will focus on gathering and refining requirements, identifying potential technical debt, and establishing a solid foundation for the subsequent phases. The key deliverables for this phase include:
- A detailed project scope statement
- A high-level architecture design
- A comprehensive requirements document
- A preliminary project schedule and timeline

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
For Phase 1, the technical scope will be limited to the following areas:
- Project scope definition: `docs/project_scope.md`
- Architecture design: `docs/architecture.md`
- Requirements gathering: `docs/requirements.md`
- Project scheduling and timeline: `docs/project_timeline.md`
- Directory structure:
  - `docs/`: Documentation files
  - `design/`: Design files (e.g., diagrams, wireframes)
  - `requirements/`: Requirements documents
- Endpoints:
  - `/project_scope`: Project scope definition
  - `/architecture`: Architecture design
  - `/requirements`: Requirements document
  - `/project_timeline`: Project schedule and timeline

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project timeline, budget, and resource allocation. Ensure that the project meets the stakeholders' requirements and is delivered on time.
- **Coder**: Assist in defining the project scope and architecture design. Participate in requirements gathering and documentation.
- **Tester**: Review the project scope and architecture design for potential testing implications. Identify potential testing requirements and document them.
- **Reviewer**: Conduct a preliminary review of the project scope, architecture design, and requirements document. Provide feedback and suggestions for improvement.
- **Docker**: Not directly involved in Phase 1, but will review the project scope and architecture design to ensure containerization requirements are met.
- **Deployer**: Not directly involved in Phase 1, but will review the project scope and architecture design to ensure deployment requirements are met.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- A detailed project scope statement has been documented and approved by stakeholders.
- A high-level architecture design has been created and reviewed by the team.
- A comprehensive requirements document has been gathered and reviewed by the team.
- A preliminary project schedule and timeline have been established and reviewed by the team.
- All sub-agents have completed their assigned tasks and provided feedback.
- The project scope, architecture design, and requirements document have been reviewed and approved by the Reviewer.
```

# Phase 2 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 2 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable web and mobile application designed to manage students across multiple centers. The tech stack includes Quarkus, Kafka, Postgres, and Docker, with deployment on Google Cloud Platform (GCP) using Google Kubernetes Engine (GKE). The application will support internal authentication via email and password, as well as external authentication through Firebase, Google, and Facebook. The front-end for the mobile app will be built using Next.js, supporting multiple languages and platforms (iOS and Android). Key features include QR code-based attendance tracking, notification systems (SMS, Zalo, and in-app notifications), and SEO optimization for both web and mobile applications.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to best practices, the following global guardrails and compliance standards will be implemented:
- **Security**: Implement OAuth 2.0 for authentication and authorization, ensuring that all data transmitted between the client and server is encrypted (HTTPS).
- **Scalability**: Design the system to scale horizontally, using containerization (Docker) and orchestration (Kubernetes) to manage resources efficiently.
- **Data Privacy**: Comply with GDPR and other relevant data protection regulations, ensuring that user data is handled and stored securely.
- **Accessibility**: Follow WCAG 2.1 guidelines to ensure the application is accessible on various devices and for users with disabilities.
- **Code Quality**: Enforce coding standards, conduct regular code reviews, and use automated testing to maintain high code quality.

#### 3. Standardized Sub-Agent Persona Definitions
The following personas will be involved in the project:
- **Manager**: Oversees the project timeline, budget, and resource allocation. Ensures that the project meets the stakeholders' requirements and is delivered on time.
- **Coder**: Responsible for writing clean, efficient, and well-documented code. Participates in code reviews and contributes to the improvement of the codebase.
- **Tester**: Develops and executes comprehensive test plans to ensure the application meets the required standards. Reports and tracks defects until they are resolved.
- **Reviewer**: Conducts thorough reviews of code, documentation, and other project artifacts to ensure they meet the project's quality and compliance standards.
- **Docker**: Responsible for containerizing the application, ensuring it can be efficiently deployed and managed in a containerized environment.
- **Deployer**: Manages the deployment of the application to the production environment, ensuring that it is properly configured and monitored.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases:
- **Phase 1: Planning and Design** (Weeks 1-4): Define project scope, create detailed designs, and plan the architecture.
- **Phase 2: Backend Development** (Weeks 5-12): Develop the backend using Quarkus, Kafka, and Postgres, focusing on core functionalities such as user management and attendance tracking.
- **Phase 3: Frontend Development** (Weeks 13-18): Build the mobile app frontend using Next.js, implementing features such as QR code scanning, notification handling, and multi-language support.
- **Phase 4: Testing and Quality Assurance** (Weeks 19-22): Conduct thorough testing of the application, including unit testing, integration testing, and user acceptance testing (UAT).
- **Phase 5: Deployment and Maintenance** (Weeks 23-26): Deploy the application to GCP, configure monitoring and logging, and plan for post-launch maintenance and updates.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------

            Your output MUST follow this exact Markdown structure for Phase 2:
            ## PHASE 2 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 2 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 2 is to develop the backend of the membership-hub project using Quarkus, Kafka, and Postgres. This phase will focus on building the core functionalities of the application, including user management, attendance tracking, and notification systems. The scope of this phase includes:

* Designing and implementing the database schema for user management and attendance tracking
* Developing the backend API for user authentication, registration, and profile management
* Integrating Kafka for real-time notification handling
* Building the attendance tracking system with QR code scanning functionality
* Implementing notification systems for SMS, Zalo, and in-app notifications

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
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

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
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

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 2 includes:

* All backend API endpoints are developed and tested
* Kafka integration is complete and functional
* Attendance tracking system with QR code scanning functionality is built and tested
* Notification systems for SMS, Zalo, and in-app notifications are developed and tested
* Backend code is reviewed and meets coding standards
* Docker containerization is configured and deployed to GCP using GKE
* Monitoring and logging are configured for backend code

The phase is considered complete when all the above criteria are met, and the backend code is fully functional and deployable to production.
```

# Phase 3 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 3 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable web and mobile application designed to manage students across multiple centers. The tech stack includes Quarkus, Kafka, Postgres, and Docker, with deployment on Google Cloud Platform (GCP) using Google Kubernetes Engine (GKE). The application will support internal authentication via email and password, as well as external authentication through Firebase, Google, and Facebook. The front-end for the mobile app will be built using Next.js, supporting multiple languages and platforms (iOS and Android). Key features include QR code-based attendance tracking, notification systems (SMS, Zalo, and in-app notifications), and SEO optimization for both web and mobile applications.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to best practices, the following global guardrails and compliance standards will be implemented:
- **Security**: Implement OAuth 2.0 for authentication and authorization, ensuring that all data transmitted between the client and server is encrypted (HTTPS).
- **Scalability**: Design the system to scale horizontally, using containerization (Docker) and orchestration (Kubernetes) to manage resources efficiently.
- **Data Privacy**: Comply with GDPR and other relevant data protection regulations, ensuring that user data is handled and stored securely.
- **Accessibility**: Follow WCAG 2.1 guidelines to ensure the application is accessible on various devices and for users with disabilities.
- **Code Quality**: Enforce coding standards, conduct regular code reviews, and use automated testing to maintain high code quality.

#### 3. Standardized Sub-Agent Persona Definitions
The following personas will be involved in the project:
- **Manager**: Oversees the project timeline, budget, and resource allocation. Ensures that the project meets the stakeholders' requirements and is delivered on time.
- **Coder**: Responsible for writing clean, efficient, and well-documented code. Participates in code reviews and contributes to the improvement of the codebase.
- **Tester**: Develops and executes comprehensive test plans to ensure the application meets the required standards. Reports and tracks defects until they are resolved.
- **Reviewer**: Conducts thorough reviews of code, documentation, and other project artifacts to ensure they meet the project's quality and compliance standards.
- **Docker**: Responsible for containerizing the application, ensuring it can be efficiently deployed and managed in a containerized environment.
- **Deployer**: Manages the deployment of the application to the production environment, ensuring that it is properly configured and monitored.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases:
- **Phase 1: Planning and Design** (Weeks 1-4): Define project scope, create detailed designs, and plan the architecture.
- **Phase 2: Backend Development** (Weeks 5-12): Develop the backend using Quarkus, Kafka, and Postgres, focusing on core functionalities such as user management and attendance tracking.
- **Phase 3: Frontend Development** (Weeks 13-18): Build the mobile app frontend using Next.js, implementing features such as QR code scanning, notification handling, and multi-language support.
- **Phase 4: Testing and Quality Assurance** (Weeks 19-22): Conduct thorough testing of the application, including unit testing, integration testing, and user acceptance testing (UAT).
- **Phase 5: Deployment and Maintenance** (Weeks 23-26): Deploy the application to GCP, configure monitoring and logging, and plan for post-launch maintenance and updates.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------

            Your output MUST follow this exact Markdown structure for Phase 3:
            ## PHASE 3 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 3 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 3 is to develop the frontend of the mobile application using Next.js, focusing on features such as QR code scanning, notification handling, and multi-language support. This phase will ensure that the mobile app provides a seamless user experience for students to manage their attendance and receive notifications. The scope includes designing and implementing the user interface, integrating with the backend APIs, and ensuring the app is optimized for both iOS and Android platforms.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 3 includes:
- Frontend framework: Next.js
- Programming languages: JavaScript, TypeScript
- Directory boundaries:
  - `components`: Reusable UI components
  - `pages`: Application pages (e.g., login, dashboard, attendance)
  - `api`: API endpoints for interacting with the backend
  - `utils`: Utility functions for handling notifications, QR code scanning, etc.
- Endpoints:
  - `/api/login`: Login API endpoint
  - `/api/attendance`: Attendance tracking API endpoint
  - `/api/notifications`: Notification API endpoint

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
- **Coder**:
  - Implement QR code scanning feature using a library like `react-qr-scanner`
  - Develop notification handling system using `react-native-push-notification`
  - Integrate multi-language support using `i18next`
- **Tester**:
  - Develop test cases for QR code scanning feature
  - Test notification handling system on different platforms (iOS, Android)
  - Conduct UI testing for multi-language support
- **Reviewer**:
  - Review code quality and adherence to coding standards
  - Verify that the frontend implementation meets the requirements and design specifications
  - Ensure that the code is well-documented and follows best practices
- **DevOps (Docker and Deployer)**:
  - Configure Dockerfile for building the frontend image
  - Set up deployment scripts for deploying the frontend to GCP

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 3 includes:
- All features and user stories for the frontend are fully implemented and tested
- The mobile app is built and deployed to the app stores (Apple App Store and Google Play Store)
- The app is optimized for both iOS and Android platforms
- All code is reviewed, and feedback is incorporated
- Automated tests are written and passing for all features
- The app is deployed to GCP, and monitoring is set up
- Documentation is updated to reflect the changes made during this phase
```

# Phase 4 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 4 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable web and mobile application designed to manage students across multiple centers. The tech stack includes Quarkus, Kafka, Postgres, and Docker, with deployment on Google Cloud Platform (GCP) using Google Kubernetes Engine (GKE). The application will support internal authentication via email and password, as well as external authentication through Firebase, Google, and Facebook. The front-end for the mobile app will be built using Next.js, supporting multiple languages and platforms (iOS and Android). Key features include QR code-based attendance tracking, notification systems (SMS, Zalo, and in-app notifications), and SEO optimization for both web and mobile applications.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to best practices, the following global guardrails and compliance standards will be implemented:
- **Security**: Implement OAuth 2.0 for authentication and authorization, ensuring that all data transmitted between the client and server is encrypted (HTTPS).
- **Scalability**: Design the system to scale horizontally, using containerization (Docker) and orchestration (Kubernetes) to manage resources efficiently.
- **Data Privacy**: Comply with GDPR and other relevant data protection regulations, ensuring that user data is handled and stored securely.
- **Accessibility**: Follow WCAG 2.1 guidelines to ensure the application is accessible on various devices and for users with disabilities.
- **Code Quality**: Enforce coding standards, conduct regular code reviews, and use automated testing to maintain high code quality.

#### 3. Standardized Sub-Agent Persona Definitions
The following personas will be involved in the project:
- **Manager**: Oversees the project timeline, budget, and resource allocation. Ensures that the project meets the stakeholders' requirements and is delivered on time.
- **Coder**: Responsible for writing clean, efficient, and well-documented code. Participates in code reviews and contributes to the improvement of the codebase.
- **Tester**: Develops and executes comprehensive test plans to ensure the application meets the required standards. Reports and tracks defects until they are resolved.
- **Reviewer**: Conducts thorough reviews of code, documentation, and other project artifacts to ensure they meet the project's quality and compliance standards.
- **Docker**: Responsible for containerizing the application, ensuring it can be efficiently deployed and managed in a containerized environment.
- **Deployer**: Manages the deployment of the application to the production environment, ensuring that it is properly configured and monitored.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases:
- **Phase 1: Planning and Design** (Weeks 1-4): Define project scope, create detailed designs, and plan the architecture.
- **Phase 2: Backend Development** (Weeks 5-12): Develop the backend using Quarkus, Kafka, and Postgres, focusing on core functionalities such as user management and attendance tracking.
- **Phase 3: Frontend Development** (Weeks 13-18): Build the mobile app frontend using Next.js, implementing features such as QR code scanning, notification handling, and multi-language support.
- **Phase 4: Testing and Quality Assurance** (Weeks 19-22): Conduct thorough testing of the application, including unit testing, integration testing, and user acceptance testing (UAT).
- **Phase 5: Deployment and Maintenance** (Weeks 23-26): Deploy the application to GCP, configure monitoring and logging, and plan for post-launch maintenance and updates.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------

            Your output MUST follow this exact Markdown structure for Phase 4:
            ## PHASE 4 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 4 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
In Phase 4, the primary objective is to conduct thorough testing and quality assurance of the membership-hub application. This phase will ensure that the application meets the required standards, is free of defects, and provides a seamless user experience. The scope of this phase includes:
- Unit testing of individual components
- Integration testing of interconnected components
- User acceptance testing (UAT) to validate the application's functionality and usability
- Performance testing to ensure the application's scalability and efficiency
- Security testing to identify and address potential vulnerabilities

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 4 includes:
- Testing frameworks such as JUnit, TestNG, or Jest for unit testing
- Integration testing tools like Postman or Apache JMeter
- UAT testing using manual testing techniques or automated tools like Selenium
- Performance testing using tools like Apache JMeter, Gatling, or Locust
- Security testing using tools like OWASP ZAP, Burp Suite, or SQLMap
- Directory boundaries:
  - `src/test/java` for unit tests
  - `src/test/integration` for integration tests
  - `src/test/uat` for UAT tests
  - `src/test/performance` for performance tests
  - `src/test/security` for security tests
- Endpoints:
  - `/api/v1/users` for user management
  - `/api/v1/attendance` for attendance tracking
  - `/api/v1/notifications` for notification handling

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
- **Coder**: Develop unit tests for individual components, ensure code coverage, and address any defects found during testing
- **Tester**: Develop and execute integration tests, UAT tests, performance tests, and security tests; report and track defects until they are resolved
- **Reviewer**: Conduct code reviews of test code, ensure testing standards are met, and provide feedback to the Coder
- **DevOps**: Configure and manage the testing environment, ensure continuous integration and continuous deployment (CI/CD) pipelines are working correctly, and provide support for testing infrastructure

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 4 includes:
- All unit tests, integration tests, UAT tests, performance tests, and security tests have been executed and passed
- All defects found during testing have been resolved and re-tested
- Code coverage meets the required standards (e.g., 80%)
- Testing infrastructure is properly configured and functioning correctly
- All test results have been documented and reviewed by the team
- The application has been certified as ready for deployment to the production environment
```

# Phase 5 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 5 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable web and mobile application designed to manage students across multiple centers. The tech stack includes Quarkus, Kafka, Postgres, and Docker, with deployment on Google Cloud Platform (GCP) using Google Kubernetes Engine (GKE). The application will support internal authentication via email and password, as well as external authentication through Firebase, Google, and Facebook. The front-end for the mobile app will be built using Next.js, supporting multiple languages and platforms (iOS and Android). Key features include QR code-based attendance tracking, notification systems (SMS, Zalo, and in-app notifications), and SEO optimization for both web and mobile applications.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to best practices, the following global guardrails and compliance standards will be implemented:
- **Security**: Implement OAuth 2.0 for authentication and authorization, ensuring that all data transmitted between the client and server is encrypted (HTTPS).
- **Scalability**: Design the system to scale horizontally, using containerization (Docker) and orchestration (Kubernetes) to manage resources efficiently.
- **Data Privacy**: Comply with GDPR and other relevant data protection regulations, ensuring that user data is handled and stored securely.
- **Accessibility**: Follow WCAG 2.1 guidelines to ensure the application is accessible on various devices and for users with disabilities.
- **Code Quality**: Enforce coding standards, conduct regular code reviews, and use automated testing to maintain high code quality.

#### 3. Standardized Sub-Agent Persona Definitions
The following personas will be involved in the project:
- **Manager**: Oversees the project timeline, budget, and resource allocation. Ensures that the project meets the stakeholders' requirements and is delivered on time.
- **Coder**: Responsible for writing clean, efficient, and well-documented code. Participates in code reviews and contributes to the improvement of the codebase.
- **Tester**: Develops and executes comprehensive test plans to ensure the application meets the required standards. Reports and tracks defects until they are resolved.
- **Reviewer**: Conducts thorough reviews of code, documentation, and other project artifacts to ensure they meet the project's quality and compliance standards.
- **Docker**: Responsible for containerizing the application, ensuring it can be efficiently deployed and managed in a containerized environment.
- **Deployer**: Manages the deployment of the application to the production environment, ensuring that it is properly configured and monitored.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases:
- **Phase 1: Planning and Design** (Weeks 1-4): Define project scope, create detailed designs, and plan the architecture.
- **Phase 2: Backend Development** (Weeks 5-12): Develop the backend using Quarkus, Kafka, and Postgres, focusing on core functionalities such as user management and attendance tracking.
- **Phase 3: Frontend Development** (Weeks 13-18): Build the mobile app frontend using Next.js, implementing features such as QR code scanning, notification handling, and multi-language support.
- **Phase 4: Testing and Quality Assurance** (Weeks 19-22): Conduct thorough testing of the application, including unit testing, integration testing, and user acceptance testing (UAT).
- **Phase 5: Deployment and Maintenance** (Weeks 23-26): Deploy the application to GCP, configure monitoring and logging, and plan for post-launch maintenance and updates.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------

            Your output MUST follow this exact Markdown structure for Phase 5:
            ## PHASE 5 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 5 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 5 is to deploy the membership-hub application to the Google Cloud Platform (GCP) using Google Kubernetes Engine (GKE), ensuring a scalable, secure, and highly available environment. This phase will also focus on configuring monitoring and logging, as well as planning for post-launch maintenance and updates. The key deliverables include:
- Deployment of the application to GCP using GKE
- Configuration of monitoring and logging tools
- Setup of security measures, including OAuth 2.0 and HTTPS
- Planning for post-launch maintenance, updates, and potential scalability adjustments

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 5 includes:
- Deployment scripts and configurations for GKE
- Monitoring and logging tools, such as Google Cloud Logging and Monitoring
- Security configurations, including OAuth 2.0 and HTTPS settings
- Directory boundaries:
  - `/deploy`: contains deployment scripts and configurations
  - `/monitoring`: contains monitoring and logging configurations
  - `/security`: contains security configurations, including OAuth 2.0 and HTTPS settings
- Endpoints:
  - `/api/deploy`: endpoint for deploying the application to GCP
  - `/api/monitoring`: endpoint for monitoring and logging
  - `/api/security`: endpoint for security configurations

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
- **Coder**: Focus on writing deployment scripts, configuring monitoring and logging tools, and implementing security measures.
- **Tester**: Conduct thorough testing of the deployment process, monitoring and logging configurations, and security settings.
- **Reviewer**: Review deployment scripts, monitoring and logging configurations, and security settings to ensure they meet the project's quality and compliance standards.
- **DevOps (Deployer)**: Responsible for deploying the application to GCP, configuring monitoring and logging tools, and setting up security measures.
- **Docker**: Ensure the application is properly containerized and can be efficiently deployed to GKE.

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 5 includes:
- The application is successfully deployed to GCP using GKE.
- Monitoring and logging tools are configured and functioning correctly.
- Security measures, including OAuth 2.0 and HTTPS, are implemented and tested.
- Post-launch maintenance and update plans are in place.
- All deployment scripts, configurations, and security settings are reviewed and approved by the Reviewer.
- The application is thoroughly tested by the Tester, and all defects are resolved.
- The DevOps team has verified the deployment and configuration of the application.
```

# Phase 1 STEPS - Prompt:


            Analyze the attached Phase 1 Context Markdown content. 
            Translate every directive, objective, and daily task mentioned inside it into a structured day-by-day JSON map.
            
            --- PHASE 1 CONTEXT MARKDOWN ---
            ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create detailed designs, and plan the architecture for the membership-hub project. This phase will focus on gathering and refining requirements, identifying potential technical debt, and establishing a solid foundation for the subsequent phases. The key deliverables for this phase include:
- A detailed project scope statement
- A high-level architecture design
- A comprehensive requirements document
- A preliminary project schedule and timeline

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
For Phase 1, the technical scope will be limited to the following areas:
- Project scope definition: `docs/project_scope.md`
- Architecture design: `docs/architecture.md`
- Requirements gathering: `docs/requirements.md`
- Project scheduling and timeline: `docs/project_timeline.md`
- Directory structure:
  - `docs/`: Documentation files
  - `design/`: Design files (e.g., diagrams, wireframes)
  - `requirements/`: Requirements documents
- Endpoints:
  - `/project_scope`: Project scope definition
  - `/architecture`: Architecture design
  - `/requirements`: Requirements document
  - `/project_timeline`: Project schedule and timeline

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversee the project timeline, budget, and resource allocation. Ensure that the project meets the stakeholders' requirements and is delivered on time.
- **Coder**: Assist in defining the project scope and architecture design. Participate in requirements gathering and documentation.
- **Tester**: Review the project scope and architecture design for potential testing implications. Identify potential testing requirements and document them.
- **Reviewer**: Conduct a preliminary review of the project scope, architecture design, and requirements document. Provide feedback and suggestions for improvement.
- **Docker**: Not directly involved in Phase 1, but will review the project scope and architecture design to ensure containerization requirements are met.
- **Deployer**: Not directly involved in Phase 1, but will review the project scope and architecture design to ensure deployment requirements are met.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- A detailed project scope statement has been documented and approved by stakeholders.
- A high-level architecture design has been created and reviewed by the team.
- A comprehensive requirements document has been gathered and reviewed by the team.
- A preliminary project schedule and timeline have been established and reviewed by the team.
- All sub-agents have completed their assigned tasks and provided feedback.
- The project scope, architecture design, and requirements document have been reviewed and approved by the Reviewer.
            ------------------------------------------

            Map your response strictly to the requested PhaseStepsPlan JSON structure.
            

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
```json
{
  "phase": "Phase 1",
  "context": "test-ai-architecture",
  "objectives": [
    "Define project scope",
    "Create detailed designs",
    "Plan architecture for membership-hub project"
  ],
  "deliverables": [
    "Detailed project scope statement",
    "High-level architecture design",
    "Comprehensive requirements document",
    "Preliminary project schedule and timeline"
  ],
  "technicalScope": {
    "directories": [
      "docs/",
      "design/",
      "requirements/"
    ],
    "endpoints": [
      "/project_scope",
      "/architecture",
      "/requirements",
      "/project_timeline"
    ],
    "files": [
      "docs/project_scope.md",
      "docs/architecture.md",
      "docs/requirements.md",
      "docs/project_timeline.md"
    ]
  },
  "subAgents": [
    {
      "name": "Manager",
      "tasks": [
        "Oversee project timeline",
        "Oversee budget and resource allocation",
        "Ensure project meets stakeholders' requirements"
      ]
    },
    {
      "name": "Coder",
      "tasks": [
        "Assist in defining project scope",
        "Assist in architecture design",
        "Participate in requirements gathering and documentation"
      ]
    },
    {
      "name": "Tester",
      "tasks": [
        "Review project scope and architecture design for testing implications",
        "Identify potential testing requirements and document them"
      ]
    },
    {
      "name": "Reviewer",
      "tasks": [
        "Conduct preliminary review of project scope, architecture design, and requirements document",
        "Provide feedback and suggestions for improvement"
      ]
    },
    {
      "name": "Docker",
      "tasks": [
        "Review project scope and architecture design for containerization requirements"
      ]
    },
    {
      "name": "Deployer",
      "tasks": [
        "Review project scope and architecture design for deployment requirements"
      ]
    }
  ],
  "definitionOfDone": [
    "Detailed project scope statement documented and approved",
    "High-level architecture design created and reviewed",
    "Comprehensive requirements document gathered and reviewed",
    "Preliminary project schedule and timeline established and reviewed",
    "All sub-agents have completed assigned tasks and provided feedback",
    "Project scope, architecture design, and requirements document reviewed and approved by Reviewer"
  ],
  "phaseStepsPlan": [
    {
      "day": 1,
      "tasks": [
        {
          "subAgent": "Manager",
          "task": "Oversee project timeline"
        },
        {
          "subAgent": "Coder",
          "task": "Assist in defining project scope"
        }
      ]
    },
    {
      "day": 2,
      "tasks": [
        {
          "subAgent": "Coder",
          "task": "Assist in architecture design"
        },
        {
          "subAgent": "Tester",
          "task": "Review project scope and architecture design for testing implications"
        }
      ]
    },
    {
      "day": 3,
      "tasks": [
        {
          "subAgent": "Reviewer",
          "task": "Conduct preliminary review of project scope, architecture design, and requirements document"
        },
        {
          "subAgent": "Docker",
          "task": "Review project scope and architecture design for containerization requirements"
        }
      ]
    },
    {
      "day": 4,
      "tasks": [
        {
          "subAgent": "Deployer",
          "task": "Review project scope and architecture design for deployment requirements"
        },
        {
          "subAgent": "Manager",
          "task": "Oversee budget and resource allocation"
        }
      ]
    },
    {
      "day": 5,
      "tasks": [
        {
          "subAgent": "Coder",
          "task": "Participate in requirements gathering and documentation"
        },
        {
          "subAgent": "Tester",
          "task": "Identify potential testing requirements and document them"
        }
      ]
    }
  ]
}
```
```

# Phase 2 STEPS - Prompt:


            Analyze the attached Phase 2 Context Markdown content. 
            Translate every directive, objective, and daily task mentioned inside it into a structured day-by-day JSON map.
            
            --- PHASE 2 CONTEXT MARKDOWN ---
            ## PHASE 2 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 2 is to develop the backend of the membership-hub project using Quarkus, Kafka, and Postgres. This phase will focus on building the core functionalities of the application, including user management, attendance tracking, and notification systems. The scope of this phase includes:

* Designing and implementing the database schema for user management and attendance tracking
* Developing the backend API for user authentication, registration, and profile management
* Integrating Kafka for real-time notification handling
* Building the attendance tracking system with QR code scanning functionality
* Implementing notification systems for SMS, Zalo, and in-app notifications

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
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

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
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

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 2 includes:

* All backend API endpoints are developed and tested
* Kafka integration is complete and functional
* Attendance tracking system with QR code scanning functionality is built and tested
* Notification systems for SMS, Zalo, and in-app notifications are developed and tested
* Backend code is reviewed and meets coding standards
* Docker containerization is configured and deployed to GCP using GKE
* Monitoring and logging are configured for backend code

The phase is considered complete when all the above criteria are met, and the backend code is fully functional and deployable to production.
            ------------------------------------------

            Map your response strictly to the requested PhaseStepsPlan JSON structure.
            

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
```json
{
  "phase": "Phase 2",
  "context": "test-ai-architecture",
  "objectives": [
    "Develop the backend of the membership-hub project using Quarkus, Kafka, and Postgres",
    "Build the core functionalities of the application, including user management, attendance tracking, and notification systems"
  ],
  "scope": [
    "Designing and implementing the database schema for user management and attendance tracking",
    "Developing the backend API for user authentication, registration, and profile management",
    "Integrating Kafka for real-time notification handling",
    "Building the attendance tracking system with QR code scanning functionality",
    "Implementing notification systems for SMS, Zalo, and in-app notifications"
  ],
  "technicalScope": [
    "Backend development using Quarkus, Kafka, and Postgres",
    "Containerization using Docker",
    "API endpoint development for user management and attendance tracking",
    "Integration with Firebase, Google, and Facebook for external authentication",
    "Development of notification systems using Kafka"
  ],
  "directoryBoundaries": {
    "src/main/java": "Quarkus backend code",
    "src/main/resources": "Database schema and configuration files",
    "src/test/java": "Unit tests and integration tests for backend code",
    "docker": "Dockerfile and containerization configuration",
    "kafka": "Kafka configuration and notification handling code"
  },
  "endpoints": [
    {
      "endpoint": "/api/v1/users",
      "description": "User management API endpoints"
    },
    {
      "endpoint": "/api/v1/attendance",
      "description": "Attendance tracking API endpoints"
    },
    {
      "endpoint": "/api/v1/notifications",
      "description": "Notification systems API endpoints"
    }
  ],
  "subAgentFunctionalDirectives": {
    "Coder": [
      "Develop the backend API for user management and attendance tracking",
      "Implement Kafka integration for real-time notification handling",
      "Build the attendance tracking system with QR code scanning functionality"
    ],
    "Tester": [
      "Develop unit tests and integration tests for backend code",
      "Test API endpoints for user management and attendance tracking",
      "Test notification systems for SMS, Zalo, and in-app notifications"
    ],
    "Reviewer": [
      "Review backend code for quality and compliance with coding standards",
      "Review database schema and configuration files",
      "Review API endpoint documentation and testing coverage"
    ],
    "DevOps": [
      "Configure Docker containerization for backend code",
      "Deploy backend code to GCP using GKE",
      "Configure monitoring and logging for backend code"
    ]
  },
  "definitionOfDone": [
    "All backend API endpoints are developed and tested",
    "Kafka integration is complete and functional",
    "Attendance tracking system with QR code scanning functionality is built and tested",
    "Notification systems for SMS, Zalo, and in-app notifications are developed and tested",
    "Backend code is reviewed and meets coding standards",
    "Docker containerization is configured and deployed to GCP using GKE",
    "Monitoring and logging are configured for backend code"
  ],
  "dayByDayPlan": [
    {
      "day": 1,
      "tasks": [
        "Design database schema for user management and attendance tracking",
        "Develop backend API for user authentication and registration"
      ]
    },
    {
      "day": 2,
      "tasks": [
        "Implement Kafka integration for real-time notification handling",
        "Develop unit tests for backend code"
      ]
    },
    {
      "day": 3,
      "tasks": [
        "Build attendance tracking system with QR code scanning functionality",
        "Test API endpoints for user management and attendance tracking"
      ]
    },
    {
      "day": 4,
      "tasks": [
        "Develop notification systems for SMS, Zalo, and in-app notifications",
        "Review backend code for quality and compliance with coding standards"
      ]
    },
    {
      "day": 5,
      "tasks": [
        "Configure Docker containerization for backend code",
        "Deploy backend code to GCP using GKE"
      ]
    },
    {
      "day": 6,
      "tasks": [
        "Configure monitoring and logging for backend code",
        "Test notification systems for SMS, Zalo, and in-app notifications"
      ]
    },
    {
      "day": 7,
      "tasks": [
        "Review API endpoint documentation and testing coverage",
        "Finalize backend code and prepare for deployment"
      ]
    }
  ]
}
```
```

# Phase 3 STEPS - Prompt:


            Analyze the attached Phase 3 Context Markdown content. 
            Translate every directive, objective, and daily task mentioned inside it into a structured day-by-day JSON map.
            
            --- PHASE 3 CONTEXT MARKDOWN ---
            ## PHASE 3 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 3 is to develop the frontend of the mobile application using Next.js, focusing on features such as QR code scanning, notification handling, and multi-language support. This phase will ensure that the mobile app provides a seamless user experience for students to manage their attendance and receive notifications. The scope includes designing and implementing the user interface, integrating with the backend APIs, and ensuring the app is optimized for both iOS and Android platforms.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 3 includes:
- Frontend framework: Next.js
- Programming languages: JavaScript, TypeScript
- Directory boundaries:
  - `components`: Reusable UI components
  - `pages`: Application pages (e.g., login, dashboard, attendance)
  - `api`: API endpoints for interacting with the backend
  - `utils`: Utility functions for handling notifications, QR code scanning, etc.
- Endpoints:
  - `/api/login`: Login API endpoint
  - `/api/attendance`: Attendance tracking API endpoint
  - `/api/notifications`: Notification API endpoint

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
- **Coder**:
  - Implement QR code scanning feature using a library like `react-qr-scanner`
  - Develop notification handling system using `react-native-push-notification`
  - Integrate multi-language support using `i18next`
- **Tester**:
  - Develop test cases for QR code scanning feature
  - Test notification handling system on different platforms (iOS, Android)
  - Conduct UI testing for multi-language support
- **Reviewer**:
  - Review code quality and adherence to coding standards
  - Verify that the frontend implementation meets the requirements and design specifications
  - Ensure that the code is well-documented and follows best practices
- **DevOps (Docker and Deployer)**:
  - Configure Dockerfile for building the frontend image
  - Set up deployment scripts for deploying the frontend to GCP

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 3 includes:
- All features and user stories for the frontend are fully implemented and tested
- The mobile app is built and deployed to the app stores (Apple App Store and Google Play Store)
- The app is optimized for both iOS and Android platforms
- All code is reviewed, and feedback is incorporated
- Automated tests are written and passing for all features
- The app is deployed to GCP, and monitoring is set up
- Documentation is updated to reflect the changes made during this phase
            ------------------------------------------

            Map your response strictly to the requested PhaseStepsPlan JSON structure.
            

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
```json
{
  "phase": "Phase 3",
  "context": "test-ai-architecture",
  "objectives": [
    "Develop the frontend of the mobile application using Next.js",
    "Implement features such as QR code scanning, notification handling, and multi-language support",
    "Ensure a seamless user experience for students to manage their attendance and receive notifications"
  ],
  "scope": [
    "Designing and implementing the user interface",
    "Integrating with the backend APIs",
    "Optimizing the app for both iOS and Android platforms"
  ],
  "technicalScope": {
    "frontendFramework": "Next.js",
    "programmingLanguages": ["JavaScript", "TypeScript"],
    "directoryBoundaries": {
      "components": "Reusable UI components",
      "pages": "Application pages (e.g., login, dashboard, attendance)",
      "api": "API endpoints for interacting with the backend",
      "utils": "Utility functions for handling notifications, QR code scanning, etc."
    },
    "endpoints": [
      { "endpoint": "/api/login", "description": "Login API endpoint" },
      { "endpoint": "/api/attendance", "description": "Attendance tracking API endpoint" },
      { "endpoint": "/api/notifications", "description": "Notification API endpoint" }
    ]
  },
  "subAgentFunctionalDirectives": {
    "Coder": [
      "Implement QR code scanning feature using a library like react-qr-scanner",
      "Develop notification handling system using react-native-push-notification",
      "Integrate multi-language support using i18next"
    ],
    "Tester": [
      "Develop test cases for QR code scanning feature",
      "Test notification handling system on different platforms (iOS, Android)",
      "Conduct UI testing for multi-language support"
    ],
    "Reviewer": [
      "Review code quality and adherence to coding standards",
      "Verify that the frontend implementation meets the requirements and design specifications",
      "Ensure that the code is well-documented and follows best practices"
    ],
    "DevOps (Docker and Deployer)": [
      "Configure Dockerfile for building the frontend image",
      "Set up deployment scripts for deploying the frontend to GCP"
    ]
  },
  "definitionOfDone": [
    "All features and user stories for the frontend are fully implemented and tested",
    "The mobile app is built and deployed to the app stores (Apple App Store and Google Play Store)",
    "The app is optimized for both iOS and Android platforms",
    "All code is reviewed, and feedback is incorporated",
    "Automated tests are written and passing for all features",
    "The app is deployed to GCP, and monitoring is set up",
    "Documentation is updated to reflect the changes made during this phase"
  ],
  "dayByDayPlan": [
    {
      "day": 1,
      "tasks": [
        "Implement QR code scanning feature using a library like react-qr-scanner (Coder)",
        "Develop test cases for QR code scanning feature (Tester)"
      ]
    },
    {
      "day": 2,
      "tasks": [
        "Develop notification handling system using react-native-push-notification (Coder)",
        "Test notification handling system on different platforms (iOS, Android) (Tester)"
      ]
    },
    {
      "day": 3,
      "tasks": [
        "Integrate multi-language support using i18next (Coder)",
        "Conduct UI testing for multi-language support (Tester)"
      ]
    },
    {
      "day": 4,
      "tasks": [
        "Review code quality and adherence to coding standards (Reviewer)",
        "Verify that the frontend implementation meets the requirements and design specifications (Reviewer)"
      ]
    },
    {
      "day": 5,
      "tasks": [
        "Configure Dockerfile for building the frontend image (DevOps)",
        "Set up deployment scripts for deploying the frontend to GCP (DevOps)"
      ]
    },
    {
      "day": 6,
      "tasks": [
        "Deploy the mobile app to the app stores (Apple App Store and Google Play Store)",
        "Optimize the app for both iOS and Android platforms"
      ]
    },
    {
      "day": 7,
      "tasks": [
        "Incorporate feedback and review code (Coder)",
        "Update documentation to reflect the changes made during this phase"
      ]
    }
  ]
}
```
```

# Phase 4 STEPS - Prompt:


            Analyze the attached Phase 4 Context Markdown content. 
            Translate every directive, objective, and daily task mentioned inside it into a structured day-by-day JSON map.
            
            --- PHASE 4 CONTEXT MARKDOWN ---
            ## PHASE 4 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
In Phase 4, the primary objective is to conduct thorough testing and quality assurance of the membership-hub application. This phase will ensure that the application meets the required standards, is free of defects, and provides a seamless user experience. The scope of this phase includes:
- Unit testing of individual components
- Integration testing of interconnected components
- User acceptance testing (UAT) to validate the application's functionality and usability
- Performance testing to ensure the application's scalability and efficiency
- Security testing to identify and address potential vulnerabilities

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 4 includes:
- Testing frameworks such as JUnit, TestNG, or Jest for unit testing
- Integration testing tools like Postman or Apache JMeter
- UAT testing using manual testing techniques or automated tools like Selenium
- Performance testing using tools like Apache JMeter, Gatling, or Locust
- Security testing using tools like OWASP ZAP, Burp Suite, or SQLMap
- Directory boundaries:
  - `src/test/java` for unit tests
  - `src/test/integration` for integration tests
  - `src/test/uat` for UAT tests
  - `src/test/performance` for performance tests
  - `src/test/security` for security tests
- Endpoints:
  - `/api/v1/users` for user management
  - `/api/v1/attendance` for attendance tracking
  - `/api/v1/notifications` for notification handling

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
- **Coder**: Develop unit tests for individual components, ensure code coverage, and address any defects found during testing
- **Tester**: Develop and execute integration tests, UAT tests, performance tests, and security tests; report and track defects until they are resolved
- **Reviewer**: Conduct code reviews of test code, ensure testing standards are met, and provide feedback to the Coder
- **DevOps**: Configure and manage the testing environment, ensure continuous integration and continuous deployment (CI/CD) pipelines are working correctly, and provide support for testing infrastructure

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 4 includes:
- All unit tests, integration tests, UAT tests, performance tests, and security tests have been executed and passed
- All defects found during testing have been resolved and re-tested
- Code coverage meets the required standards (e.g., 80%)
- Testing infrastructure is properly configured and functioning correctly
- All test results have been documented and reviewed by the team
- The application has been certified as ready for deployment to the production environment
            ------------------------------------------

            Map your response strictly to the requested PhaseStepsPlan JSON structure.
            

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
```json
{
  "phase": "Phase 4",
  "context": "test-ai-architecture",
  "objectives": [
    "Conduct thorough testing and quality assurance of the membership-hub application",
    "Ensure the application meets the required standards, is free of defects, and provides a seamless user experience"
  ],
  "scope": [
    "Unit testing of individual components",
    "Integration testing of interconnected components",
    "User acceptance testing (UAT) to validate the application's functionality and usability",
    "Performance testing to ensure the application's scalability and efficiency",
    "Security testing to identify and address potential vulnerabilities"
  ],
  "technicalScope": {
    "testingFrameworks": [
      "JUnit",
      "TestNG",
      "Jest"
    ],
    "integrationTestingTools": [
      "Postman",
      "Apache JMeter"
    ],
    "uatTestingTools": [
      "Manual testing techniques",
      "Selenium"
    ],
    "performanceTestingTools": [
      "Apache JMeter",
      "Gatling",
      "Locust"
    ],
    "securityTestingTools": [
      "OWASP ZAP",
      "Burp Suite",
      "SQLMap"
    ],
    "directoryBoundaries": {
      "unitTests": "src/test/java",
      "integrationTests": "src/test/integration",
      "uatTests": "src/test/uat",
      "performanceTests": "src/test/performance",
      "securityTests": "src/test/security"
    },
    "endpoints": [
      "/api/v1/users",
      "/api/v1/attendance",
      "/api/v1/notifications"
    ]
  },
  "subAgentFunctionalDirectives": {
    "Coder": [
      "Develop unit tests for individual components",
      "Ensure code coverage",
      "Address any defects found during testing"
    ],
    "Tester": [
      "Develop and execute integration tests",
      "Develop and execute UAT tests",
      "Develop and execute performance tests",
      "Develop and execute security tests",
      "Report and track defects until they are resolved"
    ],
    "Reviewer": [
      "Conduct code reviews of test code",
      "Ensure testing standards are met",
      "Provide feedback to the Coder"
    ],
    "DevOps": [
      "Configure and manage the testing environment",
      "Ensure continuous integration and continuous deployment (CI/CD) pipelines are working correctly",
      "Provide support for testing infrastructure"
    ]
  },
  "definitionOfDone": [
    "All unit tests, integration tests, UAT tests, performance tests, and security tests have been executed and passed",
    "All defects found during testing have been resolved and re-tested",
    "Code coverage meets the required standards (e.g., 80%)",
    "Testing infrastructure is properly configured and functioning correctly",
    "All test results have been documented and reviewed by the team",
    "The application has been certified as ready for deployment to the production environment"
  ],
  "dayByDayPlan": [
    {
      "day": 1,
      "tasks": [
        "Develop unit tests for individual components",
        "Ensure code coverage"
      ],
      "assignee": "Coder"
    },
    {
      "day": 2,
      "tasks": [
        "Develop and execute integration tests",
        "Develop and execute UAT tests"
      ],
      "assignee": "Tester"
    },
    {
      "day": 3,
      "tasks": [
        "Develop and execute performance tests",
        "Develop and execute security tests"
      ],
      "assignee": "Tester"
    },
    {
      "day": 4,
      "tasks": [
        "Conduct code reviews of test code",
        "Ensure testing standards are met"
      ],
      "assignee": "Reviewer"
    },
    {
      "day": 5,
      "tasks": [
        "Configure and manage the testing environment",
        "Ensure continuous integration and continuous deployment (CI/CD) pipelines are working correctly"
      ],
      "assignee": "DevOps"
    },
    {
      "day": 6,
      "tasks": [
        "Report and track defects until they are resolved",
        "Provide support for testing infrastructure"
      ],
      "assignee": "Tester, DevOps"
    },
    {
      "day": 7,
      "tasks": [
        "Document and review test results",
        "Certify the application as ready for deployment to the production environment"
      ],
      "assignee": "Team"
    }
  ]
}
```
```

# Phase 5 STEPS - Prompt:


            Analyze the attached Phase 5 Context Markdown content. 
            Translate every directive, objective, and daily task mentioned inside it into a structured day-by-day JSON map.
            
            --- PHASE 5 CONTEXT MARKDOWN ---
            ## PHASE 5 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 5 is to deploy the membership-hub application to the Google Cloud Platform (GCP) using Google Kubernetes Engine (GKE), ensuring a scalable, secure, and highly available environment. This phase will also focus on configuring monitoring and logging, as well as planning for post-launch maintenance and updates. The key deliverables include:
- Deployment of the application to GCP using GKE
- Configuration of monitoring and logging tools
- Setup of security measures, including OAuth 2.0 and HTTPS
- Planning for post-launch maintenance, updates, and potential scalability adjustments

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 5 includes:
- Deployment scripts and configurations for GKE
- Monitoring and logging tools, such as Google Cloud Logging and Monitoring
- Security configurations, including OAuth 2.0 and HTTPS settings
- Directory boundaries:
  - `/deploy`: contains deployment scripts and configurations
  - `/monitoring`: contains monitoring and logging configurations
  - `/security`: contains security configurations, including OAuth 2.0 and HTTPS settings
- Endpoints:
  - `/api/deploy`: endpoint for deploying the application to GCP
  - `/api/monitoring`: endpoint for monitoring and logging
  - `/api/security`: endpoint for security configurations

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
- **Coder**: Focus on writing deployment scripts, configuring monitoring and logging tools, and implementing security measures.
- **Tester**: Conduct thorough testing of the deployment process, monitoring and logging configurations, and security settings.
- **Reviewer**: Review deployment scripts, monitoring and logging configurations, and security settings to ensure they meet the project's quality and compliance standards.
- **DevOps (Deployer)**: Responsible for deploying the application to GCP, configuring monitoring and logging tools, and setting up security measures.
- **Docker**: Ensure the application is properly containerized and can be efficiently deployed to GKE.

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 5 includes:
- The application is successfully deployed to GCP using GKE.
- Monitoring and logging tools are configured and functioning correctly.
- Security measures, including OAuth 2.0 and HTTPS, are implemented and tested.
- Post-launch maintenance and update plans are in place.
- All deployment scripts, configurations, and security settings are reviewed and approved by the Reviewer.
- The application is thoroughly tested by the Tester, and all defects are resolved.
- The DevOps team has verified the deployment and configuration of the application.
            ------------------------------------------

            Map your response strictly to the requested PhaseStepsPlan JSON structure.
            

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
```json
{
  "phase": "Phase 5",
  "objectives": [
    "Deploy the membership-hub application to the Google Cloud Platform (GCP) using Google Kubernetes Engine (GKE)",
    "Configure monitoring and logging tools",
    "Setup security measures, including OAuth 2.0 and HTTPS",
    "Plan for post-launch maintenance and updates"
  ],
  "dailyTasks": [
    {
      "day": 1,
      "tasks": [
        {
          "role": "Coder",
          "task": "Write deployment scripts for GKE"
        },
        {
          "role": "DevOps",
          "task": "Prepare GCP environment for deployment"
        }
      ]
    },
    {
      "day": 2,
      "tasks": [
        {
          "role": "Coder",
          "task": "Configure monitoring and logging tools"
        },
        {
          "role": "Tester",
          "task": "Test deployment process"
        }
      ]
    },
    {
      "day": 3,
      "tasks": [
        {
          "role": "Coder",
          "task": "Implement security measures, including OAuth 2.0 and HTTPS"
        },
        {
          "role": "Reviewer",
          "task": "Review deployment scripts and configurations"
        }
      ]
    },
    {
      "day": 4,
      "tasks": [
        {
          "role": "DevOps",
          "task": "Deploy application to GCP using GKE"
        },
        {
          "role": "Tester",
          "task": "Test monitoring and logging configurations"
        }
      ]
    },
    {
      "day": 5,
      "tasks": [
        {
          "role": "DevOps",
          "task": "Configure monitoring and logging tools"
        },
        {
          "role": "Reviewer",
          "task": "Review security settings and configurations"
        }
      ]
    },
    {
      "day": 6,
      "tasks": [
        {
          "role": "Tester",
          "task": "Test security settings and configurations"
        },
        {
          "role": "DevOps",
          "task": "Verify deployment and configuration of the application"
        }
      ]
    },
    {
      "day": 7,
      "tasks": [
        {
          "role": "Reviewer",
          "task": "Review and approve all deployment scripts, configurations, and security settings"
        },
        {
          "role": "DevOps",
          "task": "Finalize post-launch maintenance and update plans"
        }
      ]
    }
  ],
  "definitionOfDone": [
    "The application is successfully deployed to GCP using GKE",
    "Monitoring and logging tools are configured and functioning correctly",
    "Security measures, including OAuth 2.0 and HTTPS, are implemented and tested",
    "Post-launch maintenance and update plans are in place",
    "All deployment scripts, configurations, and security settings are reviewed and approved by the Reviewer",
    "The application is thoroughly tested by the Tester, and all defects are resolved",
    "The DevOps team has verified the deployment and configuration of the application"
  ]
}
```
```

# Global Prompt:


        Analyze the attached project requirements. Build the GLOBAL PROJECT CONTEXT for 'test-ai-architecture'.
        
        --- RAW REQUIREMENTS ---
        ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

        --- END REQUIREMENTS ---

        Your output MUST follow this exact structure:
        ## GLOBAL PROJECT CONTEXT: test-ai-architecture
        #### 1. Executive Summary & Tech Stack Blueprint
        #### 2. Global Guardrails & Enterprise Compliance Standards
        #### 3. Standardized Sub-Agent Persona Definitions (Manager, Coder, Tester, Reviewer, Docker, Deployer)
        #### 4. Multi-Phase Segmentation Strategy Overview (Plan exactly 5 phases)
        

# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable web and mobile application designed to manage students across multiple centers. The tech stack includes Quarkus, Kafka, Postgres, and Docker, with deployment on GCP and GKE. The application supports internal authentication via email/password, Firebase, Google, and Facebook, as well as QR code-based attendance tracking. The front end is built using Next.js, with support for multiple languages, SEO optimization, and notification systems. The project aims to provide a comprehensive management system for centers, with features such as attendance tracking, membership management, and notification systems.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to industry standards, the following global guardrails and enterprise compliance standards will be implemented:
* Security: Implement OAuth 2.0 for authentication, SSL/TLS encryption for data transmission, and regular security audits.
* Data Privacy: Comply with GDPR, CCPA, and other relevant data protection regulations, ensuring the secure storage and handling of user data.
* Scalability: Design the system to scale horizontally, with load balancing and auto-scaling capabilities to handle increased traffic.
* Compliance: Adhere to industry-specific regulations, such as accessibility standards (WCAG 2.1) and data retention policies.
* Quality Assurance: Implement automated testing, code reviews, and continuous integration/continuous deployment (CI/CD) pipelines to ensure high-quality code and rapid deployment.

#### 3. Standardized Sub-Agent Persona Definitions
The following sub-agent persona definitions will be used to ensure clear roles and responsibilities:
* **Manager**: Oversees project scope, timeline, and budget, ensuring alignment with business objectives.
* **Coder**: Develops high-quality, scalable, and secure code, following industry best practices and coding standards.
* **Tester**: Designs and executes comprehensive testing plans, identifying and reporting defects to ensure high-quality software.
* **Reviewer**: Conducts code reviews, providing constructive feedback to improve code quality, readability, and maintainability.
* **Docker**: Responsible for containerization, ensuring seamless deployment and scaling of the application.
* **Deployer**: Manages deployment processes, ensuring smooth and efficient deployment of the application to production environments.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases:
* **Phase 1: Planning and Requirements Gathering** (Weeks 1-4): Define project scope, gather requirements, and create a detailed project plan.
* **Phase 2: Backend Development** (Weeks 5-12): Develop the backend using Quarkus, Kafka, and Postgres, with a focus on scalability and security.
* **Phase 3: Frontend Development** (Weeks 13-18): Develop the frontend using Next.js, with a focus on user experience, SEO optimization, and notification systems.
* **Phase 4: Testing and Quality Assurance** (Weeks 19-22): Conduct comprehensive testing, including unit testing, integration testing, and user acceptance testing.
* **Phase 5: Deployment and Maintenance** (Weeks 23-26): Deploy the application to production, ensure smooth operation, and provide ongoing maintenance and support.
```

# Phase 1 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 1 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable web and mobile application designed to manage students across multiple centers. The tech stack includes Quarkus, Kafka, Postgres, and Docker, with deployment on GCP and GKE. The application supports internal authentication via email/password, Firebase, Google, and Facebook, as well as QR code-based attendance tracking. The front end is built using Next.js, with support for multiple languages, SEO optimization, and notification systems. The project aims to provide a comprehensive management system for centers, with features such as attendance tracking, membership management, and notification systems.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to industry standards, the following global guardrails and enterprise compliance standards will be implemented:
* Security: Implement OAuth 2.0 for authentication, SSL/TLS encryption for data transmission, and regular security audits.
* Data Privacy: Comply with GDPR, CCPA, and other relevant data protection regulations, ensuring the secure storage and handling of user data.
* Scalability: Design the system to scale horizontally, with load balancing and auto-scaling capabilities to handle increased traffic.
* Compliance: Adhere to industry-specific regulations, such as accessibility standards (WCAG 2.1) and data retention policies.
* Quality Assurance: Implement automated testing, code reviews, and continuous integration/continuous deployment (CI/CD) pipelines to ensure high-quality code and rapid deployment.

#### 3. Standardized Sub-Agent Persona Definitions
The following sub-agent persona definitions will be used to ensure clear roles and responsibilities:
* **Manager**: Oversees project scope, timeline, and budget, ensuring alignment with business objectives.
* **Coder**: Develops high-quality, scalable, and secure code, following industry best practices and coding standards.
* **Tester**: Designs and executes comprehensive testing plans, identifying and reporting defects to ensure high-quality software.
* **Reviewer**: Conducts code reviews, providing constructive feedback to improve code quality, readability, and maintainability.
* **Docker**: Responsible for containerization, ensuring seamless deployment and scaling of the application.
* **Deployer**: Manages deployment processes, ensuring smooth and efficient deployment of the application to production environments.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases:
* **Phase 1: Planning and Requirements Gathering** (Weeks 1-4): Define project scope, gather requirements, and create a detailed project plan.
* **Phase 2: Backend Development** (Weeks 5-12): Develop the backend using Quarkus, Kafka, and Postgres, with a focus on scalability and security.
* **Phase 3: Frontend Development** (Weeks 13-18): Develop the frontend using Next.js, with a focus on user experience, SEO optimization, and notification systems.
* **Phase 4: Testing and Quality Assurance** (Weeks 19-22): Conduct comprehensive testing, including unit testing, integration testing, and user acceptance testing.
* **Phase 5: Deployment and Maintenance** (Weeks 23-26): Deploy the application to production, ensure smooth operation, and provide ongoing maintenance and support.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------

            Your output MUST follow this exact Markdown structure for Phase 1:
            ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather requirements, and create a detailed project plan for the membership-hub project. This phase will focus on understanding the business needs, identifying the technical requirements, and establishing a clear roadmap for the project. The key deliverables for this phase include:
* A comprehensive project plan outlining the scope, timeline, and budget
* A detailed requirements document capturing the functional and non-functional requirements
* A high-level architecture diagram illustrating the system components and interactions
* A list of potential risks and mitigation strategies

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 1 includes:
* Reviewing the existing tech stack and identifying potential areas for improvement
* Researching and recommending tools and technologies for the project (e.g., Quarkus, Kafka, Postgres, Docker, GCP, GKE, Next.js)
* Defining the directory structure and organization for the project codebase
* Establishing the endpoints and APIs for the backend and frontend components
* Identifying the required files and paths for the project (e.g., configuration files, data storage, logging)

The following directories and files are in scope for Phase 1:
* `docs/`: project documentation and meeting notes
* `requirements/`: requirements gathering and analysis
* `architecture/`: high-level architecture diagrams and design documents
* `tech-stack/`: research and recommendations for tools and technologies

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents have specific tasks and responsibilities for Phase 1:
* **Manager**: oversee the project scope, timeline, and budget; ensure alignment with business objectives
* **Coder**: research and recommend tools and technologies; define the directory structure and organization for the project codebase
* **Tester**: review the requirements document and identify potential testing scenarios
* **Reviewer**: review the project plan and provide feedback on the scope, timeline, and budget
* **Docker**: research and recommend containerization strategies for the project
* **Deployer**: research and recommend deployment options for the project (e.g., GCP, GKE)

#### 4. Phase Definition of Done (DoD)
The Definition of Done (DoD) for Phase 1 includes:
* A comprehensive project plan outlining the scope, timeline, and budget
* A detailed requirements document capturing the functional and non-functional requirements
* A high-level architecture diagram illustrating the system components and interactions
* A list of potential risks and mitigation strategies
* Review and approval of the project plan and requirements document by the stakeholders
* Completion of the research and recommendations for tools and technologies
* Establishment of the directory structure and organization for the project codebase
* Identification of the required files and paths for the project
* Review and feedback on the project plan and requirements document by the sub-agents
```

# Phase 2 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 2 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable web and mobile application designed to manage students across multiple centers. The tech stack includes Quarkus, Kafka, Postgres, and Docker, with deployment on GCP and GKE. The application supports internal authentication via email/password, Firebase, Google, and Facebook, as well as QR code-based attendance tracking. The front end is built using Next.js, with support for multiple languages, SEO optimization, and notification systems. The project aims to provide a comprehensive management system for centers, with features such as attendance tracking, membership management, and notification systems.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to industry standards, the following global guardrails and enterprise compliance standards will be implemented:
* Security: Implement OAuth 2.0 for authentication, SSL/TLS encryption for data transmission, and regular security audits.
* Data Privacy: Comply with GDPR, CCPA, and other relevant data protection regulations, ensuring the secure storage and handling of user data.
* Scalability: Design the system to scale horizontally, with load balancing and auto-scaling capabilities to handle increased traffic.
* Compliance: Adhere to industry-specific regulations, such as accessibility standards (WCAG 2.1) and data retention policies.
* Quality Assurance: Implement automated testing, code reviews, and continuous integration/continuous deployment (CI/CD) pipelines to ensure high-quality code and rapid deployment.

#### 3. Standardized Sub-Agent Persona Definitions
The following sub-agent persona definitions will be used to ensure clear roles and responsibilities:
* **Manager**: Oversees project scope, timeline, and budget, ensuring alignment with business objectives.
* **Coder**: Develops high-quality, scalable, and secure code, following industry best practices and coding standards.
* **Tester**: Designs and executes comprehensive testing plans, identifying and reporting defects to ensure high-quality software.
* **Reviewer**: Conducts code reviews, providing constructive feedback to improve code quality, readability, and maintainability.
* **Docker**: Responsible for containerization, ensuring seamless deployment and scaling of the application.
* **Deployer**: Manages deployment processes, ensuring smooth and efficient deployment of the application to production environments.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases:
* **Phase 1: Planning and Requirements Gathering** (Weeks 1-4): Define project scope, gather requirements, and create a detailed project plan.
* **Phase 2: Backend Development** (Weeks 5-12): Develop the backend using Quarkus, Kafka, and Postgres, with a focus on scalability and security.
* **Phase 3: Frontend Development** (Weeks 13-18): Develop the frontend using Next.js, with a focus on user experience, SEO optimization, and notification systems.
* **Phase 4: Testing and Quality Assurance** (Weeks 19-22): Conduct comprehensive testing, including unit testing, integration testing, and user acceptance testing.
* **Phase 5: Deployment and Maintenance** (Weeks 23-26): Deploy the application to production, ensure smooth operation, and provide ongoing maintenance and support.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------

            Your output MUST follow this exact Markdown structure for Phase 2:
            ## PHASE 2 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 2 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 2 is to develop the backend of the membership-hub project using Quarkus, Kafka, and Postgres, with a focus on scalability and security. The scope of this phase includes:
* Designing and implementing the database schema for user management, attendance tracking, and notification systems
* Developing RESTful APIs for user authentication, attendance tracking, and notification systems
* Integrating Kafka for real-time data processing and notification systems
* Implementing OAuth 2.0 for authentication and SSL/TLS encryption for data transmission
* Ensuring the backend is scalable, secure, and compliant with industry standards

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope of Phase 2 includes:
* Backend directory: `src/main/java`
* Database schema: `src/main/resources/db`
* Kafka configuration: `src/main/resources/kafka`
* API endpoints:
	+ `/api/v1/auth`: user authentication
	+ `/api/v1/attendance`: attendance tracking
	+ `/api/v1/notifications`: notification systems
* Allowed dependencies:
	+ Quarkus
	+ Kafka
	+ Postgres
	+ OAuth 2.0
	+ SSL/TLS encryption

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 2:
* **Coder**: Develop the backend using Quarkus, Kafka, and Postgres, implementing RESTful APIs and integrating OAuth 2.0 for authentication
* **Tester**: Design and execute unit tests, integration tests, and API tests to ensure the backend is functioning correctly
* **Reviewer**: Conduct code reviews to ensure the code is scalable, secure, and compliant with industry standards
* **DevOps (Docker)**: Containerize the backend using Docker and ensure seamless deployment to GCP and GKE
* **DevOps (Deployer)**: Manage the deployment process, ensuring smooth and efficient deployment of the backend to production environments

#### 4. Phase Definition of Done (DoD)
Phase 2 is considered complete when:
* The backend is fully functional, with all required features implemented
* All unit tests, integration tests, and API tests have been executed and passed
* Code reviews have been completed, and all feedback has been addressed
* The backend has been containerized using Docker and deployed to GCP and GKE
* All security and compliance requirements have been met, including OAuth 2.0 and SSL/TLS encryption
* The phase has been reviewed and approved by the Manager and all sub-agents involved.
```

# Phase 3 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 3 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable web and mobile application designed to manage students across multiple centers. The tech stack includes Quarkus, Kafka, Postgres, and Docker, with deployment on GCP and GKE. The application supports internal authentication via email/password, Firebase, Google, and Facebook, as well as QR code-based attendance tracking. The front end is built using Next.js, with support for multiple languages, SEO optimization, and notification systems. The project aims to provide a comprehensive management system for centers, with features such as attendance tracking, membership management, and notification systems.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to industry standards, the following global guardrails and enterprise compliance standards will be implemented:
* Security: Implement OAuth 2.0 for authentication, SSL/TLS encryption for data transmission, and regular security audits.
* Data Privacy: Comply with GDPR, CCPA, and other relevant data protection regulations, ensuring the secure storage and handling of user data.
* Scalability: Design the system to scale horizontally, with load balancing and auto-scaling capabilities to handle increased traffic.
* Compliance: Adhere to industry-specific regulations, such as accessibility standards (WCAG 2.1) and data retention policies.
* Quality Assurance: Implement automated testing, code reviews, and continuous integration/continuous deployment (CI/CD) pipelines to ensure high-quality code and rapid deployment.

#### 3. Standardized Sub-Agent Persona Definitions
The following sub-agent persona definitions will be used to ensure clear roles and responsibilities:
* **Manager**: Oversees project scope, timeline, and budget, ensuring alignment with business objectives.
* **Coder**: Develops high-quality, scalable, and secure code, following industry best practices and coding standards.
* **Tester**: Designs and executes comprehensive testing plans, identifying and reporting defects to ensure high-quality software.
* **Reviewer**: Conducts code reviews, providing constructive feedback to improve code quality, readability, and maintainability.
* **Docker**: Responsible for containerization, ensuring seamless deployment and scaling of the application.
* **Deployer**: Manages deployment processes, ensuring smooth and efficient deployment of the application to production environments.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases:
* **Phase 1: Planning and Requirements Gathering** (Weeks 1-4): Define project scope, gather requirements, and create a detailed project plan.
* **Phase 2: Backend Development** (Weeks 5-12): Develop the backend using Quarkus, Kafka, and Postgres, with a focus on scalability and security.
* **Phase 3: Frontend Development** (Weeks 13-18): Develop the frontend using Next.js, with a focus on user experience, SEO optimization, and notification systems.
* **Phase 4: Testing and Quality Assurance** (Weeks 19-22): Conduct comprehensive testing, including unit testing, integration testing, and user acceptance testing.
* **Phase 5: Deployment and Maintenance** (Weeks 23-26): Deploy the application to production, ensure smooth operation, and provide ongoing maintenance and support.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------

            Your output MUST follow this exact Markdown structure for Phase 3:
            ## PHASE 3 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 3 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 3 is to develop the frontend of the membership-hub application using Next.js, focusing on user experience, SEO optimization, and notification systems. The scope of this phase includes designing and implementing the user interface, integrating with the backend API, and ensuring multi-language support. The key deliverables of this phase are:
* A fully functional frontend application with a user-friendly interface
* Integration with the backend API for authentication, attendance tracking, and notification systems
* Support for multiple languages and SEO optimization for both web and mobile applications

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope of this phase includes:
* Frontend development using Next.js
* Integration with the backend API using RESTful endpoints
* Implementation of multi-language support using internationalization libraries
* SEO optimization using meta tags, header tags, and content optimization
* Development of notification systems using mobile push notifications and in-app notifications
The directory boundaries for this phase include:
* `frontend/`: contains all frontend code, including components, pages, and API integrations
* `public/`: contains static assets, such as images, fonts, and favicon
* `pages/`: contains page-level components, such as login, dashboard, and attendance tracking
* `components/`: contains reusable UI components, such as buttons, forms, and tables
* `api/`: contains API integrations with the backend, including authentication, attendance tracking, and notification systems

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in this phase:
* **Coder**: Develop the frontend application using Next.js, integrate with the backend API, and implement multi-language support and SEO optimization
* **Tester**: Develop and execute comprehensive testing plans, including unit testing, integration testing, and user acceptance testing
* **Reviewer**: Conduct code reviews, providing constructive feedback on code quality, readability, and maintainability
* **DevOps**: Ensure seamless deployment and scaling of the frontend application, including containerization using Docker and deployment to GCP and GKE

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 3 includes:
* The frontend application is fully functional and meets all requirements
* The application is integrated with the backend API and supports authentication, attendance tracking, and notification systems
* The application supports multiple languages and is optimized for SEO
* The application has been thoroughly tested, including unit testing, integration testing, and user acceptance testing
* The code has been reviewed and meets all coding standards and best practices
* The application has been deployed to production and is available to users
```

# Phase 4 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 4 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable web and mobile application designed to manage students across multiple centers. The tech stack includes Quarkus, Kafka, Postgres, and Docker, with deployment on GCP and GKE. The application supports internal authentication via email/password, Firebase, Google, and Facebook, as well as QR code-based attendance tracking. The front end is built using Next.js, with support for multiple languages, SEO optimization, and notification systems. The project aims to provide a comprehensive management system for centers, with features such as attendance tracking, membership management, and notification systems.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to industry standards, the following global guardrails and enterprise compliance standards will be implemented:
* Security: Implement OAuth 2.0 for authentication, SSL/TLS encryption for data transmission, and regular security audits.
* Data Privacy: Comply with GDPR, CCPA, and other relevant data protection regulations, ensuring the secure storage and handling of user data.
* Scalability: Design the system to scale horizontally, with load balancing and auto-scaling capabilities to handle increased traffic.
* Compliance: Adhere to industry-specific regulations, such as accessibility standards (WCAG 2.1) and data retention policies.
* Quality Assurance: Implement automated testing, code reviews, and continuous integration/continuous deployment (CI/CD) pipelines to ensure high-quality code and rapid deployment.

#### 3. Standardized Sub-Agent Persona Definitions
The following sub-agent persona definitions will be used to ensure clear roles and responsibilities:
* **Manager**: Oversees project scope, timeline, and budget, ensuring alignment with business objectives.
* **Coder**: Develops high-quality, scalable, and secure code, following industry best practices and coding standards.
* **Tester**: Designs and executes comprehensive testing plans, identifying and reporting defects to ensure high-quality software.
* **Reviewer**: Conducts code reviews, providing constructive feedback to improve code quality, readability, and maintainability.
* **Docker**: Responsible for containerization, ensuring seamless deployment and scaling of the application.
* **Deployer**: Manages deployment processes, ensuring smooth and efficient deployment of the application to production environments.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases:
* **Phase 1: Planning and Requirements Gathering** (Weeks 1-4): Define project scope, gather requirements, and create a detailed project plan.
* **Phase 2: Backend Development** (Weeks 5-12): Develop the backend using Quarkus, Kafka, and Postgres, with a focus on scalability and security.
* **Phase 3: Frontend Development** (Weeks 13-18): Develop the frontend using Next.js, with a focus on user experience, SEO optimization, and notification systems.
* **Phase 4: Testing and Quality Assurance** (Weeks 19-22): Conduct comprehensive testing, including unit testing, integration testing, and user acceptance testing.
* **Phase 5: Deployment and Maintenance** (Weeks 23-26): Deploy the application to production, ensure smooth operation, and provide ongoing maintenance and support.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------

            Your output MUST follow this exact Markdown structure for Phase 4:
            ## PHASE 4 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 4 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
In Phase 4, the primary objective is to conduct comprehensive testing and quality assurance of the membership-hub project. This phase will ensure that the application meets the required standards, is free from defects, and provides a seamless user experience. The scope of this phase includes:

* Unit testing of individual components
* Integration testing of backend and frontend services
* User acceptance testing (UAT) to validate the application's functionality and usability
* Performance testing to ensure the application's scalability and responsiveness
* Security testing to identify and address potential vulnerabilities

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 4 includes:

* Testing frameworks: JUnit, Jest, and Cypress
* Testing tools: Postman, Selenium, and Apache JMeter
* Directory boundaries:
	+ `src/test/java`: Unit tests and integration tests for backend services
	+ `src/test/javascript`: Unit tests and integration tests for frontend services
	+ `cypress/integration`: End-to-end tests for frontend services
	+ `postman collections`: API tests for backend services
* Endpoints:
	+ `/api/v1/auth`: Authentication endpoints
	+ `/api/v1/users`: User management endpoints
	+ `/api/v1/centers`: Center management endpoints
	+ `/api/v1/attendances`: Attendance management endpoints

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 4:

* **Coder**: Develop test cases, implement testing frameworks, and write automated tests
* **Tester**: Execute manual tests, create test plans, and report defects
* **Reviewer**: Review test cases, provide feedback on testing strategies, and ensure testing coverage
* **DevOps**: Configure testing environments, deploy testing frameworks, and monitor testing pipelines

Specific tasks for each sub-agent:

* Coder:
	+ Develop unit tests for backend services using JUnit
	+ Implement integration tests for frontend services using Jest
* Tester:
	+ Create test plans for user acceptance testing (UAT)
	+ Execute manual tests for frontend and backend services
* Reviewer:
	+ Review test cases for coverage and effectiveness
	+ Provide feedback on testing strategies and frameworks
* DevOps:
	+ Configure testing environments for backend and frontend services
	+ Deploy testing frameworks and tools

#### 4. Phase Definition of Done (DoD)
The Definition of Done (DoD) for Phase 4 includes:

* All unit tests and integration tests have been executed and passed
* User acceptance testing (UAT) has been completed and validated
* Performance testing has been conducted and optimized
* Security testing has been performed and vulnerabilities have been addressed
* All defects have been reported, prioritized, and resolved
* Testing frameworks and tools have been configured and deployed
* Testing environments have been set up and validated

Upon completion of Phase 4, the application will have undergone rigorous testing and quality assurance, ensuring that it meets the required standards and provides a seamless user experience.
```

# Phase 5 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 5 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable web and mobile application designed to manage students across multiple centers. The tech stack includes Quarkus, Kafka, Postgres, and Docker, with deployment on GCP and GKE. The application supports internal authentication via email/password, Firebase, Google, and Facebook, as well as QR code-based attendance tracking. The front end is built using Next.js, with support for multiple languages, SEO optimization, and notification systems. The project aims to provide a comprehensive management system for centers, with features such as attendance tracking, membership management, and notification systems.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to industry standards, the following global guardrails and enterprise compliance standards will be implemented:
* Security: Implement OAuth 2.0 for authentication, SSL/TLS encryption for data transmission, and regular security audits.
* Data Privacy: Comply with GDPR, CCPA, and other relevant data protection regulations, ensuring the secure storage and handling of user data.
* Scalability: Design the system to scale horizontally, with load balancing and auto-scaling capabilities to handle increased traffic.
* Compliance: Adhere to industry-specific regulations, such as accessibility standards (WCAG 2.1) and data retention policies.
* Quality Assurance: Implement automated testing, code reviews, and continuous integration/continuous deployment (CI/CD) pipelines to ensure high-quality code and rapid deployment.

#### 3. Standardized Sub-Agent Persona Definitions
The following sub-agent persona definitions will be used to ensure clear roles and responsibilities:
* **Manager**: Oversees project scope, timeline, and budget, ensuring alignment with business objectives.
* **Coder**: Develops high-quality, scalable, and secure code, following industry best practices and coding standards.
* **Tester**: Designs and executes comprehensive testing plans, identifying and reporting defects to ensure high-quality software.
* **Reviewer**: Conducts code reviews, providing constructive feedback to improve code quality, readability, and maintainability.
* **Docker**: Responsible for containerization, ensuring seamless deployment and scaling of the application.
* **Deployer**: Manages deployment processes, ensuring smooth and efficient deployment of the application to production environments.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases:
* **Phase 1: Planning and Requirements Gathering** (Weeks 1-4): Define project scope, gather requirements, and create a detailed project plan.
* **Phase 2: Backend Development** (Weeks 5-12): Develop the backend using Quarkus, Kafka, and Postgres, with a focus on scalability and security.
* **Phase 3: Frontend Development** (Weeks 13-18): Develop the frontend using Next.js, with a focus on user experience, SEO optimization, and notification systems.
* **Phase 4: Testing and Quality Assurance** (Weeks 19-22): Conduct comprehensive testing, including unit testing, integration testing, and user acceptance testing.
* **Phase 5: Deployment and Maintenance** (Weeks 23-26): Deploy the application to production, ensure smooth operation, and provide ongoing maintenance and support.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------

            Your output MUST follow this exact Markdown structure for Phase 5:
            ## PHASE 5 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 5 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 5 is to deploy the membership-hub application to production, ensuring a smooth and efficient deployment process. This phase will focus on deploying the application to Google Cloud Platform (GCP) and Google Kubernetes Engine (GKE), configuring load balancing and auto-scaling, and setting up monitoring and logging tools. Additionally, this phase will involve conducting final testing, including user acceptance testing (UAT) and performance testing, to ensure the application meets the required standards.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 5 includes:
* Deploying the application to GCP and GKE
* Configuring load balancing and auto-scaling
* Setting up monitoring and logging tools (e.g., Prometheus, Grafana, ELK Stack)
* Conducting final testing (UAT, performance testing)
* Ensuring compliance with security, data privacy, and scalability requirements
* Directory boundaries:
	+ Deployment scripts: `deploy/scripts`
	+ Kubernetes configurations: `deploy/k8s`
	+ Monitoring and logging configurations: `deploy/monitoring`
	+ Test scripts: `test/deployment`

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
* **Coder**: Assist in deployment scripting, configure load balancing and auto-scaling, and ensure compliance with security and scalability requirements.
* **Tester**: Conduct final testing, including UAT and performance testing, and report any defects or issues.
* **Reviewer**: Review deployment scripts, Kubernetes configurations, and monitoring and logging setups to ensure they meet the required standards.
* **Docker**: Ensure seamless deployment and scaling of the application by configuring Docker images and containers.
* **Deployer**: Manage the deployment process, ensuring smooth and efficient deployment of the application to production environments.

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 5 includes:
* Successful deployment of the application to GCP and GKE
* Configuration of load balancing and auto-scaling
* Setup of monitoring and logging tools
* Completion of final testing (UAT, performance testing)
* Resolution of all defects or issues reported during testing
* Confirmation that the application meets all security, data privacy, and scalability requirements
* Handover of the deployed application to the operations team for ongoing maintenance and support.
```

# Phase 1 STEPS - Prompt:


            Analyze the attached Phase 1 Context Markdown content. 
            Translate every directive, objective, and daily task mentioned inside it into a structured day-by-day JSON map.
            
            --- PHASE 1 CONTEXT MARKDOWN ---
            ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, gather requirements, and create a detailed project plan for the membership-hub project. This phase will focus on understanding the business needs, identifying the technical requirements, and establishing a clear roadmap for the project. The key deliverables for this phase include:
* A comprehensive project plan outlining the scope, timeline, and budget
* A detailed requirements document capturing the functional and non-functional requirements
* A high-level architecture diagram illustrating the system components and interactions
* A list of potential risks and mitigation strategies

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 1 includes:
* Reviewing the existing tech stack and identifying potential areas for improvement
* Researching and recommending tools and technologies for the project (e.g., Quarkus, Kafka, Postgres, Docker, GCP, GKE, Next.js)
* Defining the directory structure and organization for the project codebase
* Establishing the endpoints and APIs for the backend and frontend components
* Identifying the required files and paths for the project (e.g., configuration files, data storage, logging)

The following directories and files are in scope for Phase 1:
* `docs/`: project documentation and meeting notes
* `requirements/`: requirements gathering and analysis
* `architecture/`: high-level architecture diagrams and design documents
* `tech-stack/`: research and recommendations for tools and technologies

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents have specific tasks and responsibilities for Phase 1:
* **Manager**: oversee the project scope, timeline, and budget; ensure alignment with business objectives
* **Coder**: research and recommend tools and technologies; define the directory structure and organization for the project codebase
* **Tester**: review the requirements document and identify potential testing scenarios
* **Reviewer**: review the project plan and provide feedback on the scope, timeline, and budget
* **Docker**: research and recommend containerization strategies for the project
* **Deployer**: research and recommend deployment options for the project (e.g., GCP, GKE)

#### 4. Phase Definition of Done (DoD)
The Definition of Done (DoD) for Phase 1 includes:
* A comprehensive project plan outlining the scope, timeline, and budget
* A detailed requirements document capturing the functional and non-functional requirements
* A high-level architecture diagram illustrating the system components and interactions
* A list of potential risks and mitigation strategies
* Review and approval of the project plan and requirements document by the stakeholders
* Completion of the research and recommendations for tools and technologies
* Establishment of the directory structure and organization for the project codebase
* Identification of the required files and paths for the project
* Review and feedback on the project plan and requirements document by the sub-agents
            ------------------------------------------

            Map your response strictly to the requested PhaseStepsPlan JSON structure.
            

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
{
    "phase": "Phase 1",
    "context": "test-ai-architecture",
    "objectives": [
        "Define project scope",
        "Gather requirements",
        "Create a detailed project plan"
    ],
    "deliverables": [
        "Comprehensive project plan",
        "Detailed requirements document",
        "High-level architecture diagram",
        "List of potential risks and mitigation strategies"
    ],
    "dayByDayPlan": [
        {
            "day": 1,
            "tasks": [
                {
                    "task": "Review existing tech stack",
                    "assignee": "Coder"
                },
                {
                    "task": "Research and recommend tools and technologies",
                    "assignee": "Coder"
                }
            ]
        },
        {
            "day": 2,
            "tasks": [
                {
                    "task": "Define directory structure and organization",
                    "assignee": "Coder"
                },
                {
                    "task": "Establish endpoints and APIs",
                    "assignee": "Coder"
                }
            ]
        },
        {
            "day": 3,
            "tasks": [
                {
                    "task": "Review requirements document",
                    "assignee": "Tester"
                },
                {
                    "task": "Identify potential testing scenarios",
                    "assignee": "Tester"
                }
            ]
        },
        {
            "day": 4,
            "tasks": [
                {
                    "task": "Review project plan",
                    "assignee": "Reviewer"
                },
                {
                    "task": "Provide feedback on project plan",
                    "assignee": "Reviewer"
                }
            ]
        },
        {
            "day": 5,
            "tasks": [
                {
                    "task": "Research containerization strategies",
                    "assignee": "Docker"
                },
                {
                    "task": "Research deployment options",
                    "assignee": "Deployer"
                }
            ]
        },
        {
            "day": 6,
            "tasks": [
                {
                    "task": "Create high-level architecture diagram",
                    "assignee": "Coder"
                },
                {
                    "task": "Identify required files and paths",
                    "assignee": "Coder"
                }
            ]
        },
        {
            "day": 7,
            "tasks": [
                {
                    "task": "Finalize project plan",
                    "assignee": "Manager"
                },
                {
                    "task": "Finalize requirements document",
                    "assignee": "Manager"
                }
            ]
        }
    ],
    "definitionOfDone": [
        "Comprehensive project plan",
        "Detailed requirements document",
        "High-level architecture diagram",
        "List of potential risks and mitigation strategies",
        "Review and approval of project plan and requirements document",
        "Completion of research and recommendations",
        "Establishment of directory structure and organization",
        "Identification of required files and paths",
        "Review and feedback on project plan and requirements document"
    ],
    "project_name": "test-ai-architecture",
    "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
    "phase_idx": 1,
    "phase_context_file": ".ai/.plan/.context/phase-1.context.blueprint.md"
}
```

# Phase 2 STEPS - Prompt:


            Analyze the attached Phase 2 Context Markdown content. 
            Translate every directive, objective, and daily task mentioned inside it into a structured day-by-day JSON map.
            
            --- PHASE 2 CONTEXT MARKDOWN ---
            ## PHASE 2 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 2 is to develop the backend of the membership-hub project using Quarkus, Kafka, and Postgres, with a focus on scalability and security. The scope of this phase includes:
* Designing and implementing the database schema for user management, attendance tracking, and notification systems
* Developing RESTful APIs for user authentication, attendance tracking, and notification systems
* Integrating Kafka for real-time data processing and notification systems
* Implementing OAuth 2.0 for authentication and SSL/TLS encryption for data transmission
* Ensuring the backend is scalable, secure, and compliant with industry standards

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope of Phase 2 includes:
* Backend directory: `src/main/java`
* Database schema: `src/main/resources/db`
* Kafka configuration: `src/main/resources/kafka`
* API endpoints:
	+ `/api/v1/auth`: user authentication
	+ `/api/v1/attendance`: attendance tracking
	+ `/api/v1/notifications`: notification systems
* Allowed dependencies:
	+ Quarkus
	+ Kafka
	+ Postgres
	+ OAuth 2.0
	+ SSL/TLS encryption

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 2:
* **Coder**: Develop the backend using Quarkus, Kafka, and Postgres, implementing RESTful APIs and integrating OAuth 2.0 for authentication
* **Tester**: Design and execute unit tests, integration tests, and API tests to ensure the backend is functioning correctly
* **Reviewer**: Conduct code reviews to ensure the code is scalable, secure, and compliant with industry standards
* **DevOps (Docker)**: Containerize the backend using Docker and ensure seamless deployment to GCP and GKE
* **DevOps (Deployer)**: Manage the deployment process, ensuring smooth and efficient deployment of the backend to production environments

#### 4. Phase Definition of Done (DoD)
Phase 2 is considered complete when:
* The backend is fully functional, with all required features implemented
* All unit tests, integration tests, and API tests have been executed and passed
* Code reviews have been completed, and all feedback has been addressed
* The backend has been containerized using Docker and deployed to GCP and GKE
* All security and compliance requirements have been met, including OAuth 2.0 and SSL/TLS encryption
* The phase has been reviewed and approved by the Manager and all sub-agents involved.
            ------------------------------------------

            Map your response strictly to the requested PhaseStepsPlan JSON structure.
            

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
{
    "phase": "Phase 2",
    "context": "test-ai-architecture",
    "objectives": [
        "Develop the backend of the membership-hub project using Quarkus, Kafka, and Postgres",
        "Focus on scalability and security"
    ],
    "scope": [
        "Designing and implementing the database schema for user management, attendance tracking, and notification systems",
        "Developing RESTful APIs for user authentication, attendance tracking, and notification systems",
        "Integrating Kafka for real-time data processing and notification systems",
        "Implementing OAuth 2.0 for authentication and SSL/TLS encryption for data transmission",
        "Ensuring the backend is scalable, secure, and compliant with industry standards"
    ],
    "technicalScope": {
        "backendDirectory": "src/main/java",
        "databaseSchema": "src/main/resources/db",
        "kafkaConfiguration": "src/main/resources/kafka",
        "apiEndpoints": [
            "/api/v1/auth",
            "/api/v1/attendance",
            "/api/v1/notifications"
        ],
        "allowedDependencies": [
            "Quarkus",
            "Kafka",
            "Postgres",
            "OAuth 2.0",
            "SSL/TLS encryption"
        ]
    },
    "subAgents": {
        "Coder": [
            "Develop the backend using Quarkus, Kafka, and Postgres",
            "Implement RESTful APIs",
            "Integrate OAuth 2.0 for authentication"
        ],
        "Tester": [
            "Design and execute unit tests",
            "Design and execute integration tests",
            "Design and execute API tests"
        ],
        "Reviewer": [
            "Conduct code reviews to ensure the code is scalable, secure, and compliant with industry standards"
        ],
        "DevOps (Docker)": [
            "Containerize the backend using Docker"
        ],
        "DevOps (Deployer)": [
            "Manage the deployment process",
            "Ensure smooth and efficient deployment of the backend to production environments"
        ]
    },
    "definitionOfDone": [
        "The backend is fully functional, with all required features implemented",
        "All unit tests, integration tests, and API tests have been executed and passed",
        "Code reviews have been completed, and all feedback has been addressed",
        "The backend has been containerized using Docker and deployed to GCP and GKE",
        "All security and compliance requirements have been met, including OAuth 2.0 and SSL/TLS encryption",
        "The phase has been reviewed and approved by the Manager and all sub-agents involved"
    ],
    "dayByDayPlan": [
        {
            "day": 1,
            "tasks": [
                "Coder: Develop the backend using Quarkus, Kafka, and Postgres",
                "Tester: Design and execute unit tests"
            ]
        },
        {
            "day": 2,
            "tasks": [
                "Coder: Implement RESTful APIs",
                "Tester: Design and execute integration tests"
            ]
        },
        {
            "day": 3,
            "tasks": [
                "Coder: Integrate OAuth 2.0 for authentication",
                "Tester: Design and execute API tests"
            ]
        },
        {
            "day": 4,
            "tasks": [
                "Reviewer: Conduct code reviews",
                "DevOps (Docker): Containerize the backend using Docker"
            ]
        },
        {
            "day": 5,
            "tasks": [
                "DevOps (Deployer): Manage the deployment process",
                "DevOps (Deployer): Ensure smooth and efficient deployment of the backend to production environments"
            ]
        }
    ],
    "project_name": "test-ai-architecture",
    "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
    "phase_idx": 2,
    "phase_context_file": ".ai/.plan/.context/phase-2.context.blueprint.md"
}
```

# Phase 3 STEPS - Prompt:


            Analyze the attached Phase 3 Context Markdown content. 
            Translate every directive, objective, and daily task mentioned inside it into a structured day-by-day JSON map.
            
            --- PHASE 3 CONTEXT MARKDOWN ---
            ## PHASE 3 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 3 is to develop the frontend of the membership-hub application using Next.js, focusing on user experience, SEO optimization, and notification systems. The scope of this phase includes designing and implementing the user interface, integrating with the backend API, and ensuring multi-language support. The key deliverables of this phase are:
* A fully functional frontend application with a user-friendly interface
* Integration with the backend API for authentication, attendance tracking, and notification systems
* Support for multiple languages and SEO optimization for both web and mobile applications

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope of this phase includes:
* Frontend development using Next.js
* Integration with the backend API using RESTful endpoints
* Implementation of multi-language support using internationalization libraries
* SEO optimization using meta tags, header tags, and content optimization
* Development of notification systems using mobile push notifications and in-app notifications
The directory boundaries for this phase include:
* `frontend/`: contains all frontend code, including components, pages, and API integrations
* `public/`: contains static assets, such as images, fonts, and favicon
* `pages/`: contains page-level components, such as login, dashboard, and attendance tracking
* `components/`: contains reusable UI components, such as buttons, forms, and tables
* `api/`: contains API integrations with the backend, including authentication, attendance tracking, and notification systems

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in this phase:
* **Coder**: Develop the frontend application using Next.js, integrate with the backend API, and implement multi-language support and SEO optimization
* **Tester**: Develop and execute comprehensive testing plans, including unit testing, integration testing, and user acceptance testing
* **Reviewer**: Conduct code reviews, providing constructive feedback on code quality, readability, and maintainability
* **DevOps**: Ensure seamless deployment and scaling of the frontend application, including containerization using Docker and deployment to GCP and GKE

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 3 includes:
* The frontend application is fully functional and meets all requirements
* The application is integrated with the backend API and supports authentication, attendance tracking, and notification systems
* The application supports multiple languages and is optimized for SEO
* The application has been thoroughly tested, including unit testing, integration testing, and user acceptance testing
* The code has been reviewed and meets all coding standards and best practices
* The application has been deployed to production and is available to users
            ------------------------------------------

            Map your response strictly to the requested PhaseStepsPlan JSON structure.
            

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
{
    "phase": "Phase 3",
    "context": "test-ai-architecture",
    "objectives": [
        "Develop the frontend of the membership-hub application using Next.js",
        "Focus on user experience, SEO optimization, and notification systems",
        "Design and implement the user interface",
        "Integrate with the backend API",
        "Ensure multi-language support"
    ],
    "keyDeliverables": [
        "A fully functional frontend application with a user-friendly interface",
        "Integration with the backend API for authentication, attendance tracking, and notification systems",
        "Support for multiple languages and SEO optimization for both web and mobile applications"
    ],
    "technicalScope": [
        "Frontend development using Next.js",
        "Integration with the backend API using RESTful endpoints",
        "Implementation of multi-language support using internationalization libraries",
        "SEO optimization using meta tags, header tags, and content optimization",
        "Development of notification systems using mobile push notifications and in-app notifications"
    ],
    "directoryBoundaries": {
        "frontend": "contains all frontend code, including components, pages, and API integrations",
        "public": "contains static assets, such as images, fonts, and favicon",
        "pages": "contains page-level components, such as login, dashboard, and attendance tracking",
        "components": "contains reusable UI components, such as buttons, forms, and tables",
        "api": "contains API integrations with the backend, including authentication, attendance tracking, and notification systems"
    },
    "subAgents": {
        "Coder": "Develop the frontend application using Next.js, integrate with the backend API, and implement multi-language support and SEO optimization",
        "Tester": "Develop and execute comprehensive testing plans, including unit testing, integration testing, and user acceptance testing",
        "Reviewer": "Conduct code reviews, providing constructive feedback on code quality, readability, and maintainability",
        "DevOps": "Ensure seamless deployment and scaling of the frontend application, including containerization using Docker and deployment to GCP and GKE"
    },
    "definitionOfDone": [
        "The frontend application is fully functional and meets all requirements",
        "The application is integrated with the backend API and supports authentication, attendance tracking, and notification systems",
        "The application supports multiple languages and is optimized for SEO",
        "The application has been thoroughly tested, including unit testing, integration testing, and user acceptance testing",
        "The code has been reviewed and meets all coding standards and best practices",
        "The application has been deployed to production and is available to users"
    ],
    "phaseStepsPlan": [
        {
            "day": 1,
            "tasks": [
                "Initialize frontend project using Next.js",
                "Set up directory structure and create initial components"
            ]
        },
        {
            "day": 2,
            "tasks": [
                "Implement user interface for login and dashboard pages",
                "Start integrating with backend API for authentication"
            ]
        },
        {
            "day": 3,
            "tasks": [
                "Implement attendance tracking and notification systems",
                "Start working on multi-language support"
            ]
        },
        {
            "day": 4,
            "tasks": [
                "Continue working on multi-language support and SEO optimization",
                "Start testing and debugging the application"
            ]
        },
        {
            "day": 5,
            "tasks": [
                "Finish testing and debugging the application",
                "Start code review and ensure coding standards are met"
            ]
        },
        {
            "day": 6,
            "tasks": [
                "Deploy the application to production",
                "Ensure seamless deployment and scaling of the frontend application"
            ]
        },
        {
            "day": 7,
            "tasks": [
                "Monitor application performance and fix any issues that arise",
                "Continue to work on any remaining tasks or bugs"
            ]
        }
    ],
    "project_name": "test-ai-architecture",
    "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
    "phase_idx": 3,
    "phase_context_file": ".ai/.plan/.context/phase-3.context.blueprint.md"
}
```

# Phase 4 STEPS - Prompt:


            Analyze the attached Phase 4 Context Markdown content. 
            Translate every directive, objective, and daily task mentioned inside it into a structured day-by-day JSON map.
            
            --- PHASE 4 CONTEXT MARKDOWN ---
            ## PHASE 4 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
In Phase 4, the primary objective is to conduct comprehensive testing and quality assurance of the membership-hub project. This phase will ensure that the application meets the required standards, is free from defects, and provides a seamless user experience. The scope of this phase includes:

* Unit testing of individual components
* Integration testing of backend and frontend services
* User acceptance testing (UAT) to validate the application's functionality and usability
* Performance testing to ensure the application's scalability and responsiveness
* Security testing to identify and address potential vulnerabilities

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 4 includes:

* Testing frameworks: JUnit, Jest, and Cypress
* Testing tools: Postman, Selenium, and Apache JMeter
* Directory boundaries:
	+ `src/test/java`: Unit tests and integration tests for backend services
	+ `src/test/javascript`: Unit tests and integration tests for frontend services
	+ `cypress/integration`: End-to-end tests for frontend services
	+ `postman collections`: API tests for backend services
* Endpoints:
	+ `/api/v1/auth`: Authentication endpoints
	+ `/api/v1/users`: User management endpoints
	+ `/api/v1/centers`: Center management endpoints
	+ `/api/v1/attendances`: Attendance management endpoints

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 4:

* **Coder**: Develop test cases, implement testing frameworks, and write automated tests
* **Tester**: Execute manual tests, create test plans, and report defects
* **Reviewer**: Review test cases, provide feedback on testing strategies, and ensure testing coverage
* **DevOps**: Configure testing environments, deploy testing frameworks, and monitor testing pipelines

Specific tasks for each sub-agent:

* Coder:
	+ Develop unit tests for backend services using JUnit
	+ Implement integration tests for frontend services using Jest
* Tester:
	+ Create test plans for user acceptance testing (UAT)
	+ Execute manual tests for frontend and backend services
* Reviewer:
	+ Review test cases for coverage and effectiveness
	+ Provide feedback on testing strategies and frameworks
* DevOps:
	+ Configure testing environments for backend and frontend services
	+ Deploy testing frameworks and tools

#### 4. Phase Definition of Done (DoD)
The Definition of Done (DoD) for Phase 4 includes:

* All unit tests and integration tests have been executed and passed
* User acceptance testing (UAT) has been completed and validated
* Performance testing has been conducted and optimized
* Security testing has been performed and vulnerabilities have been addressed
* All defects have been reported, prioritized, and resolved
* Testing frameworks and tools have been configured and deployed
* Testing environments have been set up and validated

Upon completion of Phase 4, the application will have undergone rigorous testing and quality assurance, ensuring that it meets the required standards and provides a seamless user experience.
            ------------------------------------------

            Map your response strictly to the requested PhaseStepsPlan JSON structure.
            

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
{
    "phase": "Phase 4",
    "objectives": [
        "Conduct comprehensive testing and quality assurance of the membership-hub project",
        "Ensure the application meets the required standards, is free from defects, and provides a seamless user experience"
    ],
    "scope": [
        "Unit testing of individual components",
        "Integration testing of backend and frontend services",
        "User acceptance testing (UAT) to validate the application's functionality and usability",
        "Performance testing to ensure the application's scalability and responsiveness",
        "Security testing to identify and address potential vulnerabilities"
    ],
    "technicalScope": {
        "testingFrameworks": [
            "JUnit",
            "Jest",
            "Cypress"
        ],
        "testingTools": [
            "Postman",
            "Selenium",
            "Apache JMeter"
        ],
        "directoryBoundaries": {
            "unitTestsBackend": "src/test/java",
            "unitTestsFrontend": "src/test/javascript",
            "endToEndTestsFrontend": "cypress/integration",
            "apiTestsBackend": "postman collections"
        },
        "endpoints": [
            "/api/v1/auth",
            "/api/v1/users",
            "/api/v1/centers",
            "/api/v1/attendances"
        ]
    },
    "subAgents": {
        "Coder": {
            "tasks": [
                "Develop test cases",
                "Implement testing frameworks",
                "Write automated tests",
                "Develop unit tests for backend services using JUnit",
                "Implement integration tests for frontend services using Jest"
            ]
        },
        "Tester": {
            "tasks": [
                "Execute manual tests",
                "Create test plans",
                "Report defects",
                "Create test plans for user acceptance testing (UAT)",
                "Execute manual tests for frontend and backend services"
            ]
        },
        "Reviewer": {
            "tasks": [
                "Review test cases",
                "Provide feedback on testing strategies",
                "Ensure testing coverage",
                "Review test cases for coverage and effectiveness",
                "Provide feedback on testing strategies and frameworks"
            ]
        },
        "DevOps": {
            "tasks": [
                "Configure testing environments",
                "Deploy testing frameworks",
                "Monitor testing pipelines",
                "Configure testing environments for backend and frontend services",
                "Deploy testing frameworks and tools"
            ]
        }
    },
    "definitionOfDone": [
        "All unit tests and integration tests have been executed and passed",
        "User acceptance testing (UAT) has been completed and validated",
        "Performance testing has been conducted and optimized",
        "Security testing has been performed and vulnerabilities have been addressed",
        "All defects have been reported, prioritized, and resolved",
        "Testing frameworks and tools have been configured and deployed",
        "Testing environments have been set up and validated"
    ],
    "dayByDayPlan": [
        {
            "day": 1,
            "tasks": [
                "Coder: Develop test cases",
                "Tester: Create test plans",
                "Reviewer: Review test cases",
                "DevOps: Configure testing environments"
            ]
        },
        {
            "day": 2,
            "tasks": [
                "Coder: Implement testing frameworks",
                "Tester: Execute manual tests",
                "Reviewer: Provide feedback on testing strategies",
                "DevOps: Deploy testing frameworks"
            ]
        },
        {
            "day": 3,
            "tasks": [
                "Coder: Write automated tests",
                "Tester: Report defects",
                "Reviewer: Ensure testing coverage",
                "DevOps: Monitor testing pipelines"
            ]
        },
        {
            "day": 4,
            "tasks": [
                "Coder: Develop unit tests for backend services using JUnit",
                "Tester: Create test plans for user acceptance testing (UAT)",
                "Reviewer: Review test cases for coverage and effectiveness",
                "DevOps: Configure testing environments for backend and frontend services"
            ]
        },
        {
            "day": 5,
            "tasks": [
                "Coder: Implement integration tests for frontend services using Jest",
                "Tester: Execute manual tests for frontend and backend services",
                "Reviewer: Provide feedback on testing strategies and frameworks",
                "DevOps: Deploy testing frameworks and tools"
            ]
        }
    ],
    "project_name": "test-ai-architecture",
    "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
    "phase_idx": 4,
    "phase_context_file": ".ai/.plan/.context/phase-4.context.blueprint.md"
}
```

# Phase 5 STEPS - Prompt:


            Analyze the attached Phase 5 Context Markdown content. 
            Translate every directive, objective, and daily task mentioned inside it into a structured day-by-day JSON map.
            
            --- PHASE 5 CONTEXT MARKDOWN ---
            ## PHASE 5 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 5 is to deploy the membership-hub application to production, ensuring a smooth and efficient deployment process. This phase will focus on deploying the application to Google Cloud Platform (GCP) and Google Kubernetes Engine (GKE), configuring load balancing and auto-scaling, and setting up monitoring and logging tools. Additionally, this phase will involve conducting final testing, including user acceptance testing (UAT) and performance testing, to ensure the application meets the required standards.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 5 includes:
* Deploying the application to GCP and GKE
* Configuring load balancing and auto-scaling
* Setting up monitoring and logging tools (e.g., Prometheus, Grafana, ELK Stack)
* Conducting final testing (UAT, performance testing)
* Ensuring compliance with security, data privacy, and scalability requirements
* Directory boundaries:
	+ Deployment scripts: `deploy/scripts`
	+ Kubernetes configurations: `deploy/k8s`
	+ Monitoring and logging configurations: `deploy/monitoring`
	+ Test scripts: `test/deployment`

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
* **Coder**: Assist in deployment scripting, configure load balancing and auto-scaling, and ensure compliance with security and scalability requirements.
* **Tester**: Conduct final testing, including UAT and performance testing, and report any defects or issues.
* **Reviewer**: Review deployment scripts, Kubernetes configurations, and monitoring and logging setups to ensure they meet the required standards.
* **Docker**: Ensure seamless deployment and scaling of the application by configuring Docker images and containers.
* **Deployer**: Manage the deployment process, ensuring smooth and efficient deployment of the application to production environments.

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 5 includes:
* Successful deployment of the application to GCP and GKE
* Configuration of load balancing and auto-scaling
* Setup of monitoring and logging tools
* Completion of final testing (UAT, performance testing)
* Resolution of all defects or issues reported during testing
* Confirmation that the application meets all security, data privacy, and scalability requirements
* Handover of the deployed application to the operations team for ongoing maintenance and support.
            ------------------------------------------

            Map your response strictly to the requested PhaseStepsPlan JSON structure.
            

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
{
    "phase": "Phase 5",
    "objectives": [
        "Deploy the membership-hub application to production",
        "Ensure a smooth and efficient deployment process",
        "Configure load balancing and auto-scaling",
        "Set up monitoring and logging tools",
        "Conduct final testing, including user acceptance testing (UAT) and performance testing"
    ],
    "dailyTasks": [
        {
            "day": 1,
            "tasks": [
                {
                    "task": "Initialize deployment scripts",
                    "assignee": "Coder",
                    "directory": "deploy/scripts"
                },
                {
                    "task": "Configure Kubernetes environments",
                    "assignee": "Coder",
                    "directory": "deploy/k8s"
                }
            ]
        },
        {
            "day": 2,
            "tasks": [
                {
                    "task": "Configure load balancing and auto-scaling",
                    "assignee": "Coder",
                    "directory": "deploy/k8s"
                },
                {
                    "task": "Set up monitoring tools (Prometheus, Grafana)",
                    "assignee": "Coder",
                    "directory": "deploy/monitoring"
                }
            ]
        },
        {
            "day": 3,
            "tasks": [
                {
                    "task": "Set up logging tools (ELK Stack)",
                    "assignee": "Coder",
                    "directory": "deploy/monitoring"
                },
                {
                    "task": "Prepare test scripts for UAT and performance testing",
                    "assignee": "Tester",
                    "directory": "test/deployment"
                }
            ]
        },
        {
            "day": 4,
            "tasks": [
                {
                    "task": "Conduct UAT",
                    "assignee": "Tester",
                    "directory": "test/deployment"
                },
                {
                    "task": "Conduct performance testing",
                    "assignee": "Tester",
                    "directory": "test/deployment"
                }
            ]
        },
        {
            "day": 5,
            "tasks": [
                {
                    "task": "Review deployment scripts and Kubernetes configurations",
                    "assignee": "Reviewer",
                    "directory": "deploy/scripts"
                },
                {
                    "task": "Review monitoring and logging setups",
                    "assignee": "Reviewer",
                    "directory": "deploy/monitoring"
                }
            ]
        },
        {
            "day": 6,
            "tasks": [
                {
                    "task": "Configure Docker images and containers",
                    "assignee": "Docker",
                    "directory": "deploy/k8s"
                },
                {
                    "task": "Manage deployment process",
                    "assignee": "Deployer",
                    "directory": "deploy/scripts"
                }
            ]
        },
        {
            "day": 7,
            "tasks": [
                {
                    "task": "Resolve defects or issues reported during testing",
                    "assignee": "Coder",
                    "directory": "deploy/scripts"
                },
                {
                    "task": "Confirm application meets security, data privacy, and scalability requirements",
                    "assignee": "Coder",
                    "directory": "deploy/k8s"
                }
            ]
        }
    ],
    "definitionOfDone": [
        "Successful deployment of the application to GCP and GKE",
        "Configuration of load balancing and auto-scaling",
        "Setup of monitoring and logging tools",
        "Completion of final testing (UAT, performance testing)",
        "Resolution of all defects or issues reported during testing",
        "Confirmation that the application meets all security, data privacy, and scalability requirements",
        "Handover of the deployed application to the operations team for ongoing maintenance and support"
    ],
    "project_name": "test-ai-architecture",
    "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
    "phase_idx": 5,
    "phase_context_file": ".ai/.plan/.context/phase-5.context.blueprint.md"
}
```

# Global Prompt:


        Analyze the attached project requirements. Build the GLOBAL PROJECT CONTEXT for 'test-ai-architecture'.
        
        --- RAW REQUIREMENTS ---
        ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

        --- END REQUIREMENTS ---

        Your output MUST follow this exact structure:
        ## GLOBAL PROJECT CONTEXT: test-ai-architecture
        #### 1. Executive Summary & Tech Stack Blueprint
        #### 2. Global Guardrails & Enterprise Compliance Standards
        #### 3. Standardized Sub-Agent Persona Definitions (Manager, Coder, Tester, Reviewer, Docker, Deployer)
        #### 4. Multi-Phase Segmentation Strategy Overview (Plan exactly 5 phases)
        

# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable web and mobile application designed to manage students across multiple centers. The tech stack includes Quarkus, Kafka, Postgres, and Docker, with deployment on GCP and GKE. The application supports internal authentication via email/password, Firebase, Google, and Facebook, and manages user login and registration. The project utilizes Next.js for the mobile frontend, supporting multiple languages and building for both iOS and Android. Key features include QR code-based attendance tracking, notification systems, and SEO optimization for both web and mobile platforms.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to industry standards, the following guardrails and compliance standards will be implemented:
- **Security**: Implement OAuth 2.0 for authentication, use HTTPS for encryption, and follow OWASP guidelines for secure coding practices.
- **Scalability**: Design the system to scale horizontally, utilizing load balancers and auto-scaling groups in GKE.
- **Data Management**: Use Postgres for relational data storage and Kafka for event-driven architecture, ensuring data consistency and integrity.
- **Compliance**: Adhere to GDPR for user data protection, and follow accessibility guidelines (WCAG 2.1) for the web and mobile applications.
- **Monitoring and Logging**: Implement logging and monitoring tools (e.g., Prometheus, Grafana) to track system performance and identify potential issues.

#### 3. Standardized Sub-Agent Persona Definitions
The following personas will be involved in the project:
- **Manager**: Oversees the project timeline, budget, and resource allocation. Ensures that the project is delivered on time and within budget.
- **Coder**: Responsible for writing clean, efficient, and well-documented code. Collaborates with the team to implement new features and fix bugs.
- **Tester**: Develops and executes comprehensive test plans to ensure the application meets the required standards. Reports defects and collaborates with the development team to resolve issues.
- **Reviewer**: Conducts code reviews to ensure that the code meets the project's coding standards and best practices. Provides feedback to the development team to improve code quality.
- **Docker**: Responsible for creating and maintaining Docker images for the application, ensuring that the images are optimized for production environments.
- **Deployer**: Manages the deployment of the application to GKE, ensuring that the deployment is smooth and that the application is properly configured for production.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into the following five phases:
- **Phase 1: Planning and Design** (Weeks 1-4): Define the project scope, create a detailed design document, and develop a prototype to validate the project's feasibility.
- **Phase 2: Backend Development** (Weeks 5-12): Develop the backend API using Quarkus, implement authentication and authorization, and integrate with Kafka and Postgres.
- **Phase 3: Mobile Frontend Development** (Weeks 13-18): Develop the mobile frontend using Next.js, implement features such as QR code scanning and notification systems.
- **Phase 4: Testing and Quality Assurance** (Weeks 19-22): Conduct unit testing, integration testing, and UI testing to ensure that the application meets the required standards.
- **Phase 5: Deployment and Maintenance** (Weeks 23-26): Deploy the application to GKE, configure monitoring and logging tools, and ensure that the application is properly maintained and updated to meet changing requirements.
```

# Phase 1 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 1 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable web and mobile application designed to manage students across multiple centers. The tech stack includes Quarkus, Kafka, Postgres, and Docker, with deployment on GCP and GKE. The application supports internal authentication via email/password, Firebase, Google, and Facebook, and manages user login and registration. The project utilizes Next.js for the mobile frontend, supporting multiple languages and building for both iOS and Android. Key features include QR code-based attendance tracking, notification systems, and SEO optimization for both web and mobile platforms.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to industry standards, the following guardrails and compliance standards will be implemented:
- **Security**: Implement OAuth 2.0 for authentication, use HTTPS for encryption, and follow OWASP guidelines for secure coding practices.
- **Scalability**: Design the system to scale horizontally, utilizing load balancers and auto-scaling groups in GKE.
- **Data Management**: Use Postgres for relational data storage and Kafka for event-driven architecture, ensuring data consistency and integrity.
- **Compliance**: Adhere to GDPR for user data protection, and follow accessibility guidelines (WCAG 2.1) for the web and mobile applications.
- **Monitoring and Logging**: Implement logging and monitoring tools (e.g., Prometheus, Grafana) to track system performance and identify potential issues.

#### 3. Standardized Sub-Agent Persona Definitions
The following personas will be involved in the project:
- **Manager**: Oversees the project timeline, budget, and resource allocation. Ensures that the project is delivered on time and within budget.
- **Coder**: Responsible for writing clean, efficient, and well-documented code. Collaborates with the team to implement new features and fix bugs.
- **Tester**: Develops and executes comprehensive test plans to ensure the application meets the required standards. Reports defects and collaborates with the development team to resolve issues.
- **Reviewer**: Conducts code reviews to ensure that the code meets the project's coding standards and best practices. Provides feedback to the development team to improve code quality.
- **Docker**: Responsible for creating and maintaining Docker images for the application, ensuring that the images are optimized for production environments.
- **Deployer**: Manages the deployment of the application to GKE, ensuring that the deployment is smooth and that the application is properly configured for production.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into the following five phases:
- **Phase 1: Planning and Design** (Weeks 1-4): Define the project scope, create a detailed design document, and develop a prototype to validate the project's feasibility.
- **Phase 2: Backend Development** (Weeks 5-12): Develop the backend API using Quarkus, implement authentication and authorization, and integrate with Kafka and Postgres.
- **Phase 3: Mobile Frontend Development** (Weeks 13-18): Develop the mobile frontend using Next.js, implement features such as QR code scanning and notification systems.
- **Phase 4: Testing and Quality Assurance** (Weeks 19-22): Conduct unit testing, integration testing, and UI testing to ensure that the application meets the required standards.
- **Phase 5: Deployment and Maintenance** (Weeks 23-26): Deploy the application to GKE, configure monitoring and logging tools, and ensure that the application is properly maintained and updated to meet changing requirements.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------

            Your output MUST follow this exact Markdown structure for Phase 1:
            ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed design document, and develop a prototype to validate the project's feasibility. This phase will focus on planning and design, ensuring that all stakeholders are aligned and that the project is set up for success. The key deliverables for this phase include:
- A detailed project scope statement
- A comprehensive design document outlining the architecture and technical requirements
- A functional prototype to demonstrate the project's core features
- A project timeline and resource allocation plan

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
For Phase 1, the technical scope will be limited to the following areas:
- Project structure and organization
- Technology stack selection and validation (Quarkus, Kafka, Postgres, Docker, GCP, GKE, Next.js)
- High-level architecture design (microservices, event-driven architecture)
- Prototype development (focused on core features such as user authentication, QR code scanning, and notification systems)
- Directory boundaries:
  - `docs/`: Design documents, project scope statement, and prototype plans
  - `proto/`: Prototype code and related assets
  - `research/`: Technology stack research and validation notes
  - `meetings/`: Meeting minutes and discussion notes

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 1, with the following responsibilities:
- **Coder**: Develop the prototype, focusing on core features and technical requirements. Collaborate with the Reviewer to ensure code quality and adherence to best practices.
- **Tester**: Develop a test plan for the prototype, focusing on core features and user workflows. Identify and report defects, collaborating with the Coder to resolve issues.
- **Reviewer**: Conduct code reviews for the prototype, ensuring that the code meets the project's coding standards and best practices. Provide feedback to the Coder to improve code quality.
- **DevOps (Docker, Deployer)**: Research and validate the technology stack, focusing on Docker, GCP, and GKE. Develop a deployment plan for the prototype, ensuring that it can be easily deployed and scaled.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- A detailed project scope statement has been approved by all stakeholders
- A comprehensive design document has been completed and reviewed by the team
- A functional prototype has been developed and tested, demonstrating the project's core features
- A project timeline and resource allocation plan have been developed and approved by all stakeholders
- The prototype has been deployed to a staging environment, and the deployment plan has been validated
- All sub-agents have completed their assigned tasks and have provided feedback and approval for the phase's deliverables.
```

# Phase 2 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 2 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable web and mobile application designed to manage students across multiple centers. The tech stack includes Quarkus, Kafka, Postgres, and Docker, with deployment on GCP and GKE. The application supports internal authentication via email/password, Firebase, Google, and Facebook, and manages user login and registration. The project utilizes Next.js for the mobile frontend, supporting multiple languages and building for both iOS and Android. Key features include QR code-based attendance tracking, notification systems, and SEO optimization for both web and mobile platforms.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to industry standards, the following guardrails and compliance standards will be implemented:
- **Security**: Implement OAuth 2.0 for authentication, use HTTPS for encryption, and follow OWASP guidelines for secure coding practices.
- **Scalability**: Design the system to scale horizontally, utilizing load balancers and auto-scaling groups in GKE.
- **Data Management**: Use Postgres for relational data storage and Kafka for event-driven architecture, ensuring data consistency and integrity.
- **Compliance**: Adhere to GDPR for user data protection, and follow accessibility guidelines (WCAG 2.1) for the web and mobile applications.
- **Monitoring and Logging**: Implement logging and monitoring tools (e.g., Prometheus, Grafana) to track system performance and identify potential issues.

#### 3. Standardized Sub-Agent Persona Definitions
The following personas will be involved in the project:
- **Manager**: Oversees the project timeline, budget, and resource allocation. Ensures that the project is delivered on time and within budget.
- **Coder**: Responsible for writing clean, efficient, and well-documented code. Collaborates with the team to implement new features and fix bugs.
- **Tester**: Develops and executes comprehensive test plans to ensure the application meets the required standards. Reports defects and collaborates with the development team to resolve issues.
- **Reviewer**: Conducts code reviews to ensure that the code meets the project's coding standards and best practices. Provides feedback to the development team to improve code quality.
- **Docker**: Responsible for creating and maintaining Docker images for the application, ensuring that the images are optimized for production environments.
- **Deployer**: Manages the deployment of the application to GKE, ensuring that the deployment is smooth and that the application is properly configured for production.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into the following five phases:
- **Phase 1: Planning and Design** (Weeks 1-4): Define the project scope, create a detailed design document, and develop a prototype to validate the project's feasibility.
- **Phase 2: Backend Development** (Weeks 5-12): Develop the backend API using Quarkus, implement authentication and authorization, and integrate with Kafka and Postgres.
- **Phase 3: Mobile Frontend Development** (Weeks 13-18): Develop the mobile frontend using Next.js, implement features such as QR code scanning and notification systems.
- **Phase 4: Testing and Quality Assurance** (Weeks 19-22): Conduct unit testing, integration testing, and UI testing to ensure that the application meets the required standards.
- **Phase 5: Deployment and Maintenance** (Weeks 23-26): Deploy the application to GKE, configure monitoring and logging tools, and ensure that the application is properly maintained and updated to meet changing requirements.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------

            Your output MUST follow this exact Markdown structure for Phase 2:
            ## PHASE 2 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 2 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 2 is to develop the backend API using Quarkus, implementing authentication and authorization, and integrating with Kafka and Postgres. This phase will focus on building a scalable and secure backend infrastructure to support the membership-hub project. The key deliverables include:

* Design and implementation of the backend API using Quarkus
* Integration with Kafka for event-driven architecture
* Integration with Postgres for relational data storage
* Implementation of authentication and authorization using OAuth 2.0
* Development of API endpoints for user management, attendance tracking, and notification systems

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 2 includes:

* Backend API development using Quarkus (Java or Kotlin)
* Integration with Kafka and Postgres
* Implementation of OAuth 2.0 for authentication and authorization
* Development of API endpoints using RESTful architecture
* Use of Docker for containerization
* Deployment on GCP and GKE

Directory boundaries:

* `src/main/java`: Quarkus backend API code
* `src/main/resources`: Configuration files and properties
* `src/test/java`: Unit tests and integration tests
* `docker`: Dockerfile and containerization scripts
* `kafka`: Kafka configuration and integration code
* `postgres`: Postgres configuration and integration code

Endpoints:

* `/api/v1/users`: User management endpoints (e.g., create, read, update, delete)
* `/api/v1/attendance`: Attendance tracking endpoints (e.g., record attendance, get attendance history)
* `/api/v1/notifications`: Notification system endpoints (e.g., send notifications, get notification history)

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 2:

* **Coder**: Responsible for developing the backend API using Quarkus, integrating with Kafka and Postgres, and implementing authentication and authorization.
* **Tester**: Responsible for developing unit tests and integration tests for the backend API, ensuring that the API endpoints are working correctly and securely.
* **Reviewer**: Responsible for reviewing the code developed by the Coder, ensuring that it meets the project's coding standards and best practices.
* **DevOps**: Responsible for creating and maintaining Docker images for the backend API, ensuring that the images are optimized for production environments, and deploying the API to GKE.

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 2 includes:

* The backend API is fully implemented and tested
* All API endpoints are working correctly and securely
* Integration with Kafka and Postgres is complete and tested
* Authentication and authorization are fully implemented and tested
* Docker images are created and optimized for production environments
* The backend API is deployed to GKE and configured for production
* All unit tests and integration tests are passing
* Code reviews are complete and all feedback is addressed
* Deployment scripts and configuration files are updated and tested
```

# Phase 3 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 3 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable web and mobile application designed to manage students across multiple centers. The tech stack includes Quarkus, Kafka, Postgres, and Docker, with deployment on GCP and GKE. The application supports internal authentication via email/password, Firebase, Google, and Facebook, and manages user login and registration. The project utilizes Next.js for the mobile frontend, supporting multiple languages and building for both iOS and Android. Key features include QR code-based attendance tracking, notification systems, and SEO optimization for both web and mobile platforms.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to industry standards, the following guardrails and compliance standards will be implemented:
- **Security**: Implement OAuth 2.0 for authentication, use HTTPS for encryption, and follow OWASP guidelines for secure coding practices.
- **Scalability**: Design the system to scale horizontally, utilizing load balancers and auto-scaling groups in GKE.
- **Data Management**: Use Postgres for relational data storage and Kafka for event-driven architecture, ensuring data consistency and integrity.
- **Compliance**: Adhere to GDPR for user data protection, and follow accessibility guidelines (WCAG 2.1) for the web and mobile applications.
- **Monitoring and Logging**: Implement logging and monitoring tools (e.g., Prometheus, Grafana) to track system performance and identify potential issues.

#### 3. Standardized Sub-Agent Persona Definitions
The following personas will be involved in the project:
- **Manager**: Oversees the project timeline, budget, and resource allocation. Ensures that the project is delivered on time and within budget.
- **Coder**: Responsible for writing clean, efficient, and well-documented code. Collaborates with the team to implement new features and fix bugs.
- **Tester**: Develops and executes comprehensive test plans to ensure the application meets the required standards. Reports defects and collaborates with the development team to resolve issues.
- **Reviewer**: Conducts code reviews to ensure that the code meets the project's coding standards and best practices. Provides feedback to the development team to improve code quality.
- **Docker**: Responsible for creating and maintaining Docker images for the application, ensuring that the images are optimized for production environments.
- **Deployer**: Manages the deployment of the application to GKE, ensuring that the deployment is smooth and that the application is properly configured for production.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into the following five phases:
- **Phase 1: Planning and Design** (Weeks 1-4): Define the project scope, create a detailed design document, and develop a prototype to validate the project's feasibility.
- **Phase 2: Backend Development** (Weeks 5-12): Develop the backend API using Quarkus, implement authentication and authorization, and integrate with Kafka and Postgres.
- **Phase 3: Mobile Frontend Development** (Weeks 13-18): Develop the mobile frontend using Next.js, implement features such as QR code scanning and notification systems.
- **Phase 4: Testing and Quality Assurance** (Weeks 19-22): Conduct unit testing, integration testing, and UI testing to ensure that the application meets the required standards.
- **Phase 5: Deployment and Maintenance** (Weeks 23-26): Deploy the application to GKE, configure monitoring and logging tools, and ensure that the application is properly maintained and updated to meet changing requirements.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------

            Your output MUST follow this exact Markdown structure for Phase 3:
            ## PHASE 3 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 3 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
In Phase 3, the primary objective is to develop the mobile frontend of the membership-hub application using Next.js. This phase will focus on implementing features such as QR code scanning, notification systems, and multi-language support. The scope of this phase includes designing and developing the mobile frontend, ensuring it is scalable, and integrating it with the backend API developed in Phase 2.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 3 includes:
- Developing the mobile frontend using Next.js
- Implementing QR code scanning and notification systems
- Integrating with the backend API for authentication and data management
- Ensuring multi-language support and building for both iOS and Android
- Directory boundaries:
  - `mobile/frontend`: Next.js frontend code
  - `mobile/backend`: Backend API integration and notification systems
  - `mobile/assets`: QR code scanning and other mobile-specific assets
- Endpoints:
  - `/mobile/login`: Mobile login endpoint
  - `/mobile/qr_scan`: QR code scanning endpoint
  - `/mobile/notifications`: Notification systems endpoint

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
- **Coder**: Develop the mobile frontend using Next.js, implement QR code scanning and notification systems, and integrate with the backend API.
- **Tester**: Develop and execute comprehensive test plans for the mobile frontend, including unit testing, integration testing, and UI testing.
- **Reviewer**: Conduct code reviews to ensure the mobile frontend code meets the project's coding standards and best practices.
- **DevOps (Docker)**: Create and maintain Docker images for the mobile frontend, ensuring they are optimized for production environments.
- **DevOps (Deployer)**: Assist in deploying the mobile frontend to GKE, ensuring a smooth deployment process.

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 3 includes:
- The mobile frontend is fully developed and integrated with the backend API.
- QR code scanning and notification systems are implemented and functional.
- Multi-language support is implemented, and the application is built for both iOS and Android.
- Comprehensive testing has been completed, and all defects have been resolved.
- Code reviews have been completed, and the code meets the project's coding standards and best practices.
- Docker images are created and optimized for production environments.
- The mobile frontend is deployed to GKE, and the deployment is verified to be successful.
```

# Phase 4 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 4 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable web and mobile application designed to manage students across multiple centers. The tech stack includes Quarkus, Kafka, Postgres, and Docker, with deployment on GCP and GKE. The application supports internal authentication via email/password, Firebase, Google, and Facebook, and manages user login and registration. The project utilizes Next.js for the mobile frontend, supporting multiple languages and building for both iOS and Android. Key features include QR code-based attendance tracking, notification systems, and SEO optimization for both web and mobile platforms.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to industry standards, the following guardrails and compliance standards will be implemented:
- **Security**: Implement OAuth 2.0 for authentication, use HTTPS for encryption, and follow OWASP guidelines for secure coding practices.
- **Scalability**: Design the system to scale horizontally, utilizing load balancers and auto-scaling groups in GKE.
- **Data Management**: Use Postgres for relational data storage and Kafka for event-driven architecture, ensuring data consistency and integrity.
- **Compliance**: Adhere to GDPR for user data protection, and follow accessibility guidelines (WCAG 2.1) for the web and mobile applications.
- **Monitoring and Logging**: Implement logging and monitoring tools (e.g., Prometheus, Grafana) to track system performance and identify potential issues.

#### 3. Standardized Sub-Agent Persona Definitions
The following personas will be involved in the project:
- **Manager**: Oversees the project timeline, budget, and resource allocation. Ensures that the project is delivered on time and within budget.
- **Coder**: Responsible for writing clean, efficient, and well-documented code. Collaborates with the team to implement new features and fix bugs.
- **Tester**: Develops and executes comprehensive test plans to ensure the application meets the required standards. Reports defects and collaborates with the development team to resolve issues.
- **Reviewer**: Conducts code reviews to ensure that the code meets the project's coding standards and best practices. Provides feedback to the development team to improve code quality.
- **Docker**: Responsible for creating and maintaining Docker images for the application, ensuring that the images are optimized for production environments.
- **Deployer**: Manages the deployment of the application to GKE, ensuring that the deployment is smooth and that the application is properly configured for production.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into the following five phases:
- **Phase 1: Planning and Design** (Weeks 1-4): Define the project scope, create a detailed design document, and develop a prototype to validate the project's feasibility.
- **Phase 2: Backend Development** (Weeks 5-12): Develop the backend API using Quarkus, implement authentication and authorization, and integrate with Kafka and Postgres.
- **Phase 3: Mobile Frontend Development** (Weeks 13-18): Develop the mobile frontend using Next.js, implement features such as QR code scanning and notification systems.
- **Phase 4: Testing and Quality Assurance** (Weeks 19-22): Conduct unit testing, integration testing, and UI testing to ensure that the application meets the required standards.
- **Phase 5: Deployment and Maintenance** (Weeks 23-26): Deploy the application to GKE, configure monitoring and logging tools, and ensure that the application is properly maintained and updated to meet changing requirements.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------

            Your output MUST follow this exact Markdown structure for Phase 4:
            ## PHASE 4 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 4 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 4 is to ensure the quality and reliability of the membership-hub application through comprehensive testing and quality assurance. This phase will focus on conducting unit testing, integration testing, and UI testing to identify and resolve any defects or issues. The scope of this phase includes:

* Testing the backend API using Quarkus, Kafka, and Postgres
* Testing the mobile frontend using Next.js
* Testing the authentication and authorization mechanisms
* Testing the QR code scanning and notification systems
* Testing the SEO optimization for both web and mobile platforms

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope of this phase includes:

* Testing frameworks such as JUnit, Jest, and Enzyme
* Testing libraries such as Mockito and Hamcrest
* API testing tools such as Postman and Swagger
* UI testing frameworks such as Selenium and Appium
* Directory boundaries:
	+ Backend API: `src/main/java` and `src/main/resources`
	+ Mobile frontend: `src/mobile` and `src/components`
	+ Testing: `src/test/java` and `src/test/javascript`
* Endpoints:
	+ Backend API: `/api/*`
	+ Mobile frontend: `/mobile/*`

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in this phase:

* **Coder**: Responsible for writing unit tests and integration tests for the backend API and mobile frontend.
* **Tester**: Responsible for developing and executing comprehensive test plans, including UI testing and API testing.
* **Reviewer**: Responsible for reviewing test cases and providing feedback to the development team.
* **DevOps**: Responsible for setting up and configuring testing environments, including Docker and Kubernetes.

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 4 includes:

* All unit tests and integration tests have been written and executed successfully
* All UI tests have been executed successfully
* All defects and issues have been identified and resolved
* The application has been tested for scalability, security, and performance
* The testing environment has been set up and configured correctly
* All test cases have been reviewed and approved by the Reviewer
* The application has been verified to meet the requirements and specifications outlined in the Raw Requirements Reference.
```

# Phase 5 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 5 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable web and mobile application designed to manage students across multiple centers. The tech stack includes Quarkus, Kafka, Postgres, and Docker, with deployment on GCP and GKE. The application supports internal authentication via email/password, Firebase, Google, and Facebook, and manages user login and registration. The project utilizes Next.js for the mobile frontend, supporting multiple languages and building for both iOS and Android. Key features include QR code-based attendance tracking, notification systems, and SEO optimization for both web and mobile platforms.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to industry standards, the following guardrails and compliance standards will be implemented:
- **Security**: Implement OAuth 2.0 for authentication, use HTTPS for encryption, and follow OWASP guidelines for secure coding practices.
- **Scalability**: Design the system to scale horizontally, utilizing load balancers and auto-scaling groups in GKE.
- **Data Management**: Use Postgres for relational data storage and Kafka for event-driven architecture, ensuring data consistency and integrity.
- **Compliance**: Adhere to GDPR for user data protection, and follow accessibility guidelines (WCAG 2.1) for the web and mobile applications.
- **Monitoring and Logging**: Implement logging and monitoring tools (e.g., Prometheus, Grafana) to track system performance and identify potential issues.

#### 3. Standardized Sub-Agent Persona Definitions
The following personas will be involved in the project:
- **Manager**: Oversees the project timeline, budget, and resource allocation. Ensures that the project is delivered on time and within budget.
- **Coder**: Responsible for writing clean, efficient, and well-documented code. Collaborates with the team to implement new features and fix bugs.
- **Tester**: Develops and executes comprehensive test plans to ensure the application meets the required standards. Reports defects and collaborates with the development team to resolve issues.
- **Reviewer**: Conducts code reviews to ensure that the code meets the project's coding standards and best practices. Provides feedback to the development team to improve code quality.
- **Docker**: Responsible for creating and maintaining Docker images for the application, ensuring that the images are optimized for production environments.
- **Deployer**: Manages the deployment of the application to GKE, ensuring that the deployment is smooth and that the application is properly configured for production.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into the following five phases:
- **Phase 1: Planning and Design** (Weeks 1-4): Define the project scope, create a detailed design document, and develop a prototype to validate the project's feasibility.
- **Phase 2: Backend Development** (Weeks 5-12): Develop the backend API using Quarkus, implement authentication and authorization, and integrate with Kafka and Postgres.
- **Phase 3: Mobile Frontend Development** (Weeks 13-18): Develop the mobile frontend using Next.js, implement features such as QR code scanning and notification systems.
- **Phase 4: Testing and Quality Assurance** (Weeks 19-22): Conduct unit testing, integration testing, and UI testing to ensure that the application meets the required standards.
- **Phase 5: Deployment and Maintenance** (Weeks 23-26): Deploy the application to GKE, configure monitoring and logging tools, and ensure that the application is properly maintained and updated to meet changing requirements.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------

            Your output MUST follow this exact Markdown structure for Phase 5:
            ## PHASE 5 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 5 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 5 is to deploy the membership-hub application to Google Kubernetes Engine (GKE) and ensure its proper maintenance and updates to meet changing requirements. This phase involves configuring monitoring and logging tools, deploying the application, and performing post-deployment testing to guarantee the application's stability and performance.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 5 includes:
- Deployment scripts and configurations for GKE
- Docker image creation and optimization for production environments
- Configuration of monitoring and logging tools such as Prometheus and Grafana
- Setup of load balancers and auto-scaling groups for horizontal scaling
- Security configurations, including OAuth 2.0 and HTTPS encryption
- Directory boundaries:
  - Deployment scripts: `/deploy`
  - Docker configurations: `/docker`
  - Monitoring and logging tools: `/monitoring`
  - Security configurations: `/security`
- Endpoints:
  - API endpoints for user authentication and authorization
  - API endpoints for QR code scanning and attendance tracking
  - API endpoints for notification systems

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
- **Coder**: Focus on creating deployment scripts, configuring Docker images for production, and implementing security measures.
- **Tester**: Conduct post-deployment testing to ensure the application's stability and performance. Test the deployment, monitoring, and logging configurations.
- **Reviewer**: Review the deployment scripts, Docker configurations, and security measures to ensure they meet the project's coding standards and best practices.
- **Docker**: Create and maintain Docker images for the application, ensuring they are optimized for production environments.
- **Deployer (DevOps)**: Manage the deployment of the application to GKE, configure monitoring and logging tools, and ensure the application is properly configured for production.

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 5 includes:
- The application is successfully deployed to GKE.
- Monitoring and logging tools are configured and functioning correctly.
- Security measures, including OAuth 2.0 and HTTPS encryption, are implemented and tested.
- Post-deployment testing has been conducted, and the application's stability and performance have been verified.
- Deployment scripts, Docker configurations, and security measures have been reviewed and approved.
- The application is properly configured for production, and all necessary settings have been applied.
- Documentation for deployment, monitoring, and maintenance has been updated and is available to the team.
```

# Phase 1 STEPS - Prompt:


            Analyze the attached Phase 1 Context Markdown content. 
            Translate every directive, objective, and daily task mentioned inside it into a structured day-by-day JSON map.
            
            --- PHASE 1 CONTEXT MARKDOWN ---
            ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed design document, and develop a prototype to validate the project's feasibility. This phase will focus on planning and design, ensuring that all stakeholders are aligned and that the project is set up for success. The key deliverables for this phase include:
- A detailed project scope statement
- A comprehensive design document outlining the architecture and technical requirements
- A functional prototype to demonstrate the project's core features
- A project timeline and resource allocation plan

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
For Phase 1, the technical scope will be limited to the following areas:
- Project structure and organization
- Technology stack selection and validation (Quarkus, Kafka, Postgres, Docker, GCP, GKE, Next.js)
- High-level architecture design (microservices, event-driven architecture)
- Prototype development (focused on core features such as user authentication, QR code scanning, and notification systems)
- Directory boundaries:
  - `docs/`: Design documents, project scope statement, and prototype plans
  - `proto/`: Prototype code and related assets
  - `research/`: Technology stack research and validation notes
  - `meetings/`: Meeting minutes and discussion notes

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 1, with the following responsibilities:
- **Coder**: Develop the prototype, focusing on core features and technical requirements. Collaborate with the Reviewer to ensure code quality and adherence to best practices.
- **Tester**: Develop a test plan for the prototype, focusing on core features and user workflows. Identify and report defects, collaborating with the Coder to resolve issues.
- **Reviewer**: Conduct code reviews for the prototype, ensuring that the code meets the project's coding standards and best practices. Provide feedback to the Coder to improve code quality.
- **DevOps (Docker, Deployer)**: Research and validate the technology stack, focusing on Docker, GCP, and GKE. Develop a deployment plan for the prototype, ensuring that it can be easily deployed and scaled.

#### 4. Phase Definition of Done (DoD)
Phase 1 will be considered complete when the following criteria are met:
- A detailed project scope statement has been approved by all stakeholders
- A comprehensive design document has been completed and reviewed by the team
- A functional prototype has been developed and tested, demonstrating the project's core features
- A project timeline and resource allocation plan have been developed and approved by all stakeholders
- The prototype has been deployed to a staging environment, and the deployment plan has been validated
- All sub-agents have completed their assigned tasks and have provided feedback and approval for the phase's deliverables.
            ------------------------------------------

            Map your response strictly to the requested PhaseStepsPlan JSON structure.
            

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
{
    "phase": "Phase 1",
    "context": "test-ai-architecture",
    "objectives": [
        "Define project scope",
        "Create detailed design document",
        "Develop prototype to validate project feasibility",
        "Ensure stakeholder alignment and project setup for success"
    ],
    "deliverables": [
        "Detailed project scope statement",
        "Comprehensive design document",
        "Functional prototype",
        "Project timeline and resource allocation plan"
    ],
    "technicalScope": {
        "areas": [
            "Project structure and organization",
            "Technology stack selection and validation",
            "High-level architecture design",
            "Prototype development"
        ],
        "directoryBoundaries": {
            "docs": "Design documents, project scope statement, and prototype plans",
            "proto": "Prototype code and related assets",
            "research": "Technology stack research and validation notes",
            "meetings": "Meeting minutes and discussion notes"
        }
    },
    "subAgents": [
        {
            "role": "Coder",
            "responsibilities": [
                "Develop prototype",
                "Focus on core features and technical requirements",
                "Collaborate with Reviewer for code quality and best practices"
            ]
        },
        {
            "role": "Tester",
            "responsibilities": [
                "Develop test plan for prototype",
                "Focus on core features and user workflows",
                "Identify and report defects",
                "Collaborate with Coder to resolve issues"
            ]
        },
        {
            "role": "Reviewer",
            "responsibilities": [
                "Conduct code reviews for prototype",
                "Ensure code meets project coding standards and best practices",
                "Provide feedback to Coder for code quality improvement"
            ]
        },
        {
            "role": "DevOps",
            "responsibilities": [
                "Research and validate technology stack",
                "Focus on Docker, GCP, and GKE",
                "Develop deployment plan for prototype"
            ]
        }
    ],
    "definitionOfDone": [
        "Detailed project scope statement approved by stakeholders",
        "Comprehensive design document completed and reviewed",
        "Functional prototype developed and tested",
        "Project timeline and resource allocation plan developed and approved",
        "Prototype deployed to staging environment",
        "All sub-agents complete assigned tasks and provide feedback and approval"
    ],
    "dayByDayPlan": [
        {
            "day": 1,
            "tasks": [
                "Define project scope",
                "Create detailed design document outline"
            ],
            "subAgents": [
                "Coder",
                "Reviewer"
            ]
        },
        {
            "day": 2,
            "tasks": [
                "Develop prototype core features",
                "Research technology stack"
            ],
            "subAgents": [
                "Coder",
                "DevOps"
            ]
        },
        {
            "day": 3,
            "tasks": [
                "Develop test plan for prototype",
                "Conduct code reviews"
            ],
            "subAgents": [
                "Tester",
                "Reviewer"
            ]
        },
        {
            "day": 4,
            "tasks": [
                "Develop deployment plan for prototype",
                "Collaborate on code quality and best practices"
            ],
            "subAgents": [
                "DevOps",
                "Coder",
                "Reviewer"
            ]
        },
        {
            "day": 5,
            "tasks": [
                "Test prototype core features",
                "Gather feedback and approval from stakeholders"
            ],
            "subAgents": [
                "Tester",
                "Coder",
                "Reviewer",
                "DevOps"
            ]
        }
    ],
    "project_name": "test-ai-architecture",
    "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
    "phase_idx": 1,
    "phase_context_file": ".ai/.plan/.context/phase-1.context.blueprint.md"
}
```

# Phase 2 STEPS - Prompt:


            Analyze the attached Phase 2 Context Markdown content. 
            Translate every directive, objective, and daily task mentioned inside it into a structured day-by-day JSON map.
            
            --- PHASE 2 CONTEXT MARKDOWN ---
            ## PHASE 2 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 2 is to develop the backend API using Quarkus, implementing authentication and authorization, and integrating with Kafka and Postgres. This phase will focus on building a scalable and secure backend infrastructure to support the membership-hub project. The key deliverables include:

* Design and implementation of the backend API using Quarkus
* Integration with Kafka for event-driven architecture
* Integration with Postgres for relational data storage
* Implementation of authentication and authorization using OAuth 2.0
* Development of API endpoints for user management, attendance tracking, and notification systems

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 2 includes:

* Backend API development using Quarkus (Java or Kotlin)
* Integration with Kafka and Postgres
* Implementation of OAuth 2.0 for authentication and authorization
* Development of API endpoints using RESTful architecture
* Use of Docker for containerization
* Deployment on GCP and GKE

Directory boundaries:

* `src/main/java`: Quarkus backend API code
* `src/main/resources`: Configuration files and properties
* `src/test/java`: Unit tests and integration tests
* `docker`: Dockerfile and containerization scripts
* `kafka`: Kafka configuration and integration code
* `postgres`: Postgres configuration and integration code

Endpoints:

* `/api/v1/users`: User management endpoints (e.g., create, read, update, delete)
* `/api/v1/attendance`: Attendance tracking endpoints (e.g., record attendance, get attendance history)
* `/api/v1/notifications`: Notification system endpoints (e.g., send notifications, get notification history)

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 2:

* **Coder**: Responsible for developing the backend API using Quarkus, integrating with Kafka and Postgres, and implementing authentication and authorization.
* **Tester**: Responsible for developing unit tests and integration tests for the backend API, ensuring that the API endpoints are working correctly and securely.
* **Reviewer**: Responsible for reviewing the code developed by the Coder, ensuring that it meets the project's coding standards and best practices.
* **DevOps**: Responsible for creating and maintaining Docker images for the backend API, ensuring that the images are optimized for production environments, and deploying the API to GKE.

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 2 includes:

* The backend API is fully implemented and tested
* All API endpoints are working correctly and securely
* Integration with Kafka and Postgres is complete and tested
* Authentication and authorization are fully implemented and tested
* Docker images are created and optimized for production environments
* The backend API is deployed to GKE and configured for production
* All unit tests and integration tests are passing
* Code reviews are complete and all feedback is addressed
* Deployment scripts and configuration files are updated and tested
            ------------------------------------------

            Map your response strictly to the requested PhaseStepsPlan JSON structure.
            

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
{
    "phase": "Phase 2",
    "context": "test-ai-architecture",
    "objectives": [
        "Develop backend API using Quarkus",
        "Implement authentication and authorization",
        "Integrate with Kafka and Postgres",
        "Develop API endpoints for user management, attendance tracking, and notification systems"
    ],
    "dailyTasks": [
        {
            "day": 1,
            "tasks": [
                {
                    "task": "Design backend API using Quarkus",
                    "assignee": "Coder"
                },
                {
                    "task": "Set up Kafka and Postgres integration",
                    "assignee": "Coder"
                }
            ]
        },
        {
            "day": 2,
            "tasks": [
                {
                    "task": "Implement authentication and authorization using OAuth 2.0",
                    "assignee": "Coder"
                },
                {
                    "task": "Develop API endpoints for user management",
                    "assignee": "Coder"
                }
            ]
        },
        {
            "day": 3,
            "tasks": [
                {
                    "task": "Develop API endpoints for attendance tracking",
                    "assignee": "Coder"
                },
                {
                    "task": "Develop API endpoints for notification systems",
                    "assignee": "Coder"
                }
            ]
        },
        {
            "day": 4,
            "tasks": [
                {
                    "task": "Develop unit tests for backend API",
                    "assignee": "Tester"
                },
                {
                    "task": "Develop integration tests for backend API",
                    "assignee": "Tester"
                }
            ]
        },
        {
            "day": 5,
            "tasks": [
                {
                    "task": "Review code developed by Coder",
                    "assignee": "Reviewer"
                },
                {
                    "task": "Create and maintain Docker images for backend API",
                    "assignee": "DevOps"
                }
            ]
        },
        {
            "day": 6,
            "tasks": [
                {
                    "task": "Deploy backend API to GKE",
                    "assignee": "DevOps"
                },
                {
                    "task": "Configure backend API for production",
                    "assignee": "DevOps"
                }
            ]
        },
        {
            "day": 7,
            "tasks": [
                {
                    "task": "Test and verify backend API",
                    "assignee": "Tester"
                },
                {
                    "task": "Address feedback from code reviews",
                    "assignee": "Coder"
                }
            ]
        }
    ],
    "definitionOfDone": [
        "Backend API is fully implemented and tested",
        "All API endpoints are working correctly and securely",
        "Integration with Kafka and Postgres is complete and tested",
        "Authentication and authorization are fully implemented and tested",
        "Docker images are created and optimized for production environments",
        "Backend API is deployed to GKE and configured for production",
        "All unit tests and integration tests are passing",
        "Code reviews are complete and all feedback is addressed",
        "Deployment scripts and configuration files are updated and tested"
    ],
    "project_name": "test-ai-architecture",
    "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
    "phase_idx": 2,
    "phase_context_file": ".ai/.plan/.context/phase-2.context.blueprint.md"
}
```

# Phase 3 STEPS - Prompt:


            Analyze the attached Phase 3 Context Markdown content. 
            Translate every directive, objective, and daily task mentioned inside it into a structured day-by-day JSON map.
            
            --- PHASE 3 CONTEXT MARKDOWN ---
            ## PHASE 3 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
In Phase 3, the primary objective is to develop the mobile frontend of the membership-hub application using Next.js. This phase will focus on implementing features such as QR code scanning, notification systems, and multi-language support. The scope of this phase includes designing and developing the mobile frontend, ensuring it is scalable, and integrating it with the backend API developed in Phase 2.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 3 includes:
- Developing the mobile frontend using Next.js
- Implementing QR code scanning and notification systems
- Integrating with the backend API for authentication and data management
- Ensuring multi-language support and building for both iOS and Android
- Directory boundaries:
  - `mobile/frontend`: Next.js frontend code
  - `mobile/backend`: Backend API integration and notification systems
  - `mobile/assets`: QR code scanning and other mobile-specific assets
- Endpoints:
  - `/mobile/login`: Mobile login endpoint
  - `/mobile/qr_scan`: QR code scanning endpoint
  - `/mobile/notifications`: Notification systems endpoint

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
- **Coder**: Develop the mobile frontend using Next.js, implement QR code scanning and notification systems, and integrate with the backend API.
- **Tester**: Develop and execute comprehensive test plans for the mobile frontend, including unit testing, integration testing, and UI testing.
- **Reviewer**: Conduct code reviews to ensure the mobile frontend code meets the project's coding standards and best practices.
- **DevOps (Docker)**: Create and maintain Docker images for the mobile frontend, ensuring they are optimized for production environments.
- **DevOps (Deployer)**: Assist in deploying the mobile frontend to GKE, ensuring a smooth deployment process.

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 3 includes:
- The mobile frontend is fully developed and integrated with the backend API.
- QR code scanning and notification systems are implemented and functional.
- Multi-language support is implemented, and the application is built for both iOS and Android.
- Comprehensive testing has been completed, and all defects have been resolved.
- Code reviews have been completed, and the code meets the project's coding standards and best practices.
- Docker images are created and optimized for production environments.
- The mobile frontend is deployed to GKE, and the deployment is verified to be successful.
            ------------------------------------------

            Map your response strictly to the requested PhaseStepsPlan JSON structure.
            

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
{
    "phase": "Phase 3",
    "context": "test-ai-architecture",
    "objectives": [
        "Develop the mobile frontend of the membership-hub application using Next.js",
        "Implement features such as QR code scanning, notification systems, and multi-language support",
        "Ensure the mobile frontend is scalable and integrated with the backend API"
    ],
    "technicalScope": {
        "allowedTechnologies": [
            "Next.js"
        ],
        "features": [
            "QR code scanning",
            "notification systems",
            "multi-language support"
        ],
        "directoryBoundaries": {
            "mobile/frontend": "Next.js frontend code",
            "mobile/backend": "Backend API integration and notification systems",
            "mobile/assets": "QR code scanning and other mobile-specific assets"
        },
        "endpoints": [
            {
                "path": "/mobile/login",
                "description": "Mobile login endpoint"
            },
            {
                "path": "/mobile/qr_scan",
                "description": "QR code scanning endpoint"
            },
            {
                "path": "/mobile/notifications",
                "description": "Notification systems endpoint"
            }
        ]
    },
    "subAgentFunctionalDirectives": {
        "Coder": [
            "Develop the mobile frontend using Next.js",
            "Implement QR code scanning and notification systems",
            "Integrate with the backend API"
        ],
        "Tester": [
            "Develop and execute comprehensive test plans for the mobile frontend",
            "Unit testing",
            "Integration testing",
            "UI testing"
        ],
        "Reviewer": [
            "Conduct code reviews to ensure the mobile frontend code meets the project's coding standards and best practices"
        ],
        "DevOps (Docker)": [
            "Create and maintain Docker images for the mobile frontend",
            "Optimize Docker images for production environments"
        ],
        "DevOps (Deployer)": [
            "Assist in deploying the mobile frontend to GKE",
            "Ensure a smooth deployment process"
        ]
    },
    "definitionOfDone": [
        "The mobile frontend is fully developed and integrated with the backend API",
        "QR code scanning and notification systems are implemented and functional",
        "Multi-language support is implemented, and the application is built for both iOS and Android",
        "Comprehensive testing has been completed, and all defects have been resolved",
        "Code reviews have been completed, and the code meets the project's coding standards and best practices",
        "Docker images are created and optimized for production environments",
        "The mobile frontend is deployed to GKE, and the deployment is verified to be successful"
    ],
    "dayByDayPlan": [
        {
            "day": 1,
            "tasks": [
                {
                    "task": "Develop the mobile frontend using Next.js",
                    "assignee": "Coder"
                },
                {
                    "task": "Develop and execute comprehensive test plans for the mobile frontend",
                    "assignee": "Tester"
                }
            ]
        },
        {
            "day": 2,
            "tasks": [
                {
                    "task": "Implement QR code scanning and notification systems",
                    "assignee": "Coder"
                },
                {
                    "task": "Conduct code reviews to ensure the mobile frontend code meets the project's coding standards and best practices",
                    "assignee": "Reviewer"
                }
            ]
        },
        {
            "day": 3,
            "tasks": [
                {
                    "task": "Integrate with the backend API",
                    "assignee": "Coder"
                },
                {
                    "task": "Create and maintain Docker images for the mobile frontend",
                    "assignee": "DevOps (Docker)"
                }
            ]
        },
        {
            "day": 4,
            "tasks": [
                {
                    "task": "Optimize Docker images for production environments",
                    "assignee": "DevOps (Docker)"
                },
                {
                    "task": "Assist in deploying the mobile frontend to GKE",
                    "assignee": "DevOps (Deployer)"
                }
            ]
        },
        {
            "day": 5,
            "tasks": [
                {
                    "task": "Ensure a smooth deployment process",
                    "assignee": "DevOps (Deployer)"
                },
                {
                    "task": "Verify the deployment is successful",
                    "assignee": "DevOps (Deployer)"
                }
            ]
        }
    ],
    "project_name": "test-ai-architecture",
    "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
    "phase_idx": 3,
    "phase_context_file": ".ai/.plan/.context/phase-3.context.blueprint.md"
}
```

# Phase 4 STEPS - Prompt:


            Analyze the attached Phase 4 Context Markdown content. 
            Translate every directive, objective, and daily task mentioned inside it into a structured day-by-day JSON map.
            
            --- PHASE 4 CONTEXT MARKDOWN ---
            ## PHASE 4 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 4 is to ensure the quality and reliability of the membership-hub application through comprehensive testing and quality assurance. This phase will focus on conducting unit testing, integration testing, and UI testing to identify and resolve any defects or issues. The scope of this phase includes:

* Testing the backend API using Quarkus, Kafka, and Postgres
* Testing the mobile frontend using Next.js
* Testing the authentication and authorization mechanisms
* Testing the QR code scanning and notification systems
* Testing the SEO optimization for both web and mobile platforms

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope of this phase includes:

* Testing frameworks such as JUnit, Jest, and Enzyme
* Testing libraries such as Mockito and Hamcrest
* API testing tools such as Postman and Swagger
* UI testing frameworks such as Selenium and Appium
* Directory boundaries:
	+ Backend API: `src/main/java` and `src/main/resources`
	+ Mobile frontend: `src/mobile` and `src/components`
	+ Testing: `src/test/java` and `src/test/javascript`
* Endpoints:
	+ Backend API: `/api/*`
	+ Mobile frontend: `/mobile/*`

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in this phase:

* **Coder**: Responsible for writing unit tests and integration tests for the backend API and mobile frontend.
* **Tester**: Responsible for developing and executing comprehensive test plans, including UI testing and API testing.
* **Reviewer**: Responsible for reviewing test cases and providing feedback to the development team.
* **DevOps**: Responsible for setting up and configuring testing environments, including Docker and Kubernetes.

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 4 includes:

* All unit tests and integration tests have been written and executed successfully
* All UI tests have been executed successfully
* All defects and issues have been identified and resolved
* The application has been tested for scalability, security, and performance
* The testing environment has been set up and configured correctly
* All test cases have been reviewed and approved by the Reviewer
* The application has been verified to meet the requirements and specifications outlined in the Raw Requirements Reference.
            ------------------------------------------

            Map your response strictly to the requested PhaseStepsPlan JSON structure.
            

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
{
    "phase": "Phase 4",
    "context": "test-ai-architecture",
    "objectives": [
        "Ensure quality and reliability of membership-hub application",
        "Conduct unit testing, integration testing, and UI testing",
        "Identify and resolve defects or issues"
    ],
    "scope": [
        "Testing backend API using Quarkus, Kafka, and Postgres",
        "Testing mobile frontend using Next.js",
        "Testing authentication and authorization mechanisms",
        "Testing QR code scanning and notification systems",
        "Testing SEO optimization for web and mobile platforms"
    ],
    "technicalScope": {
        "testingFrameworks": [
            "JUnit",
            "Jest",
            "Enzyme"
        ],
        "testingLibraries": [
            "Mockito",
            "Hamcrest"
        ],
        "apiTestingTools": [
            "Postman",
            "Swagger"
        ],
        "uiTestingFrameworks": [
            "Selenium",
            "Appium"
        ],
        "directoryBoundaries": {
            "backendAPI": [
                "src/main/java",
                "src/main/resources"
            ],
            "mobileFrontend": [
                "src/mobile",
                "src/components"
            ],
            "testing": [
                "src/test/java",
                "src/test/javascript"
            ]
        },
        "endpoints": {
            "backendAPI": "/api/*",
            "mobileFrontend": "/mobile/*"
        }
    },
    "subAgents": [
        {
            "role": "Coder",
            "tasks": [
                "Write unit tests for backend API",
                "Write unit tests for mobile frontend",
                "Write integration tests for backend API",
                "Write integration tests for mobile frontend"
            ]
        },
        {
            "role": "Tester",
            "tasks": [
                "Develop comprehensive test plans",
                "Execute UI testing",
                "Execute API testing"
            ]
        },
        {
            "role": "Reviewer",
            "tasks": [
                "Review test cases",
                "Provide feedback to development team"
            ]
        },
        {
            "role": "DevOps",
            "tasks": [
                "Set up testing environments",
                "Configure testing environments",
                "Set up Docker",
                "Set up Kubernetes"
            ]
        }
    ],
    "definitionOfDone": [
        "All unit tests and integration tests have been written and executed successfully",
        "All UI tests have been executed successfully",
        "All defects and issues have been identified and resolved",
        "Application has been tested for scalability, security, and performance",
        "Testing environment has been set up and configured correctly",
        "All test cases have been reviewed and approved by Reviewer",
        "Application has been verified to meet requirements and specifications"
    ],
    "phaseStepsPlan": [
        {
            "day": 1,
            "tasks": [
                {
                    "role": "Coder",
                    "task": "Write unit tests for backend API"
                },
                {
                    "role": "DevOps",
                    "task": "Set up testing environments"
                }
            ]
        },
        {
            "day": 2,
            "tasks": [
                {
                    "role": "Coder",
                    "task": "Write unit tests for mobile frontend"
                },
                {
                    "role": "DevOps",
                    "task": "Configure testing environments"
                }
            ]
        },
        {
            "day": 3,
            "tasks": [
                {
                    "role": "Coder",
                    "task": "Write integration tests for backend API"
                },
                {
                    "role": "DevOps",
                    "task": "Set up Docker"
                }
            ]
        },
        {
            "day": 4,
            "tasks": [
                {
                    "role": "Coder",
                    "task": "Write integration tests for mobile frontend"
                },
                {
                    "role": "DevOps",
                    "task": "Set up Kubernetes"
                }
            ]
        },
        {
            "day": 5,
            "tasks": [
                {
                    "role": "Tester",
                    "task": "Develop comprehensive test plans"
                },
                {
                    "role": "Reviewer",
                    "task": "Review test cases"
                }
            ]
        },
        {
            "day": 6,
            "tasks": [
                {
                    "role": "Tester",
                    "task": "Execute UI testing"
                },
                {
                    "role": "Reviewer",
                    "task": "Provide feedback to development team"
                }
            ]
        },
        {
            "day": 7,
            "tasks": [
                {
                    "role": "Tester",
                    "task": "Execute API testing"
                },
                {
                    "role": "DevOps",
                    "task": "Verify testing environment"
                }
            ]
        }
    ],
    "project_name": "test-ai-architecture",
    "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
    "phase_idx": 4,
    "phase_context_file": ".ai/.plan/.context/phase-4.context.blueprint.md"
}
```

# Phase 5 STEPS - Prompt:


            Analyze the attached Phase 5 Context Markdown content. 
            Translate every directive, objective, and daily task mentioned inside it into a structured day-by-day JSON map.
            
            --- PHASE 5 CONTEXT MARKDOWN ---
            ## PHASE 5 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 5 is to deploy the membership-hub application to Google Kubernetes Engine (GKE) and ensure its proper maintenance and updates to meet changing requirements. This phase involves configuring monitoring and logging tools, deploying the application, and performing post-deployment testing to guarantee the application's stability and performance.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 5 includes:
- Deployment scripts and configurations for GKE
- Docker image creation and optimization for production environments
- Configuration of monitoring and logging tools such as Prometheus and Grafana
- Setup of load balancers and auto-scaling groups for horizontal scaling
- Security configurations, including OAuth 2.0 and HTTPS encryption
- Directory boundaries:
  - Deployment scripts: `/deploy`
  - Docker configurations: `/docker`
  - Monitoring and logging tools: `/monitoring`
  - Security configurations: `/security`
- Endpoints:
  - API endpoints for user authentication and authorization
  - API endpoints for QR code scanning and attendance tracking
  - API endpoints for notification systems

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
- **Coder**: Focus on creating deployment scripts, configuring Docker images for production, and implementing security measures.
- **Tester**: Conduct post-deployment testing to ensure the application's stability and performance. Test the deployment, monitoring, and logging configurations.
- **Reviewer**: Review the deployment scripts, Docker configurations, and security measures to ensure they meet the project's coding standards and best practices.
- **Docker**: Create and maintain Docker images for the application, ensuring they are optimized for production environments.
- **Deployer (DevOps)**: Manage the deployment of the application to GKE, configure monitoring and logging tools, and ensure the application is properly configured for production.

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 5 includes:
- The application is successfully deployed to GKE.
- Monitoring and logging tools are configured and functioning correctly.
- Security measures, including OAuth 2.0 and HTTPS encryption, are implemented and tested.
- Post-deployment testing has been conducted, and the application's stability and performance have been verified.
- Deployment scripts, Docker configurations, and security measures have been reviewed and approved.
- The application is properly configured for production, and all necessary settings have been applied.
- Documentation for deployment, monitoring, and maintenance has been updated and is available to the team.
            ------------------------------------------

            Map your response strictly to the requested PhaseStepsPlan JSON structure.
            

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
{
    "phase": "Phase 5",
    "context": "test-ai-architecture",
    "objectives": [
        "Deploy membership-hub application to Google Kubernetes Engine (GKE)",
        "Configure monitoring and logging tools",
        "Perform post-deployment testing",
        "Ensure proper maintenance and updates"
    ],
    "technicalScope": {
        "directories": [
            {
                "name": "Deployment scripts",
                "path": "/deploy"
            },
            {
                "name": "Docker configurations",
                "path": "/docker"
            },
            {
                "name": "Monitoring and logging tools",
                "path": "/monitoring"
            },
            {
                "name": "Security configurations",
                "path": "/security"
            }
        ],
        "endpoints": [
            {
                "name": "API endpoints for user authentication and authorization"
            },
            {
                "name": "API endpoints for QR code scanning and attendance tracking"
            },
            {
                "name": "API endpoints for notification systems"
            }
        ]
    },
    "subAgentDirectives": {
        "Coder": [
            "Create deployment scripts",
            "Configure Docker images for production",
            "Implement security measures"
        ],
        "Tester": [
            "Conduct post-deployment testing",
            "Test deployment, monitoring, and logging configurations"
        ],
        "Reviewer": [
            "Review deployment scripts",
            "Review Docker configurations",
            "Review security measures"
        ],
        "Docker": [
            "Create and maintain Docker images for the application",
            "Optimize Docker images for production environments"
        ],
        "Deployer (DevOps)": [
            "Manage deployment of the application to GKE",
            "Configure monitoring and logging tools",
            "Ensure application is properly configured for production"
        ]
    },
    "definitionOfDone": [
        "Application is successfully deployed to GKE",
        "Monitoring and logging tools are configured and functioning correctly",
        "Security measures are implemented and tested",
        "Post-deployment testing has been conducted",
        "Deployment scripts, Docker configurations, and security measures have been reviewed and approved",
        "Application is properly configured for production",
        "Documentation for deployment, monitoring, and maintenance has been updated"
    ],
    "dayByDayPlan": [
        {
            "day": 1,
            "tasks": [
                {
                    "assignee": "Coder",
                    "task": "Create deployment scripts"
                },
                {
                    "assignee": "Docker",
                    "task": "Create and maintain Docker images for the application"
                }
            ]
        },
        {
            "day": 2,
            "tasks": [
                {
                    "assignee": "Coder",
                    "task": "Configure Docker images for production"
                },
                {
                    "assignee": "Deployer (DevOps)",
                    "task": "Manage deployment of the application to GKE"
                }
            ]
        },
        {
            "day": 3,
            "tasks": [
                {
                    "assignee": "Coder",
                    "task": "Implement security measures"
                },
                {
                    "assignee": "Deployer (DevOps)",
                    "task": "Configure monitoring and logging tools"
                }
            ]
        },
        {
            "day": 4,
            "tasks": [
                {
                    "assignee": "Tester",
                    "task": "Conduct post-deployment testing"
                },
                {
                    "assignee": "Reviewer",
                    "task": "Review deployment scripts"
                }
            ]
        },
        {
            "day": 5,
            "tasks": [
                {
                    "assignee": "Tester",
                    "task": "Test deployment, monitoring, and logging configurations"
                },
                {
                    "assignee": "Reviewer",
                    "task": "Review Docker configurations and security measures"
                }
            ]
        },
        {
            "day": 6,
            "tasks": [
                {
                    "assignee": "Deployer (DevOps)",
                    "task": "Ensure application is properly configured for production"
                },
                {
                    "assignee": "Documentation",
                    "task": "Update documentation for deployment, monitoring, and maintenance"
                }
            ]
        },
        {
            "day": 7,
            "tasks": [
                {
                    "assignee": "All",
                    "task": "Review and verify Definition of Done"
                }
            ]
        }
    ],
    "project_name": "test-ai-architecture",
    "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
    "phase_idx": 5,
    "phase_context_file": ".ai/.plan/.context/phase-5.context.blueprint.md"
}
```

# Global Prompt:


        Analyze the attached project requirements. Build the GLOBAL PROJECT CONTEXT for 'test-ai-architecture'.
        
        --- RAW REQUIREMENTS ---
        ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

        --- END REQUIREMENTS ---

        Your output MUST follow this exact structure:
        ## GLOBAL PROJECT CONTEXT: test-ai-architecture
        #### 1. Executive Summary & Tech Stack Blueprint
        #### 2. Global Guardrails & Enterprise Compliance Standards
        #### 3. Standardized Sub-Agent Persona Definitions (Manager, Coder, Tester, Reviewer, Docker, Deployer)
        #### 4. Multi-Phase Segmentation Strategy Overview (Plan exactly 5 phases)
        

# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable, multi-tenant application designed to manage students across various centers. The tech stack consists of Quarkus, Kafka, Postgres, and Docker, deployed on Google Cloud Platform (GCP) using Google Kubernetes Engine (GKE). The application will have a web interface for management and a mobile app for students, built using Next.js, supporting multiple languages and platforms (iOS, Android). The project requires authentication via email/password, Firebase, Google, or Facebook, and features QR code-based attendance tracking, notification systems, and SEO optimization for both web and mobile platforms.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to industry standards, the following guardrails and compliance standards will be implemented:
- **Security**: Implement OAuth 2.0 for authentication, SSL/TLS encryption for data transmission, and follow OWASP guidelines for secure coding practices.
- **Scalability**: Design the system to scale horizontally using Kubernetes, ensuring high availability and performance under heavy loads.
- **Data Privacy**: Comply with GDPR and CCPA regulations, ensuring user data is protected and handled according to legal requirements.
- **Accessibility**: Follow WCAG 2.1 guidelines to ensure the web and mobile applications are accessible to users with disabilities.
- **Quality Assurance**: Establish a continuous integration and continuous deployment (CI/CD) pipeline, with automated testing and code reviews to maintain high-quality code.

#### 3. Standardized Sub-Agent Persona Definitions
The following personas will be involved in the project:
- **Manager**: Oversees the project timeline, budget, and resource allocation. Ensures that the project is delivered on time, within budget, and meets the required quality standards.
- **Coder**: Responsible for writing high-quality, scalable, and secure code. Collaborates with the testing team to identify and fix bugs.
- **Tester**: Develops and executes comprehensive test plans to ensure the application meets the required functionality, performance, and security standards.
- **Reviewer**: Conducts code reviews to ensure that the code is maintainable, efficient, and follows industry best practices.
- **Docker**: Responsible for creating and maintaining Docker images, ensuring that the application is properly containerized and ready for deployment.
- **Deployer**: Manages the deployment of the application to the production environment, ensuring that the deployment is smooth, and the application is properly configured.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases:
- **Phase 1: Planning and Design** (Weeks 1-4): Define the project scope, create a detailed design document, and establish the technical requirements.
- **Phase 2: Backend Development** (Weeks 5-12): Develop the backend API using Quarkus, Kafka, and Postgres, and implement authentication and authorization mechanisms.
- **Phase 3: Mobile App Development** (Weeks 13-18): Develop the mobile app using Next.js, implementing features such as QR code scanning, notification systems, and multi-language support.
- **Phase 4: Testing and Quality Assurance** (Weeks 19-22): Conduct thorough testing of the application, including unit testing, integration testing, and user acceptance testing.
- **Phase 5: Deployment and Maintenance** (Weeks 23-26): Deploy the application to the production environment, configure monitoring and logging, and establish a maintenance schedule to ensure the application remains stable and secure.
```

# Phase 1 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 1 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable, multi-tenant application designed to manage students across various centers. The tech stack consists of Quarkus, Kafka, Postgres, and Docker, deployed on Google Cloud Platform (GCP) using Google Kubernetes Engine (GKE). The application will have a web interface for management and a mobile app for students, built using Next.js, supporting multiple languages and platforms (iOS, Android). The project requires authentication via email/password, Firebase, Google, or Facebook, and features QR code-based attendance tracking, notification systems, and SEO optimization for both web and mobile platforms.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to industry standards, the following guardrails and compliance standards will be implemented:
- **Security**: Implement OAuth 2.0 for authentication, SSL/TLS encryption for data transmission, and follow OWASP guidelines for secure coding practices.
- **Scalability**: Design the system to scale horizontally using Kubernetes, ensuring high availability and performance under heavy loads.
- **Data Privacy**: Comply with GDPR and CCPA regulations, ensuring user data is protected and handled according to legal requirements.
- **Accessibility**: Follow WCAG 2.1 guidelines to ensure the web and mobile applications are accessible to users with disabilities.
- **Quality Assurance**: Establish a continuous integration and continuous deployment (CI/CD) pipeline, with automated testing and code reviews to maintain high-quality code.

#### 3. Standardized Sub-Agent Persona Definitions
The following personas will be involved in the project:
- **Manager**: Oversees the project timeline, budget, and resource allocation. Ensures that the project is delivered on time, within budget, and meets the required quality standards.
- **Coder**: Responsible for writing high-quality, scalable, and secure code. Collaborates with the testing team to identify and fix bugs.
- **Tester**: Develops and executes comprehensive test plans to ensure the application meets the required functionality, performance, and security standards.
- **Reviewer**: Conducts code reviews to ensure that the code is maintainable, efficient, and follows industry best practices.
- **Docker**: Responsible for creating and maintaining Docker images, ensuring that the application is properly containerized and ready for deployment.
- **Deployer**: Manages the deployment of the application to the production environment, ensuring that the deployment is smooth, and the application is properly configured.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases:
- **Phase 1: Planning and Design** (Weeks 1-4): Define the project scope, create a detailed design document, and establish the technical requirements.
- **Phase 2: Backend Development** (Weeks 5-12): Develop the backend API using Quarkus, Kafka, and Postgres, and implement authentication and authorization mechanisms.
- **Phase 3: Mobile App Development** (Weeks 13-18): Develop the mobile app using Next.js, implementing features such as QR code scanning, notification systems, and multi-language support.
- **Phase 4: Testing and Quality Assurance** (Weeks 19-22): Conduct thorough testing of the application, including unit testing, integration testing, and user acceptance testing.
- **Phase 5: Deployment and Maintenance** (Weeks 23-26): Deploy the application to the production environment, configure monitoring and logging, and establish a maintenance schedule to ensure the application remains stable and secure.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------

            Your output MUST follow this exact Markdown structure for Phase 1:
            ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed design document, and establish the technical requirements for the membership-hub project. This phase will focus on planning and design, ensuring that all stakeholders are aligned and that the project is set up for success. The key deliverables for this phase include:
- A detailed project scope statement
- A technical requirements document
- A high-level system architecture design
- A project timeline and resource allocation plan

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
For Phase 1, the technical scope will be limited to the following areas:
- Project scope statement: `docs/project_scope.md`
- Technical requirements document: `docs/technical_requirements.md`
- System architecture design: `docs/system_architecture.md`
- Project timeline and resource allocation plan: `docs/project_timeline.md`
- Directory structure:
  - `docs/`: documentation files
  - `design/`: design files (e.g., wireframes, prototypes)
  - `requirements/`: technical requirements files
- Endpoints:
  - None (this phase is focused on planning and design, not development)

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversees the project timeline, budget, and resource allocation. Ensures that the project scope statement, technical requirements document, and system architecture design are complete and accurate.
- **Coder**: Assists in creating the technical requirements document and system architecture design. Provides input on the feasibility of the proposed design and identifies potential technical risks.
- **Tester**: Reviews the technical requirements document and system architecture design to identify potential testing challenges and areas of concern.
- **Reviewer**: Conducts a review of the project scope statement, technical requirements document, and system architecture design to ensure that they are complete, accurate, and meet the project's requirements.
- **Docker**: Not involved in this phase.
- **Deployer**: Not involved in this phase.

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 1 is as follows:
- The project scope statement is complete and approved by all stakeholders.
- The technical requirements document is complete and approved by all stakeholders.
- The system architecture design is complete and approved by all stakeholders.
- The project timeline and resource allocation plan are complete and approved by all stakeholders.
- All sub-agents have reviewed and approved the deliverables for this phase.
- The phase has been formally closed, and all stakeholders have been notified of the phase's completion.
```

# Phase 2 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 2 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable, multi-tenant application designed to manage students across various centers. The tech stack consists of Quarkus, Kafka, Postgres, and Docker, deployed on Google Cloud Platform (GCP) using Google Kubernetes Engine (GKE). The application will have a web interface for management and a mobile app for students, built using Next.js, supporting multiple languages and platforms (iOS, Android). The project requires authentication via email/password, Firebase, Google, or Facebook, and features QR code-based attendance tracking, notification systems, and SEO optimization for both web and mobile platforms.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to industry standards, the following guardrails and compliance standards will be implemented:
- **Security**: Implement OAuth 2.0 for authentication, SSL/TLS encryption for data transmission, and follow OWASP guidelines for secure coding practices.
- **Scalability**: Design the system to scale horizontally using Kubernetes, ensuring high availability and performance under heavy loads.
- **Data Privacy**: Comply with GDPR and CCPA regulations, ensuring user data is protected and handled according to legal requirements.
- **Accessibility**: Follow WCAG 2.1 guidelines to ensure the web and mobile applications are accessible to users with disabilities.
- **Quality Assurance**: Establish a continuous integration and continuous deployment (CI/CD) pipeline, with automated testing and code reviews to maintain high-quality code.

#### 3. Standardized Sub-Agent Persona Definitions
The following personas will be involved in the project:
- **Manager**: Oversees the project timeline, budget, and resource allocation. Ensures that the project is delivered on time, within budget, and meets the required quality standards.
- **Coder**: Responsible for writing high-quality, scalable, and secure code. Collaborates with the testing team to identify and fix bugs.
- **Tester**: Develops and executes comprehensive test plans to ensure the application meets the required functionality, performance, and security standards.
- **Reviewer**: Conducts code reviews to ensure that the code is maintainable, efficient, and follows industry best practices.
- **Docker**: Responsible for creating and maintaining Docker images, ensuring that the application is properly containerized and ready for deployment.
- **Deployer**: Manages the deployment of the application to the production environment, ensuring that the deployment is smooth, and the application is properly configured.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases:
- **Phase 1: Planning and Design** (Weeks 1-4): Define the project scope, create a detailed design document, and establish the technical requirements.
- **Phase 2: Backend Development** (Weeks 5-12): Develop the backend API using Quarkus, Kafka, and Postgres, and implement authentication and authorization mechanisms.
- **Phase 3: Mobile App Development** (Weeks 13-18): Develop the mobile app using Next.js, implementing features such as QR code scanning, notification systems, and multi-language support.
- **Phase 4: Testing and Quality Assurance** (Weeks 19-22): Conduct thorough testing of the application, including unit testing, integration testing, and user acceptance testing.
- **Phase 5: Deployment and Maintenance** (Weeks 23-26): Deploy the application to the production environment, configure monitoring and logging, and establish a maintenance schedule to ensure the application remains stable and secure.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------

            Your output MUST follow this exact Markdown structure for Phase 2:
            ## PHASE 2 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 2 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 2 is to develop the backend API using Quarkus, Kafka, and Postgres. This phase will focus on implementing the core functionality of the membership-hub project, including authentication and authorization mechanisms, user management, and QR code-based attendance tracking. The scope of this phase includes:

* Designing and implementing the database schema using Postgres
* Developing the backend API using Quarkus, including endpoints for user management, attendance tracking, and notification systems
* Implementing authentication and authorization mechanisms using OAuth 2.0, including support for internal authentication via email/password, Firebase, Google, and Facebook
* Integrating Kafka for message queuing and notification systems

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope of this phase includes:

* Backend API development: `src/main/java` directory
* Database schema design: `src/main/resources` directory
* Kafka integration: `src/main/java` directory
* Authentication and authorization mechanisms: `src/main/java` directory
* Endpoints:
	+ `/api/v1/users` for user management
	+ `/api/v1/attendance` for attendance tracking
	+ `/api/v1/notifications` for notification systems

Allowed files and paths:

* `pom.xml` for dependency management
* `application.properties` for configuration settings
* `src/main/java` directory for Java source code
* `src/main/resources` directory for database schema and configuration files

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in this phase:

* **Coder**: Responsible for developing the backend API, implementing authentication and authorization mechanisms, and integrating Kafka.
* **Tester**: Responsible for developing unit tests and integration tests for the backend API.
* **Reviewer**: Responsible for reviewing the code for maintainability, efficiency, and adherence to industry best practices.
* **DevOps**: Responsible for creating and maintaining Docker images, ensuring that the application is properly containerized and ready for deployment.

Specific tasks:

* Coder:
	+ Develop the backend API using Quarkus
	+ Implement authentication and authorization mechanisms using OAuth 2.0
	+ Integrate Kafka for message queuing and notification systems
* Tester:
	+ Develop unit tests for the backend API
	+ Develop integration tests for the backend API
* Reviewer:
	+ Review the code for maintainability and efficiency
	+ Ensure adherence to industry best practices
* DevOps:
	+ Create and maintain Docker images for the application
	+ Ensure that the application is properly containerized and ready for deployment

#### 4. Phase Definition of Done (DoD)
The Definition of Done for this phase includes:

* The backend API is fully implemented and functional
* Authentication and authorization mechanisms are fully implemented and functional
* Kafka integration is complete and functional
* Unit tests and integration tests are developed and passing
* Code reviews are complete and all feedback is addressed
* Docker images are created and maintained
* The application is properly containerized and ready for deployment

The phase will be considered complete when all of the above criteria are met, and the application is ready for testing and quality assurance in Phase 4.
```

# Phase 3 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 3 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable, multi-tenant application designed to manage students across various centers. The tech stack consists of Quarkus, Kafka, Postgres, and Docker, deployed on Google Cloud Platform (GCP) using Google Kubernetes Engine (GKE). The application will have a web interface for management and a mobile app for students, built using Next.js, supporting multiple languages and platforms (iOS, Android). The project requires authentication via email/password, Firebase, Google, or Facebook, and features QR code-based attendance tracking, notification systems, and SEO optimization for both web and mobile platforms.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to industry standards, the following guardrails and compliance standards will be implemented:
- **Security**: Implement OAuth 2.0 for authentication, SSL/TLS encryption for data transmission, and follow OWASP guidelines for secure coding practices.
- **Scalability**: Design the system to scale horizontally using Kubernetes, ensuring high availability and performance under heavy loads.
- **Data Privacy**: Comply with GDPR and CCPA regulations, ensuring user data is protected and handled according to legal requirements.
- **Accessibility**: Follow WCAG 2.1 guidelines to ensure the web and mobile applications are accessible to users with disabilities.
- **Quality Assurance**: Establish a continuous integration and continuous deployment (CI/CD) pipeline, with automated testing and code reviews to maintain high-quality code.

#### 3. Standardized Sub-Agent Persona Definitions
The following personas will be involved in the project:
- **Manager**: Oversees the project timeline, budget, and resource allocation. Ensures that the project is delivered on time, within budget, and meets the required quality standards.
- **Coder**: Responsible for writing high-quality, scalable, and secure code. Collaborates with the testing team to identify and fix bugs.
- **Tester**: Develops and executes comprehensive test plans to ensure the application meets the required functionality, performance, and security standards.
- **Reviewer**: Conducts code reviews to ensure that the code is maintainable, efficient, and follows industry best practices.
- **Docker**: Responsible for creating and maintaining Docker images, ensuring that the application is properly containerized and ready for deployment.
- **Deployer**: Manages the deployment of the application to the production environment, ensuring that the deployment is smooth, and the application is properly configured.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases:
- **Phase 1: Planning and Design** (Weeks 1-4): Define the project scope, create a detailed design document, and establish the technical requirements.
- **Phase 2: Backend Development** (Weeks 5-12): Develop the backend API using Quarkus, Kafka, and Postgres, and implement authentication and authorization mechanisms.
- **Phase 3: Mobile App Development** (Weeks 13-18): Develop the mobile app using Next.js, implementing features such as QR code scanning, notification systems, and multi-language support.
- **Phase 4: Testing and Quality Assurance** (Weeks 19-22): Conduct thorough testing of the application, including unit testing, integration testing, and user acceptance testing.
- **Phase 5: Deployment and Maintenance** (Weeks 23-26): Deploy the application to the production environment, configure monitoring and logging, and establish a maintenance schedule to ensure the application remains stable and secure.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------

            Your output MUST follow this exact Markdown structure for Phase 3:
            ## PHASE 3 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 3 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 3 is to develop the mobile app for the membership-hub project. This phase will focus on designing and implementing the mobile app's features, including QR code scanning, notification systems, and multi-language support. The mobile app will be built using Next.js, ensuring a seamless user experience across both iOS and Android platforms.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 3 includes:
- Developing the mobile app's frontend using Next.js
- Implementing QR code scanning functionality
- Integrating notification systems (SMS, Zalo, and in-app notifications)
- Ensuring multi-language support for the mobile app
- Building and configuring the mobile app for both iOS and Android platforms
- Directory boundaries:
  - `mobile-app/`: The root directory for the mobile app's codebase
  - `mobile-app/components/`: Directory for reusable UI components
  - `mobile-app/screens/`: Directory for screen-specific code
  - `mobile-app/services/`: Directory for API services and notification integrations
  - `mobile-app/utils/`: Directory for utility functions and helpers
- Endpoints:
  - `/api/qr-code`: Endpoint for generating and verifying QR codes
  - `/api/notifications`: Endpoint for sending notifications (SMS, Zalo, and in-app)

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
- **Coder**:
  - Develop the mobile app's frontend using Next.js
  - Implement QR code scanning functionality
  - Integrate notification systems (SMS, Zalo, and in-app notifications)
  - Ensure multi-language support for the mobile app
- **Tester**:
  - Develop and execute comprehensive test plans for the mobile app
  - Test QR code scanning functionality
  - Test notification systems (SMS, Zalo, and in-app notifications)
  - Test multi-language support
- **Reviewer**:
  - Conduct code reviews for the mobile app's codebase
  - Ensure adherence to industry best practices and coding standards
  - Review test plans and test results
- **DevOps (Docker and Deployer)**:
  - Create and maintain Docker images for the mobile app
  - Ensure proper configuration and deployment of the mobile app to the production environment

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 3 includes:
- The mobile app is fully functional and meets all the requirements
- QR code scanning functionality is implemented and tested
- Notification systems (SMS, Zalo, and in-app notifications) are integrated and tested
- Multi-language support is implemented and tested
- The mobile app is built and configured for both iOS and Android platforms
- Code reviews are completed, and all feedback is addressed
- Comprehensive testing is completed, and all defects are resolved
- The mobile app is deployed to the production environment and configured for monitoring and logging.
```

# Phase 4 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 4 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable, multi-tenant application designed to manage students across various centers. The tech stack consists of Quarkus, Kafka, Postgres, and Docker, deployed on Google Cloud Platform (GCP) using Google Kubernetes Engine (GKE). The application will have a web interface for management and a mobile app for students, built using Next.js, supporting multiple languages and platforms (iOS, Android). The project requires authentication via email/password, Firebase, Google, or Facebook, and features QR code-based attendance tracking, notification systems, and SEO optimization for both web and mobile platforms.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to industry standards, the following guardrails and compliance standards will be implemented:
- **Security**: Implement OAuth 2.0 for authentication, SSL/TLS encryption for data transmission, and follow OWASP guidelines for secure coding practices.
- **Scalability**: Design the system to scale horizontally using Kubernetes, ensuring high availability and performance under heavy loads.
- **Data Privacy**: Comply with GDPR and CCPA regulations, ensuring user data is protected and handled according to legal requirements.
- **Accessibility**: Follow WCAG 2.1 guidelines to ensure the web and mobile applications are accessible to users with disabilities.
- **Quality Assurance**: Establish a continuous integration and continuous deployment (CI/CD) pipeline, with automated testing and code reviews to maintain high-quality code.

#### 3. Standardized Sub-Agent Persona Definitions
The following personas will be involved in the project:
- **Manager**: Oversees the project timeline, budget, and resource allocation. Ensures that the project is delivered on time, within budget, and meets the required quality standards.
- **Coder**: Responsible for writing high-quality, scalable, and secure code. Collaborates with the testing team to identify and fix bugs.
- **Tester**: Develops and executes comprehensive test plans to ensure the application meets the required functionality, performance, and security standards.
- **Reviewer**: Conducts code reviews to ensure that the code is maintainable, efficient, and follows industry best practices.
- **Docker**: Responsible for creating and maintaining Docker images, ensuring that the application is properly containerized and ready for deployment.
- **Deployer**: Manages the deployment of the application to the production environment, ensuring that the deployment is smooth, and the application is properly configured.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases:
- **Phase 1: Planning and Design** (Weeks 1-4): Define the project scope, create a detailed design document, and establish the technical requirements.
- **Phase 2: Backend Development** (Weeks 5-12): Develop the backend API using Quarkus, Kafka, and Postgres, and implement authentication and authorization mechanisms.
- **Phase 3: Mobile App Development** (Weeks 13-18): Develop the mobile app using Next.js, implementing features such as QR code scanning, notification systems, and multi-language support.
- **Phase 4: Testing and Quality Assurance** (Weeks 19-22): Conduct thorough testing of the application, including unit testing, integration testing, and user acceptance testing.
- **Phase 5: Deployment and Maintenance** (Weeks 23-26): Deploy the application to the production environment, configure monitoring and logging, and establish a maintenance schedule to ensure the application remains stable and secure.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------

            Your output MUST follow this exact Markdown structure for Phase 4:
            ## PHASE 4 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 4 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 4 is to conduct thorough testing and quality assurance of the membership-hub application. This phase will ensure that the application meets the required functionality, performance, and security standards. The scope of this phase includes:
- Unit testing of individual components
- Integration testing of the entire application
- User acceptance testing (UAT) to validate the application's functionality and usability
- Performance testing to ensure the application's scalability and reliability
- Security testing to identify and address potential vulnerabilities

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope of Phase 4 includes:
- Testing of the Quarkus-based backend API
- Testing of the Next.js-based mobile app
- Testing of the Kafka-based messaging system
- Testing of the Postgres database
- Testing of the Docker containerization
- Testing of the GCP and GKE deployment
- Endpoints for testing:
  - `/api/v1/auth` for authentication and authorization
  - `/api/v1/users` for user management
  - `/api/v1/centers` for center management
  - `/api/v1/students` for student management
  - `/api/v1/attendance` for attendance tracking
- Files and paths:
  - `src/test/java` for unit tests
  - `src/test/integration` for integration tests
  - `src/test/uat` for user acceptance tests
  - `src/main/resources` for test data and configuration files

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 4:
- **Coder**: Responsible for writing unit tests and integration tests for the application's components.
- **Tester**: Responsible for developing and executing comprehensive test plans, including user acceptance testing, performance testing, and security testing.
- **Reviewer**: Responsible for reviewing test cases and test results to ensure that the application meets the required quality standards.
- **DevOps**: Responsible for configuring and maintaining the testing environment, including the setup of Docker containers, GCP, and GKE.

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 4 includes:
- All unit tests and integration tests have been executed and passed
- User acceptance testing has been completed and the application meets the required functionality and usability standards
- Performance testing has been completed and the application meets the required scalability and reliability standards
- Security testing has been completed and all identified vulnerabilities have been addressed
- Test results have been reviewed and approved by the Reviewer
- The application has been deployed to a staging environment for final testing and validation
- All test data and configuration files have been updated and version-controlled.
```

# Phase 5 - Prompt:


            Project Name: test-ai-architecture
            You are tasked to detail **PHASE 5 OUT OF 5**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            ## GLOBAL PROJECT CONTEXT: test-ai-architecture
#### 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a scalable, multi-tenant application designed to manage students across various centers. The tech stack consists of Quarkus, Kafka, Postgres, and Docker, deployed on Google Cloud Platform (GCP) using Google Kubernetes Engine (GKE). The application will have a web interface for management and a mobile app for students, built using Next.js, supporting multiple languages and platforms (iOS, Android). The project requires authentication via email/password, Firebase, Google, or Facebook, and features QR code-based attendance tracking, notification systems, and SEO optimization for both web and mobile platforms.

#### 2. Global Guardrails & Enterprise Compliance Standards
To ensure the project's success and adherence to industry standards, the following guardrails and compliance standards will be implemented:
- **Security**: Implement OAuth 2.0 for authentication, SSL/TLS encryption for data transmission, and follow OWASP guidelines for secure coding practices.
- **Scalability**: Design the system to scale horizontally using Kubernetes, ensuring high availability and performance under heavy loads.
- **Data Privacy**: Comply with GDPR and CCPA regulations, ensuring user data is protected and handled according to legal requirements.
- **Accessibility**: Follow WCAG 2.1 guidelines to ensure the web and mobile applications are accessible to users with disabilities.
- **Quality Assurance**: Establish a continuous integration and continuous deployment (CI/CD) pipeline, with automated testing and code reviews to maintain high-quality code.

#### 3. Standardized Sub-Agent Persona Definitions
The following personas will be involved in the project:
- **Manager**: Oversees the project timeline, budget, and resource allocation. Ensures that the project is delivered on time, within budget, and meets the required quality standards.
- **Coder**: Responsible for writing high-quality, scalable, and secure code. Collaborates with the testing team to identify and fix bugs.
- **Tester**: Develops and executes comprehensive test plans to ensure the application meets the required functionality, performance, and security standards.
- **Reviewer**: Conducts code reviews to ensure that the code is maintainable, efficient, and follows industry best practices.
- **Docker**: Responsible for creating and maintaining Docker images, ensuring that the application is properly containerized and ready for deployment.
- **Deployer**: Manages the deployment of the application to the production environment, ensuring that the deployment is smooth, and the application is properly configured.

#### 4. Multi-Phase Segmentation Strategy Overview
The project will be divided into five phases:
- **Phase 1: Planning and Design** (Weeks 1-4): Define the project scope, create a detailed design document, and establish the technical requirements.
- **Phase 2: Backend Development** (Weeks 5-12): Develop the backend API using Quarkus, Kafka, and Postgres, and implement authentication and authorization mechanisms.
- **Phase 3: Mobile App Development** (Weeks 13-18): Develop the mobile app using Next.js, implementing features such as QR code scanning, notification systems, and multi-language support.
- **Phase 4: Testing and Quality Assurance** (Weeks 19-22): Conduct thorough testing of the application, including unit testing, integration testing, and user acceptance testing.
- **Phase 5: Deployment and Maintenance** (Weeks 23-26): Deploy the application to the production environment, configure monitoring and logging, and establish a maintenance schedule to ensure the application remains stable and secure.
            
            --- RAW REQUIREMENTS REFERENCE ---
            ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

            ----------------------------------

            Your output MUST follow this exact Markdown structure for Phase 5:
            ## PHASE 5 CONTEXT BLUEPRINT: test-ai-architecture
            #### 1. Phase Operational Scope & Objectives
            #### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            #### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            #### 4. Phase Definition of Done (DoD)
            

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```text
## PHASE 5 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 5 is to deploy the membership-hub application to the production environment, ensuring a smooth and secure deployment process. This phase will focus on configuring monitoring and logging, establishing a maintenance schedule, and performing final quality assurance checks to guarantee the application's stability and security. The scope of this phase includes:

* Deploying the application to Google Cloud Platform (GCP) using Google Kubernetes Engine (GKE)
* Configuring monitoring and logging tools to track application performance and identify potential issues
* Establishing a maintenance schedule to ensure the application remains up-to-date and secure
* Performing final quality assurance checks to verify the application's functionality and security

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope of Phase 5 includes:

* Deployment scripts and configuration files for GKE (e.g., `deployment.yaml`, `service.yaml`)
* Monitoring and logging tools (e.g., Prometheus, Grafana, ELK Stack)
* Maintenance scripts and schedules (e.g., `maintenance.sh`, `backup.sh`)
* Quality assurance scripts and test cases (e.g., `qa-tests.py`, `integration-tests.py`)
* Directory boundaries:
	+ `/deploy`: deployment scripts and configuration files
	+ `/monitoring`: monitoring and logging tools
	+ `/maintenance`: maintenance scripts and schedules
	+ `/qa`: quality assurance scripts and test cases

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 5:

* **Coder**: Responsible for creating deployment scripts and configuration files, as well as implementing monitoring and logging tools.
* **Tester**: Responsible for performing final quality assurance checks, including functional and security testing.
* **Reviewer**: Responsible for reviewing deployment scripts, configuration files, and maintenance schedules to ensure they meet industry standards and best practices.
* **DevOps**: Responsible for deploying the application to GKE, configuring monitoring and logging tools, and establishing a maintenance schedule.

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 5 includes:

* The application is successfully deployed to GKE and is accessible to users.
* Monitoring and logging tools are configured and tracking application performance.
* A maintenance schedule is established and automated.
* Final quality assurance checks have been performed, and the application has been verified to be functional and secure.
* All deployment scripts, configuration files, and maintenance schedules have been reviewed and approved by the Reviewer.
* The application is fully compliant with the established Global Guardrails & Enterprise Compliance Standards.
```

# Phase 1 STEPS - Prompt:


            Analyze the attached Phase 1 Context Markdown content. 
            Translate every directive, objective, and daily task mentioned inside it into a structured day-by-day JSON map.
            
            --- PHASE 1 CONTEXT MARKDOWN ---
            ## PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 1 is to define the project scope, create a detailed design document, and establish the technical requirements for the membership-hub project. This phase will focus on planning and design, ensuring that all stakeholders are aligned and that the project is set up for success. The key deliverables for this phase include:
- A detailed project scope statement
- A technical requirements document
- A high-level system architecture design
- A project timeline and resource allocation plan

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
For Phase 1, the technical scope will be limited to the following areas:
- Project scope statement: `docs/project_scope.md`
- Technical requirements document: `docs/technical_requirements.md`
- System architecture design: `docs/system_architecture.md`
- Project timeline and resource allocation plan: `docs/project_timeline.md`
- Directory structure:
  - `docs/`: documentation files
  - `design/`: design files (e.g., wireframes, prototypes)
  - `requirements/`: technical requirements files
- Endpoints:
  - None (this phase is focused on planning and design, not development)

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in Phase 1, with the following tasks:
- **Manager**: Oversees the project timeline, budget, and resource allocation. Ensures that the project scope statement, technical requirements document, and system architecture design are complete and accurate.
- **Coder**: Assists in creating the technical requirements document and system architecture design. Provides input on the feasibility of the proposed design and identifies potential technical risks.
- **Tester**: Reviews the technical requirements document and system architecture design to identify potential testing challenges and areas of concern.
- **Reviewer**: Conducts a review of the project scope statement, technical requirements document, and system architecture design to ensure that they are complete, accurate, and meet the project's requirements.
- **Docker**: Not involved in this phase.
- **Deployer**: Not involved in this phase.

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 1 is as follows:
- The project scope statement is complete and approved by all stakeholders.
- The technical requirements document is complete and approved by all stakeholders.
- The system architecture design is complete and approved by all stakeholders.
- The project timeline and resource allocation plan are complete and approved by all stakeholders.
- All sub-agents have reviewed and approved the deliverables for this phase.
- The phase has been formally closed, and all stakeholders have been notified of the phase's completion.
            ------------------------------------------

            Map your response strictly to the requested PhaseStepsPlan JSON structure.
            

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
{
    "phase": "Phase 1",
    "context": "test-ai-architecture",
    "objectives": [
        "Define project scope",
        "Create detailed design document",
        "Establish technical requirements for membership-hub project"
    ],
    "deliverables": [
        "Detailed project scope statement",
        "Technical requirements document",
        "High-level system architecture design",
        "Project timeline and resource allocation plan"
    ],
    "technicalScope": {
        "directories": [
            "docs/",
            "design/",
            "requirements/"
        ],
        "files": [
            "docs/project_scope.md",
            "docs/technical_requirements.md",
            "docs/system_architecture.md",
            "docs/project_timeline.md"
        ],
        "endpoints": []
    },
    "subAgents": [
        {
            "name": "Manager",
            "tasks": [
                "Oversee project timeline, budget, and resource allocation",
                "Ensure project scope statement, technical requirements document, and system architecture design are complete and accurate"
            ]
        },
        {
            "name": "Coder",
            "tasks": [
                "Assist in creating technical requirements document and system architecture design",
                "Provide input on feasibility of proposed design and identify potential technical risks"
            ]
        },
        {
            "name": "Tester",
            "tasks": [
                "Review technical requirements document and system architecture design to identify potential testing challenges and areas of concern"
            ]
        },
        {
            "name": "Reviewer",
            "tasks": [
                "Conduct review of project scope statement, technical requirements document, and system architecture design to ensure they are complete, accurate, and meet project's requirements"
            ]
        }
    ],
    "definitionOfDone": [
        "Project scope statement is complete and approved by all stakeholders",
        "Technical requirements document is complete and approved by all stakeholders",
        "System architecture design is complete and approved by all stakeholders",
        "Project timeline and resource allocation plan are complete and approved by all stakeholders",
        "All sub-agents have reviewed and approved deliverables for this phase",
        "Phase has been formally closed, and all stakeholders have been notified of phase's completion"
    ],
    "phaseStepsPlan": [
        {
            "day": 1,
            "tasks": [
                {
                    "subAgent": "Manager",
                    "task": "Define project scope and create project scope statement"
                },
                {
                    "subAgent": "Coder",
                    "task": "Assist in creating technical requirements document"
                }
            ]
        },
        {
            "day": 2,
            "tasks": [
                {
                    "subAgent": "Manager",
                    "task": "Review and finalize project scope statement"
                },
                {
                    "subAgent": "Coder",
                    "task": "Continue working on technical requirements document"
                }
            ]
        },
        {
            "day": 3,
            "tasks": [
                {
                    "subAgent": "Manager",
                    "task": "Create high-level system architecture design"
                },
                {
                    "subAgent": "Tester",
                    "task": "Review technical requirements document and system architecture design"
                }
            ]
        },
        {
            "day": 4,
            "tasks": [
                {
                    "subAgent": "Manager",
                    "task": "Finalize system architecture design and project timeline"
                },
                {
                    "subAgent": "Reviewer",
                    "task": "Conduct review of project scope statement, technical requirements document, and system architecture design"
                }
            ]
        },
        {
            "day": 5,
            "tasks": [
                {
                    "subAgent": "Manager",
                    "task": "Finalize project timeline and resource allocation plan"
                },
                {
                    "subAgent": "All sub-agents",
                    "task": "Review and approve all deliverables for this phase"
                }
            ]
        }
    ],
    "project_name": "test-ai-architecture",
    "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
    "phase_idx": 1,
    "phase_context_file": ".ai/.plan/.context/phase-1.context.blueprint.md"
}
```

# Phase 2 STEPS - Prompt:


            Analyze the attached Phase 2 Context Markdown content. 
            Translate every directive, objective, and daily task mentioned inside it into a structured day-by-day JSON map.
            
            --- PHASE 2 CONTEXT MARKDOWN ---
            ## PHASE 2 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 2 is to develop the backend API using Quarkus, Kafka, and Postgres. This phase will focus on implementing the core functionality of the membership-hub project, including authentication and authorization mechanisms, user management, and QR code-based attendance tracking. The scope of this phase includes:

* Designing and implementing the database schema using Postgres
* Developing the backend API using Quarkus, including endpoints for user management, attendance tracking, and notification systems
* Implementing authentication and authorization mechanisms using OAuth 2.0, including support for internal authentication via email/password, Firebase, Google, and Facebook
* Integrating Kafka for message queuing and notification systems

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope of this phase includes:

* Backend API development: `src/main/java` directory
* Database schema design: `src/main/resources` directory
* Kafka integration: `src/main/java` directory
* Authentication and authorization mechanisms: `src/main/java` directory
* Endpoints:
	+ `/api/v1/users` for user management
	+ `/api/v1/attendance` for attendance tracking
	+ `/api/v1/notifications` for notification systems

Allowed files and paths:

* `pom.xml` for dependency management
* `application.properties` for configuration settings
* `src/main/java` directory for Java source code
* `src/main/resources` directory for database schema and configuration files

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
The following sub-agents will be involved in this phase:

* **Coder**: Responsible for developing the backend API, implementing authentication and authorization mechanisms, and integrating Kafka.
* **Tester**: Responsible for developing unit tests and integration tests for the backend API.
* **Reviewer**: Responsible for reviewing the code for maintainability, efficiency, and adherence to industry best practices.
* **DevOps**: Responsible for creating and maintaining Docker images, ensuring that the application is properly containerized and ready for deployment.

Specific tasks:

* Coder:
	+ Develop the backend API using Quarkus
	+ Implement authentication and authorization mechanisms using OAuth 2.0
	+ Integrate Kafka for message queuing and notification systems
* Tester:
	+ Develop unit tests for the backend API
	+ Develop integration tests for the backend API
* Reviewer:
	+ Review the code for maintainability and efficiency
	+ Ensure adherence to industry best practices
* DevOps:
	+ Create and maintain Docker images for the application
	+ Ensure that the application is properly containerized and ready for deployment

#### 4. Phase Definition of Done (DoD)
The Definition of Done for this phase includes:

* The backend API is fully implemented and functional
* Authentication and authorization mechanisms are fully implemented and functional
* Kafka integration is complete and functional
* Unit tests and integration tests are developed and passing
* Code reviews are complete and all feedback is addressed
* Docker images are created and maintained
* The application is properly containerized and ready for deployment

The phase will be considered complete when all of the above criteria are met, and the application is ready for testing and quality assurance in Phase 4.
            ------------------------------------------

            Map your response strictly to the requested PhaseStepsPlan JSON structure.
            

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
{
    "phase": "Phase 2",
    "context": "test-ai-architecture",
    "objectives": [
        "Develop backend API using Quarkus, Kafka, and Postgres",
        "Implement core functionality of membership-hub project",
        "Implement authentication and authorization mechanisms",
        "Implement user management and QR code-based attendance tracking"
    ],
    "dailyTasks": [
        {
            "day": 1,
            "tasks": [
                {
                    "subAgent": "Coder",
                    "task": "Design database schema using Postgres"
                },
                {
                    "subAgent": "DevOps",
                    "task": "Create and maintain Docker images for the application"
                }
            ]
        },
        {
            "day": 2,
            "tasks": [
                {
                    "subAgent": "Coder",
                    "task": "Develop backend API using Quarkus"
                },
                {
                    "subAgent": "Tester",
                    "task": "Develop unit tests for the backend API"
                }
            ]
        },
        {
            "day": 3,
            "tasks": [
                {
                    "subAgent": "Coder",
                    "task": "Implement authentication and authorization mechanisms using OAuth 2.0"
                },
                {
                    "subAgent": "Reviewer",
                    "task": "Review code for maintainability and efficiency"
                }
            ]
        },
        {
            "day": 4,
            "tasks": [
                {
                    "subAgent": "Coder",
                    "task": "Integrate Kafka for message queuing and notification systems"
                },
                {
                    "subAgent": "Tester",
                    "task": "Develop integration tests for the backend API"
                }
            ]
        },
        {
            "day": 5,
            "tasks": [
                {
                    "subAgent": "DevOps",
                    "task": "Ensure application is properly containerized and ready for deployment"
                },
                {
                    "subAgent": "Reviewer",
                    "task": "Ensure adherence to industry best practices"
                }
            ]
        }
    ],
    "definitionOfDone": [
        "Backend API is fully implemented and functional",
        "Authentication and authorization mechanisms are fully implemented and functional",
        "Kafka integration is complete and functional",
        "Unit tests and integration tests are developed and passing",
        "Code reviews are complete and all feedback is addressed",
        "Docker images are created and maintained",
        "Application is properly containerized and ready for deployment"
    ],
    "project_name": "test-ai-architecture",
    "global_context_file": ".ai/.context/test-ai-architecture.global.blueprint.md",
    "phase_idx": 2,
    "phase_context_file": ".ai/.plan/.context/phase-2.context.blueprint.md"
}
```

# Phase 3 STEPS - Prompt:


            Analyze the attached Phase 3 Context Markdown content. 
            Translate every directive, objective, and daily task mentioned inside it into a structured day-by-day JSON map.
            
            --- PHASE 3 CONTEXT MARKDOWN ---
            ## PHASE 3 CONTEXT BLUEPRINT: test-ai-architecture
#### 1. Phase Operational Scope & Objectives
The primary objective of Phase 3 is to develop the mobile app for the membership-hub project. This phase will focus on designing and implementing the mobile app's features, including QR code scanning, notification systems, and multi-language support. The mobile app will be built using Next.js, ensuring a seamless user experience across both iOS and Android platforms.

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
The technical scope for Phase 3 includes:
- Developing the mobile app's frontend using Next.js
- Implementing QR code scanning functionality
- Integrating notification systems (SMS, Zalo, and in-app notifications)
- Ensuring multi-language support for the mobile app
- Building and configuring the mobile app for both iOS and Android platforms
- Directory boundaries:
  - `mobile-app/`: The root directory for the mobile app's codebase
  - `mobile-app/components/`: Directory for reusable UI components
  - `mobile-app/screens/`: Directory for screen-specific code
  - `mobile-app/services/`: Directory for API services and notification integrations
  - `mobile-app/utils/`: Directory for utility functions and helpers
- Endpoints:
  - `/api/qr-code`: Endpoint for generating and verifying QR codes
  - `/api/notifications`: Endpoint for sending notifications (SMS, Zalo, and in-app)

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
- **Coder**:
  - Develop the mobile app's frontend using Next.js
  - Implement QR code scanning functionality
  - Integrate notification systems (SMS, Zalo, and in-app notifications)
  - Ensure multi-language support for the mobile app
- **Tester**:
  - Develop and execute comprehensive test plans for the mobile app
  - Test QR code scanning functionality
  - Test notification systems (SMS, Zalo, and in-app notifications)
  - Test multi-language support
- **Reviewer**:
  - Conduct code reviews for the mobile app's codebase
  - Ensure adherence to industry best practices and coding standards
  - Review test plans and test results
- **DevOps (Docker and Deployer)**:
  - Create and maintain Docker images for the mobile app
  - Ensure proper configuration and deployment of the mobile app to the production environment

#### 4. Phase Definition of Done (DoD)
The Definition of Done for Phase 3 includes:
- The mobile app is fully functional and meets all the requirements
- QR code scanning functionality is implemented and tested
- Notification systems (SMS, Zalo, and in-app notifications) are integrated and tested
- Multi-language support is implemented and tested
- The mobile app is built and configured for both iOS and Android platforms
- Code reviews are completed, and all feedback is addressed
- Comprehensive testing is completed, and all defects are resolved
- The mobile app is deployed to the production environment and configured for monitoring and logging.
            ------------------------------------------

            Map your response strictly to the requested PhaseStepsPlan JSON structure.
            

# System Instruction

You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas.

# Raw Response / Exception:

```json
Error code: 429 - {'error': {'message': 'Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx7x6rbpftmr50sr2yyb78qm` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 98769, Requested 1497. Please try again in 3m49.824s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
```

