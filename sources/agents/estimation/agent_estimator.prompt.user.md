Perform a complete project estimation and risk registry for the project based on these documents. The entire report MUST be outputted in **{{ target_language }}**:

### 💡 [Asset 1: Core Product Idea]
{{ raw_idea_content }}

### 📄 [Asset 2: Software Requirement Specification (SRS)]
{{ raw_srs_content }}

### 📐 [Asset 3: System Architecture Blueprint]
{{ raw_blueprint_content }}

### 📊 [Asset 4: Costing Controls & Benchmarks]
- **Buffer Ratio Multiplier**: {{ buffer_ratio }} (e.g., 0.25 means adding a 25% safety margin to the max bounds)
- **AI Tooling & API Token Cost Allocation**: $350 USD per calendar month for Enterprise / $100 USD for Freelance
- **Target Language**: {{ target_language }}

---

### 🛑 TRIPLE-CHECK MATHEMATICAL DIRECTIVES:
You MUST execute your internal reasoning through 3 independent calculation passes:
1. **Pass 1 (Live Sourcing & Sizing)**: Call web search to fetch (1) Live USD to VND rate, (2) Current average monthly cost for Enterprise Software Engineer, and (3) Current average monthly cost for Senior Freelance Developer. Then calculate raw Man-Months required for each engineering role.
2. **Pass 2 (Four-Scenario Financial Budgeting)**: Compute absolute cost ranges `[Min - Max | Safe]` for exactly 4 unique execution scenarios (Enterprise Traditional, Enterprise AI-Augmented, Freelance Traditional, Freelance AI-Augmented).
3. **Pass 3 (Cross-Currency Verification)**: Convert all calculated USD figures into VND using your live exchange rate. Cross-check that VND Value / USD Value = Exchange Rate exactly to eliminate calculation drift.

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
| **Discovered Enterprise Cost / Man-Month** | $[Insert Rate] USD / Month |
| **Discovered Freelancer Cost / Man-Month** | $[Insert Rate] USD / Month |
| **Rate & Cost Extraction Date/Time** | [Insert Date/Time of Your Online Search] |
| **Data Provenance Sources** | [Insert Website Names/URLs for Live Data Mapping] |
| **Verification Method** | Independent Multi-Layer Triple-Check |
| **Status** | Audited & Validated |

#### 👥 SECTION 2: RESOURCE CAPACITY PLANNING (MAN-MONTHS)
Provide a granular breakdown of required engineering roles (Backend, Frontend, QA, DevOps).

#### 💰 SECTION 3: FINANCIAL BUDGET & TIMELINE ESTIMATION PROJECTIONS
##### 1. Corporate Enterprise Model (Mô hình Doanh nghiệp tập đoàn)
- Traditional Human-Only Total Budget: `$[Min - Max \| Safe]` USD / `[Min - Max \| Safe]` VND
- AI-Augmented Total Budget: `$[Min - Max \| Safe]` USD / `[Min - Max \| Safe]` VND

##### 2. Freelancer Team Model (Mô hình Nhóm Freelancer tự do)
- Traditional Human-Only Total Budget: `$[Min - Max \| Safe]` USD / `[Min - Max \| Safe]` VND
- AI-Augmented Total Budget: `$[Min - Max \| Safe]` USD / `[Min - Max \| Safe]` VND

##### 3. Project Duration Comparison (Calendar Months)

#### 🛡️ 🔥 SECTION 4: ARCHITECTURAL COST JUSTIFICATION (GIẢI TRÌNH BIÊN ĐỘ CHI PHÍ)
*CRITICAL MANDATE*: You MUST deliver a deep, comprehensive architectural and financial analysis explaining the massive cost variance between the Corporate Enterprise Model and the Freelancer Team Model. You MUST explicitly justify why Enterprise costing is significantly higher by breaking down the following structural pillars based on the SA Blueprint:
1. **Operational & Management Overhead**: Contrast corporate taxes, insurance, QA/QC infrastructure, Project Management layers, and premium software tooling licenses against zero-overhead freelance execution.
2. **Security Hardening Boundaries**: Explain the cost impact of implementing enterprise-grade features found in the blueprint (e.g., mTLS service-to-service communication, Envoy API Gateway with custom WAF rules, Argon2id hashing overhead, and SHA-256 hash-chained immutable logging).
3. **High Availability & Disaster Recovery (HA/DR) Infrastructure**: Justify the budget needed to achieve strict enterprise SLAs (RTO ≤ 30 mins, RPO ≤ 5 mins) using multi-region Google Kubernetes Engine (GKE) deployments and clustered/mirrored RabbitMQ topologies compared to a standard, single-instance freelance VPS deployment.
4. **Data Isolation Strategy (Multi-Tenancy)**: Explain how a physical isolation architecture (`Database-per-tenant` using encrypted dynamic routing strings) demands intensive engineering effort and operational cost compared to standard, cheap logical multi-tenancy.

#### 🚨 SECTION 5: PROJECT RISK REGISTRY & MITIGATION STRATEGY
- **Risk ID \| Description \| Severity (High/Med/Low) \| Concrete Mitigation Strategy**

#### 📊 SECTION 6: ARCHITECTURAL DATA VISUALIZATION (NATIVE MERMAID CHARTS)
- **Chart A**: Financial Cost Boundary Matrix (`xychart-beta` or `bar` code comparing all 4 scenarios).
- **Chart B**: Project Delivery Timeline (`gantt` comparing Enterprise vs Freelance schedules).
- **Chart C**: Risk Assessment Severity Matrix (`quadrantChart`).

#### 📊 SECTION 7: VISUALIZATION METADATA FOR BACKEND PROCESSING
*CRITICAL*: Update the JSON layout to include both Corporate and Freelancer metrics for precise automated image chart generation.
{% set open_json = '{' %}
{% set close_json = '}' %}
```json
{{ open_json }}
  "exchange_rate": [Insert raw float rate you found online],
  "enterprise_cost_usd": [[Min_USD], [Max_USD], [Safe_USD]],
  "freelance_cost_usd": [[Min_USD], [Max_USD], [Safe_USD]],
  "enterprise_months": [[Min_Months], [Max_Months], [Safe_Months]],
  "freelance_months": [[Min_Months], [Max_Months], [Safe_Months]]
{{ close_json }}
```
