# PHASE 1 CONTEXT BLUEPRINT: membership-hub

## 1. Phase Operational Scope & Objectives
Phase 1 focuses exclusively on initializing the multi-tenancy database context with tenant isolation schema enforcement. This includes creating the foundational PostgreSQL database schema with mandatory `tenant_id` columns across all core tables, implementing strict row-level security policies, and writing comprehensive unit tests to validate tenant-isolation at the database query level. The phase ensures that all subsequent data operations are inherently scoped to the correct tenant, preventing cross-tenant data leaks from the ground up. This phase directly supports the RBAC model where center administrators have full authority only within their assigned tenant boundary.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
*   **Backend Database Schema:** `./sources/backend/src/main/resources/db/migration/`
*   **Java Entity Classes:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/entity/`
*   **Java Repository Interfaces:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/repository/`
*   **Unit Test Classes:** `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/repository/`
*   **Database Configuration:** `./sources/backend/src/main/resources/application.properties`
*   **SQL Row-Level Security Policies:** Embedded within database migration scripts under `./sources/backend/src/main/resources/db/migration/`

## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for coder, tester, reviewer, doc, docker, GCP, GKE)
*   **coder:** Implements all database migration scripts, Java entity classes with `tenant_id` fields, and repository interfaces with tenant-scoped query methods. Must enforce parameterized queries to prevent SQL injection.
*   **tester:** Writes and executes JUnit tests that verify tenant isolation by attempting cross-tenant data access and asserting failures. Tests must cover both positive (same-tenant) and negative (cross-tenant) scenarios.
*   **doc:** Creates technical documentation detailing the multi-tenancy schema design, row-level security policies, and tenant isolation validation approach. All docs must be placed in `./sources/backend/docs/`.
*   **reviewer:** (Not allocated in Phase 1 per global context)
*   **docker:** (Not allocated in Phase 1 per global context)
*   **GCP:** (Not allocated in Phase 1 per global context)
*   **GKE:** (Not allocated in Phase 1 per global context)

## 4. Phase Definition of Done (DoD)
*   All database tables include a NOT NULL `tenant_id` column of type UUID.
*   Row-level security policies are implemented in PostgreSQL to enforce tenant isolation on `SELECT`, `INSERT`, `UPDATE`, `DELETE`.
*   Java entity classes have `tenantId` fields with appropriate JPA annotations.
*   Repository interfaces include custom query methods that automatically scope operations by `tenantId`.
*   Unit tests achieve 100% coverage of tenant isolation scenarios, with zero cross-tenant data leak possibilities.
*   Technical documentation comprehensively describes the multi-tenancy architecture and validation procedures.
*   All implementations are free from SQL injection vulnerabilities (OWASP A01).

## 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: DATABASE SCHEMA INITIALIZATION WITH TENANT ISOLATION

#### SUB-TASK 1.1: Create foundational database migration script with tenant_id columns
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/src/main/resources/db/migration/V1_0_0__init_multitenant_schema.sql`
    *   **Architectural Requirements:**
        *   Define all tables from Preliminary Data Dictionary with additional `tenant_id UUID NOT NULL` column.
        *   Implement foreign key constraint `tenant_id` references a `tenants` table (to be created in Phase 2).
        *   Use parameterized SQL expressions exclusively; no string concatenation in dynamic SQL.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [ARC-001], [NFR-002]

#### SUB-TASK 1.2: Implement row-level security policies in PostgreSQL
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/src/main/resources/db/migration/V1_0_1__enable_rls_policies.sql`
    *   **Architectural Requirements:**
        *   Enable RLS on all core tables (`users`, `centers`, `courses`, `enrollments`, `attendances`, `student_cards`).
        *   Create policies that restrict `SELECT`, `INSERT`, `UPDATE`, `DELETE` to rows where `tenant_id` matches current tenant.
        *   Use `CURRENT_SETTING('app.current_tenant_id')` to dynamically set tenant context per transaction.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [ARC-001], [NFR-002]

### DAY 2: JAVA ENTITY AND REPOSITORY LAYER IMPLEMENTATION

#### SUB-TASK 2.1: Create Java entity classes with tenantId field
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/entity/User.java`
    *   **Architectural Requirements:**
        *   Annotate `tenantId` field with `@Column(nullable = false)`.
        *   Implement equals/hashCode methods that include `tenantId` for proper cache isolation.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [ARC-001], [NFR-002]

#### SUB-TASK 2.2: Create tenant-scoped repository interfaces
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/repository/UserRepository.java`
    *   **Architectural Requirements:**
        *   Extend `JpaRepository<User, UUID>` with custom `@Query` methods that include `AND tenant_id = :tenantId`.
        *   Use Spring Data's `@Param` annotation to safely bind tenantId parameter.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [ARC-001], [NFR-002]

### DAY 3: TENANT ISOLATION VALIDATION AND UNIT TESTING

#### SUB-TASK 3.1: Write unit tests for tenant isolation validation
##### Assigned Sub-Agent: tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/repository/UserRepository.java;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/repository/UserRepositoryTest.java`
    *   **Architectural Requirements:**
        *   Test that users from tenant A cannot access users from tenant B via repository methods.
        *   Verify that `findByEmail` queries automatically include tenant_id scope.
        *   Use Testcontainers for isolated PostgreSQL testing instance.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [ARC-001], [NFR-002]

#### SUB-TASK 3.2: Create technical documentation for multi-tenancy implementation
##### Assigned Sub-Agent: doc
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/docs/multi-tenancy-architecture.md`
    *   **Architectural Requirements:**
        *   Document the database schema with emphasis on `tenant_id` column placement.
        *   Explain row-level security policy implementation and runtime behavior.
        *   Include diagrams showing data isolation between tenants.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [ARC-001], [NFR-002]