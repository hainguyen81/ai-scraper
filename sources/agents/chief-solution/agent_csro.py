import os
import sys
import asyncio
from datetime import datetime

# for abstract class
from abc import abstractmethod

# LLM
import litellm

# internal agent CrewAI
from crewai import Agent, Crew, Process, Task, LLM
from crewai.events.event_bus import crewai_event_bus
from crewai.events.base_events import reset_emission_counter
from crewai.events.event_context import _event_id_stack, EventContextConfig, _event_context_config
# use flow for blueprint diff analysis
from crewai.flow import Flow, listen, start

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from sources.agents.agent_helper import (
    write_file,
    delete_file,
    render_kwargs_prompt,
    get_logger,
    parse_args,
    datetime_for_agent
)

# super agent
from sources.agents.subagent_super import AbstractSubAgent

# ==============================================================================
# GLOBAL CONFIGURATION PATHS - CONFIG HERE TO CUSTOMIZE DIRECTORY STRUCTURE
# ==============================================================================
# Crew Agent backstory prompts
PROMPT_TEMPLATE_BACKSTORY_SOLUTION_SENTINEL     = "agent_csro.backstory.prompt.solution-sentinel.md"
PROMPT_TEMPLATE_BACKSTORY_BA                    = "agent_csro.backstory.prompt.ba.md"
PROMPT_TEMPLATE_BACKSTORY_SA                    = "agent_csro.backstory.prompt.sa.md"
PROMPT_TEMPLATE_BACKSTORY_DIFF_ANALYZER         = "agent_csro.backstory.prompt.diff-blueprint-analyzer.md"

# Crew Agent Task `expected_output` prompts
PROMPT_TEMPLATE_EXPECTED_SOLUTION_SENTINEL      = "agent_csro.expected.solution-sentinel.md"
PROMPT_TEMPLATE_EXPECTED_BA                     = "agent_csro.expected.ba.md"
PROMPT_TEMPLATE_EXPECTED_SA                     = "agent_csro.expected.sa.md"
PROMPT_TEMPLATE_EXPECTED_DIFF_ANALYZER          = "agent_csro.expected.diff-blueprint-analyzer.md"

# Crew Agent Task `task_description` prompts
PROMPT_TEMPLATE_TASK_SOLUTION_SENTINEL          = "agent_csro.task.solution-sentinel.md"
PROMPT_TEMPLATE_TASK_BA                         = "agent_csro.task.ba.md"
PROMPT_TEMPLATE_TASK_SA                         = "agent_csro.task.sa.md"
PROMPT_TEMPLATE_TASK_DIFF_ANALYZER              = "agent_csro.task.diff-blueprint-analyzer.md"

# CSRO log files
CSRO_RAW_FILE                                   = "chief-solution-review.md"
CSRO_LOG_FILE                                   = "chief-solution-review_log.md"
CSRO_DA_FILE                                    = "chief-solution-diff-analysis.md"
CSRO_LOG_DA_FILE                                = "chief-solution-diff-analysis_log.md"

DEFAULT_CSRO_LANGUAGE                           = "English"


# support for executing workflow
def __execute_function_until_complete__(func_pointer, **kwargs):
    # use asyncio to run safely while CI/CD doesn't have loop under background
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
    # execute workflow
    return loop.run_until_complete(asyncio.to_thread(func_pointer, **kwargs)) or {}


