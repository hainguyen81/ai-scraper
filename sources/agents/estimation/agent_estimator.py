import sys
import re
import json
import argparse
from datetime import datetime

import urllib.parse
import requests
import matplotlib.pyplot as plt
import numpy as np

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from sources.agents.agent_helper import (
    write_file
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

DEFAULT_EST_LANGUAGE        = "English"


class EnterpriseAutonomousProjectEstimatorAgent(AbstractSubAgent):
    def __init__(self, **kwargs):
        super().__init__(agent_id='EnterpriseAutonomousProjectEstimator', **kwargs)
    
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
    
    def __extract_metrics_and_plot_matplotlib_chart__(self, raw_response):
        """
        Scans the AI response string in RAM, extracts the strict JSON metadata block,
        and dynamically passes the arrays into matplotlib to plot a local high-res chart.
        """
        # Extract ```json { ... } ``` at the end of AI response
        json_match = re.search(r'```json\s*(\{.*?\})\s*```', raw_response, re.DOTALL)
        if not json_match:
            self.logger.warn("⚠️ Metadata JSON block not found in AI response memory. Skipping chart plotting.")
            return None

        metrics_dict = None
        try:
            # map to JSON Python
            metrics_dict = json.loads(json_match.group(1))
        except Exception as json_err:
            self.logger.warn(f"⚠️ Failed to parse JSON RAM metrics object: {str(json_err)}")
        
        # extract information to debug
        exchange_rate = float(metrics_dict.get("exchange_rate", 0) if metrics_dict else 0)
        ent_cost_usd = list(metrics_dict.get("enterprise_cost_usd", []) if metrics_dict else [])
        free_cost_usd = list(metrics_dict.get("freelance_cost_usd", []) if metrics_dict else [])
        ent_time = list(metrics_dict.get("enterprise_months", []) if metrics_dict else [])
        free_time = list(metrics_dict.get("freelance_months", []) if metrics_dict else [])

        self.logger.debug(f"[ 📊 DATA EXTRACTED ] Live Exchange Rate Captured: 1 USD = {exchange_rate} VND")
        self.logger.debug(f"| Enterprise Costs: {ent_cost_usd} | Freelance Costs: {free_cost_usd}")
        self.logger.debug(f"| Enterprise Timelines: {ent_time} | Freelance Timelines: {free_time}")
        return metrics_dict
    
    def __extract_mermaid_visualizations__(self, raw_response):
        # Non-greedy regex mapping to sweep all markdown blocks bounded by mermaid tags
        mermaid_blocks = re.findall(r'```mermaid\s*(.*?)\s*```', raw_response, re.DOTALL)
        if not mermaid_blocks:
            self.logger.warn("⚠️ Zero functional mermaid visualization blocks detected inside the markdown body.")
        
        # Explicit fallback architectural name arrays
        self.logger.info(f"[ 📊 MERMAID ENGINE ] Intercepted {len(mermaid_blocks)} dynamic diagrams. Running vector compilation pipeline...")
        visualizations_data = {}
        
        if mermaid_blocks:
            chart_names = EST_VISUALIZATION_FILES
            for idx, code in enumerate(mermaid_blocks):
                clean_code = code.strip()
                
                # URL-encode the raw code content safe string character array payloads
                encoded_code = urllib.parse.quote(clean_code)
                render_url = f"https://mermaid.ink/svg/{encoded_code}"
                
                # Polymorphic file naming boundaries to protect extra diagrams generated by AI
                file_name = chart_names[idx] if idx < len(chart_names) else f"custom_governance_chart_{idx}.svg"
                
                self.logger.info(f"⏳ Querying dynamic vector graph data for layout file: {file_name}...")
                try:
                    custom_headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                    }
                    img_response = requests.get(render_url, headers=custom_headers, timeout=25)
                    if img_response.status_code == 200 and b"<svg" in img_response.content:
                        visualizations_data = {
                            **visualizations_data,
                            file_name: img_response.content.strip()
                        }
                        self.logger.info(f"💾 Highly-scalable vector graphic successfully extracted at index: {idx}")
                    else:
                        self.logger.warn(f"⚠️ Render pipeline returned invalid metadata block structure at index: {idx}")
                except Exception as net_err:
                    self.logger.warn(f"⚠️ Network exception or latency spike during chart extraction: {str(net_err)}")
        
        return visualizations_data
    
    def __generate_sharp_summary_chart_v2__(self, output_image_path, metrics):
        """
        Generates an ultra-sharp 4-Scenario comparison matrix chart 
        (Enterprise Human/AI vs Freelance Human/AI) using the dynamically extracted exchange rate.
        """
        if not metrics:
            self.logger.warn("⚠️ Invalid metrics JSON to generate chart. Skipping chart plotting.")
            return
        
        # extract metrics information
        exchange_rate = float(metrics.get("exchange_rate", 0))
        ent_cost_usd = list(metrics.get("enterprise_cost_usd", []))
        free_cost_usd = list(metrics.get("freelance_cost_usd", []))
        ent_time = list(metrics.get("enterprise_months", []))
        free_time = list(metrics.get("freelance_months", []))
        
        plt.rcParams['figure.dpi'] = 300
        plt.rcParams['text.color'] = '#2c3e50'
        
        fig, (ax1, ax3) = plt.subplots(1, 2, figsize=(16, 6))
        fig.suptitle(f'Project Estimation Summary Matrix (1 USD = {exchange_rate:,} VND)', fontsize=14, fontweight='bold', y=0.98)
        
        categories = ['Min', 'Max', 'Safe']
        x = np.arange(len(categories))
        width = 0.20 # Narrower bars to fit 4 scenarios
        
        # -----------------------------------------------------------------
        # SUBPLOT 1: 4-SCENARIO FINANCIAL BUDGET PROJECTION ($ vs ₫)
        # -----------------------------------------------------------------
        # Enterprise Bars
        ax1.bar(x - width*1.5, ent_cost_usd[0], width, label='Enterprise Human', color='#c0392b', alpha=0.85)
        ax1.bar(x - width/2, ent_cost_usd[1], width, label='Enterprise AI', color='#e74c3c', alpha=0.85)
        # Freelancer Bars
        ax1.bar(x + width/2, free_cost_usd[0], width, label='Freelance Human', color='#27ae60', alpha=0.85)
        ax1.bar(x + width*1.5, free_cost_usd[1], width, label='Freelance AI', color='#2ecc71', alpha=0.85)
        
        ax1.set_ylabel('Total Cost in USD ($)', fontsize=11, fontweight='bold')
        ax1.set_title('Financial Budget Bounds (Corporate vs Freelance)', fontsize=11, pad=10, fontweight='bold')
        ax1.set_xticks(x)
        ax1.set_xticklabels(categories, fontsize=10)
        ax1.grid(axis='y', linestyle='--', alpha=0.3)
        ax1.legend(loc='upper left', frameon=True, facecolor='#f8f9fa')
        
        # Dual-Axis for VND Representation
        ax2 = ax1.twinx()
        ax2.set_ylabel('Equivalent Cost in VND (₫)', fontsize=11, fontweight='bold')
        ax2.set_ylim(ax1.get_ylim() * exchange_rate, ax1.get_ylim() * exchange_rate)
        ax2.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda val, loc: f"{int(val):,}"))

        # -----------------------------------------------------------------
        # SUBPLOT 2: TIMELINE DURATION COMPARISON (MONTHS)
        # -----------------------------------------------------------------
        ax3.bar(x - width, ent_time, width*2, label='Enterprise Delivery', color='#34495e', alpha=0.9)
        ax3.bar(x + width, free_time, width*2, label='Freelance Delivery', color='#3498db', alpha=0.9)
        ax3.set_ylabel('Duration (Calendar Months)', fontsize=11, fontweight='bold')
        ax3.set_title('Delivery Timeline Projections', fontsize=11, pad=10, fontweight='bold')
        ax3.set_xticks(x)
        ax3.set_xticklabels(categories, fontsize=10)
        ax3.grid(axis='y', linestyle='--', alpha=0.3)
        ax3.legend(loc='upper left', frameon=True, facecolor='#f8f9fa')
        
        plt.tight_layout()
        output_image_path.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(output_image_path, bbox_inches='tight')
        plt.close()
        self.logger.info(f"[ 💾 SHARP CHART GENERATED ] 4-Scenario Dual-Currency matrix exported to: {output_image_path}")
    
    # @override
    def clean_response(self, raw_response, **kwargs):
        return {
            **kwargs,
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
            self.logger.warn("⚠️ No any visualizations to process.")
        
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
                output_image_path=self.__storage_path__(storage_name="storage_estimation", file=EST_CHART_FILE),
                metrics=metrics
            )
        else:
            self.logger.warn("⚠️ No any metrics to process.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--idea", type=str, help="Idea Identity / Project Name for searching")
    parser.add_argument("--buffer-ratio", type=float, default=1.5, help="Estimation with buffer ratio. Ex: 1.5")
    parser.add_argument("--language", type=str, help="Translate Estimation to language. Ex: Vietnamese, English, etc.")
    args = parser.parse_args()
    EnterpriseAutonomousProjectEstimatorAgent(
        idea=args.idea,
        project=args.idea,
        language=args.language,
        buffer=args.buffer_ratio
    ).execute()
