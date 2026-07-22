# PHASE 2 CONTEXT BLUEPRINT: membership-hub
## 1. Phase Operational Scope & Objectives
- **Core Goal:** Build a robust, scalable **backend API** that powers the membership‑hub web and mobile experiences.  
- **Tech Stack:** Java 17 + Quarkus, PostgreSQL, Apache Kafka, Docker, Google Cloud Platform (GCP) readiness.  
- **Key Functional Areas:**  
  1. **Authentication & Authorization** – email/password, Firebase, Google, Facebook OAuth, JWT‑based session management, role‑based access control (System Admin, Admin, Manager, Teacher, Student).  
  2. **Entity Management** – Centers, Courses, Teachers, Students, Attendance (QR scan), Notifications, Promotions.  
  3. **Real‑time Communication** – Kafka producers/consumers for instant push notifications to Zalo groups and mobile apps.  
  4. **Security & Compliance** – Data encryption at rest/in‑transit, audit logging, GDPR/CCPA‑aligned data handling.  
  5. **DevOps Foundations** – Docker image generation, health‑checks, environment‑driven configuration, CI/CD‑ready artifacts.  

## 2. Allowed Technical Scope & Directory Boundaries (Files, Paths, and Endpoints)
```
src/main/java/com/membershiphub/backend/
├─ model/                # JPA entities (Center, Course, Teacher, Student, Attendance, Notification, Promotion)
├─ repository/           # Spring Data JPA interfaces (e.g., UserRepository, CenterRepository)
├─ service/              # Business logic (UserService, AuthService, KafkaNotificationService)
├─ resource/             # REST endpoints (AuthResource, UserResource, CenterResource, CourseResource,
│                         TeacherResource, StudentResource, AttendanceResource, NotificationResource)
├─ security/             # SecurityConfig, JwtTokenFilter, OAuth2SuccessHandler
└─ kafka/                # KafkaProducerService, KafkaConsumerService

src/main/resources/
└─ application.properties   # DB, Kafka, JWT, OAuth client configs

src/main/docker/
└─ Dockerfile               # Multi‑stage build for runtime image

src/test/java/com/membershiphub/backend/
└─ **(*Unit/Integration*)Test classes for each resource & service

docker-compose.yml          # Local dev stack (Postgres + Kafka)
```

**Endpoint Patterns (example):**  
- `POST /api/auth/login` – email/password  
- `POST /api/auth/oauth/{provider}` – Firebase/Google/Facebook callback  
- `GET /api/centers`, `POST /api/centers` … etc.  
- `POST /api/attendance/qr` – record attendance via QR  
- `POST /api/kafka/notify` – fire a Kafka event for notifications  

## 3. Dedicated Sub‑Agent Functional Directives
| Agent | Primary Responsibility |
|-------|------------------------|
| **Coder** | Implement core REST resources, services, JPA entities, authentication/authorization logic, Kafka producers/consumers, and Docker file. |
| **Tester** | Write unit & integration tests for all resources, auth flows, Kafka event handling, and security constraints. |
| **Reviewer** | Perform code‑review checks, enforce coding standards, validate security best‑practices, and ensure compliance with guardrails. |
| **DevOps** | Prepare Docker image, health‑check endpoints, environment configuration, and CI/CD stub (e.g., Cloud Build triggers). |

## 4. Phase Definition of Done (DoD)
- All **backend REST endpoints** are implemented, documented, and follow Quarkus conventions.  
- **Authentication** (local & OAuth) and **RBAC** are fully functional; JWT tokens are validated and role‑scoped.  
- **Kafka integration** can produce/consume notification events for Zalo groups & mobile push.  
- **Docker image** builds cleanly, includes health‑check, and is ready for GKE deployment.  
- **Test coverage** ≥ 80 % for core resources; security tests confirm proper role enforcement.  
- **Code review** sign‑off from Reviewer; DevOps signs off on container readiness.  

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: PROJECT BOOTSTRAP & CORE ENTITY DEFINITIONS
#### SUB‑TASK 1.1: Define JPA Entities & Repositories
##### Assigned Sub‑Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `src/main/java/com/membershiphub/backend/model/User.java`
    *   **Architectural Requirements:**  
        *   Annotate with `@Entity`, `@Table(name="users")`.  
        *   Include fields: `id`, `email`, `passwordHash`, `provider` (LOCAL, FIREBASE, GOOGLE, FACEBOOK), `role` (enum: SYSTEM_ADMIN, ADMIN, MANAGER, TEACHER, STUDENT).  
        *   Add `@OneToMany` for `Center` ownership if role = ADMIN.  
        *   Implement `equals`/`hashCode` based on `id`.  
*   **Target Path 2:** `src/main/java/com/membershiphub/backend/model/Center.java`
    *   **Architectural Requirements:**  
        *   `@Entity` with fields: `id`, `name`, `address`, `taxId`, `contactPhone`, `adminId` (`@ManyToOne` to `User`).  
        *   Add `@OneToMany` to `Course` list.  
