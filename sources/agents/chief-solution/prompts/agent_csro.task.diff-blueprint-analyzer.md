Perform a meticulous architectural diff audit and dynamic requirement integrity repair session for Project '{{ project_name }}'.

Your sole objective is to execute a rigorous cross-examination by cross-referencing and triple-checking the two decoupled incoming technical blueprints provided inside your workspace context:
- Inbound Original Blueprint Asset Baseline (OBP): {{ raw_blueprint_content }}
- Inbound Patched Blueprint Asset Payload (PBP): {{ raw_csro_blueprint_content }}

### 🚨 MANDATORY TRIPLE-CHECK GOVERNANCE LAWS:
1. **Layer 1: Structural Integrity & Tag Traceability Verification:** Audit every single character, schema key, boundary rule, and directory path to verify absolutely zero data loss or architectural regression occurred. You MUST independently trace and verify that 100% of the core systemic Tag IDs (`[REQ-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[ARC-XXX]`, `[NFR-XXX]`) are perfectly preserved, correctly mapped, and structurally unbroken between the two blueprint baselines.
2. **Layer 2: Failure Mode Resiliency Audit:** Stress-test the modified architecture under simulated runtime failures (e.g., token expiration, database crash, message broker lag, network partitioning) to detect logical vulnerabilities in message broker direct exchanges, distributed caches, and Dead-Letter Queue (DLQ/DLX) failover mechanics.
3. **Layer 3: Blind-Spot Sweeping:** Scrutinize the modified version for subtle cloud provider service misnomers, multi-continental latency traps, broken foreign key relational linkages, and data synchronization anomalies under multi-tenancy workspace isolation constraints (`dbConnectionString`). Reject any invalid cloud configurations that slow down system-wide p95 response time metrics.

### 🌴 DYNAMIC TOPOLOGY PRUNING & CO-VARIANCE RULE:
You MUST dynamically extract the framework choice and active modules from the inputs. If a system component or whole architectural layer (e.g., Persistence Database layer, Event Message Broker infrastructure, or Mobile Wrapper boundary) is entirely absent from the baseline scope (e.g., in a Frontend-Only project topology), you are STRICTLY BANNED from inventing fake cloud settings, creating ghost data schemas, or reporting artificial structural defects. Instead, you MUST output a clean, standardized corporate confirmation statement block: `[NOT APPLICABLE: This layout topology is certified as single-tier domain. Specialized persistence and messaging validation loops are automatically bypassed and marked as PASSED]` and continue evaluating the active layers.

### 🧳 INTELLIGENT DOCUMENT REFERENCING RULE:
Inside Section 1 of your report, you are STRICTLY BANNED from printing raw template variable names. Instead, you MUST dynamically scan the contents of the incoming assets to extract the official corporate Document ID string embedded inside the header of the `{{ raw_csro_blueprint_content }}` file (e.g., `ARCH-ID`). If no explicit ID token is discovered, you MUST elegantly fallback to utilizing the natural project token string derived from "{{ project_name }}" combined with the active context domain to form a polished, professional enterprise reference string.

### 📊 MINI-GRID ARCHITECTURE COMPONENT VARIANCE RULE:
To completely eliminate table format breaking and layout overflow issues, you MUST render a compact, high-density 3-row Markdown Table inside Section 2 to summarize the quantitative metrics of the modifications. The table MUST strictly follow this exact 3-column configuration:
- Column 1: **Audit Metric**
- Column 2: **Quantitative Counter**
- Column 3: **Status** (A clean literal state tag indicator formatted strictly in Technical English using **`PASSED`** or **`FAILED`**)

### 📌 MODIFICATIONS BULLET REGISTRY & RISK IMPACT ANALYSIS RAILS:
Immediately underneath the Mini-Grid Table, you MUST provide a dedicated subsection containing a clean Markdown bulleted list (`*`) explicitly detailing every single component change, chronological day adjustment, or metadata format update discovered. 

If and only if your triple-check evaluation detects fatal integration bottlenecks, invalid service definitions, or broken architectural constraints that trigger a **`FAILED`** gate status, you MUST dynamically inject a detailed evaluation block named `### ⚠️ 2__DOT__1__DOT__ Failure Root-Cause Matrix & Architecture Risk Assessment` containing the following parameters:
- **Failed Infrastructure Parameter:** [Explicitly list the failed components or log days]
- **Phân tích nguyên nhân & Điểm mù chức năng:** [Provide an exhaustive technical breakdown explaining exactly why the baseline failed or which formatting/engineering rule was breached]
- **Đánh giá rủi ro hệ thống & Tác động cộng dồn:** [Deliver a sharp, high-density impact analysis under pipeline parsers, automated branch deployment filters, and cloud infrastructure standards, explaining the system damage if left unpatched]

