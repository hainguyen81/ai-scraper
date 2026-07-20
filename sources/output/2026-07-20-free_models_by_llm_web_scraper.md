# Prompt Instruction:

Analyze the text corpus provided and isolate all AI model providers offering a free tier API. Extract the provider name, api base URL, precise model ID, and context window tokens. Return the data strictly structured as a JSON object containing a list named 'free_providers'. Each item in the list must exactly include: 1. 'provider_name' (string) 2. 'api_base_url' (string) 3. 'model_name' (string) 4. 'context_window_tokens' (integer, default to 128000 if not mentioned).

# Raw Response:

```json
{
    "id": "gen-1784523148-x4H8tXp0Yg9ldzDmBH2J",
    "choices": [
        {
            "finish_reason": "stop",
            "index": 0,
            "logprobs": null,
            "message": {
                "content": "{\n  \"free_providers\": [\n    {\n      \"provider_name\": \"NVIDIA NIM\",\n      \"api_base_url\": \"https://integrate.api.nvidia.com/v1\",\n      \"model_name\": \"z-ai/glm-5.2\",\n      \"context_window_tokens\": 1000000\n    },\n    {\n      \"provider_name\": \"ModelScope\",\n      \"api_base_url\": \"https://api-inference.modelscope.cn/v1\",\n      \"model_name\": \"MiniMax/MiniMax-M2.5\",\n      \"context_window_tokens\": 204000\n    },\n    {\n      \"provider_name\": \"Cloudflare Workers AI\",\n      \"api_base_url\": \"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run\",\n      \"model_name\": \"@cf/meta/llama-3.3-70b-instruct-fp8-fast\",\n      \"context_window_tokens\": 131000\n    },\n    {\n      \"provider_name\": \"OpenRouter\",\n      \"api_base_url\": \"https://openrouter.ai/api/v1\",\n      \"model_name\": \"tencent/hy3:free\",\n      \"context_window_tokens\": 262000\n    },\n    {\n      \"provider_name\": \"GitHub Models\",\n      \"api_base_url\": \"https://models.github.ai/inference\",\n      \"model_name\": \"Phi-4\",\n      \"context_window_tokens\": 131000\n    },\n    {\n      \"provider_name\": \"Groq\",\n      \"api_base_url\": \"https://api.groq.com/openai/v1\",\n      \"model_name\": \"moonshotai/kimi-k2-instruct\",\n      \"context_window_tokens\": 131000\n    },\n    {\n      \"provider_name\": \"Google Gemini\",\n      \"api_base_url\": \"https://generativelanguage.googleapis.com/v1beta\",\n      \"model_name\": \"gemini-3.5-flash\",\n      \"context_window_tokens\": 1000000\n    },\n    {\n      \"provider_name\": \"OVHcloud AI Endpoints\",\n      \"api_base_url\": \"https://oai.endpoints.kepler.ai.cloud.ovh.net/v1\",\n      \"model_name\": \"qwen3.5-397b-a17b\",\n      \"context_window_tokens\": 131000\n    },\n    {\n      \"provider_name\": \"Mistral AI\",\n      \"api_base_url\": \"https://api.mistral.ai/v1\",\n      \"model_name\": \"mistral-medium-3-5-128b\",\n      \"context_window_tokens\": 256000\n    },\n    {\n      \"provider_name\": \"LLM7.io\",\n      \"api_base_url\": \"https://api.llm7.io/v1\",\n      \"model_name\": \"deepseek-r1-0528\",\n      \"context_window_tokens\": 131000\n    },\n    {\n      \"provider_name\": \"Cerebras\",\n      \"api_base_url\": \"https://api.cerebras.ai/v1\",\n      \"model_name\": \"gpt-oss-120b\",\n      \"context_window_tokens\": 128000\n    },\n    {\n      \"provider_name\": \"Cohere\",\n      \"api_base_url\": \"https://api.cohere.com/v2\",\n      \"model_name\": \"command-a-111b\",\n      \"context_window_tokens\": 256000\n    },\n    {\n      \"provider_name\": \"Ollama Cloud\",\n      \"api_base_url\": \"https://api.ollama.com\",\n      \"model_name\": \"gpt-oss-120b-cloud\",\n      \"context_window_tokens\": 128000\n    },\n    {\n      \"provider_name\": \"OpenCode Zen\",\n      \"api_base_url\": \"https://opencode.ai/zen/v1\",\n      \"model_name\": \"deepseek-v4-flash-free\",\n      \"context_window_tokens\": 1000000\n    },\n    {\n      \"provider_name\": \"Agnes AI\",\n      \"api_base_url\": \"https://apihub.agnes-ai.com/v1\",\n      \"model_name\": \"agnes-1.5-flash\",\n      \"context_window_tokens\": 256000\n    },\n    {\n      \"provider_name\": \"Aion Labs\",\n      \"api_base_url\": \"https://api.aionlabs.ai/v1\",\n      \"model_name\": \"aion-2-5\",\n      \"context_window_tokens\": 128000\n    },\n    {\n      \"provider_name\": \"Hugging Face\",\n      \"api_base_url\": \"https://router.huggingface.co/v1\",\n      \"model_name\": \"meta-llama-3-1-8b-instruct\",\n      \"context_window_tokens\": 128000\n    },\n    {\n      \"provider_name\": \"Kilo Code\",\n      \"api_base_url\": \"https://api.kilo.ai/api/gateway\",\n      \"model_name\": \"x-ai-grok-code-fast-1-free\",\n      \"context_window_tokens\": 256000\n    },\n    {\n      \"provider_name\": \"Alibaba Cloud Model Studio\",\n      \"api_base_url\": \"https://dashscope-intl.aliyuncs.com/compatible-mode/v1\",\n      \"model_name\": \"qwen3-plus\",\n      \"context_window_tokens\": 1000000\n    },\n    {\n      \"provider_name\": \"Z AI (Zhipu AI)\",\n      \"api_base_url\": \"https://open.bigmodel.cn/api/paas/v4\",\n      \"model_name\": \"glm-4.7\",\n      \"context_window_tokens\": 200000\n    },\n    {\n      \"provider_name\": \"SambaNova\",\n      \"api_base_url\": \"https://api.sambanova.ai/v1\",\n      \"model_name\": \"deepseek-v3-1\",\n      \"context_window_tokens\": 128000\n    },\n    {\n      \"provider_name\": \"SiliconFlow\",\n      \"api_base_url\": \"https://api.siliconflow.cn/v1\",\n      \"model_name\": \"deepseek-ai-deepseek-r1-distill-qwen-7b\",\n      \"context_window_tokens\": 131000\n    },\n    {\n      \"provider_name\": \"xAI\",\n      \"api_base_url\": \"https://api.x.ai/v1\",\n      \"model_name\": \"grok-3-mini\",\n      \"context_window_tokens\": 131000\n    },\n    {\n      \"provider_name\": \"Chutes.ai\",\n      \"api_base_url\": \"https://api.chutes.ai/v1\",\n      \"model_name\": \"deepseek-ai/DeepSeek-R1\",\n      \"context_window_tokens\": 131000\n    },\n    {\n      \"provider_name\": \"Glhf.chat\",\n      \"api_base_url\": \"https://glhf.chat/api/openai/v1\",\n      \"model_name\": \"meta-llama/Meta-Llama-3.1-70B-Instruct\",\n      \"context_window_tokens\": 131000\n    },\n    {\n      \"provider_name\": \"Grok (xAI)\",\n      \"api_base_url\": \"https://api.x.ai/v1\",\n      \"model_name\": \"grok-2\",\n      \"context_window_tokens\": 131000\n    },\n    {\n      \"provider_name\": \"AI21 Labs\",\n      \"api_base_url\": \"https://api.ai21.com/studio/v1\",\n      \"model_name\": \"jamba-large-1-7\",\n      \"context_window_tokens\": 256000\n    },\n    {\n      \"provider_name\": \"DeepSeek\",\n      \"api_base_url\": \"https://api.deepseek.com/v1\",\n      \"model_name\": \"deepseek-chat-v3-2\",\n      \"context_window_tokens\": 128000\n    },\n    {\n      \"provider_name\": \"Nscale\",\n      \"api_base_url\": \"https://inference.api.nscale.com/v1\",\n      \"model_name\": \"llama-3-3-70b-instruct\",\n      \"context_window_tokens\": 128000\n    },\n    {\n      \"provider_name\": \"Nebius\",\n      \"api_base_url\": \"https://api.studio.nebius.com/v1\",\n      \"model_name\": \"qwen3-235b-a22b\",\n      \"context_window_tokens\": 128000\n    }\n  ]\n}",
                "refusal": null,
                "role": "assistant",
                "annotations": null,
                "audio": null,
                "function_call": null,
                "tool_calls": null
            }
        }
    ],
    "created": 1784523148,
    "model": "tencent/hy3:free",
    "object": "chat.completion",
    "moderation": null,
    "service_tier": null,
    "system_fingerprint": null,
    "usage": {
        "completion_tokens": 1859,
        "prompt_tokens": 5569,
        "total_tokens": 7428,
        "completion_tokens_details": {
            "accepted_prediction_tokens": null,
            "audio_tokens": 0,
            "reasoning_tokens": 0,
            "rejected_prediction_tokens": null
        },
        "prompt_tokens_details": {
            "audio_tokens": 0,
            "cache_write_tokens": 0,
            "cached_tokens": 0
        }
    },
    "_request_id": null
}
```