*   **Target Path 3:** `src/main/java/com/membershiphub/backend/repository/UserRepository.java`
    *   **Architectural Requirements:**  
        *   Extend `JpaRepository<User, Long>`.  
        *   Provide finder `Optional<User> findByEmail(String email)`.  
        *   Provide custom query `List<User> findByRole(UserRole role)`.  

#### SUB‑TASK 1.2: Initialize Quarkus Application & Basic Config
##### Assigned Sub‑Agent: DevOps
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `src/main/resources/application.properties`
    *   **Architectural Requirements:**  
        *   Set datasource URL, username, password for PostgreSQL.  
        *   Configure Hibernate `ddl-auto = none` (schema migration handled externally).  
        *   Define JWT `quarkus.smallrye.jwt.sign.key.location` (placeholder for secret).  
        *   Kafka bootstrap servers (`kafka:9092` for dev).  
        *   OAuth client IDs/secrets for Firebase, Google, Facebook (environment placeholders).  
*   **Target Path 2:** `src/main/docker/Dockerfile`
    *   **Architectural Requirements:**  
        *   Multi‑stage: build stage with Maven, runtime stage using `quarkus:2.15.0` base image.  
        *   Copy built uber‑jar, set `JAVA_OPTS`, expose port `8080`.  
        *   Add health‑check endpoint `/q/health`.  

#### SUB‑TASK 1.3: Write Unit Tests for Entity Persistence
##### Assigned Sub‑Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `src/test/java/com/membershiphub/backend/model/UserTest.java`
    *   **Architectural Requirements:**  
        *   Use `@DataJpaTest` to test save/find operations.  
        *   Verify that `User` with duplicate email throws constraint violation.  
        *   Assert role enum values are persisted correctly.  
*   **Target Path 2:** `src/test/java/com/membershiphub/backend/repository/UserRepositoryTest.java`
    *   **Architectural Requirements:**  
        *   Test `findByEmail` returns expected user.  
        *   Test `findByRole` filters users by role.  

### DAY 2: AUTHENTICATION & AUTHORIZATION IMPLEMENTATION
#### SUB‑TASK 2.1: Implement JWT Authentication Service
##### Assigned Sub‑Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `src/main/java/com/membershiphub/backend/service/AuthService.java`
    *   **Architectural Requirements:**  
        *   Method `String generateToken(User user)` – includes `sub`, `email`, `role`, `iat`, `exp`.  
        *   Method `User authenticateLocal(String email, String password)` – verify password hash.  
        *   Method `User authenticateOAuth(String provider, String providerId)` – look up or create user.  
*   **Target Path 2:** `src/main/java/com/membershiphub/backend/security/JwtTokenFilter.java`
    *   **Architectural Requirements:**  
        *   Extend `jakarta.ws.rs.container.ContainerRequestFilter`.  
        *   Validate `Authorization: Bearer <token>` header.  
        *   Extract claims, set `SecurityContext` with `UserPrincipal` and roles.  

#### SUB‑TASK 2.2: Create OAuth2 Success Handlers for External Providers
##### Assigned Sub‑Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `src/main/java/com/membershiphub/backend/security/OAuth2SuccessHandler.java`
    *   **Architectural Requirements:**  
        *   Implement `OAuth2SuccessHandler` interface.  
        *   For each provider (Firebase, Google, Facebook) map provider‑specific user info to `User` entity.  
        *   Generate JWT and return `Response` with token.  

#### SUB‑TASK 2.3: Write Integration Tests for Auth Flows
##### Assigned Sub‑Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `src/test/java/com/membershiphub/backend/resource/AuthResourceTest.java`
    *   **Architectural Requirements:**  
        *   Use `QuarkusTest` + `TestHTTPEndpoint`.  
        *   Test `POST /api/auth/login` with valid/invalid credentials.  
        *   Test `POST /api/auth/oauth/google` mock provider response.  
        *   Verify JWT token in response headers.  

#### SUB‑TASK 2.4: Code Review of Authentication Layer
##### Assigned Sub‑Agent: Reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** All files under `src/main/java/com/membershiphub/backend/security/` and `src/main/java/com/membershiphub/backend/service/AuthService.java`
    *   **Architectural Requirements:**  
        *   Ensure password hashing uses `BCrypt` or `Argon2`.  
        *   Validate token expiration and refresh logic placeholders.  
        *   Confirm role‑based access annotations (`@RolesAllowed`) are present in resource classes.  
        *   Check for secure handling of OAuth client secrets (environment variables).  

### DAY 3: CORE CRUD RESOURCES & KAFKA NOTIFICATION INTEGRATION
#### SUB‑TASK 3.1: Implement Center Management REST Resources
##### Assigned Sub‑Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `src/main/java/com/membershiphub/backend/resource/CenterResource.java`
    *   **Architectural Requirements:**  
        *   Expose `GET /api/centers`, `GET /api/centers/{id}`, `POST /api/centers`, `PUT /api/centers/{id}`, `DELETE /api/centers/{id}`.  
        *   Inject `CenterService` and enforce `@RolesAllowed("SYSTEM_ADMIN")` for create/delete.  
        *   Validate request DTO against business rules (e.g., taxId uniqueness).  
