import os
import sys
import json
import re
import hashlib
import argparse
from datetime import datetime
from openai import OpenAI

# for abstract class
from abc import ABC, abstractmethod

# internal agent CrewAI
from crewai import Agent, Crew, Process, Task, LLM

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from sources.agents.agent_helper import (
    resolve_absolute_path,
    read_json_file,
    read_file_raw,
    write_json_file,
    write_file,
    kwargs_by_key,
    render_kwargs_prompt
)

# super agent
from sources.agents.agent_super import AbstractAgent

# ==============================================================================
# GLOBAL CONFIGURATION PATHS - CONFIG HERE TO CUSTOMIZE DIRECTORY STRUCTURE
# ==============================================================================
PROMPT_TEMPLATE_SOLUTION_SENTINEL   = resolve_absolute_path("sources/agents/chief-solution/agent_csro.prompt.solution-sentinel.md")
PROMPT_TEMPLATE_BA                  = resolve_absolute_path("sources/agents/chief-solution/agent_csro.prompt.ba.md")
PROMPT_TEMPLATE_SA                  = resolve_absolute_path("sources/agents/chief-solution/agent_csro.prompt.sa.md")
# `MANDATORY OUTPUT FORMAT` is a section in PROMPT
EXPECTED_OUTPUT_SOLUTION_SENTINEL   = "The complete technical audit report formatted exactly as specified in the MANDATORY OUTPUT FORMAT section above."
EXPECTED_OUTPUT_BA                  = "A newly minted, flawless Enterprise SRS document syncing perfectly with the original Idea."
EXPECTED_OUTPUT_SA                  = "The complete technical audit report formatted exactly as specified in the MANDATORY OUTPUT FORMAT section above."
STORAGE_PATH                        = resolve_absolute_path("sources/storage")
IDEAS_STORAGE_PATH                  = os.path.join(STORAGE_PATH, "ideas")
BA_STORAGE_PATH                     = os.path.join(STORAGE_PATH, "business-analysis")
CSRO_STORAGE_PATH                   = os.path.join(STORAGE_PATH, "chief-solution")
BA_SUMMARY_FILE                     = resolve_absolute_path(os.path.join(BA_STORAGE_PATH, "projects-summary.json"))
BLUEPRINT_STORAGE_PATH              = os.path.join(STORAGE_PATH, "blueprint")
CSRO_OUTPUT_PATH                    = resolve_absolute_path("sources/output/chief-solution")
CSRO_RAW_FILE                       = os.path.join(CSRO_OUTPUT_PATH, "chief-solution-review.md")
CSRO_LOG_FILE                       = os.path.join(CSRO_OUTPUT_PATH, "chief-solution-review_log.md")