### 🛠️ SELF-HEALING BLUEPRINT PATCH MATRIX DIFF RULE:
Immediately following your risk analysis section, you MUST inject a dedicated section named `## 3. Blueprint Diff Matrix`. Provide a valid markdown 'diff' codeblock wrapper mapping out the exact line-by-line mechanical modifications made between the two documents. Do not translate internal diff operators, minus (`-`), or plus (`+`) technical syntax markers.

### 🌐 STRICT SEMANTIC INVARIANT SYNTAX PRESERVATION RAILS (MANDATORY LOCALIZATION):
You MUST automatically translate and naturally render every single header title, section divider, markdown table structural text descriptor, and analytical phrase into the targeted execution language: "{{ language }}". 
- **CRITICAL COMPLIANCE BOUNDARY:** You are STRICTLY BANNED from translating, changing, formatting, or breaking any structural technical syntax boundaries, including markdown operators (`#`, `##`, `| :--- |`), literal Technical English status tokens (**`PASSED`**, **`FAILED`**), requirement tag codes, and the entire content wrapped within the markdown `diff` or block code wrapper segment.

### 🛑 THE DUAL-OUTPUT REMEDIATION GATEWAY MANDATE (ABSOLUTE):
Immediately after the terminal gate status token, you MUST output the exact delimiter token string `[EXECUTION_REMEDIATION_PAYLOAD_START]`. Immediately following this delimiter token, you MUST apply this strict conditional logic to control output token expenditure:
- **IF Status is FAILED:** You MUST generate and output the total, complete text layout of the final repaired Global Context Blueprint document file, resolving 100% of the identified defects inside the body text. This segment must be a pure, raw technical file with zero code block backticks surrounding the whole payload.
- **IF Status is PASSED:** You are STRICTLY BANNED from replicating or copy-pasting the full blueprint file content. You MUST output nothing but exactly ONE unique literal keyword token: `PRISTINE` and instantly terminate response emission. Any other filler text inside this remediation segment is a fatal pipeline failure.

You MUST format your master response report strictly using the mandatory Markdown configuration layout below:

# TECHNICAL AUDIT REPORT: {{ project_name }}

## 📊 Document Control

| Audit Parameter | Information Details |
| :--- | :--- |
| **Audit Report ID** | AUDIT-DIFF-{{ current_timestamp_2 }} |
| **Idea ID** | {{ idea_id }} |
| **Project Name** | {{ project_name }} |
| **Project Description** | {{ project_description }} |
| **Target Blueprint ID** | [Dynamically extract the exact ARCH-ID token string found inside raw_csro_blueprint_content] |
| **Verification Method** | Independent Multi-Layer Triple-Check Pattern |
| **Auditor Identity** | CSRO Blueprint Diff Analyzer Sub-Agent |
| **Audit Date__SLASH__Time** | {{ current_timestamp }} |
| **Status** | Formatted & Executed |

## 1. Compliance Matrix Synthesis Analysis
[Provide your high-density technical overview analyzing the logical reconciliation of component changes and tag mapping integrity, completely translated into {{ language }} based on the rules. Explicitly declare if the system triggers a PASSED or FAILED state]

## 2. Requirements Traceability Visualization Matrix
# Render the mandatory 3-row Mini-Grid Markdown table here. Translate all structural descriptions and column headers into {{ language }}.

### 📌 Danh sách các phân đoạn thay đổi (Modifications Bullet Registry)
# Output your clean bulleted modifications list here, followed immediately by the dynamic 'Failure Root-Cause Matrix & Architecture Risk Assessment' block if failures exist. Fully translate all headers and analytical descriptions into {{ language }}.

## 3. Blueprint Diff Matrix
# Provide a valid markdown 'diff' codeblock wrapper here mapping out the exact line-by-line mechanical modifications made between the two documents. Do not translate internal diff tokens.

## 4. Final Regulatory Gate Status
- **Requirements Traceability Mappings:** [PASSED / FAILED]
- **Architectural Guardrails & Topology Paths:** [PASSED / FAILED]
- **Operational Timeline & Calendar Boundaries:** [PASSED / FAILED]

### 🛑 FINAL AUDIT ARCH STATUS
[Insert Code Token here: PASSED or FAILED]

[EXECUTION_REMEDIATION_PAYLOAD_START]
[Generate and output the clean repaired full Blueprint document text layout OR the single word token PRISTINE here based strictly on the conditional state rules. Do not wrap in triple backticks.]
