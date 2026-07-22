```json
{
  "phase_id": 1,
  "phase_name": "Phase 1",
  "project_name": "membership-hub",
  "global_context_file": ".ai/.context/membership-hub.global.blueprint.md",
  "source_target_dir": "",
  "days": [
    {
      "day": 1,
      "context_file": ".ai/.plan/.context/phase-1.context.blueprint.md",
      "context_section": "DAY 1",
      "sub_tasks": [
        {
          "id": "1.1",
          "agent": "Coder",
          "desc": "Configure Enterprise Multi-Module Backend",
          "components": [
            "./sources/backend/pom.xml",
            "./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/rest/HealthResource.java"
          ]
        },
        {
          "id": "1.2",
          "agent": "Docker",
          "desc": "Initialize Core Multi-Stage Container Setup",
          "components": [
            "./sources/backend/Dockerfile"
          ]
        },
        {
          "id": "1.3",
          "agent": "Tester",
          "desc": "Execute Core Unit and Ingestion Suite",
          "components": [
            "./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/rest/HealthResource.java;./sources/backend/src/test/java/org/nlh4j/saas/membership-hub/rest/HealthResourceTest.java"
          ]
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
          "desc": "Define Database Schema",
          "components": [
            "./sources/backend/src/main/resources/db/schema.sql"
          ]
        },
        {
          "id": "2.2",
          "agent": "Coder",
          "desc": "Initialize Database Connection",
          "components": [
            "./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/config/DatabaseConfig.java"
          ]
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
          "desc": "Initialize Frontend Project Structure",
          "components": [
            "./sources/frontend/"
          ]
        },
        {
          "id": "3.2",
          "agent": "Coder",
          "desc": "Configure Frontend Dependencies",
          "components": [
            "./sources/frontend/package.json"
          ]
        }
      ]
    }
  ]
}
```
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
                    "desc": "Configure Enterprise Multi-Module Backend",
                    "components": [
                        "./sources/backend/pom.xml",
                        "./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/rest/HealthResource.java"
                    ]
                },
                {
                    "id": "1.2",
                    "agent": "Docker",
                    "desc": "Initialize Core Multi-Stage Container Setup",
                    "components": [
                        "./sources/backend/Dockerfile"
                    ]
                },
                {
                    "id": "1.3",
                    "agent": "Tester",
                    "desc": "Execute Core Unit and Ingestion Suite",
                    "components": [
                        "./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/rest/HealthResource.java;./sources/backend/src/test/java/org/nlh4j/saas/membership-hub/rest/HealthResourceTest.java"
                    ]
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
                    "desc": "Define Database Schema",
                    "components": [
                        "./sources/backend/src/main/resources/db/schema.sql"
                    ]
                },
                {
                    "id": "2.2",
                    "agent": "Coder",
                    "desc": "Initialize Database Connection",
                    "components": [
                        "./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/config/DatabaseConfig.java"
                    ]
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
                    "desc": "Initialize Frontend Project Structure",
                    "components": [
                        "./sources/frontend/"
                    ]
                },
                {
                    "id": "3.2",
                    "agent": "Coder",
                    "desc": "Configure Frontend Dependencies",
                    "components": [
                        "./sources/frontend/package.json"
                    ]
                }
            ]
        }
    ],
    "phase_idx": 1,
    "phase_context_file": ".ai/.plan/.context/phase-1.context.blueprint.md"
}
-------------------------------------------------
