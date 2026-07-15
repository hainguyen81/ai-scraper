import os
import argparse
from google import genai
from google.genai import types

# ==============================================================================
# 🏢 ENTERPRISE INTER-PACKAGE ROUTING LAYER
# ==============================================================================
# Programmatically appends the parent directory (.ai/.agents/) into Python's runtime
# search path array. This completely unlocks importing 'agent_helper.py'.
# ==============================================================================
CURRENT_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) # .ai/.agents/.sub-agents/
PARENT_AGENTS_DIR  = os.path.abspath(os.path.join(CURRENT_SCRIPT_DIR, "../")) # .ai/.agents/

# jump to `agent_helper.py` folder path
if PARENT_AGENTS_DIR not in sys.path:
    sys.path.insert(0, PARENT_AGENTS_DIR)

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from agent_helper import resolve_absolute_path

def run_architect_agent(requirements_path: str, num_phases: int, output_dir: str):
    """
    Lead Architect Agent: Parses raw requirements, establishes strict system rules 
    and guardrails for all sub-agents, and generates a structured multi-phase execution plan.
    """
    # Initialize the Gemini client. It automatically picks up the GEMINI_API_KEY environment variable.
    client = genai.Client()
    
    # Verify the existence of the source requirements file before proceeding.
    absolute_requirements_path = resolve_absolute_path(requirements_path)
    if not os.path.exists(absolute_requirements_path):
        print(f"❌ Target requirements file not found at: {requirements_path}")
        return
        
    # Read the entire raw text containing the project requirements and specifications.
    with open(absolute_requirements_path, "r", encoding="utf-8") as f:
        project_requirements = f.read()

    print(f"📖 Loaded requirements file ({len(project_requirements)} characters)...")
    print(f"🏗️ Initializing system architecture breakdown into {num_phases} distinct phases...")

    # Define the core identity, mission, and absolute compliance rules for the Architect Agent.
    # This instructs the model to act as an unshakeable master coordinator that enforces strict discipline.
    architect_instruction = """
    You are the Lead AI System Architect. Your job is to parse raw project requirements and generate an unshakeable, strict, and highly technical coordination framework for a multi-agent team.
    
    You must output two components:
    1. GLOBAL CONTEXT & SUB-AGENT SYSTEM PROMPTS: Define the system truth, tech stack, and exact rules/constraints that Sub-Agents MUST follow.
    2. PHASE CONTEXT PLAN: Breakdown the development into sequential phases with strict inputs, outputs, and DoD per phase.
    
    You must enforce extreme discipline:
    - Coder cannot write code without Reviewer approval.
    - Tester must fail the build if coverage is below 90%.
    - DevOps cannot deploy unless Docker build passes perfectly.
    - Output must be purely in Markdown format, highly scannable, and extremely clear.
    """

    # Construct the final execution prompt. This enforces a standardized Markdown output structure
    # and explicitly commands the model to generate custom System Prompts for each sub-agent role.
    prompt = f"""
    Analyze the following project requirements and build the Global Context and a {num_phases}-Phase Context Plan.
    
    --- RAW REQUIREMENTS ---
    {project_requirements}
    --- END REQUIREMENTS ---
    
    Your output MUST follow this exact structure:
    
    # PART 1: GLOBAL CONTEXT & SUB-AGENT CONSTRAINTS
    
    ## 1. Project Overview & Tech Stack
    (Define exact technologies, architecture, database schemas, and integration points based on requirements).
    
    ## 2. Hard Constraints & Guardrails for Sub-Agents
    - **General Rule**: No sub-agent is allowed to deviate from the Tech Stack or add unrequested features.
    - **Strict Coder Rules**: Must write clean code, handle all edge cases, and use strict TypeScript/Python typing. Cannot push code directly without peer review.
    - **Strict Reviewer Rules**: Reject code with security flaws, missing logs, or poor error handling.
    - **Strict Tester Rules**: Must enforce 90%+ test coverage. Write integration tests for all API endpoints.
    - **Strict DevOps Rules**: Docker multi-stage builds only. GKE deployment manifests must include resource limits (CPU/Memory).
    
    ## 3. Dedicated System Prompts for Sub-Agents
    (Generate the exact System Prompt text that will be injected into each sub-agent):
    - **Prompt for [Coder Agent]**
    - **Prompt for [Reviewer Agent]**
    - **Prompt for [Tester Agent]**
    - **Prompt for [Technical Document Writer Agent]**
    - **Prompt for [Docker Build Agent]**
    - **Prompt for [GCP/GKE Deployment Agent]**
    
    # PART 2: {num_phases}-PHASE CONTEXT PLAN
    (Break down the development into exactly {num_phases} chronological phases. Each phase acts as an isolated context window for execution).
    
    For each phase (from Phase 1 to Phase {num_phases}), specify:
    - **Phase Objective**: What value does this phase deliver?
    - **Allowed Tech Scope**: Exactly which components/folders can be touched.
    - **Sub-Agent Execution Checklist**: Specific commands/tasks for Coder, Tester, Reviewer, Docker, and GCP agents *only* for this phase.
    - **Definition of Done (DoD)**: Strict metrics required to unlock the next phase.
    """

    try:
        # Call the Google GenAI API using 'gemini-2.5-pro' for heavy architectural reasoning tasks.
        # Temperature is set to 0.2 to prioritize deterministic, logical, and highly strict outputs over creativity.
        response = client.models.generate_content(
            model='gemini-2.5-pro',
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=architect_instruction,
                temperature=0.2,
            )
        )
        
        # Ensure the target output directory exists before writing files.
        absolute_out_dir = resolve_absolute_path(output_dir)
        os.makedirs(absolute_out_dir, exist_ok=True)
        full_output_path = os.path.join(absolute_out_dir, "architect_blueprint.md")
        
        # Save the completely generated strict blueprint layout into a single comprehensive Markdown file.
        with open(full_output_path, "w", encoding="utf-8") as f:
            f.write(response.text)
            
        print(f"🎯 Success! The master architectural blueprint has been saved to: {full_output_path}")
        print("💡 You can now inject the generated sections directly into your sub-agents.")

    except Exception as e:
        # Catch and report any API-related failures, network losses, or structural errors.
        print(f"❌ Google GenAI API Execution Failed: {e}")

if __name__ == "__main__":
    # Configure CLI arguments parsing to allow dynamic inputs for requirements path, phase count, and output location.
    parser = argparse.ArgumentParser(description="AI Lead Architect Agent Configuration")
    parser.add_argument("--req", type=str, default="requirements.txt", help="Path to the raw project requirements file")
    parser.add_argument("--phases", type=int, default=3, help="Total number of execution phases to segment")
    parser.add_argument("--out", type=str, default="./blueprint", help="Target output directory for the generated blueprint")
    
    args = parser.parse_args()
    
    # Trigger the primary agent orchestration function.
    run_architect_agent(args.req, args.phases, args.out)
