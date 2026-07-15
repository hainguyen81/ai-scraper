# ==============================================================================
# 🛠️ ENTERPRISE PIPELINE ENVIRONMENT-BASED PATH RESOLVER
# ==============================================================================
# Programmatically retrieves the absolute root directory of the active project 
# using GitHub Actions infrastructure environment tokens instead of brittle backtracking.
# ==============================================================================

import os
import ast

def resolve_absolute_path(relative_target_path):
    """
    Ingests a relative path string and safely interpolates it using the absolute 
    workspace anchor provided natively by the GitHub Actions Runner environment.
    """
    # 🚀 CORE RAIL: Ingest the absolute repository root path straight from GitHub infrastructure
    # Fallback to current working directory (os.getcwd()) if executing on a local machine
    current_directory_path = os.getcwd()
    github_workspace = os.environ.get("GITHUB_WORKSPACE", '')
    project_workspace = os.environ.get("PROJECT_WORKSPACE", '')
    print(f"CURRENT WORKING DIR: { current_directory_path } | GITHUB_WORKSPACE: { github_workspace } | PROJECT_WORKSPACE: { project_workspace }")
    repo_root_path = os.environ.get("PROJECT_WORKSPACE", os.environ.get("GITHUB_WORKSPACE", os.getcwd()))
    
    # Clean up the incoming string parameters by removing leading path descriptors
    cleaned_relative_path = relative_target_path.removeprefix("./")
    
    # Synthesize the non-negotiable absolute hardware computing path destinations
    absolute_hardware_path = os.path.join(repo_root_path, cleaned_relative_path)
    
    # full path from root workspace
    return absolute_hardware_path

def json_raw_content(raw_content):
    """Securely serialize input telemetry payloads and generate standard markdown log contents."""
    
    # ✅ STEP 1: Process inputs if they arrive as live Python Dictionary or List types directly
    if isinstance(raw_content, (dict, list)):
        try:
            # Convert dictionary objects to a strict double-quoted JSON string with indentation rules
            return json.dumps(raw_content, indent=4, ensure_ascii=False)
        except Exception:
            return str(raw_content)
    
    # ✅ STEP 2: Handle string inputs that might be single-quoted representation strings or flat JSON blocks
    if isinstance(raw_content, str):
        cleaned_str = raw_content.strip()
        
        # Hotfix for Python object representation strings containing single quotes instead of valid JSON double quotes
        if cleaned_str.startswith("{") and "'" in cleaned_str:
            try:
                # Replace structural single quotes with standardized JSON compliant double quotes safely using literal evaluation
                import ast
                evaluated_object = ast.literal_eval(cleaned_str)
                return json.dumps(evaluated_object, indent=4, ensure_ascii=False)
            except Exception:
                pass
        
        # Handle standard double-quoted minified JSON strings safely
        if cleaned_str.startswith("{") or cleaned_str.startswith("["):
            try:
                parsed_object = json.loads(cleaned_str)
                return json.dumps(parsed_object, indent=4, ensure_ascii=False)
            except Exception:
                pass
        
        return cleaned_str
    
    if raw_content is None:
        return "None"
    
    return str(raw_content)
