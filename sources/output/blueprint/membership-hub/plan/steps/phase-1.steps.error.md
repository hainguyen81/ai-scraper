```json
{
  "phase_id": 1,
  "phase_name": "membership-hub",
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
          "desc": "Create Domain Entities with Multi‑Tenant & OWASP Controls",
          "components": [
            "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/domain/Tenant.java",
            "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/domain/User.java",
            "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/domain/Role.java",
            "./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/domain/TenantTest.java",
            "./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/domain/UserTest.java",
            "./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/domain/RoleTest.java"
          ]
        },
        {
          "id": "1.2",
          "agent": "Docker",
          "desc": "Build Multi‑Stage Docker Image",
          "components": [
            "./sources/backend/docker/Dockerfile"
          ]
        },
        {
          "id": "1.3",
          "agent": "GCP",
          "desc": "Provision GCP IAM Service Account",
          "components": [
            "./sources/backend/gcp/iam-config.yaml"
          ]
        },
        {
          "id": "1.4",
          "agent": "Manager",
          "desc": "Orchestrate Phase 1 Deliverables",
          "components": [
            "./sources/backend/Phase1-Orchestration.md"
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
          "desc": "Develop Core Authentication Service with OAuth & JWT",
          "components": [
            "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/AuthService.java"
          ]
        },
        {
          "id": "2.2",
          "agent": "Reviewer",
          "desc": "Review Security & Code Quality",
          "components": [
            "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/AuthService.java"
          ]
        },
        {
          "id": "2.3",
          "agent": "Tester",
          "desc": "Unit Test Authentication Service",
          "components": [
            "AuthService.java;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/service/AuthServiceTest.java"
          ]
        },
        {
          "id": "2.4",
          "agent": "GKE",
          "desc": "Create GKE Deployment Manifests",
          "components": [
            "./sources/backend/kubernetes/deployment.yaml"
          ]
        }
      ]
    }
  ]
}
```
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
                    "desc": "Create Domain Entities with Multi‑Tenant & OWASP Controls",
                    "components": [
                        "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/domain/Tenant.java",
                        "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/domain/User.java",
                        "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/domain/Role.java",
                        "./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/domain/TenantTest.java",
                        "./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/domain/UserTest.java",
                        "./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/domain/RoleTest.java"
                    ]
                },
                {
                    "id": "1.2",
                    "agent": "Docker",
                    "desc": "Build Multi‑Stage Docker Image",
                    "components": [
                        "./sources/backend/docker/Dockerfile"
                    ]
                },
                {
                    "id": "1.3",
                    "agent": "GCP",
                    "desc": "Provision GCP IAM Service Account",
                    "components": [
                        "./sources/backend/gcp/iam-config.yaml"
                    ]
                },
                {
                    "id": "1.4",
                    "agent": "Manager",
                    "desc": "Orchestrate Phase 1 Deliverables",
                    "components": [
                        "./sources/backend/Phase1-Orchestration.md"
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
                    "desc": "Develop Core Authentication Service with OAuth & JWT",
                    "components": [
                        "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/AuthService.java"
                    ]
                },
                {
                    "id": "2.2",
                    "agent": "Reviewer",
                    "desc": "Review Security & Code Quality",
                    "components": [
                        "./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/AuthService.java"
                    ]
                },
                {
                    "id": "2.3",
                    "agent": "Tester",
                    "desc": "Unit Test Authentication Service",
                    "components": [
                        "AuthService.java;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/service/AuthServiceTest.java"
                    ]
                },
                {
                    "id": "2.4",
                    "agent": "GKE",
                    "desc": "Create GKE Deployment Manifests",
                    "components": [
                        "./sources/backend/kubernetes/deployment.yaml"
                    ]
                }
            ]
        }
    ],
    "phase_idx": 1,
    "phase_context_file": ".ai/.plan/.context/phase-1.context.blueprint.md"
}```
-------------------------------------------------
