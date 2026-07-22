### JSON Output Based on Provided Markdown Content

Given the detailed Phase 1 context and the strict guidelines for translation, the following JSON schema represents the day-by-day engineering tracking steps for Phase 1 of the `membership-hub` project.

```json
{
  "phase_id": 1,
  "phase_name": "Phase 1",
  "project_name": "membership-hub",
  "global_context_file": ".ai/.context/membership-hub.global.blueprint.md",
  "source_target_dir": "./",
  "days": [
    {
      "day": 1,
      "context_file": ".ai/.plan/.context/phase-1.context.blueprint.md",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "1.1",
          "agent": "Coder",
          "desc": "Backend Scaffolding & DB/Kafka Config",
          "components": [
            "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/Center.java",
            "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/User.java",
            "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/Role.java"
          ]
        },
        {
          "id": "1.2",
          "agent": "Coder",
          "desc": "Frontend Next.js Init & i18n Middleware",
          "components": [
            "./sources/frontend/pages/_app.js",
            "./sources/frontend/pages/index.js",
            "./sources/frontend/components/Layout.js"
          ]
        },
        {
          "id": "1.3",
          "agent": "DevOps",
          "desc": "CI/CD Pipeline & Docker Stub",
          "components": [
            "./Dockerfile",
            "./github/workflows/ci-cd.yml"
          ]
        },
        {
          "id": "1.4",
          "agent": "Tester",
          "desc": "Initial Unit Test Suite",
          "components": [
            "./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/CenterTest.java;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/UserTest.java"
          ]
        },
        {
          "id": "1.5",
          "agent": "Reviewer",
          "desc": "Static Analysis & Path Compliance",
          "components": []
        }
      ]
    },
    {
      "day": 2,
      "context_file": ".ai/.plan/.context/phase-1.context.blueprint.md",
      "context_section": "DAY 2",
      "sub_tasks": [
        {
          "id": "2.1",
          "agent": "Coder",
          "desc": "Core JPA Entities & Repositories",
          "components": [
            "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/Course.java",
            "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/Enrollment.java",
            "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/Attendance.java"
          ]
        },
        {
          "id": "2.2",
          "agent": "Coder",
          "desc": "Auth Page & Role-Based Routing Guard",
          "components": [
            "./sources/frontend/pages/login.js",
            "./sources/frontend/components/RoleGuard.js"
          ]
        },
        {
          "id": "2.3",
          "agent": "Tester",
          "desc": "Repository & Entity Validation Tests",
          "components": [
            "INTEGRATION_SCOPE;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/RepositoryTest.java"
          ]
        },
        {
          "id": "2.4",
          "agent": "Reviewer",
          "desc": "Data Model & Routing Compliance Audit",
          "components": []
        }
      ]
    },
    {
      "day": 3,
      "context_file": ".ai/.plan/.context/phase-1.context.blueprint.md",
      "context_section": "DAY 3",
      "sub_tasks": [
        {
          "id": "3.1",
          "agent": "Coder",
          "desc": "Auth Endpoint Stubs & Locale Detection Finalization",
          "components": [
            "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/AuthEndpoint.java",
            "./sources/frontend/components/LocaleDetector.js"
          ]
        },
        {
          "id": "3.2",
          "agent": "Tester",
          "desc": "Integration & E2E Auth/Route Tests",
          "components": [
            "./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/AuthTest.java;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/RouteTest.java"
          ]
        },
        {
          "id": "3.3",
          "agent": "DevOps",
          "desc": "Pipeline Execution & Image Build Validation",
          "components": [
            "./github/workflows/ci-cd.yml"
          ]
        },
        {
          "id": "3.4",
          "agent": "Reviewer",
          "desc": "Final Guardrail Sign-off",
          "components": []
        }
      ]
    }
  ]
}
```

