# ==========================================
# FILE: ./marketing_pipeline/video_extractor.py
# DESCRIPTION: Enterprise Raw Multi-media Stream Fetcher for Manual Local Storage
# COMMENTS: Written in English as mandated
# ==========================================
import sys
import time
import requests

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from sources.agents.agent_helper import (
    exception_stacktrace,
    read_json_file,
    write_file,
    parse_args,
)

# super agent
from sources.agents.subagent_super import AbstractSubAgent

# ==============================================================================
# GLOBAL CONFIGURATION PATHS - CONFIG HERE TO CUSTOMIZE DIRECTORY STRUCTURE
# ==============================================================================
VIDEO_FETCHER_LOG_FILE          = "video-fetcher_log.md"
VIDEO_FETCHER_API_SECRETS_KEY   = "VIDEO_FETCHER_API_SECRETS_KEY"         


class EnterpriseRawVideoFetcher(AbstractSubAgent):
    def __init__(self, **kwargs):
        super().__init__(
            agent_id='EnterpriseRawVideoFetcher',
            agent_name='🎞️ EnterpriseRawVideoFetcher',
            **kwargs
        )
    
    def __project_marketing_scenes_video_file__(self):
        return self.__storage_path__(storage_name="storage_multimedia", file=f"{self.project_name}/marketing-video-creator.json")
    
    # @override
    def initialize_models(self):
        pass
    
    def agent_secrets_key(self) -> str:
        return VIDEO_FETCHER_API_SECRETS_KEY
    
    # @override
    def agent_log_file(self) -> str:
        return self.__output_storage_path__(storage_name="output_multimedia", file=VIDEO_FETCHER_LOG_FILE)
    
    # @override
    def system_prompt_template(self) -> str:
        pass
    
    # @override
    def user_prompt_template(self) -> str:
        pass
    
    # @override
    def __pre_execute__(self, **kwargs):
        # read scenes video file
        scenes_file = self.__project_marketing_scenes_video_file__()
        _, json_scenes = read_json_file(file_path=scenes_file)
        
        # not anything to publish, exit
        if not json_scenes or "storyboard_flow" not in json_scenes or len(json_scenes.get("storyboard_flow", [])) <= 0:
            self.logger.warning(f"⚠️ Not found MARKETING SCENES VIDEO file to process")
            sys.exit(0)
        
        # return merged new values
        return {
            **kwargs,
            "scenes": json_scenes.get("storyboard_flow", [])
        }
    
    def __trigger_video_generation_task__(self, api_key: str, base_url: str, scene_virtual_prompt: str) -> str:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "taskType": "text_to_video",
            "prompt": scene_virtual_prompt,
            "aspectRatio": "16:9",
            "duration": 5 # 5 seconds per structural scene block
        }
        
        # Executes native programmatic request dispatch loop
        response = requests.post(base_url, json=payload, headers=headers, timeout=120)
        return response.json()["taskId"]
    
    def __video_render_status_polling__(self, api_key: str, base_url: str, task_id: str) -> str:
        endpoint = f"{base_url}/{task_id}"
        headers = {"Authorization": f"Bearer {api_key}"}
        
        # Execute active polling loops until status switches to complete
        while True:
            response = requests.get(endpoint, headers=headers, timeout=120)
            status_data = response.json()
            if status_data.get("status") == "SUCCEEDED":
                return status_data.get("assetUrl")
            elif status_data.get("status") == "FAILED":
                raise RuntimeError(f"[ERROR] Remote cloud render pipeline crashed for task: {task_id}")
            time.sleep(5) # Wait 5 seconds between status verification check beats
    
    def __render_video_scene__(self, api_key: str, base_url: str, scene: dict) -> bytes:
        scene = scene or {}
        scene_id = scene.get("scene_id")
        scene_visual_prompt = scene.get("visual_description")
        self.logger.info(f"[PROCESS] Spawning render task for Scene {scene_id}")
        
        # Step 1: Dispatch text-to-video prompt to cloud AI engine
        task_id = self.__trigger_video_generation_task__(
            api_key=api_key,
            base_url=base_url,
            scene_virtual_prompt=scene_visual_prompt
        )
        
        # Step 2: Poll and grab the raw CDN download URL link string
        video_download_url = self.__video_render_status_polling__(
            api_key=api_key,
            base_url=base_url,
            task_id=task_id
        )
        
        # Step 3: Stream and capture the pure raw video binary bytes from the network server
        self.logger.info(f"[DOWNLOAD] Pulling video bytes data from endpoint: {video_download_url}")
        raw_video_response = requests.get(video_download_url, stream=True, timeout=120)
        if raw_video_response.status_code == 200:
            return (scene_id, raw_video_response.content)
        else:
            raise ConnectionError(f"[CRITICAL] Network buffer failed fetching bytes. Status: {raw_video_response.status_code}")
    
    # @override
    def __execute__(self, **kwargs):
        scenes = self.get_kwargs_by_key(key="scenes", **kwargs)
        if not scenes:
            raise RuntimeError("❌ Invalid scenes data: No scenes to process")
        
        # loop to try for each video API
        rendered_videos = []
        for api in self.secrets:
            # parse API configuration from secrets
            api_key = api.get("api_key")
            base_url = api.get("base_url")
            if not api_key or not base_url:
                self.logger.warning(f"⚠️ Invalid API configuration: Missing api_key or base_url")
                continue
            
            # call API to rendering video scenes
            try:
                for scene in scenes:
                    # render scene video and get raw bytes
                    scene_id, raw_video_bytes = self.__render_video_scene__(
                        api_key=api_key,
                        base_url=base_url,
                        scene=scene
                    )
                    
                    # write raw video bytes to local storage
                    video_file = self.__storage_path__(storage_name="storage_multimedia", file=f"{self.project_name}/scene-{scene_id}.mp4")
                    write_file(
                        file=video_file,
                        data=raw_video_bytes
                    )
                    rendered_videos.append(scene_id)
                    self.logger.info(f"[SUCCESS] Scene {scene_id} video fetched and stored at: {video_file}")
            except Exception as e:
                self.logger.error(f"❌ Error processing Scene {scene.get('scene_id')}: {exception_stacktrace(e)}")
            
            # remove rendered videos out of scenes list to avoid reprocessing
            scenes = [scene for scene in scenes if scene.get("scene_id") not in rendered_videos]
            
            # out of scenes
            if len(scenes) <= 0:
                break
    
    # @override
    def process_communication(self, **kwargs):
        pass


if __name__ == "__main__":
    def add_known_arguments(parser):
        parser.add_argument("--idea", type=str, help="Idea Identity / Project Name for searching")
    
    args, unknown_args = parse_args(
        description="🎞️ EnterpriseRawVideoFetcher",
        parser_callback=add_known_arguments
    )
    EnterpriseRawVideoFetcher(
        idea=args.idea,
        project=args.idea,
        **unknown_args
    ).execute()
