# Giai đoạn 1: <!--PHASE_NAME_START-->Thiết lập cơ sở hạ tầng và xác thực<!--PHASE_NAME_END--> | [Translate "Description"]: Giai đoạn này tập trung vào việc xây dựng dịch vụ xác thực, quản lý trung tâm và khóa học.

## 📊 Document Control

| [Translate "Item"] | [Translate "Details"] |
| :--- | :--- |
| **[Translate "Blueprint ID"]** | ARCH-20260805161738 |
| **[Translate "Project Name"]** | membership-hub |
| **[Translate "Phase"]** | 1 |
| **[Translate "Phase Name"]** | <!--PHASE_NAME_START-->Thiết lập cơ sở hạ tầng và xác thực<!--PHASE_NAME_END--> |
| **[Translate "Description"]** | <!--PHASE_DESC_START-->Giai đoạn này tập trung vào việc xây dựng dịch vụ xác thực, quản lý trung tâm và khóa học<!--PHASE_DESC_END--> |
| **[You MUST translate the literal token "Version" into 🇻🇳 Vietnamese]** | 1.0 (Baseline) |
| **[You MUST translate the literal token "Date/Time" into 🇻🇳 Vietnamese]** | 2026/08/05 16:17:38 |
| **[You MUST translate the literal token "Author" into 🇻🇳 Vietnamese]** | Enterprise System Architect (SA Agent) |
| **[You MUST translate the literal token "Approval" into 🇻🇳 Vietnamese]** | Pending Technical Governance Review |

## 1. Phase Operational Scope & Objectives
Giai đoạn này tập trung vào việc xây dựng dịch vụ xác thực, quản lý trung tâm và khóa học. Các dịch vụ này bao gồm xác thực người dùng, quản lý trung tâm và khóa học, và các tính năng liên quan đến việc đăng ký khóa học và điểm danh.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
- `./sources/backend/auth`
- `./sources/backend/centers`
- `./sources/backend/courses`

## 3. Dedicated Sub-Agent Functional Directives
*   **Coder**: Acts as a Senior/Principal Application Developer. Responsible for pure application source code implementation across both backend services and frontend/mobile client applications. Banned from writing test suites or infrastructure manifests.
*   **Tester**: Acts as a Lead/Principal QC/QA. Specialized in test suite engineering, validation, and quality gates. Responsible for generating JUnit, integration tests, E2E automation tests, and performance validation scripts. Banned from modifying application production code.
*   **Reviewer**: Responsible for compiler verification, static analysis gating, and defensive patching. Specialized in code quality audits, resolving compilation bugs, fixing OWASP security vulnerabilities, and addressing SonarQube quality gate blockers.
*   **Doc**: Functions as a Principal Technical Writer and Enterprise Systems Architect. Specialized in compiling comprehensive Markdown technical specifications, schema references, system blueprints, and architecture catalogs. Every single document file generated MUST reside strictly within the centralized storage layout: `./sources/docs/`.
<!-- START_COMMAND_DIRECTIVE_DO_NOT_DISPLAY
[CRITIAL COMMAND:
    # MANDATORY AGENT DOC ALLOCATION MANDATE (CRITICAL GATE):
    - You are STRICTLY FORBIDDEN from omitting or dropping the 'Doc' agent from any computed phase. 
    - For EVERY calculated phase, on **Day 1** of that phase, you MUST explicitly allocate a foundational system documentation task to the **Doc** agent. This task MUST require the 'Doc' agent to map out the architecture, endpoints, database schemas, or deployment topology blueprints corresponding to the active stack of that phase.
    - Failing to allocate the 'Doc' agent on Day 1 of any phase triggers a catastrophic engineering contract violation.
]
END_COMMAND_DIRECTIVE_DO_NOT_DISPLAY-->
*   **Docker**: Specialized strictly in containerization, multi-stage Dockerfile engineering, package optimization, and pushing verified application image assets to DockerHub.
*   **GCP**: Specialized in cloud automation within Google Cloud Platform. Responsible for building and pushing images to Google Cloud Artifact Registry (GCR), and orchestrating container environments natively on Google Cloud Run.
*   **GKE**: Specialized in production container orchestration inside Google Kubernetes Engine. Responsible for building Kubernetes deployment manifests, routing controls, HPA configurations, Helm charts, and deploying microservices workloads into active GKE clusters.

