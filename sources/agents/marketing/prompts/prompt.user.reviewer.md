# 📥 SYSTEM DATA INPUT CHANNEL
- **Target Project Identity Name**: "{{ project_name }}"
- **Document Control Tracking ID**: "MKT-{{ doc_id }}"
- **System Generation Timestamp**: "{{ current_timestamp }}"
- **Raw Marketing Planner Source Reference**:
```text
{{ raw_planner_content }}
```
- **Draft Creative Assets Generated for Audit**:
```json
{{ raw_assets_content }}
```
- **Corporate Compliance Rules & Guidelines**:
```text
{{ raw_compliance_content }}
```

# ⚡ EXECUTION INSTRUCTION
Ingest the draft creative assets payload and execute a multi-layer deep self-auditing pipeline against the original Corporate Compliance Guidelines and the Raw Marketing Planner Source Reference.

You MUST completely fulfill the mandatory dual-zone layout specified in the system prompt rules:
1. Construct **ZONE 1: THE C-SUITE GOVERNANCE REPORT** by formatting the audit evaluation summary, document control governance matrix, and the explicit Markdown Diff blocks showing the strict changes required. Fully execute the translation process on human-readable elements to match the requested target language variable context.
2. Construct **ZONE 2: THE RESPONDER KNOWLEDGE PAYLOAD** immediately after Zone 1, keeping it strictly as a raw, valid, un-translated JSON object matching the Technical English schema configuration.

🚨 **RIGID MOUNTING DIRECTIVE**: You MUST precisely inject the hidden HTML comment delimiters (`<!--START_GOVERNANCE_REPORT-->`, `<!--END_GOVERNANCE_REPORT-->`, `<!--START_RESPONDER_PAYLOAD-->`, and `<!--END_RESPONDER_PAYLOAD-->`) exactly on their own individual lines enclosing their respective data zones. Do not merge or output any conversational text outside these boundaries.

Output the complete multi-zone professional document now.
