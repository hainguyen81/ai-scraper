Perform a complete architectural guardrail and scheduling validation audit and dynamic blueprint repair session for Project '{{ project_name }}'. 

You MUST thoroughly cross-examine the structural data metrics of these two assets:
- Inbound BA SRS Data Source: {{ raw_srs_content }}
- Inbound Generated Initial SA Blueprint Document: {{ raw_blueprint_content }}

Your infrastructure governance loop MUST strictly enforce exactly four compliance gate rules:
1. **Dynamic Topology Path Audit Gate:** Read the technology framework choices from the inputs. All file components must start strictly with `./sources/`. Verify that the directory path prefixing matches the active topology. Reject any relative file path masks or dummy paths.
2. **Phase Ceiling Evaluation Gate:** Do NOT reject short, un-padded, high-density timelines that consume fewer phases than {{ num_phases }} or fewer days than {{ max_days_per_phase }}, provided they successfully map 100% of the BA requirement tags. You MUST instantly reject the blueprint if any phase or log exceeds {{ num_phases }} or {{ max_days_per_phase }}, or incorporates chronological day bundling ranges (e.g., "DAY 1 - DAY 3").
3. **Anti-Padding & Task Rác Audit Gate:** Audit the daily logs for rác filler tasks. If you detect placeholder activities, artificial sync meetings, empty reviews, or documentation padding to expand the calendar, reject immediately.
4. **Sub-Task Metadata Blueprint Audit Gate:** Verify that every daily log subsection contains an atomic sub-agent role token strictly capitalized ('Coder' | 'Tester' | 'Reviewer' | 'Doc' | 'Docker' | 'Gcp' | 'Gke'), and links each relative file path to a valid `D<day_num>_ST<task_index>` identifier node inline.

### 🧳 INTELLIGENT DOCUMENT REFERENCING RULE:
Inside Section 1 of your report, you are STRICTLY BANNED from printing raw template variable names. Instead, you MUST dynamically scan the contents of the assets to extract their official corporate document ID strings (e.g., `BA-SRS-{{ project_name }}` or `ARCH-ID`). If no explicit ID tokens are found inside the assets, you MUST elegantly fallback to utilizing the natural project token string derived from "{{ project_name }}" combined with the active context domain to form a polished, professional enterprise reference string.

### 📊 MINI-GRID ARCHITECTURE AUDIT QUANTITATIVE RULE:
To completely eliminate table format breaking and layout overflow issues, you MUST render a compact, high-density 3-row Markdown Table inside Section 2 to summarize the quantitative counters. The table MUST strictly follow this exact 3-column configuration:
- Column 1: **Audit Metric**
- Column 2: **Quantitative Counter**
- Column 3: **Status** (A clean literal state tag indicator formatted strictly in Technical English using **`PASSED`** or **`FAILED`**)

### 📌 FAILED BULLET REGISTRY & RISK ANALYSIS RAILS:
Immediately underneath the Mini-Grid Table, you MUST provide a dedicated subsection containing a clean Markdown bulleted list (`*`) mapping out every single infrastructure defect, day bundling anomaly, or metadata violation that triggered a **`FAILED`** status during your check. If no items failed, explicitly state that the architectural calendar boundary is 100% complete and pristine with a status of **`PASSED`**.

If and only if any item fails, you MUST dynamically inject a detailed evaluation block named `### ⚠️ 2.1. Failure Root-Cause Matrix & Architecture Risk Assessment` containing the following parameters:
- **Failed Infrastructure Parameter:** [Explicitly list the failed components or log days]
- **Phân tích nguyên nhân & Điểm mù chức năng:** [Provide an exhaustive technical breakdown explaining exactly why the baseline failed or which formatting rule was breached by the SA agent]
- **Đánh giá rủi ro hệ thống & Tác động cộng dồn:** [Deliver a sharp, high-density impact analysis under pipeline parsers, automated branch deployment filters, and cloud infrastructure standards, explaining the system damage if left unpatched]