## 4. Phase Definition of Done (DoD)
- Xây dựng dịch vụ xác thực, quản lý trung tâm và khóa học hoàn thành.
- Tất cả các yêu cầu chức năng được xác định trong giai đoạn này đã được triển khai và kiểm tra.
- Tất cả các yêu cầu bảo mật OWASP đã được tuân thủ.
- Tất cả các bài kiểm tra đơn vị và tích hợp đã được thực hiện và vượt qua.

## 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

### 🌤️ [TRANSLATED DAY] 1: <!--DAY_HEADER_START-->XÂY DỰNG DỊCH VỤ XÁC THỰC<!--DAY_HEADER_END-->

#### 📝 [TRANSLATED SUB-TASK] 1.1: Triển khai dịch vụ xác thực với các phương thức đăng ký và đăng nhập qua email/mật khẩu và OAuth2
##### [Translate "Assigned Sub-Agent"]: Coder
##### [Translate "Targeted Components & Technical Requirements"]:
* **[Translate "Target Path"]:** `./sources/backend/auth`
* **[Translate "Traceability Tag Tokens"]:** <!--START_TAGS-->[REQ-001], [REQ-002], [DAT-001]<!--END_TAGS-->

#### 📝 [TRANSLATED SUB-TASK] 1.2: Viết các bài kiểm tra đơn vị và tích hợp cho dịch vụ xác thực
##### [Translate "Assigned Sub-Agent"]: Tester
##### [Translate "Targeted Components & Technical Requirements"]:
* **[Translate "Target Path"]:** `./sources/backend/auth;./sources/backend/auth/src/test/java/org/nlh4j/saas/membershiphub/auth/AuthServiceTest.java`
* **[Translate "Traceability Tag Tokens"]:** <!--START_TAGS-->[REQ-001], [REQ-002]<!--END_TAGS-->

#### 📝 [TRANSLATED SUB-TASK] 1.3: Đánh giá mã nguồn và đảm bảo tuân thủ các tiêu chuẩn lập trình
##### [Translate "Assigned Sub-Agent"]: Reviewer
##### [Translate "Targeted Components & Technical Requirements"]:
* **[Translate "Target Path"]:** `./sources/backend/auth`
* **[Translate "Traceability Tag Tokens"]:** <!--START_TAGS-->[REQ-001], [REQ-002]<!--END_TAGS-->

### 🌤️ [TRANSLATED DAY] 2: <!--DAY_HEADER_START-->XÂY DỰNG DỊCH VỤ QUẢN LÝ TRUNG TÂM VÀ KHÓA HỌC<!--DAY_HEADER_END-->

#### 📝 [TRANSLATED SUB-TASK] 2.1: Triển khai dịch vụ quản lý trung tâm và khóa học
##### [Translate "Assigned Sub-Agent"]: Coder
##### [Translate "Targeted Components & Technical Requirements"]:
* **[Translate "Target Path"]:** `./sources/backend/centers`
* **[Translate "Traceability Tag Tokens"]:** <!--START_TAGS-->[REQ-004], [REQ-005], [REQ-006], [DAT-003]<!--END_TAGS-->

#### 📝 [TRANSLATED SUB-TASK] 2.2: Viết các bài kiểm tra đơn vị và tích hợp cho dịch vụ quản lý trung tâm và khóa học
##### [Translate "Assigned Sub-Agent"]: Tester
##### [Translate "Targeted Components & Technical Requirements"]:
* **[Translate "Target Path"]:** `./sources/backend/centers;./sources/backend/centers/src/test/java/org/nlh4j/saas/membershiphub/centers/CenterServiceTest.java`
* **[Translate "Traceability Tag Tokens"]:** <!--START_TAGS-->[REQ-004], [REQ-005], [REQ-006]<!--END_TAGS-->

#### 📝 [TRANSLATED SUB-TASK] 2.3: Đánh giá mã nguồn và đảm bảo tuân thủ các tiêu chuẩn lập trình
##### [Translate "Assigned Sub-Agent"]: Reviewer
##### [Translate "Targeted Components & Technical Requirements"]:
* **[Translate "Target Path"]:** `./sources/backend/centers`
* **[Translate "Traceability Tag Tokens"]:** <!--START_TAGS-->[REQ-004], [REQ-005], [REQ-006]<!--END_TAGS-->