This JSON output adheres to the specified schema and incorporates all the requirements and constraints outlined in the Phase 1 context markdown, including the day-by-day breakdown, sub-tasks, agent assignments, and component paths.
-------------------------------------------------
{
    "phase_id": 1,
    "phase_name": "Phase 1",
    "project_name": "membership-hub",
    "global_context_file": ".ai/.context/membership-hub.global.blueprint.md",
    "source_target_dir": "sources/",
    "objectives": [],
    "days": [
        {
            "day": 1,
            "context_file": ".ai/.plan/.context/phase-1.context.blueprint.md",
            "context_section": "DAY 1",
            "sub_tasks": [
                {
                    "id": "1.1",
                    "agent": "Coder",
                    "desc": "Backend Scaffolding & DB/Kafka Config",
                    "components": [
                        "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/Center.java",
                        "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/User.java",
                        "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/Role.java"
                    ]
                },
                {
                    "id": "1.2",
                    "agent": "Coder",
                    "desc": "Frontend Next.js Init & i18n Middleware",
                    "components": [
                        "./sources/frontend/pages/_app.js",
                        "./sources/frontend/pages/index.js",
                        "./sources/frontend/components/Layout.js"
                    ]
                },
                {
                    "id": "1.3",
                    "agent": "DevOps",
                    "desc": "CI/CD Pipeline & Docker Stub",
                    "components": [
                        "./Dockerfile",
                        "./github/workflows/ci-cd.yml"
                    ]
                },
                {
                    "id": "1.4",
                    "agent": "Tester",
                    "desc": "Initial Unit Test Suite",
                    "components": [
                        "./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/CenterTest.java;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/UserTest.java"
                    ]
                },
                {
                    "id": "1.5",
                    "agent": "Reviewer",
                    "desc": "Static Analysis & Path Compliance",
                    "components": []
                }
            ]
        },
        {
            "day": 2,
            "context_file": ".ai/.plan/.context/phase-1.context.blueprint.md",
            "context_section": "DAY 2",
            "sub_tasks": [
                {
                    "id": "2.1",
                    "agent": "Coder",
                    "desc": "Core JPA Entities & Repositories",
                    "components": [
                        "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/Course.java",
                        "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/Enrollment.java",
                        "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/Attendance.java"
                    ]
                },
                {
                    "id": "2.2",
                    "agent": "Coder",
                    "desc": "Auth Page & Role-Based Routing Guard",
                    "components": [
                        "./sources/frontend/pages/login.js",
                        "./sources/frontend/components/RoleGuard.js"
                    ]
                },
                {
                    "id": "2.3",
                    "agent": "Tester",
                    "desc": "Repository & Entity Validation Tests",
                    "components": [
                        "INTEGRATION_SCOPE;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/RepositoryTest.java"
                    ]
                },
                {
                    "id": "2.4",
                    "agent": "Reviewer",
                    "desc": "Data Model & Routing Compliance Audit",
                    "components": []
                }
            ]
        },
        {
            "day": 3,
            "context_file": ".ai/.plan/.context/phase-1.context.blueprint.md",
            "context_section": "DAY 3",
            "sub_tasks": [
                {
                    "id": "3.1",
                    "agent": "Coder",
                    "desc": "Auth Endpoint Stubs & Locale Detection Finalization",
                    "components": [
                        "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/AuthEndpoint.java",
                        "./sources/frontend/components/LocaleDetector.js"
                    ]
                },
                {
                    "id": "3.2",
                    "agent": "Tester",
                    "desc": "Integration & E2E Auth/Route Tests",
                    "components": [
                        "./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/AuthTest.java;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/RouteTest.java"
                    ]
                },
                {
                    "id": "3.3",
                    "agent": "DevOps",
                    "desc": "Pipeline Execution & Image Build Validation",
                    "components": [
                        "./github/workflows/ci-cd.yml"
                    ]
                },
                {
                    "id": "3.4",
                    "agent": "Reviewer",
                    "desc": "Final Guardrail Sign-off",
                    "components": []
                }
            ]
        }
    ],
    "phase_idx": 1,
    "phase_context_file": ".ai/.plan/.context/phase-1.context.blueprint.md"
}
-------------------------------------------------