# =====================================================================
# 🕵️‍♂️ SUPER: THE SUPREME AGENT (ENTERPRISE SOLUTION SUPER AGENT)
# =====================================================================
class AbstractCrewEnterpriseSuperAgent(AbstractAgent):
    """
    A Class-based Agent representing the Supreme Gatekeeper.
    It scans Idea, SRS, and Blueprint files for gaps, loopholes, and enterprise compliance.
    """
    def __init__(self, agent_id, **kwargs):
        super().__init__(agent_id=agent_id, **kwargs)
    
    def project_name(self):
        return self.project_info.get("technical_codename") if self.project_info else None
    
    def file_idea(self):
        return os.path.join(IDEAS_STORAGE_PATH, f"{self.idea_id}.md")
    
    def file_ba(self):
        return self.project_info.get("requirements") if self.project_info else None
    
    def file_blueprint(self):
        project_name = self.project_name()
        return os.path.join(BLUEPRINT_STORAGE_PATH, project_name, "context", f"{project_name}.global.blueprint.md") if project_name else None
    
    def load_project_info(self, **kwargs):
        idea_id = kwargs_by_key(key="idea", **kwargs)
        _, projects = read_json_file(BA_SUMMARY_FILE)
        if not projects:
            print(f"[ 💀 {self.agent_id} Agent | CRITICAL ERROR ] (2) Not found project information by idea { idea_id }")
            sys.exit(1)
        
        # find project information
        project_info = next((pi for pi in projects if isinstance(pi, dict) and idea_id in [ pi.get("technical_codename"), pi.get("idea"), pi.get("brand_name") ]), None)
        if not projects:
            print(f"[ 💀 {self.agent_id} Agent | CRITICAL ERROR ] (3) Not found project information by idea { idea_id }")
            sys.exit(1)
        
        # return project information
        return project_info
    
    def __pre_initialize__(self):
        # require idea identity to analyze
        self.idea_id = self.get_kwargs("idea") or self.get_kwargs("idea_id")
        if not self.idea_id:
            print(f"[ 💀 {self.agent_id} Agent | CRITICAL ERROR ] (1) Invalid idea identity to analyze!")
            sys.exit(1)
        
        # load project_info by idea
        self.project_info = self.load_project_info(**{ "idea": self.idea_id })
        
        # check idea file
        self.idea_file = self.file_idea()
        if not os.path.exists(resolve_absolute_path(self.idea_file)):
            print(f"[ 💀 {self.agent_id} Agent | CRITICAL ERROR ] (4) Not found IDEA file {self.idea_file}")
            sys.exit(1)
        
        # check requirments file
        self.ba_file = self.file_ba()
        if not os.path.exists(resolve_absolute_path(self.ba_file)):
            print(f"[ 💀 {self.agent_id} Agent | CRITICAL ERROR ] (5) Not found BA file {self.ba_file}")
            sys.exit(1)
        
        # check blueprint file
        self.blueprint_file = self.file_blueprint()
        if not os.path.exists(resolve_absolute_path(self.blueprint_file)):
            print(f"[ 💀 {self.agent_id} Agent | CRITICAL ERROR ] (6) Not found BLUEPRINT file {self.blueprint_file}")
            sys.exit(1)
    
    def config_llm(self):
        model_name = self.config_model_name()
        return LLM(
            model=model_name,
            temperature=self.agent_temperature
        ) if model_name else None
    
    @abstractmethod
    def __create_llm_agent__(self, **kwargs):
        pass
    
    @abstractmethod
    def __create_agent_task__(self, **kwargs) -> Task:
        pass
    
    # @override
    def initialize(self):
        # pre-initialize
        self.__pre_initialize__()
        
        # initialize super
        super().initialize()
    
    # @override
    def agent_secrets_key(self) -> str:
        pass
    
    # @override
    def agent_log_file(self) -> str:
        pass
    
    # @override
    def system_prompt_template(self) -> str:
        pass
    
    # @override
    def build_system_prompt(self, **kwargs) -> str:
        pass
    
    # @override
    def user_prompt_template(self) -> str:
        pass
    
    # @override
    def build_user_prompt(self, **kwargs) -> str:
        pass
    
    # @override
    def agent_temperature(self):
        return 0.8
    
    # @override
    def process_communication(self, response_data, **kwargs):
        pass
    
    # @override
    def pre_execute(self, **kwargs):
        pass


# =====================================================================
# 🕵️‍♂️ CLASS 1: THE SUPREME REVIEWER AGENT (ENTERPRISE SOLUTION SENTINEL)
# =====================================================================
class EnterpriseSolutionSentinelAgent(AbstractCrewEnterpriseSuperAgent):
    """
    A Class-based Agent representing the Supreme Gatekeeper.
    It scans Idea, SRS, and Blueprint files for gaps, loopholes, and enterprise compliance.
    """
    def __init__(self, **kwargs):
        super().__init__(agent_id='EnterpriseSolutionSentinel', **kwargs)
    
    # @override
    def initialize(self):
        pass # no need to initialize, just need creating agent/task
    
    # @override
    def __create_llm_agent__(self, **kwargs):
        self.agent = Agent(
            role="Enterprise Solution Sentinel & Principal / Senior Architecture Gatekeeper",
            goal="Audit system alignment across Idea, SRS, and Blueprint. Detect loopholes and enforce structural fixes.",
            backstory=(
                "You are the ultimate Technical Governance Board in an automated ecosystem. "
                "With 20+ years of Enterprise Architecture experience, you analyze engineering assets "
                "with absolute precision. If layers mismatch, you issue mandatory rewrite orders."
            ),
            llm=kwargs_by_key(key="llm", **kwargs),
            verbose=True
        )
        return self.agent
    
    # @override
    def __create_agent_task__(self, **kwargs) -> Task:
        """
        Generates the core evaluation task with injectible document payloads.
        """
        return Task(
            description=kwargs_by_key(key="prompt_solution_sentinel", **kwargs),
            expected_output=kwargs_by_key(key="expected_output_solution_sentinel", **kwargs),
            agent=self.agent
        )
    
    # @override
    def __ai_execute__(self, **kwargs):
        pass

