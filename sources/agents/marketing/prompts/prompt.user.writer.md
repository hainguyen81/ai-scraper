# 📥 SYSTEM DATA INPUT CHANNEL
- **Target Project Identity Name**: "{{ project_name }}"
- **Target Project Description**: "{{ project_description }}"
- **Document Control Tracking ID**: "COPY-{{ doc_id }}"
- **System Generation Timestamp**: "{{ current_timestamp }}"
- **Approved Marketing Planner Source Reference**:
```text
{{ raw_planner_content }}
```
- **Target Platform Boundary**: "{{ platform_target }}"
- **Specific Campaign Target Interval**: "{{ target_interval }}"

# ⚡ EXECUTION INSTRUCTION
Locate the specific target interval row inside the Editorial Calendar of the Approved Marketing Planner Source Reference. Extract the designated campaign focus and topic specifications.

You MUST fully expand both **ZONE 1: THE C-SUITE GOVERNANCE REPORT** (Markdown presentation style) and **ZONE 2: THE RESPONDER KNOWLEDGE PAYLOAD** (JSON schema style) in a single execution stream. Maintain absolute structural detail. Ensure 100% data synchronization between the visual text article in Zone 1 and the string value of the JSON object payload in Zone 2. 

🚨 **RIGID MOUNTING DIRECTIVE**: You MUST precisely inject the hidden HTML comment delimiters (`<!--START_GOVERNANCE_REPORT-->`, `<!--END_GOVERNANCE_REPORT-->`, `<!--START_RESPONDER_PAYLOAD-->`, and `<!--END_RESPONDER_PAYLOAD-->`) exactly on their own individual lines enclosing their respective data zones. Do not merge or output any conversational text outside these boundaries.

Output the complete multi-zone copywriting document now.
