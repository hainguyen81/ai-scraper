# Phase 2: <!--PHASE_NAME_START-->centerCourseMgmt<!--PHASE_NAME_END--> | Description: Implement center, course, enrollment, membership card, notification, promotion, and announcement capabilities with full CRUD, validation, audit logging, role-based access control, and compliance with performance, availability, security, and scalability requirements.

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260802082615 |
| **Project Name** | membership-hub |
| **Phase** | 2 |
| **Technical Phase Name** | <!--PHASE_NAME_START-->centerCourseMgmt<!--PHASE_NAME_END--> |
| **Description** | Implement center, course, enrollment, membership card, notification, promotion, and announcement capabilities with full CRUD, validation, audit logging, role-based access control, and compliance with performance, availability, security, and scalability requirements. |
| **Version** | 1.0 (Baseline) |
| **Date/Time** | 2026/08/02 08:26:15 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 1. Phase Operational Scope & Objectives
- **Core Objectives**: Deploy backend modules for Centers, Courses, Enrollments, StudentCards, Notifications, Promotions, and Announcements with complete REST API coverage, Sequelize ORM models, validation, audit logging, and role‑based access control.
- **Technical Deliverables**:
  - **DDL SQL Schemas** (DAT‑002 to DAT‑010) defining tables: `centers`, `courses`, `enrollments`, `studentcards`, `notifications`, `promotions`, `announcements` with constraints, indexes, and foreign keys.
  - **API Contracts** (REQ‑004 to REQ‑018) specifying HTTP methods, request/response payloads, validation rules, and error handling.
  - **Exception Flows** (EXC‑003, EXC‑004, EXC‑005) covering notification delivery failures, validation errors, and taxID conflicts.
  - **NFR Compliance** (NFR‑001 to NFR‑004) integrated across components: performance (≤200 ms average), 99.9 % availability, OWASP security hardening, and horizontal scalability on GKE.
- **Quality Gates**: All DDLs applied, API endpoints functional, unit test coverage ≥85 % for new models/controllers, OWASP compliance verified, 100 % traceability tag mapping.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
**Permitted Backend Artifacts** (all under `./sources/backend/`):
- `./sources/backend/src/models/centers.model.ts`
- `./sources/backend/src/models/courses.model.ts`
- `./sources/backend/src/models/enrollments.model.ts`
- `./sources/backend/src/models/studentcards.model.ts`
- `./sources/backend/src/models/notifications.model.ts`
- `./sources/backend/src/models/promotions.model.ts`
- `./sources/backend/src/models/announcements.model.ts`
- `./sources/backend/src/controllers/centers.controller.ts`
- `./sources/backend/src/controllers/courses.controller.ts`
- `./sources/backend/src/controllers/enrollments.controller.ts`
- `./sources/backend/src/controllers/studentcards.controller.ts`
- `./sources/backend/src/controllers/notifications.controller.ts`
- `./sources/backend/src/controllers/promotions.controller.ts`
- `./sources/backend/src/controllers/announcements.controller.ts`
- `./sources/backend/src/middleware/validation.middleware.ts`
- `./sources/backend/src/middleware/auth.middleware.ts`
- `./sources/backend/src/middleware/audit.middleware.ts`
- `./sources/backend/tests/centers.test.ts`
- `./sources/backend/tests/courses.test.ts`
- `./sources/backend/tests/enrollments.test.ts`
- `./sources/backend/tests/studentcards.test.ts`
- `./sources/backend/tests/notifications.test.ts`
- `./sources/backend/tests/promotions.test.ts`
- `./sources/backend/tests/announcements.test.ts`

**REST Endpoints** (Phase 2 scope):
- `GET /api/v1/centers`
- `POST /api/v1/centers`
- `PUT /api/v1/centers/{centerId}`
- `DELETE /api/v1/centers/{centerId}`
- `POST /api/v1/centers/{centerId}/admin`
- `GET /api/v1/courses`
- `POST /api/v1/courses`
- `PUT /api/v1/courses/{courseId}`
- `DELETE /api/v1/courses/{courseId}`
- `POST /api/v1/courses/{courseId}/teacher`
- `GET /api/v1/courses/browse?studentId={studentId}`
- `POST /api/v1/enrollments`
- `GET /api/v1/studentcards/{studentId}`
- `PUT /api/v1/studentcards/{cardId}/extend`
- `POST /api/v1/notifications`
- `POST /api/v1/promotions`