# =====================================================================
# 📋 CLASS 2: BUSINESS ANALYST AGENT
# =====================================================================
class EnterpriseBusinessAnalystAgent(AbstractCrewEnterpriseSuperAgent):
    """
    A Class-based Agent responsible for authoring and revising the SRS.
    """
    def __init__(self, **kwargs):
        super().__init__(agent_id='EnterpriseBusinessAnalyst', **kwargs)
    
    # @override
    def initialize(self):
        pass # no need to initialize, just need creating agent/task
    
    # @override
    def __create_llm_agent__(self, **kwargs):
        self.agent = Agent(
            role="Enterprise Business Analyst",
            goal="Author and overhaul software requirements specifications ensuring absolute alignment with product ideas.",
            backstory="Senior BA specializing in Fortune-500 scale system requirements. Processes review failures instantly to patch gaps.",
            llm=kwargs_by_key(key="llm", **kwargs),
            verbose=True
        )
        return self.agent

    # @override
    def __create_agent_task__(self, **kwargs) -> Task:
        return Task(
            description=kwargs_by_key(key="prompt_ba" **kwargs),
            expected_output=kwargs_by_key(key="expected_output_ba", **kwargs),
            agent=self.agent,
            context=kwargs_by_key(key="context_tasks_ba" **kwargs)
        )
    
    # @override
    def __ai_execute__(self, **kwargs):
        pass


# =====================================================================
# 📐 CLASS 3: SYSTEM ARCHITECT AGENT
# =====================================================================
class EnterpriseSystemArchitectAgent(AbstractCrewEnterpriseSuperAgent):
    """
    A Class-based Agent responsible for structural and infrastructural Blueprints.
    """
    def __init__(self, **kwargs):
        super().__init__(agent_id='EnterpriseSystemArchitect', **kwargs)
    
    # @override
    def initialize(self):
        pass # no need to initialize, just need creating agent/task
    
    # @override
    def __create_llm_agent__(self, **kwargs):
        self.agent = Agent(
            role="Enterprise System Architect",
            goal="Architect and refactor system blueprint infrastructures to match software specifications.",
            backstory="Principal Solutions Architect. Re-engineers database models and microservices whenever requirements change.",
            llm=kwargs_by_key(key="llm", **kwargs),
            verbose=True
        )
        return self.agent

    # @override
    def __create_agent_task__(self, **kwargs) -> Task:
        return Task(
            description=kwargs_by_key(key="prompt_sa" **kwargs),
            expected_output=kwargs_by_key(key="expected_output_sa", **kwargs),
            agent=self.agent,
            context=kwargs_by_key(key="context_tasks_ba" **kwargs)
        )
    
    # @override
    def __ai_execute__(self, **kwargs):
        pass