# =====================================================================
# 🕵️‍♂️ SUPER: THE SUPREME AGENT (ENTERPRISE SOLUTION SUPER AGENT)
# =====================================================================
class AbstractCrewEnterpriseSuperAgent(AbstractSubAgent):
    """
    A Class-based Agent representing the Supreme Gatekeeper.
    It scans Idea, SRS, and Blueprint files for gaps, loopholes, and enterprise compliance.
    """
    def __init__(self, agent_id, **kwargs):
        super().__init__(agent_id=agent_id, **kwargs)
    
    def file_blueprint_approval(self, prefix):
        project_name = self.__current_project_name__()
        prefix = prefix if prefix else "_"
        return self.__storage_path__(
            storage_name="storage_sa",
            file=f"{project_name}/context/{prefix}-csro.{project_name}.global.blueprint.md"
        ) if project_name else None
    
    def file_blueprint_diff_analysis(self, prefix):
        project_name = self.__current_project_name__()
        prefix = prefix if prefix else "_"
        return self.__storage_path__(
            storage_name="storage_sa",
            file=f"{project_name}/context/{prefix}-diff-analysis.{project_name}.global.blueprint.md"
        ) if project_name else None
    
    def file_ba_approval(self, prefix):
        project_name = self.__current_project_name__()
        prefix = prefix if prefix else "_"
        return self.__storage_path__(
            storage_name="storage_ba",
            file=f"{project_name}/{prefix}-csro.requirements.md"
        ) if project_name else None
    
    def file_report_ba_approval(self, prefix):
        project_name = self.__current_project_name__()
        prefix = prefix if prefix else "_"
        return self.__storage_path__(
            storage_name="storage_csro",
            file=f"{project_name}/{prefix}.chief-solution-report-ba.md"
        ) if project_name else None
    
    def file_report_sa_approval(self, prefix):
        project_name = self.__current_project_name__()
        prefix = prefix if prefix else "_"
        return self.__storage_path__(
            storage_name="storage_csro",
            file=f"{project_name}/{prefix}.chief-solution-report-sa.md"
        ) if project_name else None
    
    def file_report_da_approval(self, prefix):
        project_name = self.__current_project_name__()
        prefix = prefix if prefix else "_"
        return self.__storage_path__(
            storage_name="storage_csro",
            file=f"{project_name}/{prefix}.chief-solution-report-diff-analysis.md"
        ) if project_name else None
    
    def file_report_sentinel_approval(self, prefix):
        project_name = self.__current_project_name__()
        prefix = prefix if prefix else "_"
        return self.__storage_path__(
            storage_name="storage_csro",
            file=f"{project_name}/{prefix}.chief-solution-report-sentinel.md"
        ) if project_name else None
    
    def file_report_kickoff(self, prefix):
        project_name = self.__current_project_name__()
        prefix = prefix if prefix else "_"
        return self.__storage_path__(
            storage_name="storage_csro",
            file=f"{project_name}/{prefix}.chief-solution-kickoff.md"
        ) if project_name else None
    
    def template_prompt_backstory_sentinel(self):
        return self.__agents_path__(storage_name="storage_csro_prompts", file=PROMPT_TEMPLATE_BACKSTORY_SOLUTION_SENTINEL)
    
    def template_prompt_backstory_ba(self):
        return self.__agents_path__(storage_name="storage_csro_prompts", file=PROMPT_TEMPLATE_BACKSTORY_BA)
    
    def template_prompt_backstory_sa(self):
        return self.__agents_path__(storage_name="storage_csro_prompts", file=PROMPT_TEMPLATE_BACKSTORY_SA)
    
    def template_prompt_backstory_diff_analysis(self):
        return self.__agents_path__(storage_name="storage_csro_prompts", file=PROMPT_TEMPLATE_BACKSTORY_DIFF_ANALYZER)
    
    def template_prompt_exptected_sentinel(self):
        return self.__agents_path__(storage_name="storage_csro_prompts", file=PROMPT_TEMPLATE_EXPECTED_SOLUTION_SENTINEL)
    
    def template_prompt_expected_ba(self):
        return self.__agents_path__(storage_name="storage_csro_prompts", file=PROMPT_TEMPLATE_EXPECTED_BA)
    
    def template_prompt_expected_sa(self):
        return self.__agents_path__(storage_name="storage_csro_prompts", file=PROMPT_TEMPLATE_EXPECTED_SA)
    
    def template_prompt_expected_diff_analysis(self):
        return self.__agents_path__(storage_name="storage_csro_prompts", file=PROMPT_TEMPLATE_EXPECTED_DIFF_ANALYZER)
    
    def template_prompt_task_sentinel(self):
        return self.__agents_path__(storage_name="storage_csro_prompts", file=PROMPT_TEMPLATE_TASK_SOLUTION_SENTINEL)
    
    def template_prompt_task_ba(self):
        return self.__agents_path__(storage_name="storage_csro_prompts", file=PROMPT_TEMPLATE_TASK_BA)
    
    def template_prompt_task_sa(self):
        return self.__agents_path__(storage_name="storage_csro_prompts", file=PROMPT_TEMPLATE_TASK_SA)
    
    def template_prompt_task_diff_analysis(self):
        return self.__agents_path__(storage_name="storage_csro_prompts", file=PROMPT_TEMPLATE_TASK_DIFF_ANALYZER)
    
    def __common_prompt_context__(self):
        datetime_prompt, datetime_docid = datetime_for_agent()
        return {
            "idea_id": self.idea_id,
            "language": self.language,
            "project_name": self.__current_project_name__() or "-",
            "project_description": self.__current_project_description__() or "-",
            "current_timestamp": datetime_prompt,
            "doc_id": datetime_docid
        }
    
    def __pre_initialize__(self):
        # require idea identity to analyze
        if not self.project_info:
            self.logger.critical(f"💀 (1) Invalid idea identity / project name to analyze!")
            sys.exit(1)
        
        # check idea file
        abs_idea_file, phys_idea_file = self.__idea_files__()
        if not os.path.exists(phys_idea_file):
            self.logger.critical(f"💀 (4) Not found IDEA file {abs_idea_file}")
            sys.exit(1)
        else:
            self.idea_file = abs_idea_file
        
        # check requirments file
        self.ba_file = self.__ba_file__()
        if not os.path.exists(self.ba_file):
            self.logger.critical(f"💀 (5) Not found BA file by idea identity / project name '{self.idea_id}'")
            sys.exit(1)
        
        # check blueprint file
        self.blueprint_file = self.__sa_file__()
        if not os.path.exists(self.blueprint_file):
            self.logger.critical(f"💀 (6) Not found BLUEPRINT file by idea identity / project name '{self.idea_id}")
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
        self.language = self.get_kwargs("language") or DEFAULT_CSRO_LANGUAGE
    
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
        return 0.1 # require strickly, exact requirements
    
    # @override
    def process_communication(self, **kwargs):
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
        super().__init__(agent_id='🕵️‍♂️ EnterpriseSolutionSentinelAgent', **kwargs)
    
    # @override
    def initialize(self):
        pass # no need to initialize, just need creating agent/task
    
    # @override
    def __create_llm_agent__(self, **kwargs):
        self.agent = Agent(
            role="Enterprise Solution Sentinel & Principal / Senior Architecture Gatekeeper",
            goal="Audit system alignment across Idea, SRS, and Blueprint. Detect loopholes and enforce structural fixes.",
            backstory=self.get_kwargs_by_key(key="backstory_sentinel", **kwargs),
            llm=self.get_kwargs_by_key(key="llm", **kwargs),
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
            description=self.get_kwargs_by_key(key="task_sentinel", **kwargs),
            expected_output=self.get_kwargs_by_key(key="expected_sentinel", **kwargs),
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
        super().__init__(agent_id='📋 EnterpriseBusinessAnalystAgent', **kwargs)
    
    # @override
    def initialize(self):
        pass # no need to initialize, just need creating agent/task
    
    # @override
    def __create_llm_agent__(self, **kwargs):
        self.agent = Agent(
            role="Enterprise Business Analyst",
            goal="Author and overhaul software requirements specifications ensuring absolute alignment with product ideas.",
            backstory=self.get_kwargs_by_key(key="backstory_ba", **kwargs),
            llm=self.get_kwargs_by_key(key="llm", **kwargs),
            verbose=True,
            max_iter=1,                 # maximum 1 interation
            allow_delegation=False      # to avoid loop
        )
        return self.agent

    # @override
    def __create_agent_task__(self, **kwargs) -> Task:
        return Task(
            description=self.get_kwargs_by_key(key="task_ba", **kwargs),
            expected_output=self.get_kwargs_by_key(key="expected_ba", **kwargs),
            agent=self.agent,
            context=self.get_kwargs_by_key(key="context_tasks_ba", **kwargs)
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
        super().__init__(agent_id='📐 EnterpriseSystemArchitectAgent', **kwargs)
    
    # @override
    def initialize(self):
        pass # no need to initialize, just need creating agent/task
    
    # @override
    def __create_llm_agent__(self, **kwargs):
        self.agent = Agent(
            role="Enterprise System Architect",
            goal="Architect and refactor system blueprint infrastructures to match software specifications.",
            backstory=self.get_kwargs_by_key(key="backstory_sa", **kwargs),
            llm=self.get_kwargs_by_key(key="llm", **kwargs),
            verbose=False,
            max_iter=1,                 # maximum 1 interation
            allow_delegation=False      # to avoid loop
        )
        return self.agent

    # @override
    def __create_agent_task__(self, **kwargs) -> Task:
        return Task(
            description=self.get_kwargs_by_key(key="task_sa", **kwargs),
            expected_output=self.get_kwargs_by_key(key="expected_sa", **kwargs),
            agent=self.agent,
            context=self.get_kwargs_by_key(key="context_tasks_sa", **kwargs)
        )
    
    # @override
    def __create_ai_client__(self):
        pass
    
    # @override
    def __ai_execute__(self, **kwargs):
        pass


# =====================================================================
# 🕵️‍♂️ CLASS 4: THE SUPREME SYSTEM ARCHITECTURE WORKFLOW AGENT (ENTERPRISE WORKFLOW)
# =====================================================================
class AbstractCrewEnterpriseWorkflowAgent(AbstractCrewEnterpriseSuperAgent):
    """
    A Class-based Agent representing the Supreme Gatekeeper.
    It scans Idea, SRS, and Blueprint files for gaps, loopholes, and enterprise compliance.
    """
    def __init__(self, agent_id, **kwargs):
        super().__init__(agent_id=agent_id, **kwargs)
    
    @abstractmethod
    def build_prompts(self, **kwargs):
        pass
    
    # @override
    def agent_log_file(self) -> str:
        return self.__output_storage_path__(storage_name="output_csro", file=CSRO_LOG_FILE)
    
    @abstractmethod
    def __build_arguments_for_communicating__(self, **kwargs):
        pass
    
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
            print(f"[ ✅ {self.agent_id} Agent | CLEAN ] Reset present Event Stack to rotate new model.")
            return True
        except Exception as e:
            print(f"[ ❌ {self.agent_id} Agent | ERROR ] Could not reset Event Bus: {str(e)}")
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
        built_kwargs = self.__build_arguments_for_communicating__(**kwargs) or {}
        
        # create CrewAI
        crew_ai = Crew(
            agents=self.get_kwargs_by_key(key="agents", **built_kwargs),
            tasks=self.get_kwargs_by_key(key="tasks", **built_kwargs),
            process=Process.sequential
        )
        
        # kick-off CrewAI
        return crew_ai.kickoff()
    
    # @override
    def __ai_execute__(self, **kwargs):
        # build prompts first
        kwargs = self.build_prompts(**kwargs)
        
        # execute
        return super().__ai_execute__(**kwargs)
    
    # @override
    def __do_execute__(self, **kwargs):
        # execute
        kwargs = super().__do_execute__(**kwargs)
        
        # success, due to not reach exception from super function, do delete log if neccessary
        delete_file(file=self.agent_log_file())
        
        # return result
        return kwargs


# =====================================================================
# 🕵️‍♂️ CLASS 5: THE SUPREME SYSTEM ARCHITECTURE WORKFLOW AGENT (ENTERPRISE WORKFLOW)
# =====================================================================
class CrewEnterpriseSolutionWorkflowAgent(AbstractCrewEnterpriseWorkflowAgent):
    """
    A Class-based Agent representing the Supreme Gatekeeper.
    It scans Idea, SRS, and Blueprint files for gaps, loopholes, and enterprise compliance.
    """
    def __init__(self, **kwargs):
        super().__init__(agent_id='🤖🏛️ EnterpriseSolutionWorkflowReviewerAgent', **kwargs)
    
    # @override
    def agent_log_file(self) -> str:
        return self.__output_storage_path__(storage_name="output_csro", file=CSRO_LOG_FILE)
    
    # @override
    def build_prompts(self, **kwargs):
        return {
            **kwargs,
            "backstory_sentinel": render_kwargs_prompt(self.template_prompt_backstory_sentinel(), **kwargs),
            "backstory_ba": render_kwargs_prompt(self.template_prompt_backstory_ba(), **kwargs),
            "backstory_sa": render_kwargs_prompt(self.template_prompt_backstory_sa(), **kwargs),
            
            "expected_sentinel": render_kwargs_prompt(self.template_prompt_exptected_sentinel(), **kwargs),
            "expected_ba": render_kwargs_prompt(self.template_prompt_expected_ba(), **kwargs),
            "expected_sa": render_kwargs_prompt(self.template_prompt_expected_sa(), **kwargs),
            
            "task_sentinel": render_kwargs_prompt(self.template_prompt_task_sentinel(), **kwargs),
            "task_ba": render_kwargs_prompt(self.template_prompt_task_ba(), **kwargs),
            "task_sa": render_kwargs_prompt(self.template_prompt_task_sa(), **kwargs),
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
            "context_tasks_sa": [ self.task_solution_sentinel, self.task_business_analyst ]
        }
        self.task_system_architect = self.agent_system_architect.__create_agent_task__(**kwargs)
        return None
    
    # @override
    def pre_execute(self, **kwargs):
        # read idea file
        _, raw_idea_content = self.__read_idea_or_requirements__(ignore_not_found=True)
        
        # no idea also no requirements
        if not raw_idea_content:
            self.logger.critical(f"💀 Not found IDEA / Requirements file to process")
            sys.exit(1)
        
        # read BA file
        raw_ba_content = self.__read_srs__(ignore_not_found=False)
        
        # read BluePrint file
        raw_blueprint_content = self.__read_blueprint__(ignore_not_found=False)
        
        # return merged new values
        return {
            **kwargs,
            **self.__common_prompt_context__(),
            "raw_idea_content": raw_idea_content,
            "raw_srs_content": raw_ba_content,
            "raw_blueprint_content": raw_blueprint_content
        }
    
    # @override
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
            self.task_system_architect,
        ]
        return {
            **built_kwargs,
            "agents": agents,
            "tasks": tasks
        }
    
    # @override
    def __parse_ai_response__(self, response):
        # 🔥 Extract output of tasks
        raw_sentinel_response = None
        raw_ba_response = None
        raw_sa_response = None
        try:
            # Task 1 (Sentinel) response - Audit Report
            raw_sentinel_response = self.task_solution_sentinel.output.raw
            
            # Task 2 (Business Analyst) response
            raw_ba_response = self.task_business_analyst.output.raw
            
            # Task 3 (System Architect) response - fixed blueprint
            raw_sa_response = self.task_system_architect.output.raw
        except Exception as e:
            self.logger.error(f"❌ Could extract task output: {str(e)}")

        # parsed responses
        return {
            "kickoff": response,
            "report_sentinel": raw_sentinel_response,
            "report_ba": raw_ba_response,
            "report_sa": raw_sa_response
        }
    
    # @override
    def process_communication(self, **kwargs):
        response_data = self.get_kwargs_by_key(key="clean_response", **kwargs)
        if not response_data or not isinstance(response_data, dict):
            raise RuntimeError(f"💀 (7) Invalid AI raw response.")
        
        # project info
        timestamp = self.get_kwargs_by_key(key="current_timestamp_2", **kwargs)
        
        # export storage audit report
        if "kickoff" in response_data and response_data.get("kickoff"):
            write_file(file=self.file_report_kickoff(prefix=timestamp), data=response_data.get("kickoff"))
        else:
            self.logger.warning(f"⚠️ No any kickoff report!")
        
        # export task sentinel response
        if "report_sentinel" in response_data and response_data.get("report_sentinel"):
            write_file(file=self.file_report_sentinel_approval(prefix=timestamp), data=response_data.get("report_sentinel"))
        else:
            self.logger.warning(f"⚠️ No any sentinel report!")
        
        # export task BA response
        if "report_ba" in response_data and response_data.get("report_ba"):
            response_ba = response_data.get("report_ba")
            write_file(file=self.file_report_ba_approval(prefix=timestamp), data=response_ba)
            write_file(file=self.file_ba_approval(prefix=timestamp), data=response_ba)
        else:
            self.logger.warning(f"⚠️ No any business-analysis report!")
        
        # export task SA response
        if "report_sa" in response_data and response_data.get("report_sa"):
            response_sa = response_data.get("report_sa")
            write_file(file=self.file_report_sa_approval(prefix=timestamp), data=response_sa)
            write_file(file=self.file_blueprint_approval(prefix=timestamp), data=response_sa)
        else:
            self.logger.warning(f"⚠️ No any system-architect report!")
        
        # export raw response if necessary as log tracing
        raw_response = self.get_kwargs_by_key(key="raw_response", **kwargs)
        if raw_response:
            write_file(
                file=self.__output_storage_path__(storage_name="output_csro", file=CSRO_RAW_FILE),
                data=raw_response
            )
        
        return { **kwargs }


# =====================================================================
# 📐 CLASS 6: SYSTEM ARCHITECT DIFF ANALYZER AGENT
# =====================================================================
class CrewEnterpriseBluePrintDiffAnalyzerAgent(AbstractCrewEnterpriseWorkflowAgent):
    """
    A Class-based Agent representing the Supreme Gatekeeper.
    It scans Idea, SRS, and Blueprint files for gaps, loopholes, and enterprise compliance.
    """
    def __init__(self, **kwargs):
        super().__init__(agent_id='🤖🔬 EnterpriseBluePrintDiffAnalyzerAgent', **kwargs)
    
    # @override
    def build_prompts(self, **kwargs):
        return {
            **kwargs,
            "backstory_da": render_kwargs_prompt(self.template_prompt_backstory_diff_analysis(), **kwargs),
            "task_da": render_kwargs_prompt(self.template_prompt_task_diff_analysis(), **kwargs),
            "expected_da": render_kwargs_prompt(self.template_prompt_expected_diff_analysis(), **kwargs)
        }
    
    # @override
    def __create_llm_agent__(self, **kwargs):
        self.agent = Agent(
            role="Principal Enterprise Systems Auditor",
            goal="Execute independent triple-check architectural audits on system blueprints.",
            backstory=self.get_kwargs_by_key(key="backstory_da", **kwargs),
            llm=self.get_kwargs_by_key(key="llm", **kwargs),
            verbose=False,
            max_iter=1,                 # maximum 1 interation
            allow_delegation=False      # to avoid loop
        )
        return self.agent
    
    # @override
    def __create_agent_task__(self, **kwargs) -> Task:
        return Task(
            description=self.get_kwargs_by_key(key="task_da", **kwargs),
            expected_output=self.get_kwargs_by_key(key="expected_da", **kwargs),
            agent=self.agent
        )
    
    # @override
    def agent_log_file(self) -> str:
        return self.__output_storage_path__(storage_name="output_csro", file=CSRO_LOG_DA_FILE)
    
    # @override
    def pre_execute(self, **kwargs):
        # read BluePrint file
        raw_blueprint_content = self.__read_blueprint__()
        
        # return merged new values
        return {
            **kwargs,
            **self.__common_prompt_context__(),
            "raw_blueprint_content": raw_blueprint_content
        }
    
    def __build_arguments_for_communicating__(self, **kwargs):
        # initialize LLM model, belongs to rotating models
        built_kwargs = {
            **kwargs,
            "llm": self.client
        }
        
        # initial crew with internal agent, task
        agents = [ self.__create_llm_agent__(**built_kwargs) ]
        tasks = [ self.__create_agent_task__(**built_kwargs) ]
        return {
            **built_kwargs,
            "agents": agents,
            "tasks": tasks
        }
    
    # @override
    def process_communication(self, **kwargs):
        response_data = self.get_kwargs_by_key(key="clean_response", **kwargs)
        if not response_data or not isinstance(response_data, dict):
            raise RuntimeError(f"[ 💀 {self.agent_id} Agent | CRITICAL ERROR ] (7) Invalid AI raw response.")
        
        # project info
        timestamp = self.get_kwargs_by_key(key="current_timestamp_2", **kwargs)
        
        # export task DA response
        write_file(file=self.file_report_da_approval(prefix=timestamp), data=response_data)
        write_file(file=self.file_blueprint_diff_analysis(prefix=timestamp), data=response_data)
        
        # export raw response if necessary as log tracing
        raw_response = self.get_kwargs_by_key(key="raw_response", **kwargs)
        if raw_response:
            write_file(
                file=self.__output_storage_path__(storage_name="output_csro", file=CSRO_DA_FILE),
                data=raw_response
            )
        
        return { **kwargs }


# =====================================================================
# 🕵️‍♂️ FINAL: THE SUPREME WORKFLOW AGENT (ENTERPRISE WORKFLOW)
# =====================================================================
class CrewEnterpriseGovernanceFlow(Flow):
    """
    An asynchronous, stateful event-driven workflow execution layer.
    Utilizes native CrewAI Flow hooks (@start, @listen) to eliminate 
    Pydantic re-validation failure loops and preserve clean memory handoffs.
    """

    def __init__(self, **kwargs):
        super().__init__()
        # Inject pre-initialized custom wrappers containing the actual CrewAI Agents
        self.kwargs = kwargs or {}
        self.logger = get_logger("CrewEnterpriseGovernanceFlow")
        self.agent_solution_review = CrewEnterpriseSolutionWorkflowAgent(**self.kwargs)
        self.agent_diff_analyzer = CrewEnterpriseBluePrintDiffAnalyzerAgent(**self.kwargs)

    @start()
    def execute_solution_review(self):
        """
        STAGE 1: Kicks off the linear 3-Agent generation sub-crew (Sentinel -> BA -> SA).
        Returns the raw modified blueprint string fetched directly from SA's RAM cache.
        """
        self.logger.info("[ 🚀 SOLUTION ARCHITECT REVIEW ] Enterprise Solution Architecture Review CSRO...")
        return __execute_function_until_complete__(func_pointer=self.agent_solution_review.execute) or {}

    @listen(execute_solution_review)
    def execute_blueprint_diff_analysis(self, solution_architect_review_result):
        """
        STAGE 2: Explicitly triggered via native event hooks once STAGE 1 returns successfully.
        Ingests the fixed blueprint payload into your explicit custom template keyword.
        """
        self.logger.info("[ 🔎 BLUEPRINT CHANGES ANALYSIS ] Analyze new changes of Solution Architecture Report...")
        kwargs = {
            **solution_architect_review_result,
            "raw_csro_blueprint_content": solution_architect_review_result.get("report_sa", None)
        }
        return __execute_function_until_complete__(func_pointer=self.agent_diff_analyzer.execute, **kwargs) or {}


if __name__ == "__main__":
    def add_known_arguments(parser):
        parser.add_argument("--idea", type=str, help="Idea Identity for searching")
        parser.add_argument("--language", type=str, help="Translate SRS to language. Ex: Vietnamese, English, etc.")
    
    args, unknown_args = parse_args(
        description="🕵️‍♂️ CrewEnterpriseGovernanceFlow",
        parser_callback=add_known_arguments
    )
    
    # force litellm stop collecting old exceptions to metadata
    litellm.suppress_helper_warnings = True
    litellm.drop_params = True
    
    # initializ workflow agent
    enterprise_workflow_agent = CrewEnterpriseGovernanceFlow(
        idea=args.idea,
        language=args.language,
        **unknown_args
    )
    
    # execute workflow
    __execute_function_until_complete__(enterprise_workflow_agent.kickoff)