*   **Target Path 2:** `src/main/java/com/membershiphub/backend/service/CenterService.java`
    *   **Architectural Requirements:**  
        *   Implement CRUD delegating to `CenterRepository`.  
        *   Add method `Center assignAdmin(Long centerId, Long adminId)` with role update.  

#### SUB‑TASK 3.2: Implement Course, Teacher, Student & Attendance Resources
##### Assigned Sub‑Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `src/main/java/com/membershiphub/backend/resource/CourseResource.java`
    *   **Architectural Requirements:**  
        *   Endpoints for course CRUD, `POST /api/courses/{courseId}/teachers/{teacherId}` (assign).  
        *   Role restrictions: `ADMIN` can create/delete, `MANAGER` can assign teachers.  
*   **Target Path 2:** `src/main/java/com/membershiphub/backend/resource/TeacherResource.java`
    *   **Architectural Requirements:**  
        *   CRUD for Teacher entity, `GET /api/teachers/{id}/courses`.  
        *   Role restrictions: `ADMIN`/`MANAGER` can manage, `TEACHER` can view own data.  
*   **Target Path 3:** `src/main/java/com/membershiphub/backend/resource/StudentResource.java`
    *   **Architectural Requirements:**  
        *   CRUD for Student, `POST /api/students/{id}/courses/{courseId}` (enroll).  
        *   Role restrictions: `ADMIN`/`MANAGER` can manage, `STUDENT` can view own profile.  
*   **Target Path 4:** `src/main/java/com/membershiphub/backend/resource/AttendanceResource.java`
    *   **Architectural Requirements:**  
        *   `POST /api/attendance/qr` – accepts `qrPayload` (studentId + timestamp).  
        *   Business rule: only record once per student per day (use `LocalDate`).  
        *   Emit Kafka event `AttendanceRecordedEvent` after persistence.  

#### SUB‑TASK 3.3: Build Kafka Producer & Consumer Services
##### Assigned Sub‑Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `src/main/java/com/membershiphub/backend/kafka/AttendanceEventProducer.java`
    *   **Architectural Requirements:**  
        *   Use `KafkaProducer<String, AttendanceRecordedEvent>` configured via CDI.  
        *   Method `sendAttendanceEvent(AttendanceRecordedEvent event)` with async send and callback logging.  
*   **Target Path 2:** `src/main/java/com/membershiphub/backend/kafka/NotificationEventConsumer.java`
    *   **Architectural Requirements:**  
        *   Subscribe to topic `notifications`.  
        *   On message, invoke `NotificationService.notifyZaloGroup` and `MobilePushService.sendPush`.  

#### SUB‑TASK 3.4: Write Integration Tests for Core Resources
##### Assigned Sub‑Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `src/test/java/com/membershiphub/backend/resource/CenterResourceTest.java`
    *   **Architectural Requirements:**  
        *   Test CRUD operations with role‑based security (expect 403 for non‑admin).  
        *   Verify Kafka event emission on center creation (mock producer).  
*   **Target Path 2:** `src/test/java/com/membershiphub/backend/resource/AttendanceResourceTest.java`
    *   **Architectural Requirements:**  
        *   Simulate QR payload, assert attendance record created.  
        *   Verify duplicate attendance for same student/date is rejected.  
        *   Verify Kafka producer called exactly once.  

#### SUB‑TASK 3.5: DevOps – Finalize Docker Image & Health Checks
##### Assigned Sub‑Agent: DevOps
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `src/main/docker/Dockerfile`
    *   **Architectural Requirements:**  
        *   Add `COPY target/membership-hub-backend.jar app.jar`.  
        *   Add `RUN java -Djgroups.tcp.address=redis -jar app.jar` placeholder for runtime args.  
        *   Include `HEALTHCHECK --interval=30s --timeout=10s CMD curl -f http://localhost:8080/q/health || exit 1`.  
*   **Target Path 2:** `docker-compose.yml`
    *   **Architectural Requirements:**  
        *   Define services: `app`, `postgres`, `kafka`.  
        *   Link app service to postgres & kafka networks.  
        *   Set environment variables for DB connection, Kafka bootstrap, JWT secret.  

#### SUB‑TASK 3.6: Final Code Review & Sign‑off
##### Assigned Sub‑Agent: Reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** All source files created/modified in Days 1‑3 (entities, resources, services, security, kafka, Docker)
    *   **Architectural Requirements:**  
        *   Verify adherence to Java 17 coding standards (line length, naming conventions).  
        *   Confirm all REST endpoints have proper OpenAPI annotations (`@Path`, `@GET`, `@POST`).  
        *   Validate security annotations (`@RolesAllowed`, `@Authenticated`).  
        *   Ensure Kafka events follow a consistent schema (DTOs with `@Valid`).  
        *   Check that Docker image includes only necessary layers and health‑check is present.  

---  

**Phase 2 is now complete.** All backend core functionalities, authentication/authorization, role‑based access, Kafka notification pipeline, and DevOps containerization have been implemented, tested, reviewed, and are ready for the subsequent Frontend Development phase.