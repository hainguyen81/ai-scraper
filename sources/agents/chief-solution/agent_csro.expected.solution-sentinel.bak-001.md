The complete technical audit report.

# MANDATORY CRITICAL FORMAT RULES:
1. Your output MUST start exactly with the top-level header: '# TECHNICAL AUDIT REPORT: {{ project_name }}'.
2. It MUST follow immediately with a '## 📊 Document Information' (or '## 📊 Document Control' or '## 📊 Document Revision') section. You must render every metadata key and resolve every variable defined in the system instructions (including Report ID, Idea ID, Project Name, Project Description, Version, and Date/Time). Do not skip any requested fields, but you are allowed to include extra enterprise fields.
3. It must strictly output the Executive Summary containing the Overall Status label formatted exactly as '❌ AUDIT STATUS: FAILED - REVISION MANDATORY' or '✅ AUDIT STATUS: PASSED', followed by the Chain-of-Thought logs, and detailed loopholes mapping specific [Gap-ID] flaws. Raw Markdown output only.
