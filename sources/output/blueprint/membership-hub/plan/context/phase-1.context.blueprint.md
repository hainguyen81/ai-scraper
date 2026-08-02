# Phase 1: <!--PHASE_NAME_START-->coreDataAuth<!--PHASE_NAME_END--> | Description: Comprehensive foundational data model, user lifecycle, authentication/authorization, and core validation/exception handling for the membership-hub microservice platform.

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260802082615 |
| **Project Name** | membership-hub |
| **Phase** | 1 |
| **Technical Phase Name** | <!--PHASE_NAME_START-->coreDataAuth<!--PHASE_NAME_END--> |
| **Description** | Comprehensive foundational data model, user lifecycle, authentication/authorization, and core validation/exception handling for the membership-hub microservice platform. |
| **Version** | 1.0 (Baseline) |
| **Date/Time** | 2026/08/02 08:26:15 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 1. Phase Operational Scope & Objectives
Establish the core data model and user lifecycle, implementing essential authentication/authorization, role management, and robust validation/exception handling to support downstream features. Deliver production‑ready Sequelize models, JWT‑based auth, role assignment, and comprehensive error handling aligned with OWASP best practices and full traceability tag coverage.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
All backend artifacts must reside under `./sources/backend/`. Permitted file paths include:
- `./sources/backend/src/models/users.model.ts`
- `./sources/backend/src/models/centers.model.ts`
- `./sources/backend/src/models/courses.model.ts`
- `./sources/backend/src/models/enrollments.model.ts`
- `./sources/backend/src/models/attendance.model.ts`
- `./sources/backend/src/models/studentcards.model.ts`
- `./sources/backend/src/models/notifications.model.ts`
- `./sources/backend/src/models/roles.model.ts`
- `./sources/backend/src/models/promotions.model.ts`
- `./sources/backend/src/models/announcements.model.ts`
- `./sources/backend/src/models/systemsettings.model.ts`
- `./sources/backend/src/services/social-auth.service.ts`
- `./sources/backend/src/controllers/centers.controller.ts`
- `./sources/backend/src/controllers/courses.controller.ts`
- `./sources/backend/src/controllers/enrollments.controller.ts`
- `./sources/backend/src/controllers/notifications.controller.ts`
- `./sources/backend/src/middleware/validation.middleware.ts`
- `./sources/backend/src/middleware/auth.middleware.ts`
- `./sources/backend/src/middleware/audit.middleware.ts`
- `./sources/backend/tests/users.test.ts`
- `./sources/backend/tests/centers.test.ts`
- `./sources/backend/tests/courses.test.ts`
- `./sources/backend/tests/enrollments.test.ts`
- `./sources/backend/tests/attendance.test.ts`
- `./sources/backend/tests/studentcards.test.ts`
- `./sources/backend/tests/notifications.test.ts`
- `./sources/backend/tests/roles.test.ts`
- `./sources/backend/tests/promotions.test.ts`
- `./sources/backend/tests/announcements.test.ts`
- `./sources/backend/tests/systemsettings.test.ts`

REST endpoints to be implemented (Phase 1 scope):
- `POST /api/v1/auth/register`
- `POST /api/v1/auth/social`
- `PUT /api/v1/users/{userId}/role`
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
- `PUT /api/v1/promotions/{promoId}`
- `DELETE /api/v1/promotions/{promoId}`
- `POST /api/v1/announcements`
- `PUT /api/v1/announcements/{announcementId}`
- `DELETE /api/v1/announcements/{announcementId}`

## 3. Dedicated Sub-Agent Functional Directives
- **Coder**: Implement Sequelize models, validation hooks, JWT auth, role management, and all required API controllers and middleware. Ensure OWASP compliance (SQL injection prevention, input validation, secure password handling, rate limiting). Write unit tests covering happy paths, validation errors, duplicate scenarios, and exception flows.
- **Tester**: Develop comprehensive test suites for each model