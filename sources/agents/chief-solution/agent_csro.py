import os
import sys
import json
import re
import hashlib
import argparse
import asyncio
import litellm
from datetime import datetime
from openai import OpenAI

# for abstract class
from abc import ABC, abstractmethod

# internal agent CrewAI
from crewai import Agent, Crew, Process, Task, LLM
from crewai.events.event_bus import crewai_event_bus
from crewai.events.base_events import reset_emission_counter
from crewai.events.event_context import _event_id_stack, EventContextConfig, _event_context_config

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from sources.agents.agent_helper import (
    resolve_absolute_path,
    read_json_file,
    read_file_raw,
    write_json_file,
    write_file,
    delete_file,
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
EXPECTED_OUTPUT_SOLUTION_SENTINEL   = (
    "The complete technical audit report formatted EXACTLY as specified "
    "in the 'MANDATORY OUTPUT FORMAT' section of your system instructions. "
    "It must contain the Overall Status (PASSED/FAILED) and Detailed Loopholes with Gap-IDs."
)
EXPECTED_OUTPUT_BA                  = (
    "The complete, flawless Enterprise SRS document formatted EXACTLY "
    "as specified in the 'MANDATORY OUTPUT FORMAT (Markdown Enterprise SRS)' section."
)
EXPECTED_OUTPUT_SA                  = (
    "The complete Enterprise Global Blueprint Report formatted EXACTLY "
    "as specified in the 'MANDATORY OUTPUT FORMAT (Markdown Blueprint)' section."
)
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
    
    def __create_ai_client__(self):
        return LLM(
            model=self.config_model_name(),
            base_url=self.config_api_endpoint(),
            api_key=self.__config_api_key__(),
            provider="openrouter",                  # force LLM provider
            temperature=self.agent_temperature()
        )
    
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
            backstory=kwargs_by_key(key="prompt_solution_sentinel", **kwargs),
            llm=kwargs_by_key(key="llm", **kwargs),
            verbose=True,
            max_iter=1,                 # maximum 1 interation
            allow_delegation=False      # to avoid loop
        )
        return self.agent
    
    # @override
    def __create_agent_task__(self, **kwargs) -> Task:
        """
        Generates the core evaluation task with injectible document payloads.
        """
        return Task(
            description=(
                "You must audit the injected documents payload. "
                "Execute the MANDATORY TRIPLE-CHECK AUDIT PROTOCOL strictly. "
                f"Your internal thought and rules are defined here:\n{kwargs_by_key(key="prompt_solution_sentinel", **kwargs)}"
            ),
            expected_output=kwargs_by_key(key="expected_output_solution_sentinel", **kwargs),
            agent=self.agent
        )
    
    # @override
    def __create_ai_client__(self):
        pass
    
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
            backstory=kwargs_by_key(key="prompt_ba", **kwargs),
            llm=kwargs_by_key(key="llm", **kwargs),
            verbose=True,
            max_iter=1,                 # maximum 1 interation
            allow_delegation=False      # to avoid loop
        )
        return self.agent

    # @override
    def __create_agent_task__(self, **kwargs) -> Task:
        return Task(
            description=f"Analyze the review signals and rewrite the SRS based on these instructions:\n{kwargs_by_key(key="prompt_ba", **kwargs)}",
            expected_output=kwargs_by_key(key="expected_output_ba", **kwargs),
            agent=self.agent,
            context=kwargs_by_key(key="context_tasks_ba", **kwargs)
        )
    
    # @override
    def __create_ai_client__(self):
        pass
    
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
            backstory=kwargs_by_key(key="prompt_sa", **kwargs),
            llm=kwargs_by_key(key="llm", **kwargs),
            verbose=False,
            max_iter=1,                 # maximum 1 interation
            allow_delegation=False      # to avoid loop
        )
        return self.agent

    # @override
    def __create_agent_task__(self, **kwargs) -> Task:
        return Task(
            description=f"Overhaul the System Architecture Blueprint based on these instructions:\n{kwargs_by_key(key="prompt_sa", **kwargs)}",
            expected_output=kwargs_by_key(key="expected_output_sa", **kwargs),
            agent=self.agent,
            context=kwargs_by_key(key="context_tasks_sa", **kwargs)
        )
    
    # @override
    def __create_ai_client__(self):
        pass
    
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
    def __create_llm_agent__(self, **kwargs):
        # re-initialialize agent classes to release memory
        self.agent_solution_sentinel = EnterpriseSolutionSentinelAgent(**kwargs)
        self.agent_business_analyst = EnterpriseBusinessAnalystAgent(**kwargs)
        self.agent_system_architect = EnterpriseSystemArchitectAgent(**kwargs)
        
        # create internal agents
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
    
    def __build_arguments_for_communicating__(self, **kwargs):
        # initialize LLM model, belongs to rotating models
        built_kwargs = {
            **kwargs,
            "llm": self.client
        }
        
        # create internal LLM agents
        self.__create_llm_agent__(**built_kwargs)
        
        # create task
        self.__create_agent_task__(**built_kwargs)
        
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
        return {
            **built_kwargs,
            "agents": agents,
            "tasks": tasks
        }
    
    def __reset_crew_event_bus_to_rotate_model__(self):
        try:
            # 1. reset events counter of CrewAI
            reset_emission_counter()
            
            # 2. for ContextVar contains Event ID Stack to empty tuple ()
            _event_id_stack.set(()) 
            _event_context_config.set(EventContextConfig())
            
            # 3. reset stuck sync/async handlers / events
            if hasattr(crewai_event_bus, '_sync_handlers'):
                crewai_event_bus._sync_handlers.clear()
            if hasattr(crewai_event_bus, '_async_handlers'):
                crewai_event_bus._async_handlers.clear()
            if hasattr(crewai_event_bus, '_event_scopes'):
                crewai_event_bus._event_scopes = []
            if hasattr(crewai_event_bus, '_events'):
                crewai_event_bus._events = {}
            print("[ ✅ CLEAN ] Reset present Event Stack to rotate new model.")
            return True
        except Exception as e:
            print(f"[ ❌ ERROR ] Could not reset Event Bus: {str(e)}")
            return False
    
    # @override
    def __rotate_next_model__(self):
        # require clear event stack to avoid events stuck before rotating new model
        if self.__reset_crew_event_bus_to_rotate_model__():
            return super().__rotate_next_model__()
        return False
    
    # @override
    def __communicate_ai__(self, **kwargs):
        # build arguments
        built_kwargs = self.__build_arguments_for_communicating__(**kwargs)
        
        # create CrewAI
        crew_ai = Crew(
            agents=kwargs_by_key(key="agents", **built_kwargs),
            tasks=kwargs_by_key(key="tasks", **built_kwargs),
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
        # build prompts first
        kwargs = self.build_prompts(**kwargs)
        
        # execute
        return super().__ai_execute__(**kwargs)
    
    # @override
    def __do_execute__(self, **kwargs):
        # execute
        result = super().__do_execute__(**kwargs)
        
        # success, due to not reach exception from super function, do delete log if neccessary
        delete_file(file=self.agent_log_file())
        
        # return result
        return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--idea", type=str, help="Idea Identity for searching")
    args = parser.parse_args()
    
    # force litellm stop collecting old exceptions to metadata
    litellm.suppress_helper_warnings = True
    litellm.drop_params = True
    
    # initializ workflow agent
    workflow_agent = CrewEnterpriseSolutionWorkflowAgent(
        idea=args.idea,
    )
    
    # use asyncio to run safely while CI/CD doesn't have loop under background
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
    # execute workflow
    loop.run_until_complete(asyncio.to_thread(workflow_agent.execute))


