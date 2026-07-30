# PHASE 1 CONTEXT BLUEPRINT: membership-hub

## 1. Phase Operational Scope & Objectives
Initialize the backend database context with a multi‑tenancy `tenant_id` schema that supports isolation across centers and enforces OWASP‑compliant data handling. Produce comprehensive technical documentation for the schema and implement unit tests that validate tenant‑isolation queries.

## 2. Allowed Technical Scope & Directory Boundaries
- `./sources/backend/src/` – core Node.js service code, models, migrations, and tenancy configuration.  
- `./sources/backend/src/models/` – Sequelize/TypeORM model definitions (must include `tenant_id` column).  
- `./sources/backend/src/migrations/` – SQL or migration scripts that add `tenant_id` to all relevant tables.  
- `./sources/backend/src/queries/` – repository functions that filter by `tenant_id`.  
- `./sources/backend/tests/` – Jest/Mocha unit test suites.  
- `./sources/backend/docs/` – markdown documentation for schema and tenancy rules.  
- REST endpoints under `./sources/backend/src/routes/tenancy/*.js` (e.g., `GET /api/v1/tenants/:tenantId/users`).

## 3. Dedicated Sub-Agent Functional Directives
- **coder**: Create the multi‑tenancy schema, add `tenant_id` columns to core tables, define foreign‑key constraints, and embed OWASP mitigations (parameterized queries, input validation). Also generate migration scripts.  
- **doc**: Compile a complete data‑dictionary and architectural diagram documenting the tenancy model, column definitions, and security controls. Store under `./sources/backend/docs/tenant-schema.md`.  
- **tester**: Write unit tests that verify tenant‑isolation queries return only records belonging to the authenticated tenant and that unauthorized access is blocked. Ensure test coverage aligns with `[NFR-002]` performance and reliability expectations.

## 4. Phase Definition of Done (DoD)
- All core tables (`users`, `centers`, `courses`, `enrollments`, `attendance`, `student_cards`, `notifications`, `promotions`, `announcements`) contain a `tenant_id` column of type `UUID` with appropriate NOT NULL constraints.  
- Foreign‑key relationships reference `tenant_id` to enforce isolation.  
- Migration scripts are version‑controlled and idempotent.  
- OWASP Top 10 mitigations are applied (parameterized queries, input validation, output encoding).  
- Unit tests achieve ≥ 90 % coverage for tenant‑validation queries and pass CI checks.  
- Documentation files exist and describe the schema, tenancy rules, and security controls.  
- All artifacts reside under `./sources/` respecting the Mandatory Path Subdirectory Rule.

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: Initialize Multi‑Tenancy Database Schema and Documentation
#### SUB‑TASK 1.1: Design and Create Multi‑Tenancy Schema
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/src/migrations/202511010001_add_tenant_id_to_users.js`
* **Architectural Requirements:**
  * Define a `tenant_id` column (UUID, NOT NULL) in the `users` table migration.  
  * Add a composite index `(tenant_id, email)` for fast tenant‑specific lookups.  
  * Use parameterized queries in migration to avoid SQL injection.  
  * Enforce OWASP A03:2021 – SQL Injection by using prepared statements.  
* **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
  * **Targeted Tag IDs:** [REQ-001], [ARC-001], [DAT-001]

#### SUB‑TASK 1.2: Document the New Tenancy Schema
##### Assigned Sub-Agent: doc
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/docs/tenant-schema.md`
* **Architectural Requirements:**
  * Include a table listing each migrated entity, its columns, data types, and the new `tenant_id` field.  
  * Add a section on tenancy isolation rules and OWASP compliance notes.  
  * Ensure markdown follows project style guide and is placed under `./sources/`.  
* **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
  * **Targeted Tag IDs:** [REQ-001], [ARC-001], [DAT-001]

#### SUB‑TASK 1.3: Write Unit Tests for Tenant‑Isolation Validation Queries
##### Assigned Sub-Agent: tester
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/src/queries/tenantValidation.js;./sources/backend/tests/tenantValidation.test.js`
* **Architectural Requirements:**
  * Implement a query function that selects records filtered by `tenant_id`.  
  * Write Jest tests that assert correct record retrieval for the owning tenant and no records for a different tenant.  
  * Validate that the query uses parameterized statements to prevent injection.  
  * Ensure test suite runs within the 200 ms latency target (`[NFR-002]`).  
* **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
  * **Targeted Tag IDs:** [ARC-001], [NFR-002]

All Phase 1 objectives are satisfied on Day 1; no further daily logs are required.