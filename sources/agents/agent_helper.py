# ==============================================================================
# 🛠️ ENTERPRISE PIPELINE ENVIRONMENT-BASED PATH RESOLVER
# ==============================================================================
# Programmatically retrieves the absolute root directory of the active project 
# using GitHub Actions infrastructure environment tokens instead of brittle backtracking.
# ==============================================================================

import os

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
    
    # ✅ STEP 1: If input is already a string, attempt to safely parse it into a dict/list first
    if isinstance(raw_content, str):
        cleaned_str = raw_content.strip()
        # Verify if the string pattern looks like a potential JSON structure
        if cleaned_str.startswith("{") or cleaned_str.startswith("["):
            try:
                raw_content = json.loads(cleaned_str)
            except Exception:
                # Fallback silently if it is a standard plain text instead of JSON string
                pass
    
    # ✅ STEP 2: Once object identity is recovered, execute absolute beautification constraints
    if isinstance(raw_content, (dict, list)):
        try:
            # Convert the target data layout into a beautiful formatted JSON string with 4-space indent lines
            raw_content = json.dumps(raw_content, indent=4, ensure_ascii=False)
        except Exception as serialize_err:
            # Emergency fallback to prevent total execution runtime pipeline crashes
            raw_content = str(raw_content)
    
    elif raw_content is None:
        raw_content = "None"
    
    else:
        # Enforce character string datatype constraints for any other variable types
        raw_content = str(raw_content)
    
    return raw_content
