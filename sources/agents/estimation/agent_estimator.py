import sys
import re
import argparse
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import mermaidx

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from sources.agents.agent_helper import (
    write_file,
    makedirs,
    json_loads,
    parse_args
)

# super agent
from sources.agents.subagent_super import AbstractSubAgent

# ==============================================================================
# GLOBAL CONFIGURATION PATHS - CONFIG HERE TO CUSTOMIZE DIRECTORY STRUCTURE
# ==============================================================================
# models list
SYSTEM_PROMPT_TEMPLATE      = "agent_estimator.prompt.system.md"
USER_PROMPT_TEMPLATE        = "agent_estimator.prompt.user.md"

EST_RAW_FILE                = "estimation.md"
EST_LOG_FILE                = "estimation_log.md"
EST_CHART_FILE              = "estimation_pilot_chart.png"
EST_VISUALIZATION_FILES     = [ "cost_chart.svg", "timeline_chart.svg", "risk_matrix.svg" ]

DEFAULT_BUFFER_RATION       = 1.5
DEFAULT_EXCHANGE_RATE       = 25500.0

DEFAULT_EST_LANGUAGE        = "English"

MERMAID_URL                 = "https://mermaid.ink/svg/base64:"


class EnterpriseAutonomousProjectEstimatorAgent(AbstractSubAgent):
    def __init__(self, **kwargs):
        super().__init__(
            agent_id='EnterpriseAutonomousProjectEstimatorAgent',
            agent_name='👷 EnterpriseAutonomousProjectEstimatorAgent',
            **kwargs
        )
    
    # @override
    def initialize(self):
        # start initialization
        super().initialize()
        self.buffer_ratio = self.get_kwargs("buffer") or DEFAULT_BUFFER_RATION
        self.language = self.get_kwargs("language") or DEFAULT_EST_LANGUAGE
    
    # @override
    def agent_log_file(self) -> str:
        return self.__output_storage_path__(storage_name="output_estimation", file=EST_LOG_FILE)
    
    # @override
    def system_prompt_template(self) -> str:
        return self.__agents_path__(storage_name="storage_estimation", file=SYSTEM_PROMPT_TEMPLATE)
    
    # @override
    def user_prompt_template(self) -> str:
        return self.__agents_path__(storage_name="storage_estimation", file=USER_PROMPT_TEMPLATE)
    
    # @override
    def pre_execute(self, **kwargs):
        # read idea
        idea_same_project, raw_idea_content = self.__read_idea_or_requirements__(ignore_not_found=True)
        self.idea_is_project = idea_same_project
        
        # no idea also no requirements
        if not raw_idea_content:
            self.logger.critical(f"💀 Not found IDEA / Requirements file to process")
            sys.exit(1)
        
        # read ba/SRS
        raw_srs_content = self.__read_srs__(ignore_not_found=False)
        
        # read sa/blueprint
        raw_blueprint_content = self.__read_blueprint__(ignore_not_found=False)
        
        # return merged new values
        now = datetime.now()
        return {
            **kwargs,
            "target_language": self.language,
            "idea_id": self.idea_id,
            "project_name": self.__current_project_name__() or "-",
            "project_description": self.__current_project_description__() or "-",
            "current_timestamp": now.strftime("%Y/%m/%d %H:%M:%S"),
            "current_timestamp_2": now.strftime("%Y%m%d%H%M%S"),
            "buffer_ratio": self.buffer_ratio,
            "raw_idea_content": raw_idea_content,
            "raw_srs_content": raw_srs_content,
            "raw_blueprint_content": raw_blueprint_content
        }
    
    def __safe_parse_float_numbers_list__(self, raw_value):
        if raw_value is None:
            return []
        
        # if value already was array
        if isinstance(raw_value, list):
            float_list = []
            for val in raw_value:
                try:
                    clean_val = re.sub(r'[^\d\.]', '', str(val).strip())
                    if clean_val:
                        float_list.append(float(clean_val))
                except ValueError:
                    float_list.append(0.0)
            return float_list
        
        # try to convert
        raw_str = str(raw_value)
        clean_str = re.sub(r'[^\d\.,]', '', raw_str)
        clean_str = clean_str.replace(',', '')
        tokens = clean_str.split(',')
        
        float_list = []
        for token in tokens:
            if token.strip():
                try:
                    float_list.append(float(token.strip()))
                except ValueError:
                    float_list.append(0.0)
        return float_list
    
    def __extract_metrics_and_plot_matplotlib_chart__(self, raw_response):
        """
        Scans the AI response string, extracts the strict JSON metadata block safely,
        and returns a clean dictionary. All comments are in English.
        """
        # Use a highly resilient regex to capture only the valid JSON structural boundaries
        json_match = re.search(r'```json\s*(\{.*?\})\s*```', raw_response, re.DOTALL)
        if not json_match:
            self.logger.warning("⚠️ Metadata JSON block not found in AI response memory.")
            return {}

        try:
            # Strip latent trailing whitespaces or markdown leaks before loading
            json_content = json_match.group(1).strip()
            metrics_dict = json_loads(json_content)

            # Extract dynamic properties securely with hard fallback safeguards
            exchange_rate = float(metrics_dict.get("exchange_rate", DEFAULT_EXCHANGE_RATE))
            
            # Process flat arrays safely through the robust parser function
            return {
                "exchange_rate": exchange_rate,
                "enterprise_human_cost_usd": self.__safe_parse_float_numbers_list__(metrics_dict.get("enterprise_human_cost_usd")),
                "enterprise_ai_cost_usd": self.__safe_parse_float_numbers_list__(metrics_dict.get("enterprise_ai_cost_usd")),
                "freelance_human_cost_usd": self.__safe_parse_float_numbers_list__(metrics_dict.get("freelance_human_cost_usd")),
                "freelance_ai_cost_usd": self.__safe_parse_float_numbers_list__(metrics_dict.get("freelance_ai_cost_usd")),
                "enterprise_human_months": self.__safe_parse_float_numbers_list__(metrics_dict.get("enterprise_human_months")),
                "enterprise_ai_months": self.__safe_parse_float_numbers_list__(metrics_dict.get("enterprise_ai_months")),
                "freelance_human_months": self.__safe_parse_float_numbers_list__(metrics_dict.get("freelance_human_months")),
                "freelance_ai_months": self.__safe_parse_float_numbers_list__(metrics_dict.get("freelance_ai_months")),
                "enterprise_cloud_opex_usd": self.__safe_parse_float_numbers_list__(metrics_dict.get("enterprise_cloud_opex_usd")),
                "freelance_cloud_opex_usd": self.__safe_parse_float_numbers_list__(metrics_dict.get("freelance_cloud_opex_usd"))
            }
        except Exception as json_err:
            self.logger.warning(f"⚠️ Failed to parse JSON RAM metrics object: {str(json_err)}")
            return {}

    def __extract_mermaid_visualizations__(self, raw_response):
        """
        Extracts all Mermaid code blocks from the AI markdown response,
        compiles them into high-res SVG vectors via the Mermaid.ink API using Base64 encoding,
        and returns a dictionary mapping target filenames to their raw binary SVG content.
        """
        # Non-greedy regex mapping to sweep all markdown blocks bounded by mermaid tags
        mermaid_blocks = re.findall(r'```mermaid\s*(.*?)\s*```', raw_response, re.DOTALL)
        if not mermaid_blocks:
            self.logger.warning("⚠️ Zero functional mermaid visualization blocks detected inside the markdown body.")
            return {}

        self.logger.info(f"[ 📊 MERMAID ENGINE ] Intercepted {len(mermaid_blocks)} dynamic diagrams. Running vector compilation pipeline...")
        visualizations_data = {}
        chart_names = EST_VISUALIZATION_FILES  # Ensured this array is pre-defined within your class
        
        for idx, code in enumerate(mermaid_blocks):
            clean_code = code.strip()
            if not clean_code:
                continue
                
            try:
                mermaid_block = clean_code
                clean_code = re.sub(r'[\?\u200b-\u200d\uFEFF]', '', clean_code)
                
                # Polymorphic file naming boundaries to protect extra diagrams generated by AI
                file_name = chart_names[idx] if idx < len(chart_names) else f"custom_governance_chart_{idx}.svg"
                self.logger.info(f"⏳ Rendering dynamic vector graph data for layout file: {file_name}...")
                self.logger.debug(f"  - Mermaid: {mermaid_block}")
                self.logger.debug(f"  - Cleaned Mermaid: {clean_code}")
                
                # render mermaid
                mermaid_diagram = mermaidx.render(source=clean_code, backend="v8")
                
                # Validate response status and strictly verify the payload contains XML vector text schemas
                if mermaid_diagram:
                    visualizations_data[file_name] = mermaid_diagram.svg()
                    self.logger.info(f"💾 Highly-scalable vector graphic successfully extracted at index: {idx}")
                else:
                    self.logger.warning(f"⚠️ Source code causing compilation error: \n{clean_code}")
                    
            except Exception as net_err:
                self.logger.warning(f"⚠️ Exception while rendering mermaid vector graphic: {str(net_err)}")
                
        return visualizations_data

    def __generate_sharp_summary_chart_v2__(self, output_image_path, metrics):
        """
        Generates an ultra-sharp 3-panel summary matrix chart including:
        1. Financial Labor Budgets (4 Scenarios - Dual Currency)
        2. Cloud Infrastructure OpEx Projections (Corporate HA vs Freelance VPS)
        3. Delivery Timeline Projections (4 Scenarios)
        Safely handles dynamic exchange rates and eliminates tuple multiplication crashes.
        """
        if not metrics:
            self.logger.warning("⚠️ Invalid metrics JSON to generate chart. Skipping chart plotting.")
            return

        try:
            # 1. Safely extract live financial exchange rate
            exchange_rate = float(metrics.get("exchange_rate", 25500.0))
            
            # 2. Extract core financial labor cost flat arrays
            ent_human_cost = list(metrics.get("enterprise_human_cost_usd", []))
            ent_ai_cost = list(metrics.get("enterprise_ai_cost_usd", []))
            free_human_cost = list(metrics.get("freelance_human_cost_usd", []))
            free_ai_cost = list(metrics.get("freelance_ai_cost_usd", []))
            
            # 3. Extract core timeline duration flat arrays
            ent_human_time = list(metrics.get("enterprise_human_months", []))
            ent_ai_time = list(metrics.get("enterprise_ai_months", []))
            free_human_time = list(metrics.get("freelance_human_months", []))
            free_ai_time = list(metrics.get("freelance_ai_months", []))

            # 4. Extract newly added automated Cloud OpEx infrastructure flat arrays
            ent_cloud_opex = list(metrics.get("enterprise_cloud_opex_usd", []))
            free_cloud_opex = list(metrics.get("freelance_cloud_opex_usd", []))

            # Fallback safeguard: Guarantee exactly 3 array data points [Min, Max, Safe] for all lists
            all_metric_lists = [
                ent_human_cost, ent_ai_cost, free_human_cost, free_ai_cost,
                ent_human_time, ent_ai_time, free_human_time, free_ai_time,
                ent_cloud_opex, free_cloud_opex
            ]
            for data_list in all_metric_lists:
                while len(data_list) < 3: 
                    data_list.append(0.0)

            # 5. Initialize high-resolution rendering canvas with a 3-panel matrix framework (1 row, 3 subplots)
            plt.rcParams['figure.dpi'] = 300
            plt.rcParams['text.color'] = '#2c3e50'
            fig, (ax1, ax3, ax5) = plt.subplots(1, 3, figsize=(22, 6))
            
            fig.suptitle(f'Project Estimation & Cloud Governance Summary Matrix (1 USD = {exchange_rate:,} VND)', fontsize=14, fontweight='bold', y=0.98)
            
            categories = ['Min Bound', 'Max Bound', 'Safe Bound']
            x = np.arange(len(categories))
            width = 0.16  # Optimized bar width to prevent spatial overlapping across 4 scenario series

            # -----------------------------------------------------------------
            # SUBPLOT 1: 4-SCENARIO FINANCIAL LABOR BUDGET MATRIX ($ vs ₫)
            # -----------------------------------------------------------------
            ax1.bar(x - width * 1.5, ent_human_cost, width, label='Enterprise Human', color='#c0392b', alpha=0.85)
            ax1.bar(x - width / 2, ent_ai_cost, width, label='Enterprise AI', color='#e74c3c', alpha=0.85)
            ax1.bar(x + width / 2, free_human_cost, width, label='Freelance Human', color='#27ae60', alpha=0.85)
            ax1.bar(x + width * 1.5, free_ai_cost, width, label='Freelance AI', color='#2ecc71', alpha=0.85)
            
            ax1.set_ylabel('Total Cost in USD ($)', fontsize=11, fontweight='bold')
            ax1.set_title('Labor Financial Budget Bounds', fontsize=11, pad=10, fontweight='bold')
            ax1.set_xticks(x)
            ax1.set_xticklabels(categories, fontsize=10)
            ax1.grid(axis='y', linestyle='--', alpha=0.3)
            ax1.legend(loc='upper left', frameon=True, facecolor='#f8f9fa')

            # CRITICAL FIX: Decouple get_ylim tuple to prevent the mathematical string sequence crash
            ax1_ymin, ax1_ymax = ax1.get_ylim()
            ax2 = ax1.twinx()
            ax2.set_ylabel('Equivalent Cost in VND (₫)', fontsize=11, fontweight='bold')
            ax2.set_ylim(ax1_ymin * exchange_rate, ax1_ymax * exchange_rate)
            ax2.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda val, loc: f"{int(val):,}"))

            # -----------------------------------------------------------------
            # SUBPLOT 2: NEWLY ADDED CLOUD INFRASTRUCTURE OPEX PROJECTIONS ($ vs ₫)
            # -----------------------------------------------------------------
            # CRITICAL FIX: Aligned width constraints to width/2 offsets to prevent bar overlapping anomalies
            ax3.bar(x - width / 2, ent_cloud_opex, width, label='Enterprise Cloud (GKE HA)', color='#8e44ad', alpha=0.85)
            ax3.bar(x + width / 2, free_cloud_opex, width, label='Freelance Cloud (VPS)', color='#2980b9', alpha=0.85)
            
            ax3.set_ylabel('Monthly Cloud OpEx in USD ($)', fontsize=11, fontweight='bold')
            ax3.set_title('Monthly Cloud Infrastructure OpEx', fontsize=11, pad=10, fontweight='bold')
            ax3.set_xticks(x)
            ax3.set_xticklabels(categories, fontsize=10)
            ax3.grid(axis='y', linestyle='--', alpha=0.3)
            ax3.legend(loc='upper left', frameon=True, facecolor='#f8f9fa')

            # Decouple ax3 ylim to apply currency conversion on the cloud infrastructure dashboard subplot
            ax3_ymin, ax3_ymax = ax3.get_ylim()
            ax4 = ax3.twinx()
            ax4.set_ylabel('Equivalent OpEx in VND (₫)', fontsize=11, fontweight='bold')
            ax4.set_ylim(ax3_ymin * exchange_rate, ax3_ymax * exchange_rate)
            ax4.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda val, loc: f"{int(val):,}"))

            # -----------------------------------------------------------------
            # SUBPLOT 3: 4-SCENARIO DELIVERY TIMELINE TRACKING (MONTHS)
            # -----------------------------------------------------------------
            ax5.bar(x - width * 1.5, ent_human_time, width, label='Enterprise Human', color='#2c3e50', alpha=0.9)
            ax5.bar(x - width / 2, ent_ai_time, width, label='Enterprise AI', color='#5d6d7e', alpha=0.8)
            ax5.bar(x + width / 2, free_human_time, width, label='Freelance Human', color='#16a085', alpha=0.9)
            ax5.bar(x + width * 1.5, free_ai_time, width, label='Freelance AI', color='#1abc9c', alpha=0.8)
            
            ax5.set_ylabel('Duration (Calendar Months)', fontsize=11, fontweight='bold')
            ax5.set_title('Delivery Timeline Projections', fontsize=11, pad=10, fontweight='bold')
            ax5.set_xticks(x)
            ax5.set_xticklabels(categories, fontsize=10)
            ax5.grid(axis='y', linestyle='--', alpha=0.3)
            ax5.legend(loc='upper left', frameon=True, facecolor='#f8f9fa')

            # 6. Clean layout margins and export the 3-panel sharp asset to disk destinations
            plt.tight_layout()
            makedirs(output_image_path)
            plt.savefig(output_image_path, bbox_inches='tight')
            plt.close()
            
            self.logger.info(f"[ 💾 SHARP CHART GENERATED ] 3-Panel Consolidated Governance chart exported to: {output_image_path}")
            
        except Exception as e:
            self.logger.warning(f"⚠️ Exception while generating pilot chart to file {output_image_path}: {str(e)}")

    # @override
    def clean_response(self, raw_response, **kwargs):
        return {
            "visualizations": self.__extract_mermaid_visualizations__(raw_response=raw_response),
            "metrics": self.__extract_metrics_and_plot_matplotlib_chart__(raw_response=raw_response)
        }

    # @override
    def process_communication(self, **kwargs):
        response_data = self.get_kwargs_by_key(key="raw_response", **kwargs)
        cleaned_response = self.get_kwargs_by_key(key="clean_response", **kwargs)
        if not response_data:
            raise RuntimeError("❌ Invalid AI raw response.")
        
        # export estimation as md files
        write_file(
            file=self.__storage_path__("storage_estimation", file=f"{self.project_name}/enterprise-estimation.md"),
            data=response_data
        )
        
        # write output file
        write_file(
            file=self.__output_storage_path__(storage_name="output_estimation", file=EST_RAW_FILE),
            data=response_data
        )
        
        # export visualizations
        visualizations = cleaned_response.get("visualizations", None) if cleaned_response else None
        if visualizations:
            for file, data in visualizations.items():
                write_file(
                    file=self.__storage_path__("storage_estimation", file=f"{self.project_name}/visualizations/{file}"),
                    data=data
                )
        else:
            self.logger.warning("⚠️ No any visualizations to process.")
        
        # export pilot chart
        metrics = cleaned_response.get("metrics", None) if cleaned_response else None
        if metrics:
            # to storage
            self.__generate_sharp_summary_chart_v2__(
                output_image_path=self.__storage_path__(storage_name="storage_estimation", file=f"{self.project_name}/{EST_CHART_FILE}"),
                metrics=metrics
            )
            
            # to output
            self.__generate_sharp_summary_chart_v2__(
                output_image_path=self.__output_storage_path__(storage_name="output_estimation", file=EST_CHART_FILE),
                metrics=metrics
            )
        else:
            self.logger.warning("⚠️ No any metrics to process.")


if __name__ == "__main__":
    def add_known_arguments(parser):
        parser.add_argument("--idea", type=str, help="Idea Identity / Project Name for searching")
        parser.add_argument("--buffer-ratio", type=float, default=1.5, help="Estimation with buffer ratio. Ex: 1.5")
        parser.add_argument("--language", type=str, help="Translate Estimation to language. Ex: Vietnamese, English, etc.")
    
    args, unknown_args = parse_args(
        description="👷 EnterpriseAutonomousProjectEstimatorAgent",
        parser_callback=add_known_arguments
    )
    EnterpriseAutonomousProjectEstimatorAgent(
        idea=args.idea,
        project=args.idea,
        language=args.language,
        buffer=args.buffer_ratio,
        **unknown_args
    ).execute()
