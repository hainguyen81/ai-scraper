### 1. AI MODELS CONFIGURATION (CENTRALIZED JSON)
*   **`AI_MODELS_KEYS_JSON`**
    *   *Description:* 1 tệp JSON duy nhất chứa toàn bộ API Keys của các mô hình AI phục vụ cơ chế Failover.
    *   *Format to paste into GitHub Secrets:*
        ```json
        {
          "gemini-2.5-pro": "AIzaSyYourActualGoogleStudioApiKeyHere",
          "gemini-2.5-flash": "AIzaSyYourActualGoogleStudioApiKeyHere",
          "deepseek-coder": "sk-yourActualDeepSeekPlatformApiKeyHere",
          "gpt-4o-mini": "sk-proj-yourActualOpenAIApiKeyHere",
          "qwen-coder-32b-instruct": "gsk_yourActualGroqConsoleApiKeyHere"
        }
        ```



