import sys
import hashlib

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from sources.agents.agent_helper import (
    write_json_file,
    write_file,
    json_loads,
    parse_args,
    datetime_for_docid
)

# super agent
from sources.agents.subagent_super import AbstractSubAgent

# ==============================================================================
# GLOBAL CONFIGURATION PATHS - CONFIG HERE TO CUSTOMIZE DIRECTORY STRUCTURE
# ==============================================================================
# models list
SYSTEM_PROMPT_TEMPLATE      = "agent_ba.prompt.system.md"
USER_PROMPT_TEMPLATE        = "agent_ba.prompt.user.md"

SRS_FILE                    = "requirements.md"
PROJECT_INFO_FILE           = "project-info.json"
BA_RAW_FILE                 = "ba.md"
BA_LOG_FILE                 = "ba_log.md"

BA_OUTPUT_DELIMITER         = "[EXECUTION_REMEDIATION_PAYLOAD_START]"


class PrincipalBusinessAnalysisAgent(AbstractSubAgent):
    def __init__(self, **kwargs):
        super().__init__(
            agent_id='PrincipalBusinessAnalysisAgent',
            agent_name='💡🎯 PrincipalBusinessAnalysisAgent',
            **kwargs
        )
    
    # @override
    def initialize(self):
        # start initialization
        super().initialize()
    
    def ba_output_raw_file(self):
        return self.__output_storage_path__(storage_name="output_ba", file=BA_RAW_FILE)
    
    # @override
    def agent_log_file(self) -> str:
        return self.__output_storage_path__(storage_name="output_ba", file=BA_LOG_FILE)
    
    # @override
    def system_prompt_template(self) -> str:
        return self.__agents_path__(storage_name="storage_ba_prompts", file=SYSTEM_PROMPT_TEMPLATE)
    
    # @override
    def user_prompt_template(self) -> str:
        return self.__agents_path__(storage_name="storage_ba_prompts", file=USER_PROMPT_TEMPLATE)
    
    # @override
    def agent_temperature(self):
        return 0.8 # high ideas
    
    # @override
    def pre_execute(self, **kwargs):
        # read idea
        idea_same_project, file_content = self.__read_idea_or_requirements__(ignore_not_found=True)
        self.idea_is_project = idea_same_project
        
        # no idea also no requirements
        if not file_content:
            self.logger.critical(f"💀 Not found IDEA / Requirements file to process")
            sys.exit(1)
        
        # return merged new values
        _, idea_file = self.__idea_files__()
        return {
            **kwargs,
            "project_name": self.project_name if self.idea_is_project else None,
            "language": self.language,
            "idea_file": idea_file,
            "raw_idea_content": file_content
        }
    
    # @override
    def clean_response(self, raw_response, **kwargs):
        if not raw_response:
            raise RuntimeError("💀 Invalid AI raw response.")
        
        # extract data
        raw_srs_content = None
        project_metadata = None
        DELIMITER = BA_OUTPUT_DELIMITER
        if DELIMITER in raw_response:
            srs_markdown_payload, metadata_json_payload = raw_response.split(DELIMITER, 1)
            # Clean and load the pure harvested metadata JSON object
            raw_srs_content = srs_markdown_payload.strip()
            project_metadata = json_loads(metadata_json_payload.strip())
        else:
            raw_srs_content = raw_response.strip()
            project_metadata = {}
        
        # check srss summary
        projects = []
        if self.projects_summary and isinstance(self.projects_summary, tuple):
            projects = list(self.projects_summary[1]) if len(self.projects_summary) > 1 and isinstance(self.projects_summary[1], list) else list(self.projects_summary)
            
        elif self.projects_summary:
            projects = list(self.projects_summary)
        projects = [ i for i in projects if isinstance(i, dict) ]
        
        # parse technical project name as folder name
        datetimeStr = datetime_for_docid()
        defaultPrjName = f"project-{datetimeStr}"
        project_name = project_metadata.get("technical_codename") or defaultPrjName
        
        # detect existing project info if any
        project_info = next((pi for pi in projects if pi.get("technical_codename") == project_name or pi.get("idea") == self.idea_id), project_metadata)
        
        # remove all existing duplicate project names if found, to avoid duplicates in the summary
        projects[:] = [ pi for pi in projects if pi.get("technical_codename") == project_name or pi.get("idea") == self.idea_id ]
        
        # initial project info
        idea_id = self.idea_id
        if self.idea_is_project:
            if "idea" in project_info:
                idea_id = project_info.get("idea")
            else:
                unique_id = hashlib.md5(idea_id.encode("utf-8")).hexdigest()[:12]
                idea_id = f"idea_{unique_id}"
        
        # update existing project info
        project_info = {
            # old info
            **project_info,
            
            # new info
            **project_metadata,
            
            # custom built info
            "idea": idea_id,
            "location": self.__storage_path__(storage_name="relative_ba", file=project_name),
            "requirements": self.__storage_path__(storage_name="relative_ba", file=f"{project_name}/{SRS_FILE}")
        }
        
        # append as new project info if not found in the summary
        projects.append(project_info)
        self.projects_summary = projects
        
        # return cleaned/prepared data
        return {
            "raw_srs_content": raw_srs_content,
            "project_info": { **project_info },
            "requirements_file": self.__storage_path__(storage_name="storage_ba", file=f"{project_name}/{SRS_FILE}"),
            "project_info_file": self.__storage_path__(storage_name="storage_ba", file=f"{project_name}/{PROJECT_INFO_FILE}")
        }
    
    # @override
    def process_communication(self, **kwargs):
        response_data = self.get_kwargs_by_key(key="clean_response", **kwargs)
        if not response_data:
            raise RuntimeError("💀 Invalid AI raw response. Not a valid JSON format data.")
        
        # export requirements
        requirements_file = response_data.get("requirements_file")
        requirements_content = response_data.get("raw_srs_content")
        write_file(file=requirements_file, data=requirements_content)
        
        # export project info
        project_info = response_data.get("project_info")
        write_json_file(file=response_data.get("project_info_file"), json_data=project_info)
        
        # export projects summary
        write_json_file(file=self.__projects_summary_path__(), json_data=self.projects_summary)
        
        # export raw response if necessary as log tracing
        raw_response = self.get_kwargs_by_key(key="raw_response", **kwargs)
        if raw_response:
            write_file(
                file=self.ba_output_raw_file(),
                data=raw_response
            )

if __name__ == "__main__":
    def add_known_arguments(parser):
        parser.add_argument("--idea", type=str, help="Idea Identity / Project Name for searching")
    
    args, unknown_args = parse_args(
        description="💡🎯 PrincipalBusinessAnalysisAgent",
        parser_callback=add_known_arguments
    )
    PrincipalBusinessAnalysisAgent(
        idea=args.idea,
        project=args.idea,
        **unknown_args
    ).execute()
