Execute the master governance arbitration and cross-validation verification loop for Project '{{ project_name }}'.

You MUST thoroughly read, analyze, and cross-examine the following independent incoming asset payloads injected into your workspace context:
- Inbound Core Product Idea Baseline: {{ raw_idea_content }}
- Inbound Validated Software Requirements Specification (SRS): {{ raw_srs_content }}
- Inbound Validated Global Context Blueprint Document: {{ raw_blueprint_content }}

### 🚨 MANDATORY GOVERNANCE AUDIT RULES:
1. **Intelligent Timeline Auto-Detection & Density Audit:** You MUST dynamically extract and audit the actual generated phase count and day-by-day logs metrics embedded within `{{ raw_blueprint_content }}`. Evaluate whether this generated timeline is architecturally optimal, lean, and balanced against the logical complexity of the requirements in `{{ raw_srs_content }}`. You MUST instantly fail and reject the timeline if you detect chronological day bundling ranges (e.g., NO "DAY 1 - DAY 3"), artificial padding days, placeholder review syncs, or garbage tasks introduced solely to expand the project timeline viewport.
2. **Dynamic Topology Verification:** Verify that the physical relative directory file path masks initialized across the daily log segments strictly adhere to the system topology choice. All paths must start strictly with `./sources/`. Ensure zero frontend paths contaminate backend-only projects, and zero backend paths contaminate frontend-only systems.
3. **Sub-Task Metadata Integrity Audit:** Cross-check that every active daily log subsection utilizes individual sequential integers starting natively from DAY 1 for each phase boundary. Verify that every sub-task explicitly assigns a single capitalized sub-agent role token ('Coder' | 'Tester' | 'Reviewer' | 'Doc' | 'Docker' | 'Gcp' | 'Gke') and maps to a valid `D<day_num>_ST<task_index>` identifier node inline.
4. **Strict Domain Scope Control:** You are strictly forbidden from allowing any new, unassigned features, ghost requirement tag codes, or invented data columns outside the BA SRS boundary to pass. If the blueprint has trace omissions or creative fabrications, flag it instantly.

### 🧳 INTELLIGENT DOCUMENT REFERENCING RULE:
Inside Section 1 of your report, you are STRICTLY BANNED from printing raw template variable names (e.g., do NOT print raw strings like raw_idea_content, raw_srs_content, or raw_blueprint_content). Instead, you MUST dynamically scan the contents of the assets to extract their official corporate document ID strings (e.g., `BA-SRS-{{ project_name }}` or `ARCH-ID`). If no explicit ID tokens are found inside the assets, you MUST elegantly fallback to utilizing the natural project token string derived from "{{ project_name }}" combined with the active context domain to form a polished, professional enterprise reference string.

### 📊 MINI-GRID REQUIREMENTS TRACEABILITY MATRIX RULE:
To completely eliminate table format breaking and layout overflow issues caused by large lists of tags, you MUST render a compact, high-density 3-row Markdown Table inside Section 2 to summarize the quantitative metrics. The table MUST strictly follow this exact 3-column configuration:
- Column 1: **Audit Metric**
- Column 2: **Quantitative Counter**
- Column 3: **Status** (A clean literal state tag indicator formatted strictly in Technical English using **`PASSED`** or **`FAILED`**)

### 📌 FAILED BULLET REGISTRY & RISK ANALYSIS RAILS:
Immediately underneath the Mini-Grid Table, you MUST provide a dedicated subsection containing a clean Markdown bulleted list (`*`) mapping out every single dynamic requirement or data Tag ID (`[REQ-XXX]`, `[DAT-XXX]`, `[EXC-XXX]`, etc.) that triggered a **`FAILED`** status (omitted, missing, or misaligned) during your trace check. If no tags failed, explicitly state that functional matrix coverage is 100% complete and pristine with a status of **`PASSED`**.

If and only if any tag fails, you MUST dynamically inject a detailed evaluation block named `### ⚠️ 2.1. Failure Root-Cause Matrix & Architecture Risk Assessment` containing the following parameters:
- **Failed Tag Identifier:** [Explicitly list the failed BA Tag IDs]
- **Root-Cause Analysis & Functional Blind Spot:** [Provide an exhaustive technical breakdown explaining exactly why the baseline failed or which functional contract string from the BA specification was dropped by the SA agent]
- **Systemic Risk Assessment & Compounding Impact:** [Deliver a sharp, high-density impact analysis under OWASP, security data isolation, and business revenue standards, explaining the system damage if left unpatched]

### 🌐 STRICT SEMANTIC INVARIANT SYNTAX PRESERVATION RAILS (MANDATORY LOCALIZATION):
You MUST automatically translate and naturally render every single header title, section divider, markdown table structural text descriptor, and analytical phrase into the targeted execution language: "{{ language }}". However, you are STRICTLY BANNED from translating, changing, or breaking any core technical syntax layers, including markdown operators (`#`, `##`, `| :--- |`), literal Technical English status tokens (**`PASSED`**, **`FAILED`**), and requirement tag code string primitives (e.g. `[REQ-001]`).

You MUST format your master response report strictly using the mandatory Markdown configuration layout below:

# GOVERNANCE VERDICT REPORT: {{ project_name }}

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Audit Report ID** | AUDIT-SENTINEL-{{ doc_id }} |
| **Idea ID** | {{ idea_id }} |
| **Project Name** | {{ project_name }} |
| **Project Description** | {{ project_description }} |
| **Version** | 1.0 (Automated Governance) |
| **Date/Time** | {{ current_timestamp }} |
| **Author** | [Insert your exact assigned sub-agent CRO/CFO persona token dynamically] |
| **Approval** | Certified by Enterprise Technical Governance Board |

## 1. Compliance Matrix Synthesis Analysis
[Provide your high-density technical analysis here, completely translated into {{ language }} based on the referencing rules]

## 2. Requirements Traceability Visualization Matrix
# Render the mandatory 3-row Mini-Grid Markdown table here. Translate all structural descriptions and column headers 1 and 2 into {{ language }}.

### 📌 Failed Bullet Registry
# Output your clean bulleted failure registry list here, followed immediately by the dynamic 'Failure Root-Cause Matrix & Architecture Risk Assessment' block if failures exist. Fully translate all headers and analytical descriptions into {{ language }}.

## 3. Final Regulatory Gate Status
- **Requirements Traceability Mappings:** [PASSED / FAILED]
- **Architectural Guardrails & Topology Paths:** [PASSED / FAILED]
- **Operational Timeline & Calendar Boundaries:** [PASSED / FAILED]

### 🛑 FINAL AUDIT TERMINATION GATEWAY VERDICT
[Insert Code Token here: PASSED or FAILED]
