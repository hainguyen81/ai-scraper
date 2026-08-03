# ==========================================
# FILE: ./marketing_pipeline/schemas.py
# DESCRIPTION: Enterprise Data Structures for OpenAI Response Format
# COMMENTS: Written in English as mandated
# ==========================================
from pydantic import BaseModel, Field
from typing import List, Dict

class CustomerSegment(BaseModel):
    segment_name: str = Field(..., description="Target demographic name")
    essential_needs: List[str] = Field(..., description="Core pain points and essential needs of this segment based on BA data")
    approach_strategy: List[str] = Field(..., description="Actionable technical or business approach strategy using SA blueprint capabilities")

class MarketingPlanPayload(BaseModel):
    project_name: str = Field(..., description="The name of the target project")
    target_segments: List[CustomerSegment] = Field(..., description="Detailed list of customer segments, needs, and approaches")
    key_messages: Dict[str, str] = Field(..., description="Platform-specific core marketing messages mapped to business value")
    weekly_schedule: List[Dict[str, str]] = Field(..., description="Step-by-step editorial calendar layout")
    seo_keywords: List[str] = Field(..., description="Target high-intent SEO keywords based on market demand")

class ContentDraft(BaseModel):
    platform: str = Field(..., description="Target social network platform like X, Facebook, LinkedIn")
    content_body: str = Field(..., description="The fully generated human-readable content with strictly escaped URLs")
    tags: List[str] = Field(..., description="List of highly relevant contextual hashtags")

class ContentDraftList(BaseModel):
    drafts: List[ContentDraft]

class VideoStoryboardRow(BaseModel):
    scene_id: int = Field(..., description="Sequential index number of the scene")
    visual_description: str = Field(..., description="Cinematic or UI visual cues describing what appears on screen")
    voiceover_script: str = Field(..., description="The exact high-impact narration text to be spoken")
    technical_overlay: str = Field(..., description="Raw Technical English tokens, code blocks, or architecture flows to display")

class VideoStoryboard(BaseModel):
    format_type: str = Field(..., description="Shorts, Reels, or Long-form configuration")
    storyboard_flow: List[VideoStoryboardRow] = Field(..., description="Chronological sequence of video production rows")

class ComplianceReport(BaseModel):
    status: str = Field(..., description="Must be exactly 'APPROVED_VAULT' or 'REJECTED_NEED_FIX'")
    issue_analysis: str = Field(..., description="Deep analysis of any detected out-of-bounds fluff, unescaped links, or hallucination")
    fix_directives: List[str] = Field(..., description="Exact code-level change directives with clear anchor points if rejected")

class ExecutionPublishLog(BaseModel):
    status: str = Field(..., description="API execution status like SUCCESS or FAILED")
    platform_post_ids: Dict[str, str] = Field(..., description="Mapping of platform names to their respective live API deployment IDs")
    timestamp: str = Field(..., description="System timestamp of the dispatch execution")

class EngagementResponsePayload(BaseModel):
    sentiment_score: str = Field(..., description="Evaluated tone classification: POSITIVE, NEUTRAL, CRITICAL_TOXIC")
    trigger_crisis_alarm: bool = Field(..., description="Set to True if comment is highly toxic, malicious, or damaging")
    response_body: str = Field(..., description="Professional answer strictly anchored to project realities. Empty string if crisis triggered.")
