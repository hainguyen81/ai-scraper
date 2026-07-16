# Global Prompt:


        Analyze the attached project requirements. Build the GLOBAL PROJECT CONTEXT for 'test-ai-architecture'.
        
        --- RAW REQUIREMENTS ---
        ## Project Name: membership-hub

*	**Requirements:**
	- Project vừa web để quản lý, vừa mobile để học viên xài.
	- Project này xây dựng backend bằng quarkus, kafka, postgres, có thể scalable, build docker image, deploy GCP, GKE.
	- Hỗ trợ xác thực internal bằng email password, hoặc qua firebase, google, facebook. quản lý user internal lẫn login qua xác thực với các bên bên trên.
	- Project này quản lý các học viên của trung tâm bất kỳ, dùng được cho nhiều trung tâm 1 lúc được.
	- Các học viên của trung tâm khi tới học sẽ điểm danh qua QR. Điểm danh sẽ đánh dấu ngày đó học viên có đi học. Cho dù điểm danh nhiều lần cũng không vấn đề và chỉ xem như đã điểm danh ngày hôm đó.
	- Sau khi điểm danh sẽ hiển thị thẻ học viên còn bao nhiêu ngày hiệu lực như kiểu trừ dần ngày tập gym chẳng hạn.
	- Đồng thời lúc đó gửi tin nhắn qua số đt zalo của học viên và nhóm zalo có học viên đó tham gia, và cả notification của app mobile trên đt học viên.
	- App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android.
	- Project này có phần SEO đa ngôn ngữ cho cả web, app mobile.
	- Detect default locale ngôn ngữ nếu user đã chọn trước đó thì dùng nó, không thì dùng locale từ browser hay mobile.

        --- END REQUIREMENTS ---

        Your output MUST follow this exact structure:
        ## GLOBAL PROJECT CONTEXT: test-ai-architecture
        #### 1. Executive Summary & Tech Stack Blueprint
        #### 2. Global Guardrails & Enterprise Compliance Standards
        #### 3. Standardized Sub-Agent Persona Definitions (Manager, Coder, Tester, Reviewer, Docker, Deployer)
        #### 4. Multi-Phase Segmentation Strategy Overview (Plan exactly 5 phases)
        

# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```json
Error code: 400 - {'error': {'message': 'The model `deepseek-r1-distill-qwen-32b` has been decommissioned and is no longer supported. Please refer to https://console.groq.com/docs/deprecations for a recommendation on which model to use instead.', 'type': 'invalid_request_error', 'code': 'model_decommissioned'}}
```

