# CONTEXT
I have a raw, high-level product idea that needs to be engineered into a production-ready specification document. 

# INPUTS
- **Project Codename (Optional)**: {{ project_name }}
- **Raw Idea**: 
---------
{{ raw_idea_content }}
---------
- **Target Language**: {% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}

# INSTRUCTIONS AND STRICT LIMITS
1. Act as our Principal BA / Product Strategist. Review the raw idea provided above.
2. **Project Naming**: Propose 3 tailored project names (Technical Codename, Descriptive Name, and Brand Name) and populate them into the "project_names" keys.
- IF Project Codename is provided (not empty), you MUST use that exact string for the "technical_codename" value without any changes.
- ELSE (if Project Codename is blank or omitted), you are free to creatively generate a unique technical codename based on the raw idea.
3. Fill in all implicit technical gaps, infrastructure needs, and logical holes that were omitted in the raw text.
4. Author a highly detailed, flawless Software Requirements Specification (SRS) based on the 5-section structure defined in your System Prompt.
5. **CRITICAL FOR TRACEABILITY**: Ensure that EVERY SINGLE user story, acceptance criteria group, exception flow, architectural constraint, and non-functional metric inside "srs_content_markdown" is strictly assigned an incremental Tag ID ([REQ-XXX], [ARC-XXX], [EXC-XXX], [NFR-XXX]) as instructed. Double-check that no requirement is left unnumbered.
6. **CRITICAL**: The text inside the "srs_content_markdown" key MUST be written entirely in {% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}.
7. **STRICT ZERO-THINKING POLICY**: Do not include any explanation, introductory words, markdown backticks (```), or conversational filler. Output ONLY the raw JSON block.
