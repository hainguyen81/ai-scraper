Perform a complete traceability matrix validation audit and dynamic requirement repair session for Project '{{ project_name }}'. 

You MUST independently parse, count, and contrast every unique requirement and data tracking tag string present inside these two decoupled assets:
- Inbound Raw Baseline Requirements Asset: {{ raw_idea_content }}
- Inbound Generated BA SRS Context Asset: {{ raw_srs_content }}

Your structural audit loop MUST evaluate the assets through exactly two distinct gate filters:
1. **Trace Omission Audit Gate:** Track down and identify any requirement tag present in the baseline that was dropped or missed by the BA agent.
2. **Ghost Tag Injection Audit Gate:** Track down and identify if the BA agent invented any new functional capabilities, features, or requirement tag codes outside the raw requirements documentation boundary.

### 🧳 INTELLIGENT DOCUMENT REFERENCING RULE:
Inside Section 1 of your report, you are STRICTLY BANNED from printing raw template variable names. Instead, you MUST dynamically scan the contents of the assets to extract their official corporate document ID strings (e.g., `BA-SRS-{{ project_name }}`). If no explicit ID tokens are found inside the assets, you MUST elegantly fallback to utilizing the natural project token string derived from "{{ project_name }}" combined with the active context domain to form a polished, professional enterprise reference string.

### 📊 MINI-GRID REQUIREMENTS TRACEABILITY QUANTITATIVE RULE:
To completely eliminate table format breaking and layout overflow issues caused by large lists of tags, you MUST render a compact, high-density 3-row Markdown Table inside Section 2 to summarize the quantitative counters. The table MUST strictly follow this exact 3-column configuration:
- Column 1: **Audit Metric**
- Column 2: **Quantitative Counter**
- Column 3: **Status** (A clean literal state tag indicator formatted strictly in Technical English using **`PASSED`** or **`FAILED`**)

### 📌 FAILED BULLET REGISTRY & RISK ANALYSIS RAILS:
Immediately underneath the Mini-Grid Table, you MUST provide a dedicated subsection containing a clean Markdown bulleted list (`*`) mapping out every single dynamic requirement or data Tag ID (`[REQ-XXX]`, `[DAT-XXX]`, `[EXC-XXX]`, etc.) that triggered a **`FAILED`** status (omitted, missing, or misaligned) during your trace check. If no tags failed, explicitly state that functional matrix coverage is 100% complete and pristine with a status of **`PASSED`**.

If and only if any tag fails, you MUST dynamically inject a detailed evaluation block named `### ⚠️ 2__DOT__1__DOT__ Failure Root-Cause Matrix & Architecture Risk Assessment` containing the following parameters:
- **Failed Tag Identifier:** [Explicitly list the failed BA Tag IDs]
- **Root-Cause Analysis & Functional Blind Spot:** [Provide an exhaustive technical breakdown explaining exactly why the baseline failed or which functional contract string from the BA specification was dropped or added by the BA agent]
- **Systemic Risk Assessment & Compounding Impact:** [Deliver a sharp, high-density impact analysis under OWASP, security data isolation, and business revenue standards, explaining the system damage if left unpatched]

### 🛠️ SELF-HEALING SRS PATCH MATRIX DIFF RULE:
Immediately following your risk analysis section, you MUST inject a dedicated section named `## 3. Self-Healing SRS Patch Matrix`. 
- If the status is **`PASSED`**, simply output a clean system confirmation sentence translated naturally into `{{ language }}` stating that the document requires zero remediation.
- If the status is **`FAILED`**, you MUST leverage your domain expertise to automatically re-write and fix the broken or missing specification chapters inside the resource text matching the exact context of `{{ raw_srs_content }}`. You MUST wrap this entire structural patch inside a standard markdown `diff` codeblock wrapper (triple backticks followed by `diff`). Delineate lines to be deleted or fixed with a leading minus sign (`-`) which triggers a native red highlight, and lines to be newly inserted or healed with a leading plus sign (`+`) which triggers a native green highlight. Ensure all tracking Tag IDs are accurately embedded inside the fixed lines.

### 🌐 STRICT SEMANTIC INVARIANT SYNTAX PRESERVATION RAILS (MANDATORY LOCALIZATION):
You MUST automatically translate and naturally render every single header title, section divider, markdown table structural text descriptor, and analytical phrase into the targeted execution language: "{{ language }}". 
- **CRITICAL COMPLIANCE:** You are STRICTLY BANNED from translating, changing, or breaking any structural technical syntax boundaries, including markdown operators (`#`, `##`, `| :--- |`), literal Technical English status tokens (**`PASSED`**, **`FAILED`**), requirement tag codes, and the entire content wrapped within the `diff` codeblock.

### 🛑 THE DUAL-OUTPUT REMEDIATION GATEWAY MANDATE (ABSOLUTE):
Immediately after the terminal gate status token, you MUST output the exact delimiter token string `[EXECUTION_REMEDIATION_PAYLOAD_START]`. Immediately following this delimiter token, you MUST apply this strict conditional logic to control output token expenditure:
- **IF Status is FAILED:** You MUST generate and output the total, complete text layout of the final repaired document file, resolving 100% of the identified defects inside the body text. This segment must be a pure, raw technical file with zero code block backticks surrounding the whole payload.
- **IF Status is PASSED:** You are STRICTLY BANNED from replicating or copy-pasting the original file content. You MUST output nothing but exactly ONE unique literal keyword token: `PRISTINE` and instantly terminate response emission. Any other filler text before or after this keyword inside the remediation segment is a fatal framework violation.

You MUST format your total response report strictly using the mandatory Markdown configuration layout below:

# AUDIT REPORT: BUSINESS REQUIREMENTS ACCURACY

## 📊 Document Control

| Audit Parameter | Information Details |
| :--- | :--- |
| **Audit Report ID** | AUDIT-BA-{{ current_timestamp_2 }} |
| **Idea ID** | {{ idea_id }} |
| **Project Name** | {{ project_name }} |
| **Project Description** | {{ project_description }} |
| **Verification Method** | Independent Requirements Matrix Coverage Check |
| **Auditor Identity** | CSRO Business Analyst Auditor Sub-Agent |
| **Audit Date__SLASH__Time** | {{ current_timestamp }} |
| **Status** | Formatted & Executed |

## 1. Compliance Matrix Synthesis Analysis
[Provide your high-density technical analysis here, completely translated into {{ language }} based on the rules. Explicitly declare if the system triggers a PASSED or FAILED state]

## 2. Quantitative Trace Audit Counters
# Render the mandatory 3-row Mini-Grid Markdown table here. Translate all structural descriptions and column headers into {{ language }}.

### 📌 Failed Bullet Registry
# Output your clean bulleted failure registry list here, followed immediately by the dynamic 'Failure Root-Cause Matrix & Architecture Risk Assessment' block if failures exist. Fully translate all headers and analytical descriptions into {{ language }}.

## 3. Self-Healing SRS Patch Matrix
# Render your clean conditional markdown system confirmation statement or the executable diff codeblock wrapper here. Do not translate the internal syntax markers of the diff wrapper block.

### 🛑 FINAL AUDIT REQ STATUS
[Insert Code Token here: PASSED or FAILED]

[EXECUTION_REMEDIATION_PAYLOAD_START]
[Generate and output the total, complete text payload of the clean repaired SRS document file here based strictly on the conditional state rules. Do not wrap in triple backticks.]
