{
  "phase_id": 1,
  "phase_name": "Phase 1: Membership Hub",
  "project_name": "membership-hub",
  "global_context_file": "./sources/.ai/.context/membership-hub.global.blueprint.md",
  "source_target_dir": "",
  "days": [
    {
      "day": 1,
      "context_file": "./sources/.ai/.plan/.context/phase-1.context.blueprint.md",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "1.1",
          "agent": "Coder",
          "desc": "Create Maven project structure and core package layout. Generate `pom.xml` with Quarkus platform, Java 17, Hibernate ORM, SmallRye Kafka, Argon2id, JWT dependencies. Create `Application.java` with `@QuarkusMain` and default config. Add `AppConfig.java` defining `tenantId` property placeholder and `AES256GCMConfig`. Implement `PasswordEncoderConfig`, `JwtConfig`, and `OAuth2Config` for Firebase/Google/Facebook adapters. Enforce OWASP compliance with parameterized queries, tenant isolation, and input validation.",
          "components": [
            "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/"
          ]
        },
        {
          "id": "1.2",
          "agent": "Coder",
          "desc": "Define Kafka topics and event models. Create `notifications.yaml` and `attendance-events.yaml` defining topic names, partitions, and retention. Add `NotificationEvent.java` and `AttendanceEvent.java` POJOs annotated with `@KafkaKey` and `@KafkaTopic`. Ensure event payloads are serialized with Jackson and sensitive fields are encrypted using AES-256-GCM.",
          "components": [
            "./sources/backend/kafka/"
          ]
        },
        {
          "id": "1.3",
          "agent": "Coder",
          "desc": "Implement authentication and JWT issuance. Expose `POST /auth/login` for username/password validation using Argon2id hashed passwords. Expose `GET /auth/oauth/{provider}` for OAuth2 redirects and callback handling. Generate JWT token with `tenant_id`, user id, role list, and expiration. Enforce OWASP compliance with parameterized authentication queries, rate-limiting, and encrypted refresh tokens.",
          "components": [
            "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/resource/AuthResource.java"
          ]
        },
        {
          "id": "1.4",
          "agent": "Docker",
          "desc": "Create base Docker image for backend. Multi-stage build: builder stage (Maven compile) → runtime stage (distroless Java 17). Set non-root user, copy JAR, expose port 8080. Include health-check endpoint `/q/health`. Use `java -Dquarkus.profile=prod` and disable debug flags.",
          "components": [
            "./sources/backend/docker/Dockerfile"
          ]
        },
        {
          "id": "1.5",
          "agent": "GCP",
          "desc": "Draft GCP service account and IAM policies. Generate `service-account.json` placeholder with `membership-hub@<project>.iam.gserviceaccount.com`. Create `iam-policy.yaml` granting `roles/owner` and `roles/container.admin` for GKE provisioning. Enforce least-privilege principle and include `tenant_id` condition in IAM policies where possible.",
          "components": [
            "./sources/gcp/service-account.json",
            "./sources/gcp/iam-policy.yaml"
          ]
        },
        {
          "id": "1.6",
          "agent": "Tester",
          "desc": "Write unit tests for authentication. Test successful login, failed credentials, OAuth2 redirect, and JWT claim validation. Mock `UserService` and `JwtService` to isolate behavior. Verify Argon2id password verification and JWT `tenant_id` inclusion. Ensure tests do not store real passwords and use test-specific hashed values.",
          "components": [
            "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/resource/AuthResource.java;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/resource/AuthResourceTest.java"
          ]
        }
      ]
    },
    {
      "day": 2,
      "context_file": "./sources/.ai/.plan/.context/phase-1.context.blueprint.md",
      "context_section": "DAY 2",
      "sub_tasks": [
        {
          "id": "2.1",
          "agent": "Coder",
          "desc": "Design and create PostgreSQL migration scripts. Create `V1__init.sql` for core tables, `V2__tenant_discriminator.sql` for tenant_id column, and `V3__user_roles.sql` for user-role junction table. Enforce OWASP compliance with `IF NOT EXISTS`, `NOT NULL` constraints, and `CHECK` constraints.",
          "components": [
            "./sources/backend/src/main/resources/db/migration/"
          ]
        },
        {
          "id": "2.2",
          "agent": "Coder",
          "desc": "Implement core JPA entities with tenant isolation. Create `TenantEntity.java` base class and derive `User.java`, `Center.java`, `Course.java`, `Enrollment.java`, `Attendance.java`, `Point.java`, `Promotion.java`, and `Announcement.java`. Annotate with `@Table`, `@Entity`, and `@TenantFilter`. Enforce OWASP compliance with column length limits and tenant filtering.",
          "components": [
            "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/model/"
          ]
        },
        {
          "id": "2.3",
          "agent": "Coder",
          "desc": "Develop role-based access control (RBAC) filter. Implement `ContainerRequestFilter` to extract JWT `tenant_id` and roles. Enforce per-endpoint role permissions and return `403` for unauthorized accesses. Validate JWT signature and ensure `tenant_id` is present.",
          "components": [
            "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/filter/RbacFilter.java"
          ]
        },
        {
          "id": "2.4",
          "agent": "Coder",
          "desc": "Add multi-language locale detection and SEO utilities. Implement `LocaleUtil.java` to read `Accept-Language` header and fallback to user’s stored locale. Create `SeoMetaTagUtil.java` for generating SEO meta tags. Sanitize locale strings to prevent XSS and ensure meta tags are HTML-escaped.",
          "components": [
            "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/util/LocaleUtil.java"
          ]
        },
        {
          "id": "2.5",
          "agent": "Tester",
          "desc": "Write unit tests for schema and RBAC. Test JPA persistence of a `User` with tenant isolation. Verify `TenantEntity` enforces `tenant_id` population. Test RBAC filter logic with mocked JWT claims. Ensure test data does not contain real PII.",
          "components": [
            "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/model/User.java;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/model/UserTest.java"
          ]
        },
        {
          "id": "2.6",
          "agent": "Reviewer",
          "desc": "Perform security review and OWASP validation. Review Java source files for parameterized queries, tenant isolation, encryption of PII fields, and password storage using Argon2id. Provide compliance checklist and flag deviations.",
          "components": [
            "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/"
          ]
        },
        {
          "id": "2.7",
          "agent": "Coder",
          "desc": "Create placeholder frontend skeleton. Generate `package.json`, `next.config.js`, and `tsconfig.json` with TypeScript and i18n plugins. Add `pages/_app.tsx` with locale detection and SEO `<head>` injection. Ensure CSRF tokens are set via headers.",
          "components": [
            "./sources/frontend/"
          ]
        }
      ]
    },
    {
      "day": 3,
      "context_file": "./sources/.ai/.plan/.context/phase-1.context.blueprint.md",
      "context_section": "DAY 3",
      "sub_tasks": [
        {
          "id": "3.1",
          "agent": "Docker",
          "desc": "Complete multi-stage Docker build for backend. Refine builder stage to copy `pom.xml`, run `mvn dependency:go-offline`, and compile source. Runtime stage: copy JAR, set JVM options, and define health-check script. Add labels for maintainer and version.",
          "components": [
            "./sources/backend/docker/Dockerfile"
          ]
        },
        {
          "id": "3.2",
          "agent": "GKE",
          "desc": "Produce GKE deployment manifests. Create `deployment.yaml` with image pull secret, resource limits, and environment variables. Create `service.yaml` to expose port 8080. Create `ingress.yaml` with NGINX ingress and `tls` block. Create `hpa.yaml` for autoscaling.",
          "components": [
            "./sources/gke/deployment.yaml",
            "./sources/gke/service.yaml",
            "./sources/gke/ingress.yaml",
            "./sources/gke/hpa.yaml"
          ]
        },
        {
          "id": "3.3",
          "agent": "GCP",
          "desc": "Draft GCP Cloud Build pipeline. Define steps for Maven build, Docker build, and Docker push to Artifact Registry. Trigger on `main` branch. Include substitutions for `PROJECT_ID`, `IMAGE_NAME`, and `SERVICE_ACCOUNT`. Use service account with limited permissions.",
          "components": [
            "./sources/gcp/cloudbuild.yaml"
          ]
        },
        {
          "id": "3.4",
          "agent": "Tester",
          "desc": "Write integration tests for core flows. Verify user registration, login, JWT acquisition, tenant isolation, attendance QR scan endpoint idempotency, and Kafka event publishing. Use Playwright or Cypress with fixtures. Ensure tests do not store real credentials.",
          "components": [
            "INTEGRATION_SCOPE;./sources/frontend/tests/integration.spec.ts"
          ]
        },
        {
          "id": "3.5",
          "agent": "Manager",
          "desc": "Produce Phase 1 summary and final validation. Document completed artifacts, list open items, confirm adherence to `./sources/` rule and Java package structure, and provide sign-off checklist aligned with Phase Definition of Done.",
          "components": [
            "./sources/phase1-summary.md"
          ]
        }
      ]
    }
  ]
}
-------------------------------------------------
```text{
    "phase_id": 1,
    "phase_name": "Phase 1",
    "project_name": "membership-hub",
    "global_context_file": ".ai/.context/membership-hub.global.blueprint.md",
    "source_target_dir": "sources/",
    "objectives": [],
    "days": [
        {
            "day": 1,
            "context_file": "./sources/.ai/.plan/.context/phase-1.context.blueprint.md",
            "context_section": "DAY 1",
            "sub_tasks": [
                {
                    "id": "1.1",
                    "agent": "Coder",
                    "desc": "Create Maven project structure and core package layout. Generate `pom.xml` with Quarkus platform, Java 17, Hibernate ORM, SmallRye Kafka, Argon2id, JWT dependencies. Create `Application.java` with `@QuarkusMain` and default config. Add `AppConfig.java` defining `tenantId` property placeholder and `AES256GCMConfig`. Implement `PasswordEncoderConfig`, `JwtConfig`, and `OAuth2Config` for Firebase/Google/Facebook adapters. Enforce OWASP compliance with parameterized queries, tenant isolation, and input validation.",
                    "components": [
                        "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/"
                    ]
                },
                {
                    "id": "1.2",
                    "agent": "Coder",
                    "desc": "Define Kafka topics and event models. Create `notifications.yaml` and `attendance-events.yaml` defining topic names, partitions, and retention. Add `NotificationEvent.java` and `AttendanceEvent.java` POJOs annotated with `@KafkaKey` and `@KafkaTopic`. Ensure event payloads are serialized with Jackson and sensitive fields are encrypted using AES-256-GCM.",
                    "components": [
                        "./sources/backend/kafka/"
                    ]
                },
                {
                    "id": "1.3",
                    "agent": "Coder",
                    "desc": "Implement authentication and JWT issuance. Expose `POST /auth/login` for username/password validation using Argon2id hashed passwords. Expose `GET /auth/oauth/{provider}` for OAuth2 redirects and callback handling. Generate JWT token with `tenant_id`, user id, role list, and expiration. Enforce OWASP compliance with parameterized authentication queries, rate-limiting, and encrypted refresh tokens.",
                    "components": [
                        "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/resource/AuthResource.java"
                    ]
                },
                {
                    "id": "1.4",
                    "agent": "Docker",
                    "desc": "Create base Docker image for backend. Multi-stage build: builder stage (Maven compile) → runtime stage (distroless Java 17). Set non-root user, copy JAR, expose port 8080. Include health-check endpoint `/q/health`. Use `java -Dquarkus.profile=prod` and disable debug flags.",
                    "components": [
                        "./sources/backend/docker/Dockerfile"
                    ]
                },
                {
                    "id": "1.5",
                    "agent": "GCP",
                    "desc": "Draft GCP service account and IAM policies. Generate `service-account.json` placeholder with `membership-hub@<project>.iam.gserviceaccount.com`. Create `iam-policy.yaml` granting `roles/owner` and `roles/container.admin` for GKE provisioning. Enforce least-privilege principle and include `tenant_id` condition in IAM policies where possible.",
                    "components": [
                        "./sources/gcp/service-account.json",
                        "./sources/gcp/iam-policy.yaml"
                    ]
                },
                {
                    "id": "1.6",
                    "agent": "Tester",
                    "desc": "Write unit tests for authentication. Test successful login, failed credentials, OAuth2 redirect, and JWT claim validation. Mock `UserService` and `JwtService` to isolate behavior. Verify Argon2id password verification and JWT `tenant_id` inclusion. Ensure tests do not store real passwords and use test-specific hashed values.",
                    "components": [
                        "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/resource/AuthResource.java;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/resource/AuthResourceTest.java"
                    ]
                }
            ]
        },
        {
            "day": 2,
            "context_file": "./sources/.ai/.plan/.context/phase-1.context.blueprint.md",
            "context_section": "DAY 2",
            "sub_tasks": [
                {
                    "id": "2.1",
                    "agent": "Coder",
                    "desc": "Design and create PostgreSQL migration scripts. Create `V1__init.sql` for core tables, `V2__tenant_discriminator.sql` for tenant_id column, and `V3__user_roles.sql` for user-role junction table. Enforce OWASP compliance with `IF NOT EXISTS`, `NOT NULL` constraints, and `CHECK` constraints.",
                    "components": [
                        "./sources/backend/src/main/resources/db/migration/"
                    ]
                },
                {
                    "id": "2.2",
                    "agent": "Coder",
                    "desc": "Implement core JPA entities with tenant isolation. Create `TenantEntity.java` base class and derive `User.java`, `Center.java`, `Course.java`, `Enrollment.java`, `Attendance.java`, `Point.java`, `Promotion.java`, and `Announcement.java`. Annotate with `@Table`, `@Entity`, and `@TenantFilter`. Enforce OWASP compliance with column length limits and tenant filtering.",
                    "components": [
                        "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/model/"
                    ]
                },
                {
                    "id": "2.3",
                    "agent": "Coder",
                    "desc": "Develop role-based access control (RBAC) filter. Implement `ContainerRequestFilter` to extract JWT `tenant_id` and roles. Enforce per-endpoint role permissions and return `403` for unauthorized accesses. Validate JWT signature and ensure `tenant_id` is present.",
                    "components": [
                        "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/filter/RbacFilter.java"
                    ]
                },
                {
                    "id": "2.4",
                    "agent": "Coder",
                    "desc": "Add multi-language locale detection and SEO utilities. Implement `LocaleUtil.java` to read `Accept-Language` header and fallback to user’s stored locale. Create `SeoMetaTagUtil.java` for generating SEO meta tags. Sanitize locale strings to prevent XSS and ensure meta tags are HTML-escaped.",
                    "components": [
                        "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/util/LocaleUtil.java"
                    ]
                },
                {
                    "id": "2.5",
                    "agent": "Tester",
                    "desc": "Write unit tests for schema and RBAC. Test JPA persistence of a `User` with tenant isolation. Verify `TenantEntity` enforces `tenant_id` population. Test RBAC filter logic with mocked JWT claims. Ensure test data does not contain real PII.",
                    "components": [
                        "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/model/User.java;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/model/UserTest.java"
                    ]
                },
                {
                    "id": "2.6",
                    "agent": "Reviewer",
                    "desc": "Perform security review and OWASP validation. Review Java source files for parameterized queries, tenant isolation, encryption of PII fields, and password storage using Argon2id. Provide compliance checklist and flag deviations.",
                    "components": [
                        "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/"
                    ]
                },
                {
                    "id": "2.7",
                    "agent": "Coder",
                    "desc": "Create placeholder frontend skeleton. Generate `package.json`, `next.config.js`, and `tsconfig.json` with TypeScript and i18n plugins. Add `pages/_app.tsx` with locale detection and SEO `<head>` injection. Ensure CSRF tokens are set via headers.",
                    "components": [
                        "./sources/frontend/"
                    ]
                }
            ]
        },
        {
            "day": 3,
            "context_file": "./sources/.ai/.plan/.context/phase-1.context.blueprint.md",
            "context_section": "DAY 3",
            "sub_tasks": [
                {
                    "id": "3.1",
                    "agent": "Docker",
                    "desc": "Complete multi-stage Docker build for backend. Refine builder stage to copy `pom.xml`, run `mvn dependency:go-offline`, and compile source. Runtime stage: copy JAR, set JVM options, and define health-check script. Add labels for maintainer and version.",
                    "components": [
                        "./sources/backend/docker/Dockerfile"
                    ]
                },
                {
                    "id": "3.2",
                    "agent": "GKE",
                    "desc": "Produce GKE deployment manifests. Create `deployment.yaml` with image pull secret, resource limits, and environment variables. Create `service.yaml` to expose port 8080. Create `ingress.yaml` with NGINX ingress and `tls` block. Create `hpa.yaml` for autoscaling.",
                    "components": [
                        "./sources/gke/deployment.yaml",
                        "./sources/gke/service.yaml",
                        "./sources/gke/ingress.yaml",
                        "./sources/gke/hpa.yaml"
                    ]
                },
                {
                    "id": "3.3",
                    "agent": "GCP",
                    "desc": "Draft GCP Cloud Build pipeline. Define steps for Maven build, Docker build, and Docker push to Artifact Registry. Trigger on `main` branch. Include substitutions for `PROJECT_ID`, `IMAGE_NAME`, and `SERVICE_ACCOUNT`. Use service account with limited permissions.",
                    "components": [
                        "./sources/gcp/cloudbuild.yaml"
                    ]
                },
                {
                    "id": "3.4",
                    "agent": "Tester",
                    "desc": "Write integration tests for core flows. Verify user registration, login, JWT acquisition, tenant isolation, attendance QR scan endpoint idempotency, and Kafka event publishing. Use Playwright or Cypress with fixtures. Ensure tests do not store real credentials.",
                    "components": [
                        "INTEGRATION_SCOPE;./sources/frontend/tests/integration.spec.ts"
                    ]
                },
                {
                    "id": "3.5",
                    "agent": "Manager",
                    "desc": "Produce Phase 1 summary and final validation. Document completed artifacts, list open items, confirm adherence to `./sources/` rule and Java package structure, and provide sign-off checklist aligned with Phase Definition of Done.",
                    "components": [
                        "./sources/phase1-summary.md"
                    ]
                }
            ]
        }
    ],
    "phase_idx": 1,
    "phase_context_file": ".ai/.plan/.context/phase-1.context.blueprint.md"
}```
-------------------------------------------------