# =====================================================================
# 🕵️‍♂️ CLASS 4: THE SUPREME WORKFLOW AGENT (ENTERPRISE WORKFLOW)
# =====================================================================
class CrewEnterpriseSolutionWorkflowAgent(AbstractCrewEnterpriseSuperAgent):
    """
    A Class-based Agent representing the Supreme Gatekeeper.
    It scans Idea, SRS, and Blueprint files for gaps, loopholes, and enterprise compliance.
    """
    def __init__(self, **kwargs):
        super().__init__(agent_id='CrewEnterpriseSolutionWorkflowReviewer', **kwargs)
    
    def build_prompts(self, **kwargs):
        return {
            **kwargs,
            "prompt_solution_sentinel": render_kwargs_prompt(PROMPT_TEMPLATE_SOLUTION_SENTINEL, **kwargs),
            "prompt_ba": render_kwargs_prompt(PROMPT_TEMPLATE_BA, **kwargs),
            "prompt_sa": render_kwargs_prompt(PROMPT_TEMPLATE_SA, **kwargs)
        }
    
    # @override
    def __pre_initialize__(self):
        super().__pre_initialize__()
        
        # initial agents
        self.agent_solution_sentinel = EnterpriseSolutionSentinelAgent(**self.kwargs)
        self.agent_business_analyst = EnterpriseBusinessAnalystAgent(**self.kwargs)
        self.agent_system_architect = EnterpriseSystemArchitectAgent(**self.kwargs)
    
    # @override
    def __create_llm_agent__(self, **kwargs):
        self.agent_solution_sentinel.__create_llm_agent__(**kwargs)
        self.agent_business_analyst.__create_llm_agent__(**kwargs)
        self.agent_system_architect.__create_llm_agent__(**kwargs)
        return None
    
    # @override
    def __create_agent_task__(self, **kwargs) -> Task:
        # solution sentinel task
        self.task_solution_sentinel = self.agent_solution_sentinel.__create_agent_task__(**kwargs)
        
        # business analyst task
        kwargs = {
            **kwargs,
            "context_tasks_ba": [ self.task_solution_sentinel ]
        }
        self.task_business_analyst = self.agent_business_analyst.__create_agent_task__(**kwargs)
        
        # system architect task
        kwargs = {
            **kwargs,
            "context_tasks_sa": [ self.task_business_analyst ]
        }
        self.task_system_architect = self.agent_system_architect.__create_agent_task__(**kwargs)
        return None
    
    # @override
    def agent_log_file(self) -> str:
        return CSRO_LOG_FILE
    
    # @override
    def pre_execute(self, **kwargs):
        # read idea file
        idea_f = resolve_absolute_path(self.idea_file)
        _, raw_idea_content = read_file_raw(file_path=idea_f)
        
        # read BA file
        ba_f = resolve_absolute_path(self.ba_file)
        _, raw_ba_content = read_file_raw(file_path=ba_f)
        
        # read BluePrint file
        blueprint_f = resolve_absolute_path(self.blueprint_file)
        _, raw_blueprint_content = read_file_raw(file_path=blueprint_f)
        
        # return merged new values
        now = datetime.now()
        return {
            **kwargs,
            "current_timestamp": now.strftime("%Y/%m/%d %H:%M:%S"),
            "current_timestamp_2": now.strftime("%Y%m%d%H%M%S"),
            "raw_idea_content": raw_idea_content,
            "raw_srs_content": raw_ba_content,
            "raw_blueprint_content": raw_blueprint_content,
            "expected_output_solution_sentinel": EXPECTED_OUTPUT_SOLUTION_SENTINEL,
            "expected_output_ba": EXPECTED_OUTPUT_BA,
            "expected_output_sa": EXPECTED_OUTPUT_SA
        }
    
    # @override
    def __communicate_ai__(self, **kwargs):
        # create CrewAI
        crew_ai = Crew(
            agents=kwargs_by_key(key="agents", **kwargs),
            tasks=kwargs_by_key(key="tasks", **kwargs),
            process=Process.sequential
        )
        
        # kick-off CrewAI
        return crew_ai.kickoff()
    
    # @override
    def __parse_ai_response__(self, response):
        return response
    
    # @override
    def process_communication(self, response_data, **kwargs):
        if not response_data:
            raise RuntimeError(f"[ 💀 {self.agent_id} Agent | CRITICAL ERROR ] (7) Invalid AI raw response.")
        
        # export storage audit report
        project_name = self.project_name()
        timestamp = kwargs_by_key(key="current_timestamp_2", **kwargs)
        csro_report_file = os.path.join(CSRO_STORAGE_PATH, project_name, f"{timestamp}_chief-solution-report.md")
        write_file(file=csro_report_file, data=response_data)
        
        # export raw response if necessary as log tracing
        raw_response = kwargs_by_key(key="raw_response", **kwargs)
        if raw_response:
            write_file(
                file=CSRO_RAW_FILE,
                data=raw_response
            )
    
    # @override
    def __ai_execute__(self, **kwargs):
        # build prompts
        kwargs = self.build_prompts(**kwargs)
        
        # initialize LLM model
        llm = self.config_llm()
        kwargs = {
            **kwargs,
            "llm": llm
        }
        
        # create internal LLM agents
        self.__create_llm_agent__(**kwargs)
        
        # create task
        self.__create_agent_task__(**kwargs)
        
        # initial crew with internal agent, task
        agents = [
            self.agent_solution_sentinel.agent,
            self.agent_business_analyst.agent,
            self.agent_system_architect.agent,
        ]
        tasks = [
            self.task_solution_sentinel,
            self.task_business_analyst,
            self.task_system_architect
        ]
        kwargs = {
            **kwargs,
            "agents": agents,
            "tasks": tasks
        }
        return super().__ai_execute__(**kwargs)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--idea", type=str, help="Idea Identity for searching")
    args = parser.parse_args()
    CrewEnterpriseSolutionWorkflowAgent(
        idea=args.idea,
    ).execute()