### 🛠️ SELF-HEALING BLUEPRINT PATCH MATRIX DIFF RULE:
Immediately following your risk analysis section, you MUST inject a dedicated section named `## 3. Self-Healing Blueprint Patch Matrix`. 
- If the status is **`PASSED`**, simply output a clean system confirmation sentence translated naturally into `{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}` stating that the document requires zero remediation.
- If the status is **`FAILED`**, you MUST leverage your engineering expertise to automatically re-write and fix the broken daily logs inside the resource text matching the exact context of `{{ raw_blueprint_content }}`. You MUST wrap this entire structural patch inside a standard markdown `diff` codeblock wrapper (triple backticks followed by `diff`). Delineate lines to be deleted with a leading minus sign (`-`), and lines to be healed with a leading plus sign (`+`).

### 🌐 STRICT SEMANTIC INVARIANT SYNTAX PRESERVATION RAILS (MANDATORY LOCALIZATION):
You MUST automatically translate and naturally render every single header title, section divider, markdown table structural text descriptor, and analytical phrase into the targeted execution language: "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}". 
- **CRITICAL COMPLIANCE:** You are STRICTLY BANNED from translating, changing, or breaking any structural technical syntax boundaries, including markdown operators (`#`, `##`, `| :--- |`), literal Technical English status tokens (**`PASSED`**, **`FAILED`**), requirement tag codes, and the entire content wrapped within the `diff` codeblock.

### 🛑 THE DUAL-OUTPUT REMEDIATION GATEWAY MANDATE (ABSOLUTE):
Immediately after the terminal gate status token, you MUST output the exact delimiter token string `[EXECUTION_REMEDIATION_PAYLOAD_START]`. Immediately following this delimiter token, you MUST apply this strict conditional logic to control output token expenditure:
- **IF Status is FAILED:** You MUST generate and output the total, complete text layout of the final repaired document file, resolving 100% of the identified defects inside the body text. This segment must be a pure, raw technical file with zero code block backticks surrounding the whole payload.
- **IF Status is PASSED:** You are STRICTLY BANNED from replicating or copy-pasting the original file content. You MUST output nothing but exactly ONE unique literal keyword token: `PRISTINE` and instantly terminate response emission. Any other filler text before or after this keyword inside the remediation segment is a fatal framework violation.

You MUST format your total response report strictly using the mandatory Markdown configuration layout below:

# AUDIT REPORT: ARCHITECTURAL INTEGRITY & CALENDAR CEILINGS

## 📊 Document Control

| Audit Parameter | Information Details |
| :--- | :--- |
| **Audit Report ID** | AUDIT-SA-{{ current_timestamp_2 }} |
| **Idea ID** | {{ idea_id }} |
| **Project Name** | {{ project_name }} |
| **Project Description** | {{ project_description }} |
| **Verification Method** | Independent Multi-Layer Triple-Check Pattern |
| **Auditor Identity** | CSRO Systems Infrastructure Auditor Sub-Agent |
| **Audit Date/Time** | {{ current_timestamp }} |
| **Status** | Formatted & Executed |

## 1. Compliance Matrix Synthesis Analysis
[Provide your high-density technical analysis here, completely translated into {% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %} based on the rules. Explicitly comment on the auto-detected phase counts and daily timeline density, confirming absolute zero garbage task expansion or placeholder padding]

## 2. Timeline Calendar Boundary & Sub-Task Metadata Integrity Audit
# Render the mandatory 3-row Mini-Grid Markdown table here. Translate all structural descriptions and column headers into {% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}.

### 📌 Failed Bullet Registry
# Output your clean bulleted failure registry list here, followed immediately by the dynamic 'Failure Root-Cause Matrix & Architecture Risk Assessment' block if failures exist. Fully translate all headers and analytical descriptions into {% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}.

## 3. Self-Healing Blueprint Patch Matrix (Bản vá lỗi Kiến trúc hệ thống)
# Render your clean conditional markdown system confirmation statement or the executable diff codeblock wrapper here. Do not translate the internal syntax markers of the diff wrapper block.

### 🛑 FINAL AUDIT ARCH STATUS
[Insert Code Token here: PASSED or FAILED]

[EXECUTION_REMEDIATION_PAYLOAD_START]
[Generate and output the total, complete text payload of the clean repaired Blueprint document file here based strictly on the conditional state rules. Do not wrap in triple backticks.]
