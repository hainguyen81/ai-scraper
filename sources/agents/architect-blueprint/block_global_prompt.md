Analyze the attached project requirements. Build the GLOBAL PROJECT CONTEXT for Project '{{ project_name }}'.

--- RAW REQUIREMENTS ---
{{ project_requirements }}
--- END REQUIREMENTS ---

# CRITICAL ENTERPRISE STRUCTURAL CONSTRAINTS (ABSOLUTE HARD LIMIT):
## 1. EXACT PHASE COUNT MANDATE: You MUST segment the entire project architecture and development plan into EXACTLY {{ num_phases }} sequential phases. 
## 2. NO MORE, NO LESS: Generating fewer than {{ num_phases }} phases or exceeding {{ num_phases }} phases is a critical engine failure. Under no circumstances are you allowed to create a Phase {{ num_phases + 1 }}.
## 3. SCOPE COMPRESSION: If the project requirements are small, you MUST distribute and stretch the tasks to fit exactly {{ num_phases }} phases. If the requirements are massive, you MUST compress, aggregate, and streamline the architectural components so they fit strictly within the {{ num_phases }} phases boundary.
## 4. CHRONOLOGICAL PACKING: Every single requirement item specified in the documentation must be fully covered and packed cleanly across these {{ num_phases }} phases. Do not leave any loose ends or plan for post-phase execution.
	
# CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
## 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to {{ max_days_per_phase }} days maximum (Absolute Hard Limit: Maximum {{ max_days_per_phase }} days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day {{ max_days_per_phase }}.
## 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

Your output MUST follow this exact structure:
# GLOBAL PROJECT CONTEXT: {{ project_name }}
## 1. Executive Summary & Tech Stack Blueprint
## 2. Global Guardrails & Enterprise Compliance Standards
## 3. Standardized Sub-Agent Persona Definitions (Manager, Coder, Tester, Reviewer, DevOps)
## 4. Multi-Phase Segmentation Strategy Overview (Plan exactly {{ num_phases }} phases)