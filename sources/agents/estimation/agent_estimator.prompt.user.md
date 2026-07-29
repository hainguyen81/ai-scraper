Perform a complete project estimation and risk registry for the project based on these documents. The entire report MUST be outputted in **{{ target_language }}**:

### 💡 [Asset 1: Core Product Idea]
{{ raw_idea_content }}

### 📄 [Asset 2: Software Requirement Specification (SRS)]
{{ raw_srs_content }}

### 📐 [Asset 3: System Architecture Blueprint]
{{ raw_blueprint_content }}

### 📊 [Asset 4: Costing Controls]
- **Buffer Ratio Multiplier**: {{ buffer_ratio }} (e.g., 0.25 means adding a 25% safety margin to the max bounds)
- **AI Tooling & API Token Cost Allocation**: $350 USD per calendar month
- **Target Language**: {{ target_language }}

---
### 🛑 TRIPLE-CHECK MATHEMATICAL DIRECTIVES:
You MUST execute your internal reasoning through 3 independent calculation passes:
1. **Pass 1 (Live Sourcing & Base Sizing)**: Call web search to find (1) Live USD to VND rate, and (2) Current average monthly cost per software engineer. Then calculate the raw Man-Months required for each standard role (Backend, Frontend, QA, DevOps) based on granularity analysis. Split into Traditional Human-Only and AI-Augmented paradigms.
2. **Pass 2 (Buffer & Financial Boundary Math)**: Compute the absolute development cost ranges using your dynamically discovered human cost per man-month benchmark.
   - Calculate the Buffer Margin: Base Cost * Buffer Ratio Multiplier.
   - Calculate the Safe Cost: Max Cost + Buffer Margin.
3. **Pass 3 (Cross-Currency Verification)**: Convert all calculated USD figures (Min, Max, Safe) into VND using your live fetched exchange rate. Cross-check that VND Value / USD Value = Exchange Rate exactly to eliminate any calculation drift.

---
### 📋 MANDATORY OUTPUT STRUCTURE (MARKDOWN REPORT):
Your response MUST start directly with the main title header and follow this layout strictly in **{{ target_language }}**:

#### 📊 0. DOCUMENT INFORMATION / THÔNG TIN TÀI LIỆU

| Item / Thành phần | Details / Chi tiết |
| :--- | :--- |
| **Report ID** | AUDIT-{{ current_timestamp_2 }} |
| **Idea ID** | {{ idea_id }} |
| **Project Name** | {{ project_name }} |
| **Project Description** | {{ project_description }} |
| **Version** | 1.0 (Automated Governance) |
| **Date/Time** | {{ current_timestamp }} |
| **Author** | Chief Solution Review Officer (CSRO Agent) |
| **Approval** | Certified by Enterprise Technical Governance Board |

#### 📑 SECTION 1: DOCUMENT CONTROL & PROVENANCE METADATA
You MUST extract the data from your live search and inject it precisely into this table:

| Audit Parameter | Information Details |
| :--- | :--- |
| **Live Exchange Rate Applied** | 1 USD = [Insert The Exact Rate You Found] VND |
| **Discovered Human Cost / Man-Month** | $[Insert Rate You Found] USD / Month |
| **Rate & Cost Extraction Date/Time** | [Insert Date/Time of Your Online Search] |
| **Data Provenance Sources** | [Insert Website Names/URLs for Both Rate and Salary Information] |
| **Verification Method** | Independent Multi-Layer Triple-Check |
| **Status** | Audited & Validated |

#### 👥 SECTION 2: RESOURCE CAPACITY PLANNING (MAN-MONTHS)
Provide a granular breakdown of required engineering roles.
- Traditional Human-Only: `[Min - Max \| Safe]` Man-Months.
- AI-Augmented: `[Min - Max \| Safe]` Man-Months.

#### 💰 SECTION 3: FINANCIAL BUDGET PROJECTIONS (DUAL-CURRENCY MAPPING)
- **Traditional Human-Only Total Budget**:
  - **USD**: `$[Min - Max \| Safe]` USD
  - **VND**: `[Min - Max \| Safe]` VND
- **AI-Augmented Total Budget**:
  - **USD**: `$[Min - Max \| Safe]` USD
  - **VND**: `[Min - Max \| Safe]` VND

#### 🚨 SECTION 4: PROJECT RISK REGISTRY & MITIGATION STRATEGY
- **Risk ID \| Description \| Severity (High/Med/Low) \| Concrete Mitigation Strategy**

#### 📊 SECTION 5: ARCHITECTURAL DATA VISUALIZATION (NATIVE MERMAID CHARTS)
You MUST generate valid **Mermaid.js** code blocks here (Keep Mermaid code labels/syntax in English, but you can translate titles).
- Chart A: Financial Cost Boundary Matrix (`xychart-beta`)
- Chart B: Project Delivery Timeline (`gantt`)
- Chart C: Risk Assessment Severity Matrix (`quadrantChart`)

#### 📊 SECTION 6: VISUALIZATION METADATA FOR BACKEND PROCESSING
*CRITICAL*: Keep this JSON block strictly in this raw format for Python parsing, using the raw USD float numbers you independently calculated.
{% set open_json = '{' %}
{% set close_json = '}' %}
```json
{{ open_json }}
  "exchange_rate": [Insert raw float rate you found online],
  "human_cost_usd": [[Min_USD], [Max_USD], [Safe_USD]],
  "ai_cost_usd": [[Min_USD], [Max_USD], [Safe_USD]],
  "human_months": [[Min_Months], [Max_Months], [Safe_Months]],
  "ai_months": [[Min_Months], [Max_Months], [Safe_Months]]
{{ close_json }}
```
