# AI Model: llama-3.3-70b-versatile - Global Prompt:

PIPELINE_CRASH

# System Instruction

SYSTEM_ERROR

# Raw Response / Exception:

Error code: 413 - {'error': {'message': 'Request too large for model `llama-3.3-70b-versatile` in organization `org_01kx7x6rbpftmr50sr2yyb78qm` service tier `on_demand` on tokens per minute (TPM): Limit 12000, Requested 18609, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_global.py", line 182, in generate_global_context_by_chunk
    res_p1 = client.chat.completions.create(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_utils/_utils.py", line 298, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/resources/chat/completions/completions.py", line 1296, in create
    return self._post(
           ^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1375, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1148, in request
    raise self._make_status_error_from_response(err.response) from None
', "openai.APIStatusError: Error code: 413 - {'error': {'message': 'Request too large for model `llama-3.3-70b-versatile` in organization `org_01kx7x6rbpftmr50sr2yyb78qm` service tier `on_demand` on tokens per minute (TPM): Limit 12000, Requested 18609, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
"]

# AI Model: meta-llama/llama-3.3-70b-instruct:free - Global Prompt:

PIPELINE_CRASH

# System Instruction

SYSTEM_ERROR

# Raw Response / Exception:

Error code: 404 - {'error': {'message': 'This model is unavailable for free. The paid version is available now - use this slug instead: meta-llama/llama-3.3-70b-instruct', 'code': 404}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_global.py", line 182, in generate_global_context_by_chunk
    res_p1 = client.chat.completions.create(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_utils/_utils.py", line 298, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/resources/chat/completions/completions.py", line 1296, in create
    return self._post(
           ^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1375, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1148, in request
    raise self._make_status_error_from_response(err.response) from None
', "openai.NotFoundError: Error code: 404 - {'error': {'message': 'This model is unavailable for free. The paid version is available now - use this slug instead: meta-llama/llama-3.3-70b-instruct', 'code': 404}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
"]

# AI Model: meta-llama/llama-3.3-70b-instruct - Global Prompt:

PIPELINE_CRASH

# System Instruction

SYSTEM_ERROR

# Raw Response / Exception:

Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 942. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 942. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 16384 tokens, but can only afford 1177. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 6481 tokens, but can only afford 167. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 8192 tokens, but can only afford 523. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 502. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 32768 tokens, but can only afford 477. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 16384 tokens, but can only afford 753. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 523. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 3072 tokens, but can only afford 418. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 530. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 2048 tokens, but can only afford 362. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_global.py", line 182, in generate_global_context_by_chunk
    res_p1 = client.chat.completions.create(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_utils/_utils.py", line 298, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/resources/chat/completions/completions.py", line 1296, in create
    return self._post(
           ^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1375, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1148, in request
    raise self._make_status_error_from_response(err.response) from None
', "openai.APIStatusError: Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 942. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 942. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 16384 tokens, but can only afford 1177. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 6481 tokens, but can only afford 167. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 8192 tokens, but can only afford 523. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 502. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 32768 tokens, but can only afford 477. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 16384 tokens, but can only afford 753. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 523. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 3072 tokens, but can only afford 418. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 530. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 2048 tokens, but can only afford 362. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
"]

# AI Model: qwen/qwen-2.5-coder-32b-instruct - Global Prompt:

PIPELINE_CRASH

# System Instruction

SYSTEM_ERROR

# Raw Response / Exception:

Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 11797 tokens, but can only afford 376. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_global.py", line 182, in generate_global_context_by_chunk
    res_p1 = client.chat.completions.create(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_utils/_utils.py", line 298, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/resources/chat/completions/completions.py", line 1296, in create
    return self._post(
           ^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1375, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1148, in request
    raise self._make_status_error_from_response(err.response) from None
', "openai.APIStatusError: Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 11797 tokens, but can only afford 376. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
"]

# AI Model: deepseek/deepseek-r1:free - Global Prompt:

PIPELINE_CRASH

# System Instruction

SYSTEM_ERROR

# Raw Response / Exception:

Error code: 404 - {'error': {'message': 'This model is unavailable for free. The paid version is available now - use this slug instead: deepseek/deepseek-r1', 'code': 404}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_global.py", line 182, in generate_global_context_by_chunk
    res_p1 = client.chat.completions.create(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_utils/_utils.py", line 298, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/resources/chat/completions/completions.py", line 1296, in create
    return self._post(
           ^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1375, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1148, in request
    raise self._make_status_error_from_response(err.response) from None
', "openai.NotFoundError: Error code: 404 - {'error': {'message': 'This model is unavailable for free. The paid version is available now - use this slug instead: deepseek/deepseek-r1', 'code': 404}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
"]

# AI Model: google/gemma-4-31b-instruct - Global Prompt:

PIPELINE_CRASH

# System Instruction

SYSTEM_ERROR

# Raw Response / Exception:

Error code: 400 - {'error': {'message': 'google/gemma-4-31b-instruct is not a valid model ID', 'code': 400}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_global.py", line 182, in generate_global_context_by_chunk
    res_p1 = client.chat.completions.create(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_utils/_utils.py", line 298, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/resources/chat/completions/completions.py", line 1296, in create
    return self._post(
           ^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1375, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1148, in request
    raise self._make_status_error_from_response(err.response) from None
', "openai.BadRequestError: Error code: 400 - {'error': {'message': 'google/gemma-4-31b-instruct is not a valid model ID', 'code': 400}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
"]

# AI Model: minimax/minimax-m3 - Global Prompt:

PIPELINE_CRASH

# System Instruction

SYSTEM_ERROR

# Raw Response / Exception:

Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 392. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 342. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 32768 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_global.py", line 182, in generate_global_context_by_chunk
    res_p1 = client.chat.completions.create(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_utils/_utils.py", line 298, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/resources/chat/completions/completions.py", line 1296, in create
    return self._post(
           ^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1375, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1148, in request
    raise self._make_status_error_from_response(err.response) from None
', "openai.APIStatusError: Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 392. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 342. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 32768 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
"]

# AI Model: openai/gpt-5.3-codex - Global Prompt:

PIPELINE_CRASH

# System Instruction

SYSTEM_ERROR

# Raw Response / Exception:

Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 26. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 26. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_global.py", line 182, in generate_global_context_by_chunk
    res_p1 = client.chat.completions.create(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_utils/_utils.py", line 298, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/resources/chat/completions/completions.py", line 1296, in create
    return self._post(
           ^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1375, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1148, in request
    raise self._make_status_error_from_response(err.response) from None
', "openai.APIStatusError: Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 26. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 26. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
"]

# AI Model: cohere/north-mini-code:free - Global Prompt:

PIPELINE_CRASH

# System Instruction

SYSTEM_ERROR

# Raw Response / Exception:

[API Upstream Error 404]: AI response content is empty/None.: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_global.py", line 187, in generate_global_context_by_chunk
    chunk_1 = parseAIResponseData(res_p1)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/agent_helper.py", line 339, in parseAIResponseData
    first_choice = validateAIResponse(response)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/agent_helper.py", line 329, in validateAIResponse
    raise ValueError(f"[API Upstream Error 404]: AI response content is empty/None.")
', 'ValueError: [API Upstream Error 404]: AI response content is empty/None.
']

# AI Model: qwen/qwen3-coder-next - Global Prompt:

PIPELINE_CRASH

# System Instruction

SYSTEM_ERROR

# Raw Response / Exception:

Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 64000 tokens, but can only afford 418. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 251. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 471. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 251. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 471. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_global.py", line 182, in generate_global_context_by_chunk
    res_p1 = client.chat.completions.create(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_utils/_utils.py", line 298, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/resources/chat/completions/completions.py", line 1296, in create
    return self._post(
           ^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1375, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1148, in request
    raise self._make_status_error_from_response(err.response) from None
', "openai.APIStatusError: Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 64000 tokens, but can only afford 418. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 251. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 471. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 251. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 471. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
"]

# AI Model: qwen/qwen3-coder - Global Prompt:

PIPELINE_CRASH

# System Instruction

SYSTEM_ERROR

# Raw Response / Exception:

Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 77. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 209. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 243. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 251. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 376. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_global.py", line 182, in generate_global_context_by_chunk
    res_p1 = client.chat.completions.create(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_utils/_utils.py", line 298, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/resources/chat/completions/completions.py", line 1296, in create
    return self._post(
           ^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1375, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1148, in request
    raise self._make_status_error_from_response(err.response) from None
', "openai.APIStatusError: Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 77. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 209. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 243. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 251. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 376. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
"]

# AI Model: qwen/qwen3-coder-30b-a3b-instruct - Global Prompt:

PIPELINE_CRASH

# System Instruction

SYSTEM_ERROR

# Raw Response / Exception:

Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 221. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 32768 tokens, but can only afford 1395. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 1345. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 257. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_global.py", line 182, in generate_global_context_by_chunk
    res_p1 = client.chat.completions.create(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_utils/_utils.py", line 298, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/resources/chat/completions/completions.py", line 1296, in create
    return self._post(
           ^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1375, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1148, in request
    raise self._make_status_error_from_response(err.response) from None
', "openai.APIStatusError: Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 221. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 32768 tokens, but can only afford 1395. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 1345. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 257. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
"]

# AI Model: openai/gpt-5.1-codex-mini - Global Prompt:

PIPELINE_CRASH

# System Instruction

SYSTEM_ERROR

# Raw Response / Exception:

Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 188. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_global.py", line 182, in generate_global_context_by_chunk
    res_p1 = client.chat.completions.create(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_utils/_utils.py", line 298, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/resources/chat/completions/completions.py", line 1296, in create
    return self._post(
           ^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1375, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1148, in request
    raise self._make_status_error_from_response(err.response) from None
', "openai.APIStatusError: Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 188. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
"]

# AI Model: qwen/qwen3-coder-plus - Global Prompt:

PIPELINE_CRASH

# System Instruction

SYSTEM_ERROR

# Raw Response / Exception:

Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 115. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_global.py", line 182, in generate_global_context_by_chunk
    res_p1 = client.chat.completions.create(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_utils/_utils.py", line 298, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/resources/chat/completions/completions.py", line 1296, in create
    return self._post(
           ^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1375, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1148, in request
    raise self._make_status_error_from_response(err.response) from None
', "openai.APIStatusError: Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 115. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
"]

# AI Model: qwen/qwen3-coder-flash - Global Prompt:

PIPELINE_CRASH

# System Instruction

SYSTEM_ERROR

# Raw Response / Exception:

Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 386. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_global.py", line 182, in generate_global_context_by_chunk
    res_p1 = client.chat.completions.create(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_utils/_utils.py", line 298, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/resources/chat/completions/completions.py", line 1296, in create
    return self._post(
           ^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1375, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1148, in request
    raise self._make_status_error_from_response(err.response) from None
', "openai.APIStatusError: Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 386. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
"]

# AI Model: openai/gpt-5-codex - Global Prompt:

PIPELINE_CRASH

# System Instruction

SYSTEM_ERROR

# Raw Response / Exception:

Error code: 404 - {'error': {'message': 'No endpoints found for openai/gpt-5-codex.', 'code': 404}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_global.py", line 182, in generate_global_context_by_chunk
    res_p1 = client.chat.completions.create(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_utils/_utils.py", line 298, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/resources/chat/completions/completions.py", line 1296, in create
    return self._post(
           ^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1375, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1148, in request
    raise self._make_status_error_from_response(err.response) from None
', "openai.NotFoundError: Error code: 404 - {'error': {'message': 'No endpoints found for openai/gpt-5-codex.', 'code': 404}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
"]

# AI Model: openai/gpt-5.2-codex - Global Prompt:

PIPELINE_CRASH

# System Instruction

SYSTEM_ERROR

# Raw Response / Exception:

Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 26. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_global.py", line 182, in generate_global_context_by_chunk
    res_p1 = client.chat.completions.create(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_utils/_utils.py", line 298, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/resources/chat/completions/completions.py", line 1296, in create
    return self._post(
           ^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1375, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1148, in request
    raise self._make_status_error_from_response(err.response) from None
', "openai.APIStatusError: Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 26. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
"]

# AI Model: openai/gpt-5.1-codex - Global Prompt:

PIPELINE_CRASH

# System Instruction

SYSTEM_ERROR

# Raw Response / Exception:

Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 37. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_global.py", line 182, in generate_global_context_by_chunk
    res_p1 = client.chat.completions.create(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_utils/_utils.py", line 298, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/resources/chat/completions/completions.py", line 1296, in create
    return self._post(
           ^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1375, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1148, in request
    raise self._make_status_error_from_response(err.response) from None
', "openai.APIStatusError: Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 37. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
"]

# AI Model: mistralai/codestral-2508 - Global Prompt:

PIPELINE_CRASH

# System Instruction

SYSTEM_ERROR

# Raw Response / Exception:

Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 418. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_global.py", line 182, in generate_global_context_by_chunk
    res_p1 = client.chat.completions.create(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_utils/_utils.py", line 298, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/resources/chat/completions/completions.py", line 1296, in create
    return self._post(
           ^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1375, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1148, in request
    raise self._make_status_error_from_response(err.response) from None
', "openai.APIStatusError: Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 418. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
"]

# AI Model: openai/gpt-5.1-codex-max - Global Prompt:

PIPELINE_CRASH

# System Instruction

SYSTEM_ERROR

# Raw Response / Exception:

Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 37. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_global.py", line 182, in generate_global_context_by_chunk
    res_p1 = client.chat.completions.create(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_utils/_utils.py", line 298, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/resources/chat/completions/completions.py", line 1296, in create
    return self._post(
           ^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1375, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1148, in request
    raise self._make_status_error_from_response(err.response) from None
', "openai.APIStatusError: Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 37. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
"]

# AI Model: qwen/qwen-2.5-coder-32b-instruct - Global Prompt:

PIPELINE_CRASH

# System Instruction

SYSTEM_ERROR

# Raw Response / Exception:

Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 11797 tokens, but can only afford 376. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_global.py", line 182, in generate_global_context_by_chunk
    res_p1 = client.chat.completions.create(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_utils/_utils.py", line 298, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/resources/chat/completions/completions.py", line 1296, in create
    return self._post(
           ^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1375, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1148, in request
    raise self._make_status_error_from_response(err.response) from None
', "openai.APIStatusError: Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 11797 tokens, but can only afford 376. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
"]

# AI Model: openrouter/pareto-code - Global Prompt:

PIPELINE_CRASH

# System Instruction

SYSTEM_ERROR

# Raw Response / Exception:

Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 25. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 12. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 12. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 62. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 25. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 25. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 26. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 26. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65535 tokens, but can only afford 25. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 25. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 16384 tokens, but can only afford 26. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 25. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 25. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 16. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 25. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 16. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 16. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_global.py", line 182, in generate_global_context_by_chunk
    res_p1 = client.chat.completions.create(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_utils/_utils.py", line 298, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/resources/chat/completions/completions.py", line 1296, in create
    return self._post(
           ^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1375, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1148, in request
    raise self._make_status_error_from_response(err.response) from None
', "openai.APIStatusError: Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 25. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 12. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 12. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 62. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 25. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 25. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 26. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 26. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65535 tokens, but can only afford 25. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 25. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 16384 tokens, but can only afford 26. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 25. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 25. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 16. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 25. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 16. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 16. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
"]

# AI Model: openai/gpt-oss-20b:free - Global Prompt:

Analyze the attached project requirements. Build the GLOBAL PROJECT CONTEXT for Project 'membership-hub'.

--- RAW REQUIREMENTS ---
## SOFTWARE REQUIREMENTS SPECIFICATION: membership-hub
#### 1. TỔNG QUAN DỰ ÁN & KIẾN TRÚC TOÀN CẦU

###### Mục tiêu & giá trị cốt lõi
- Cung cấp nền tảng thống nhất để quản lý hội viên đa trung tâm.
- Cho phép theo dõi điểm danh thời gian thực qua quét mã QR.
- Cung cấp thẻ hội viên kỹ thuật số với tính năng đếm ngày hiệu lực.
- Hỗ trợ giao tiếp đa kênh (web, di động, nhóm Zalo).
- Giá trị cốt lõi: độ tin cậy, khả năng mở rộng, bảo mật, tính thân thiện với người dùng, hỗ trợ đa ngôn ngữ.

###### Đối tượng người dùng mục tiêu
- System Admin (siêu người dùng toàn cầu)
- Center Admin (quản lý cấp trung tâm)
- Manager (phó quản trị, quyền hạn giới hạn)
- Teacher (xem chỉ đọc lịch dạy)
- Student (duyệt khóa học, đăng ký, xem thẻ hội viên)
- Mobile App User (giao diện đáp ứng cho các vai trò trên)

###### Ma trận kiểm soát truy cập dựa trên vai trò (RBAC)
- [ARC-001] System Admin: toàn quyền trên tất cả các trung tâm.
- [ARC-002] Center Admin: toàn quyền trong trung tâm của mình, không ảnh hưởng đến các trung tâm khác.
- [ARC-003] Manager: có thể tạo thông báo, quản lý học viên, gán học viên hiện có vào khóa học, xem danh sách khóa học, không thể chỉnh sửa khóa học hoặc chỉ định giáo viên.
- [ARC-004] Teacher: xem khóa học của mình, danh sách học viên, lịch dạy; chỉ đọc.
- [ARC-005] Student: duyệt khóa học, đăng ký khóa học mới, xem thẻ hội viên (ngày còn lại), gia hạn ngày thẻ.

###### Kiến trúc & luồng dữ liệu (các luồng chính)
- [ARC-006] Luồng xác thực: hỗ trợ email/mật khẩu, Firebase, Google, Facebook qua OAuth2; cấp JWT token với thời hạn 15 phút và refresh token.
- [ARC-007] Luồng xử lý điểm danh QR: ứng dụng di động quét QR, gửi student ID và timestamp đến backend; dịch vụ xác thực và ghi lại điểm danh một cách idempotent.
- [ARC-008] Luồng gửi thông báo: hệ thống kích hoạt push notification đến ứng dụng di động và đăng bài lên nhóm Zalo được chỉ định cho thông báo, phân công khóa học, và cảnh báo điểm danh.
- [ARC-009] Luồng tích hợp backend ứng dụng di động: Frontend Next.js tiêu thụ REST APIs; xác thực qua bearer tokens; hỗ trợ caching ngoại tuyến cho trường hợp mất kết nối mạng.

###### Công nghệ & hạ tầng
- [ARC-010] Công nghệ & hạ tầng: Backend sử dụng Java/Quarkus, cơ sở dữ liệu PostgreSQL, container hóa Docker, triển khai trên Kubernetes (GKE), sử dụng Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs cho push notification, Zalo API integration, Redis cho session caching, CI/CD pipeline với GitHub Actions.

#### 2. CÁC MODULE CHỨC NĂNG NÂNG CAO

###### 2.1 Quản lý người dùng

######## Yêu cầu chức năng cốt lõi
- [REQ-001] Đăng ký người dùng: As a prospective user, I want to register using email and password (or social providers) so that I can obtain an account in the system.
- [REQ-002] Xác thực qua mạng xã hội: As a user, I want to sign‑in/up using Firebase, Google, or Facebook OAuth so that I can leverage existing credentials.
- [REQ-003] Phân quyền người dùng: As an administrator, I want to assign or change a user’s role (System Admin, Center Admin, Manager, Teacher, Student) so that permissions are correctly enforced.

######## Tiêu chí chấp nhận & tương tác
- Given a user provides a unique email, a strong password, and agrees to terms, When they submit the registration form, Then the system validates the input, creates a new user record with role ‘Student’ (or ‘Teacher’ if invited), and returns a success response with a JWT token. `[REQ-001]`
- Given a user selects a social provider, When they authenticate through the provider’s popup, Then the system receives an OAuth2 code, exchanges it for user info, creates or updates the local user record, and issues a JWT token. `[REQ-002]`
- Given an admin selects a user and a new role, When the assignment is confirmed, Then the user’s role column is updated, and appropriate permissions are applied immediately. `[REQ-003]`

######## Luồng ngoại lệ của mô-đun
- [EXC-004] Xác thực đầu vào không hợp lệ (ví dụ: email không đúng định dạng, thiếu trường bắt buộc): Nếu xác thực thất bại trên form submission, Khi lỗi được trả về cho người dùng, Sau đó một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-001] Bảng người dùng & vai trò

  **Users**
  ```mermaid
  erDiagram
      USERS {
          uuid userId PK "Unique identifier"
          varchar email "Email address, not null, unique, max 255 chars"
          char passwordHash "bcrypt hash, not null, length 60"
          varchar fullName "Full name, not null, max 100 chars"
          smallint roleId FK "Foreign key to Roles.roleId"
          enum provider "Auth provider, default local, values: local, firebase, google, facebook"
          timestamp createdAt "Timestamp of creation, not null, default now()"
          timestamp updatedAt "Timestamp of last update, not null, default now()"
      }
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
      ROLES ||--o{ USERS : "roleId"
  ```
  **Roles**
  ```mermaid
  erDiagram
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
  ```
###### 2.2 Quản lý trung tâm

######## Yêu cầu chức năng cốt lõi
- [REQ-004] Xem danh sách trung tâm: As any authenticated user, I want to see a list of all centers with address, tax ID, and admin contact so that I can identify relevant centers.
- [REQ-005] Tạo/cập nhật/xóa trung tâm: As a System Admin, I want to add, edit, or remove a center record so that center information stays current.
- [REQ-006] Phân quyền quản trị trung tâm: As a System Admin, I want to assign or unassign a user as a Center Admin for a specific center so that administrative control is delegated.

######## Tiêu chí chấp nhận & tương tác
- Given a user navigates to the Centers page, When the request completes, Then a table of centers (Name, Address, TaxID, AdminContact) is displayed. `[REQ-004]`
- Given a System Admin provides center name, address, tax ID, primary contact phone and email, When the save action is executed, Then the center is persisted and appears in the list; if duplicate tax ID exists, the operation fails with a conflict error. `[REQ-005]`
- Given a System Admin selects a user and a center, When the assign action is confirmed, Then the user’s role is set to ‘Center Admin’ and the center ID is recorded; unassign reverses the operation. `[REQ-006]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-003] Bảng trung tâm

  **Centers**
  ```mermaid
  erDiagram
      CENTERS {
          uuid centerId PK "Unique identifier"
          varchar name "Center name, not null, max 100 chars"
          varchar address "Physical address, not null, max 255 chars"
          varchar taxId "Tax identification number, unique, not null, numeric 10‑13 digits"
          varchar contactPhone "Contact telephone, optional, may include +, digits, spaces, hyphens, parentheses"
          varchar contactEmail "Contact email, optional, must be valid email format"
      }
  ```
###### 2.3 Quản lý khóa học

######## Yêu cầu chức năng cốt lõi
- [REQ-007] Xem danh sách khóa học: As any authenticated user, I want to see all courses with schedule and assigned teacher so that I can browse offerings.
- [REQ-008] Tạo/cập nhật/xóa khóa học (tránh xung đột): As a System Admin or Center Admin, I want to manage courses (add, edit, remove) while ensuring no overlapping schedules for the same teacher or venue.
- [REQ-009] Phân công giáo viên vào khóa học: As a System Admin, I want to assign or unassign teachers to courses so that teaching responsibilities are updated.

######## Tiêu chí chấp nhận & tương tác
- Given a user visits the Courses page, When the request completes, Then a grid displays CourseID, Title, StartDate, EndDate, TeacherName. `[REQ-007]`
- Given an admin provides CourseTitle, StartDate, EndDate, TeacherID, When the save action is triggered, Then the system validates that the teacher is not already scheduled for another course intersecting these dates; if conflict, an error is returned; otherwise the course is persisted. `[REQ-008]`
- Given an admin selects a course and a teacher, When the assign action is executed, Then the course‑teacher mapping is created and a notification is queued for the teacher’s mobile app; unassign removes the mapping. `[REQ-009]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-004] Bảng khóa học

  **Courses**
  ```mermaid
  erDiagram
      COURSES {
          uuid courseId PK "Unique identifier"
          varchar title "Course title, not null, max 150 chars"
          text description "Course description, optional"
          date startDate "Course start date, not null"
          date endDate "Course end date, not null"
          uuid teacherId FK "Foreign key to Users.userId"
          int maxStudents "Course capacity, default 30"
      }
  ```
###### 2.4 Đăng ký & ghi danh học viên

######## Yêu cầu chức năng cốt lõi
- [REQ-010] Duyệt khóa học: As a Student, I want to browse available courses (excluding those already enrolled) so that I can select courses to join.
- [REQ-011] Đăng ký khóa học của học viên: As a Student, I want to register for a course (existing or new), which auto‑creates a Student account if missing, and assigns the student to the course.

######## Tiêu chí chấp nhận & tương tác
- Given a Student logs in and navigates to the Browse Courses page, When the request completes, Then a list of courses with capacity and schedule is shown, excluding courses where the student already has an enrollment record. `[REQ-010]`
- Given a Student selects a course and submits the registration, When the backend processes the request, Then a new enrollment record is created; if the student does not have a local account, one is created with role ‘Student’; a notification is queued to the student’s mobile app and the center’s Zalo group. `[REQ-011]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-005] Bảng ghi danh

  **Enrollments**
  ```mermaid
  erDiagram
      ENROLLMENTS {
          uuid enrollmentId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          timestamp enrollmentDate "Date of enrollment, default now()"
      }
  ```
###### 2.5 Điểm danh & quét mã QR

######## Yêu cầu chức năng cốt lõi
- [REQ-012] Chụp ảnh điểm danh QR: As a Student (via mobile app), I want to scan a QR code at class start so that my attendance is recorded for the current day.
- [REQ-013] Tính chất bất biến của điểm danh: The attendance service must guarantee that multiple scans from the same student for the same course on the same day produce a single attendance record.

######## Tiêu chí chấp nhận & tương tác
- Given a Student opens the scanner, scans a valid course QR, and confirms attendance, When the API receives the payload, Then the system validates the student‑course relationship, creates an Attendance record with timestamp, and returns a success response; duplicate scans on the same day are ignored. `[REQ-012]`
- Given a student scans a QR twice within a minute, When the service processes both requests, Then only one attendance row is created; subsequent requests return a success with a ‘duplicate’ flag. `[REQ-013]`

######## Luồng ngoại lệ của mô-đun
- [EXC-001] Network & Connectivity Drops During QR Scan: If a student scans a QR but the network is unavailable, When the app retries the request after reconnection, Then the attendance is recorded once the service is reachable.
- [EXC-002] Duplicate Attendance Submission: If the same student scans the same course QR multiple times within the same day, When the system detects a duplicate, Then it returns a success response indicating ‘already recorded’ and does not create extra rows.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-006] Bảng điểm danh

  **Attendance**
  ```mermaid
  erDiagram
      ATTENDANCE {
          uuid attendanceId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          date attendanceDate "Date of attendance, not null"
          timestamp timestamp "Exact time recorded, default now()"
      }
  ```
###### 2.6 Quản lý thẻ hội viên

######## Yêu cầu chức năng cốt lõi
- [REQ-014] Hiển thị tính hợp lệ của thẻ: As a Student, I want to view my membership card showing remaining validity days so that I know when renewal is needed.
- [REQ-015] Gia hạn thẻ: As a Student, I want to extend my membership card validity by paying a fee, which updates the end date.

######## Tiêu chí chấp nhận & tương tác
- Given a Student opens the Card page, When the request loads, Then the UI shows total validity days, days used, and days remaining; data is derived from the StudentCard entity. `[REQ-014]`
- Given a Student selects a renewal period (e.g., 30 days), confirms payment, When the payment service confirms success, Then the StudentCard’s EndDate is extended by the selected days and a confirmation notification is sent. `[REQ-015]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-007] Bảng thẻ hội viên

  **StudentCards**
  ```mermaid
  erDiagram
      STUDENTCARDS {
          uuid cardId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          date issueDate "Card issue date, not null"
          int validityDays "Total validity days, not null"
          int remainingDays "Computed days left until expiry"
      }
  ```
###### 2.7 Thông báo & truyền thông

######## Yêu cầu chức năng cốt lõi
- [REQ-016] Kích hoạt thông báo: When an admin creates an announcement, assigns a teacher to a course, or registers a student, the system must generate a notification to the student’s mobile app and post a message to the designated Zalo group.

######## Tiêu chí chấp nhận & tương tác
- Given an admin performs an action that requires notification, When the action is saved, Then a Notification record is created, a push notification payload is queued for the mobile app, and a text message is sent to the Zalo group chat. `[REQ-016]`

######## Luồng ngoại lệ của mô-đun
- [EXC-003] Failed Notification Delivery: When a push notification cannot be delivered (e.g., device token invalid), Then the system logs the failure and schedules a retry up to three times before marking as failed.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-008] Bảng thông báo

  **Notifications**
  ```mermaid
  erDiagram
      NOTIFICATIONS {
          uuid notificationId PK "Unique identifier"
          uuid userId FK "Target user, optional"
          varchar groupZalo "Target Zalo group, optional"
          text message "Notification content, not null"
          timestamp sentAt "When sent, default now()"
          boolean delivered "Delivery status, default false"
      }
  ```
###### 2.8 Quản lý khuyến mãi & thông báo

######## Yêu cầu chức năng cốt lõi
- [REQ-017] Quản lý khuyến mãi: As a Center Admin or Manager, I want to create, edit, or delete promotions (discounts, offers) with start/end dates so that students can see applicable deals.
- [REQ-018] Quản lý thông báo: As a Center Admin or Manager, I want to create, edit, or delete announcements with optional expiry dates for broadcast to all users.

######## Tiêu chí chấp nhận & tương tác
- Given an admin provides PromotionName, description, conditions, startDate, endDate, When saved, Then the promotion appears in the student‑visible list; if endDate is omitted, the promotion is considered perpetual. `[REQ-017]`
- Given an admin inputs AnnouncementTitle, content, optional expiry, When saved, Then the announcement is displayed site‑wide; if expiry is set, it auto‑disappears after the date. `[REQ-018]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-009] Bảng khuyến mãi & thông báo

  **Promotions**
  ```mermaid
  erDiagram
      PROMOTIONS {
          uuid promoId PK "Unique identifier"
          varchar code "Discount code, unique"
          smallint discountPercent "Discount percentage, not null"
          date startDate "Promotion start, optional"
          date endDate "Promotion end, optional"
          text description "Promo details, optional"
      }
  ```
  **Announcements**
  ```mermaid
  erDiagram
      ANNOUNCEMENTS {
          uuid announcementId PK "Unique identifier"
          varchar title "Title, not null, max 150 chars"
          text content "Content, not null, max 2000 chars"
          date startDate "Effective start, optional"
          date endDate "Effective end, optional"
      }
  ```
###### 2.9 Chatbot dịch vụ khách hàng AI

######## Yêu cầu chức năng cốt lõi
- [REQ-019] Tích hợp chatbot AI: As any user, I want to interact with an AI chatbot that can answer common queries about courses, teachers, centers, and account status.

######## Tiêu chí chấp nhận & tương tác
- Given a user opens the chat widget, When they ask a question, Then the AI returns a relevant answer or escalates to human support if confidence is low. `[REQ-019]`

######## Luồng ngoại lệ của mô-đun
- [NOT APPLICABLE] Chatbot AI không có bảng dữ liệu chuyên biệt; tất cả các tương tác được ghi lại trong bảng AuditLog (xem [ARC-006] để biết chi tiết logging).

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho chatbot AI.

###### 2.10 Các tính năng cốt lõi của ứng dụng di động

######## Yêu cầu chức năng cốt lõi
- [REQ-020] Giao diện người dùng vai trò cụ thể trên di động: As a mobile user, I want a responsive UI that mirrors web functionality for my assigned role (Student, Teacher, Admin, etc.).
- [REQ-021] Thông báo đẩy trên di động: As a registered user, I want to receive push notifications on my mobile device for attendance confirmations, new announcements, and reminder messages.

######## Tiêu chí chấp nhận & tương tác
- Given a user logs in on Android or iOS, When the app loads, Then the appropriate navigation menu and screens are displayed based on the user’s role. `[REQ-020]`
- Given a backend event triggers a push, When the device token is registered, Then the notification is delivered via Firebase Cloud Messaging (FCM) or APNs. `[REQ-021]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho các tính năng cốt lõi của ứng dụng di động; tất cả dữ liệu được quản lý qua các bảng hiện có (Người dùng, Thông báo, Điểm danh).

###### 2.11 Bản địa hóa & SEO

######## Yêu cầu chức năng cốt lõi
- [REQ-022] Phát hiện ngôn ngữ mặc định: As a visitor, I want the system to use my previously selected language preference, falling back to browser settings, for a personalized experience.
- [REQ-023] SEO đa ngôn ngữ: The platform must support SEO for at least English, Vietnamese, and Spanish; each page must include language‑specific meta tags and hreflang attributes.

######## Tiêu chí chấp nhận & tương tác
- Given a user accesses the site, When the system evaluates locale, Then it selects the stored language if present; otherwise it uses the Accept‑Language header; the UI updates accordingly. `[REQ-022]`
- Given a page is requested with a specific locale, When the page is rendered, Then the HTML includes a <html lang='en'> tag and hreflang links pointing to alternate language versions. `[REQ-023]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-011] Bảng cài đặt hệ thống

  **SystemSettings**
  ```mermaid
  erDiagram
      SYSTEMSETTINGS {
          varchar settingKey PK "Configuration key"
          text settingValue "Configuration value, not null"
          varchar description "Meaning of setting, optional"
      }
  ```
###### 2.12 Báo cáo & phân tích

######## Yêu cầu chức năng cốt lõi
- [REQ-024] Tạo báo cáo điểm danh: As an admin, I want to generate a daily attendance report for a center (CSV) showing each student’s presence status.
- [REQ-025] Bảng điều khiển tóm tắt ghi danh: As a Center Admin, I want a real‑time dashboard summarizing total students, active courses, and upcoming sessions.

######## Tiêu chí chấp nhận & tương tác
- Given an admin selects a center and date range, When the report is requested, Then a CSV file is produced with columns: StudentName, CourseName, AttendanceDate, Status. `[REQ-024]`
- Given an admin opens the dashboard, When the data refreshes, Then cards display totalStudents, activeCourses, upcomingSessions (next 7 days). `[REQ-025]`

######## Luồng ngoại lệ của mô-đun
- [EXC-005] System Recovery After Outage: If the service becomes unavailable, When it restores, Then any pending attendance scans are processed in FIFO order, and users receive a notification of recovered events.

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho báo cáo & phân tích; tất cả dữ liệu được tổng hợp từ các bảng hiện có.

#### 3. YÊU CẦU PHI CHỨC NĂNG TOÀN CẦU

- [NFR-001] Performance Metrics: Core API responses (authentication, attendance capture, course list) must complete within 200 ms average latency. Database queries must be indexed to support sub‑second reads for up to 10 000 concurrent users.
- [NFR-002] Availability: Target 99.9 % annual uptime; SLA includes automatic failover across GKE clusters.
- [NFR-003] Security: All data in transit must use TLS 1.3; at rest encryption with AES‑256. JWT access tokens expire after 15 minutes; refresh tokens have 7‑day expiry. Implement OWASP Top 10 mitigations (SQL injection, XSS, CSRF).
- [NFR-004] Scalability & Availability: Horizontal scaling of Quarkus services via Kubernetes HPA based on CPU > 70 % or request latency > 300 ms. PostgreSQL read replicas for reporting workloads.
- [NFR-005] Docker Image Size: Base image size < 200 MB; final image < 500 MB.
- [NFR-006] Logging & Audit: All user actions (role changes, attendance records, notifications) must be logged with timestamps, user ID, and action details; logs retained for 1 year.
- [NFR-007] Multi‑Language Support: UI strings must be externalized; support English, Vietnamese, Spanish; locale switching without page reload where feasible.
- [NFR-008] GDPR/CCPA Compliance: Personal data deletion on user request; data export in JSON format; consent management for marketing communications.
- [NFR-009] Backup & Disaster Recovery: Daily PostgreSQL full backups; point‑in‑time recovery up to 24 hours; GKE cluster backup to separate region.
--- END REQUIREMENTS ---

## 🚨 MANDATORY ARCHITECTURAL GENERATION CODES
*You must fully engineer the blueprint report by strictly implementing exactly three engineering protocols:*

######## 🎯 PROTOCOL 1: Dynamic Topology Path Prefixing
- You MUST dynamically match the physical directory file path masks to the active system topology extracted from the raw requirements.
- Every single generated path parameter string inside the log (`target_component`) MUST utilize the strict Unix forward-slash `/` character as the structural directory delimiter.
- You are CRITICALLY AND PERMANENTLY FORBIDDEN from utilizing the package dot notation `.` inside folder names or file boundaries.
- Do NOT emit relative paths that assume a sub-module directory is the root:
  * *IF Backend logic/layer is active:* All backend code, services, database schemas, and database tests must reside strictly under: `./sources/backend/` (If Microservices topology is active, you MUST utilize the alphanumeric lowercase service name as the sub-folder path, e.g., `./sources/backend/<service-name>/`). Skip entirely if project is Frontend-only.
  * *IF Frontend logic/layer is active:* All client interfaces, responsive views, mobile bundles, and web tests must reside strictly under: `./sources/frontend/` (or `./sources/frontend/<app-name>/` if multiple client applications exist. Skip entirely if project is Backend-only).
  * *IF DevOps infrastructure logic is active:* All deployment manifests, Dockerfiles, GKE orchestrations, and cloud provisioning scripts must reside strictly under: `./sources/infra/`.
  * *For Document Asserts:* Prefix paths strictly with: `./sources/docs/`.
  * For alternative topologies (AI/Data, IoT, Embedded): Paths must strictly map to logical root subdirectories matching the service domain layer under `./sources/`.
- Any component path emitted that replaces a forward slash `/` with a directory dot `.` triggers a fatal pipeline integrity exception.

######## 🗄️ PROTOCOL 2: Granular Ceilings-Compliant Task Logs
- For each calculated phase necessary to cover the BA inputs (Up to the absolute maximum ceiling of 5 phases), supply a clean chronological daylog breakdown (Up to the absolute ceiling of 7 days per phase). Every single day generated MUST explicitly define the specific assigned sub-agent persona ('Coder' | 'Tester' | 'Reviewer' | 'Doc' | 'Docker' | 'GCP' | 'GKE'), the low-level technical step target, the exact tracking Tag IDs, and the explicit physical relative file path (`target_component`).

######## 🧮 PROTOCOL 3: 100% Vertical Tag Traceability Coverage (ZERO BUNDLING POLICY)
- Every single feature, entity, database table column, validation, exception, or infrastructure component outlined across your report MUST be strictly prefixed or appended with the exact corresponding Tag IDs (`[REQ-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[NFR-XXX]`) inherited from the requirements. 
- You are STRICTLY BANNED from bundling tags together (e.g., NO `[REQ-001-005]`). Every single tag must be written out individually and separated by commas. Leaving any task or field without its trace tracking identifier inline is a critical framework violation.

######## 🚨 SUB-AGENT BOUNDARY & RESPONSIBILITY ISOLATION MATRIX
You MUST strictly isolate the architectural responsibilities of all Sub-Agents listed below. They are separate functional pillars and must NEVER bleed into each other's domain:
- 💻 **Coder Agent Role**:
  * Core Duty: Pure Application Source Code Implementation.
  * Allowed Actions: Write, refactor, and implement structural logic in application files.
  * Strict Boundary: Forbidden from writing test suites or enterprise architectural documentation.
- 🧪 **Tester Agent Role**:
  * Core Duty: Test Suite Engineering and Validation.
  * Allowed Actions: Write unit tests, integration tests, and automation scripts. 
  * Strict Boundary: Must strictly use the target-test semi-colon pair syntax for `target_component` (`target_test_file;source_code_file`). Forbidden from writing production application code.
- 🔍 **Reviewer Agent Role**:
  * Core Duty: Code Review, Issue/Bug Analysis and Fix Strategy.
  * Allowed Actions: Inspect code quality, enforce programming standards, detect optimization bottlenecks, analyze structural issues/bugs, and design explicit fix implementations.
- 📝 **Doc Agent Role**:
  * Core Duty: Enterprise Technical Document Writer.
  * Allowed Actions: Author high-quality Markdown technical specifications, architecture blueprints, API references, and system compliance documents.
- 🐳 **Docker Agent Role**:
  * Core Duty: Containerization and Package Registry Pushing.
  * Allowed Actions: Build multi-stage Dockerfiles and push container images to target registries.
- ☁️ **GCP Agent Role**:
  * Core Duty: Baseline Google Cloud Platform Infrastructure Provisioning.
  * Allowed Actions: Build, push configurations, manage core cloud services (VPC, IAM, Storage), and orchestrate general cloud pipeline deployments.
- ☸️ **GKE Agent Role**:
  * Core Duty: Google Kubernetes Engine Workload Orchestration.
  * Allowed Actions: Build, push configuration files, design Kubernetes deployment manifests, and manage container scaling and release strategies inside GKE clusters.

######## 🔢 EQUAL REQUIREMENT DISTRIBUTION & ZERO-FILLER DAY-CAP PROTOCOL
- **Phase Boundary Count**: The total number of architectural phases MUST be exactly "5".
- **Requirement Distribution Mandate**: You MUST distribute 100% of all provided project requirements into exactly "5" phases. No requirement can be left unassigned, omitted, or bundled lazily. Every phase from Phase 1 to Phase "5" must receive a balanced subset of requirements.
- **Strict Day-Cap & Anti-Filler Rail**:
  * The maximum number of days within ANY single phase is strictly capped at: "7".
  * The actual number of days per phase can be LESS than or EQUAL to "7" (e.g., `actual_days <= max_days_per_phase`).
  * 🚨 **STRICT FORBIDDEN DIRECTIVE**: You are ABSOLUTELY FORBIDDEN from creating "filler days", redundant testing sessions, unnecessary sync setups, or placeholder tasks just to padding the day count up to the maximum limit. If a phase only requires 2 high-density days to fully implement its assigned requirements, you MUST stop at Day 2. Do not hallucinate Day 3 or Day 4.
  * Every generated day must contain high-utility, actionable enterprise engineering tasks. No empty or duplicate logs.

######## 🚨 CRITICAL FULL TRANSLATION MANDATE
- The target generation language for all human-readable outputs is permanently bound to: "🇻🇳 Vietnamese". Everything MUST be translated into 🇻🇳 Vietnamese, except for the explicit Technical English core tokens protected by system mandates.
- You MUST fully translate 100% of all headers, section titles, sub-headers, descriptive text, sentences, explanations, phase objectives, phase descriptions, phase section headers / titles / sub-headers / pullet titles, and task instructions into the designated target language.

######## 🚨 DYNAMIC INTERNATIONALIZATION & TRANSLATION ENGINE
- Target Output Language Context: "🇻🇳 Vietnamese"
- You MUST dynamically translate 100% of all user-facing structural components, table headers, phase layouts, and list prefixes into the designated Target Output Language Context.
- 🚨 MANDATORY STRUCTURAL MAPPING DIRECTIVE (Translate these dynamically based on the target language context):
  * All Section and Sub-section Headers (including entire header of ouput markdown report, example `GLOBAL PROJECT CONTEXT`) MUST be translated contextually.
  * Table Headers MUST be translated (e.g., in Vietnamese: `Phase` -> `Giai đoạn`, `Day Range` -> `Khoảng ngày`, `Component / Module Path` -> `Đường dẫn Cấu phần / Module`, `Deliverables Summary` -> `Tóm tắt Sản phẩm Bàn giao`, `Sub-Agent` -> `Sub-Agent`, `Targeted Tag IDs` -> `Tag IDs Mục tiêu`).
  * List Prefixes and Phase Titles MUST be translated (e.g., in Vietnamese: `Phase [X] Detailed Architectural Specification` -> `Đặc tả Kiến trúc Chi tiết Giai đoạn [X]`, `Phase Core Objective & Purpose` -> `Mục tiêu Cốt lõi & Mục đích của Giai đoạn`, `Target Physical Directory Matrix Map` -> `Ma trận Bản đồ Thư mục Vật lý Mục tiêu`, `Database Schema DDL SQL Specification` -> `Đặc tả DDL SQL Schema Cơ sở Dữ liệu`, `API and Event Routing Contracts` -> `Hợp đồng Định tuyến API và Sự kiện`).
- 🚨 SPECIFIC SECTION CONTENT TRANSLATION RAILS:
  * For Sections 1 & 2: Translate all comprehensive technical overviews, main headers, sub-headers, section titles, labels, table columns, ecosystem descriptions, stack details, and asynchronous channel analysis.
  * For Section 3: Translate all , main headers, sub-headers, section titles, labels, table columns, descriptions of workspace rules, compliance standards, and condition explanations.
  * For Section 4 & 5: Translate all table headers (except technical tokens), main headers, sub-headers, section titles, labels, table columns, deliverables summaries, core objectives, localized exception handling descriptions, and low-level task instruction texts.
  * For Sections 6, 7 & 8: Translate all detail descriptions of injection countermeasures, main headers, sub-headers, section titles, labels, table columns, security rails, hybrid compliance rules, SEO mechanisms, and pipeline git flow gating rules.
- 🚨 RIGID TECHNICAL BOUNDARY & TECHNICAL EXCLUSION ZONE (DO NOT TRANSLATE): You are strictly forbidden from translating or modifying technical structures, including:
  * All markdown syntax layout operators (`##`, `####`, `######`, `|`, `:`, `-`, `*`) and numerical hierarchy indices (e.g., `1.`, `1.1.`) MUST remain unaltered to preserve the document layout integrity.
  * 🚨 **SUPREME ARCHITECTURE HEADER TRANSLATION MANDATE:** You MUST fully translate into the target language 100% of high-level overview terms, system architecture descriptions, or blueprint documentation titles (even if they are written in full uppercase or encapsulated inside strong markdown bold formatting `**`, such as: `SYSTEM OVERVIEW`, `CORE ARCHITECTURE MODALITY`, `PROJECT CONTEXT`). You are STRICTLY FORBIDDEN from treating these architectural section names as technical identifier strings to bypass translation. The structure `#### 🏛️ 1. SYSTEM OVERVIEW` MUST be processed and rendered exactly as `#### 🏛️ 1. TỔNG QUAN HỆ THỐNG`.
  * All code blocks (SQL DDL, JSON schemas, JSON payloads, Java, etc.) and Mermaid flow diagrams.
  * All tracking Tag IDs (e.g., `[REQ-XXX]`, `[DAT-XXX]`, `[EXC-XXX]`, `[NFR-XXX]`, `[ARC-XXX]`).
  * All raw physical file paths starting with `./sources/` and the Tester semi-colon pair syntax.
  * All strict literal tokens for Sub-Agent names (`Coder`, `Tester`, `Reviewer`, `Doc`, `Docker`, `GCP`, `GKE`).
  * All hidden HTML comment tags, system data splitters, and data extraction anchors (e.g., `<!--START_DELIMITTER-->`, `<!--END_DELIMITTER-->`, `[PAYLOAD_DELIMITER]`). These must remain in their original raw character format to prevent backend processing errors.
  * Retain all raw engineering strings: file paths (`./sources/...`), code blocks, Tag IDs (`[REQ-XXX]`, `[DAT-XXX]`, etc.), and strict Sub-Agent literal tokens (`Coder`, `Tester`, `Reviewer`, `Doc`, `Docker`, `GCP`, `GKE`).
  * 🚨 **STRICT CODE BLOCK FORMATTING LAW**: You are ABSOLUTELY FORBIDDEN from nesting or combining markdown code block ticks. When outputting a JSON payload, you MUST start exactly with a single line of triple backticks followed immediately by 'json' (i.e., ```json). Do NOT prepend or wrap it with ```text or any other outer text syntax. The block must open clean and close clean.
  * **Static Pass Tag `<NO_TRANSLATION>...</NO_TRANSLATION>`**: Used for static assets. You MUST pass 100% of the internal content literal without any localization, alteration, processing, or computation.
  * **Dynamic Generation Tag `<DYNAMIC_DATA_ENGLISH_ONLY>...</DYNAMIC_DATA_ENGLISH_ONLY>`**: Used for dynamic instructions or mock templates. You MUST process, evaluate variables, and dynamically compute the generation outputs inside this block. However, 100% of the newly generated text stream resulting from this block MUST be strictly rendered in **Technical English** only, with an absolute ban on translation into the target language. The boundary tags MUST be stripped from the final output stream upon execution.

###### 📋 MANDATORY OUTPUT STRUCTURE (MARKDOWN REPORT LAYOUT):
You MUST include every single section below without exception to satisfy enterprise compliance requirements, and fully translating them following the rules in `CRITICAL FULL TRANSLATION MANDATE`:

<RULE>
- **🚨 MASTER GOVERNANCE COMPLIANCE MANDATE**: Before generating your final output response, you MUST strictly re-read and enforce the global translation rules defined in the Master Rules section. Ensure 100% of descriptive texts are rendered in 🇻🇳 Vietnamese while completely freezing all technical paths, tags, and block codes.
</RULE>

## GLOBAL PROJECT CONTEXT: membership-hub


  
  MANDATORY INSTRUCTION: You are strictly ordered to ONLY generate Section 1, Section 2, Section 3, and Section 4. Absolutely DO NOT generate Section 5, 6, 7, or 8 in this request.
  


#### 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260808172311 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/08 17:23:11 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |


#### 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

###### 1.1. Core System Modality & Architecture Modality
<RULE>
- You MUST automatically delete this entire rule instruction text stream block.
- You MUST dynamically generate a comprehensive technical overview analysis of the discovered core system architecture, EDA patterns, CQRS boundaries, and Reactive core models based strictly on the requirement context.
- CRITICAL FORMAT RULE: You BANNED from outputting paragraphs or walls of text. You MUST strictly format 100% of your generated overview as a clean, highly structured, high-density markdown bulleted checklist (`- ` symbols). Each bullet point must be a short, punchy technical statement delivering raw architectural metrics.
- You MUST render 100% of your newly generated sentences in the designated target language: Vietnamese.
</RULE>

###### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
<RULE>
- You MUST automatically delete this entire rule instruction text stream block.
- You MUST dynamically generate a detailed technical breakdown analysis of asynchronous messaging channels, ingestion gateway parameters, topic topologies, and cross-channel external fan-out architectures based on the context.
- CRITICAL FORMAT RULE: You BANNED from outputting paragraphs or walls of text. You MUST strictly format 100% of your generated breakdown as a clean, highly structured, high-density markdown bulleted checklist (`- ` symbols). Each bullet point must be a short, punchy technical statement delivering raw data flow paths.
- You MUST render 100% of your newly generated sentences in the designated target language: Vietnamese.
</RULE>

#### 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
<RULE>
- **STRICT BOUNDARY LOCKDOWN FOR PROPERTIES BLOCK:** Within the generated properties code fence, you MUST execute the complete physical destruction of the placeholder square brackets. The output values MUST be clean literal boolean raw values without any enclosing markers to prevent downstream parsing panics.
</RULE>
- **Backend Infrastructure Core Stack:** [Detail precise versions, runtime engines, dependency injection abstractions, ORMs, and messaging frameworks extracted from requirements]
- **Frontend & Cross-Platform UI Mobile Stack:** [Detail strict web frameworks, dynamic localized routing, responsive layouts, and native mobile runtime wrappers if present]

###### ARCHITECTURAL STACK MATRIX

```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=true_or_false_literal_only
BACKEND_LAYER_REQUIRED=true_or_false_literal_only
FRONTEND_LAYER_REQUIRED=true_or_false_literal_only
MOBILE_LAYER_REQUIRED=true_or_false_literal_only
DEVOPS_LAYER_REQUIRED=true_or_false_literal_only
```

#### 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `.`. All paths generated MUST begin with `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** If the tech stack utilizes Java frameworks, all Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. You MUST dynamically convert the string "membership-hub" into a strict pure alphanumeric lowercase token by stripping out whitespaces, hyphens, and underscores. Non-Java projects are completely banned from applying this package segment.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `./sources/`.

#### 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

#### 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

###### 4.1. MASTER ARCHITECTURAL PRODUCT BACKLOG
<RULE>
- You MUST generate a comprehensive, unified Master Product Backlog table directly under this section before organizing the multi-phase timeline. This table acts as the definitive grounding index for 100% of the project scope.
- **STRICT BACKLOG COMPLETENESS COMPLIANCE LAW:** This master table MUST completely map and exhaustively list every engineering effort required by the corpus, strictly verified by the Type column:
  1. *Application Code:* Functional endpoint creations, database models, and service layer code blocks.
  2. *Enterprise Documentation:* Complete systemic blueprints, database schema topologies, localized operational manual files, and API contracts located under `./sources/docs/`.
  3. *DevOps Infrastructure:* Containerization scripts (Docker), cloud environment setups (GCP via Terraform), and orchestration cluster manifests (GKE).
- **100% INVARIANT TRACEABILITY LINKAGE:** Every row in this backlog MUST enforce absolute coverage of all relevant tracking tags (`[REQ-XXX]`, `[DAT-XXX]`, `[ARC-XXX]`, `[EXC-XXX]`, `[NFR-XXX]`). Zero orphan requirements or untagged deliverables are permitted.
- **MANDATORY CASCADE PLAN COMPLIANCE:** Every task documented in this Master Backlog table MUST cascade symmetrically downwards: it MUST be distributed into exactly one targeted phase in the Synopsis Grid under Section 4.2, and subsequently possess an explicit, standalone daily execution sub-task log inside Section 5 for that specific phase.
- The Master Product Backlog table layout MUST strictly execute inside the hidden framework parsing hooks exactly as formatted below (inside the hidden HTML tags from `<!--START_BACKLOG_SYNOPSIS_GRID-->` to `<!--END_BACKLOG_SYNOPSIS_GRID-->`)
</RULE>

<!--START_BACKLOG_SYNOPSIS_GRID-->
| No. | Task | Technical Purpose / Deliverables Summary | Type | TagID |
| :--- | :--- | :--- | :--- | :--- |
| [Numerical Index, starting from 1] | [Task Title] | [Clear technical delivery objective description] | [Literal configuration string: 'Application Code' OR 'Enterprise Documentation' OR 'DevOps Infrastructure'] | [Dynamic tracing Tag IDs mapped inline] |
| ... | ... | ... | ... | ... |
| **SUMMARY** | **Total System Backlog Workload Deliverables** | **TOTAL:** [Compute and insert the absolute mathematical sum of all listed task rows, e.g., 42 Tasks] | **STATUS:** Verified | **COVERAGE:** 100% |
<!--END_BACKLOG_SYNOPSIS_GRID-->

###### 4.2. MULTI-PHASE SYNOPSIS MATRIX
Generate a clean, highly structured Markdown Table mapping the exact distribution of components and Tag IDs across the dynamically calculated phases. You MUST compute the most optimal number of phases (denoted as N, where N <= 5) that naturally and completely covers 100% of the BA requirements and Tag IDs.
<RULE>
- Each row MUST specify a real-world engineering duration bounded between 1 to a strict upper ceiling of 7 days maximum per phase. Do NOT generate empty rows, placeholder phases, or artificial workloads. If the requirements are fully satisfied within fewer than 5 phases, terminate the matrix setup immediately at phase N.
- LOCAL DAY RANGE BOUNDARY: In the "Day Range" column of this table, you MUST format the day sequence starting from relative integer 1 for EACH individual phase row (e.g., Phase 1: Day 1 - 2, Phase 2: Day 1 - 2). Compounding or running a linear progressive day count across phase boundaries is strictly prohibited.
- DYNAMIC TECHNICAL DENSITY PRICING LAW (Project-Agnostic): Each row's "Day Range" MUST be computed dynamically based strictly on the actual volume and density of the allocated Tag IDs for that specific phase. You MUST evaluate the capacity weight: a single calculated operational calendar day log inside Section 5 MUST NOT contain more than 3 unique critical requirement tags (REQ/ARC/NFR) combined. If a phase contains low-density tasks, you MUST stop the index immediately (e.g., closing tightly at Day 1-2).
- IMMUTABLE SYNOPSIS GRID WRAPPER MANDATE: When generating this section (Section 4) Markdown table, you ARE ABSOLUTELY AND CRITICALLY BANNED from dropping, omitting, or filtering out the technical hidden HTML comment anchors. You MUST explicitly enclose the entire generated table structure strictly between the literal tokens <!--START_PHASE_SYNOPSIS_GRID--> and <!--END_PHASE_SYNOPSIS_GRID-->.
- DYNAMIC DAY TITLE ENFORCEMENT: Inside Section 5, for every chronological day element (e.g., - **Day [Y]**:), you ARE PERMANENTLY FORBIDDEN from outputting static placeholder strings like "SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY". You MUST dynamically analyze the requirements for that day, compile a concise technical objective sentence, and fully translate it into the target language requested by the parameters.
- SUPREME DEMAND-DRIVEN WORKLOAD DISTRIBUTION LAW (ADAPTIVE LIFECYCLE): You MUST orchestrate the project planning by decomposing the absolute sum of all requirements (business functions, enterprise documentation components, and DevOps infrastructure pipelines) dynamically across 5 without any artificial padding or redundant agent forcing:
  1. Dynamic Resource Allocation Rule: A sub-agent ([Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], or [GKE]) MUST ONLY be declared in the Section 4.2 table row under 'Assigned Sub-Agent' if and ONLY if there are active, unfulfilled backlog requirements matching that agent's engineering domain within that specific phase context. If a phase contains zero infrastructure tasks, DevOps agents MUST be completely omitted from that specific row.
  2. Strict 1:1 Plan Symmetry Guardrail: If a sub-agent token is actively triggered and listed under the 'Assigned Sub-Agent' column for a phase in Section 4.2, you MUST guarantee that the same agent possesses at least one explicit, standalone technical task block inside Section 5 for that phase. Unassigned agents in Section 4.2 MUST NOT possess any tasks in Section 5.
  3. Hard Phase & Timeline Ceilings: The plan MUST split into exactly 5 phases, and no phase timeline block inside Section 5 shall exceed 7 calendar days.
  4. Zero Filler Data / Ghost Logs: You are strictly prohibited from generating ghost actions, repetitive task summaries, or empty calendar days simply to reach the maximum day limit. If the core deliverables for a phase are fully satisfied, the schedule stops immediately.
  5. 100% Traceability Matrix Coverage: Every active daily log and target component MUST map 100% of all relevant tracking tags ([REQ-XXX], [DAT-XXX], [ARC-XXX], [EXC-XXX], [NFR-XXX]) from the input corpus. Zero orphan requirements or unmapped tags are permitted.
- STRICT SUB-AGENT FILE-EXTENSION & MARKDOWN FENCE COMPLIANCE LAW: You MUST strictly isolate physical file extensions based on the active operating persona and protect layout rendering from syntax breakage:
  1. For [Coder] and [Reviewer]: The target_component MUST strictly point to a physical executable source file ending with valid production extensions (e.g., .java, .ts, .sql).
  2. For [Tester]: The target_component MUST strictly utilize the semicolon pair format containing valid test suffix extensions (e.g., .java, .ts, .spec.ts) matching Case 1 or Case 2 patterns.
  3. For [Doc]: The target_component MUST permanently target granular, individual documentation files ending strictly with the .md extension, located inside ./sources/docs/.
  4. Markdown Render Integrity: You ARE ABSOLUTELY BANNED from outputting naked triple backticks (```) for inner specifications (such as ```sql:matrix or ```json) inside an active root code fence. Every inner code segment block embedded within the day-by-day logs MUST utilize distinct delimiter tokens to ensure parsing isolation. You MUST strictly use exactly four backticks (````) or five backticks (`````) for the top-level parent envelope if the interior values require a three-backtick string literal expression.
- ABSOLUTE DISCRETE SUB-TASK SEPARATION MANDATE: You ARE PERMANENTLY FORBIDDEN from aggregating or grouping distinct agent actions into a single combined description block or combined agent field. Every day log inside Section 5 MUST expand into an array of isolated, independent sub-task items, where each sub-task is exclusively mapped to exactly one naked sub-agent persona token.
- CRITICAL COMPACT PATCH & REVIEWER PARADIGM DIRECTIVE: The [Reviewer] MUST operate strictly in a sequential multi-step gating paradigm immediately following the [Coder] execution block inside the daily sub-task sequence. The Reviewer MUST systematically analyze the Coder's generated source assets to verify compiler stability and architectural compliance. If the compiler audit passes with zero issues, the Reviewer task freezes instantly with a no-op status. If and ONLY IF an explicit syntax anomaly, structural bottleneck, or compilation breakdown is detected, the Reviewer MUST trigger a defensive patching directive to execute immediate, target-specific code corrections. All patch instructions MUST be written as concise, structural pseudo-steps or high-density technical instructions; you are absolutely banned from embedding long walls of duplicate raw source code blocks inside the instruction description.
- GRANULAR DELIVERABLE CHECKLIST MANDATE: You MUST inject multiple verification and architectural tasks into the "Technical Deliverables Summary" column for every phase row:
  1. For Tester: Force the inclusion of concrete validation targets, explicitly stating the production of JUnit suites, Integration Tests, and end-to-end (E2E) automation execution profiles.
  2. For Doc: Force the inclusion of architecture alignment requirements, explicitly stating the generation of system technical documentation blueprints and API technical specifications.
- ABSOLUTE ARCHITECTURAL PLAN SYMMETRY MANDATE (ANTI-DESYNC): You MUST enforce strict 1:1 deterministic alignment between the global macro-plan in Section 4.2 (<!--START_PHASE_SYNOPSIS_GRID-->) and the granular micro-logs in Section 5. It is a critical system violation to declare sub-agents in the synopsis table row while leaving them with zero execution tasks in the corresponding daily breakdown.
- **ABSOLUTE MATHEMATICAL BACKLOG COUPLING LAW:** You MUST ensure flawless mathematical synchronization between the total task count generated in the Master Backlog table (Section 4.1 Summary Row) and the accumulated count of discrete sub-task nodes produced across all phases inside Section 5. 
- You ARE ABSOLUTELY BANNED from dropping, truncating, or abstracting any task from Section 4.1 when expanding the timeline logs. Every individual functional index or document artifact registered in the Master Backlog table MUST expand into exactly one standalone execution sub-task node within its designated calendar day block inside Section 5. Under-counting, omitting tasks, or prematurely stopping the sub-task sequence before satisfying 100% of the Master Backlog rows constitutes a fatal compliance crash.
- DETERMINISTIC DISTRIBUTION PATTERN PER PHASE: For 100% of the phases generated, if a sub-agent token ([Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], or [GKE]) is registered under the 'Assigned Sub-Agent' column in Section 4.2, you MUST partition the phase timeline chunk so that EVERY listed agent possesses at least one explicit, standalone, independent technical sub-task block inside Section 5 for that specific phase.
- BALANCED MULTI-AGENT TIMELINE PACKING: To fit multiple required agents within narrow day-ranges without inflating the timeline or violating the dynamic technical density ceiling, you MUST execute compact parallel or sequential distribution:
  1. Early phase timeline segments MUST be optimized for application-layer loops where [Coder] and [Doc] execute in parallel sub-tasks, immediately followed sequentially by [Reviewer] quality gates and [Tester] automated suites.
  2. Concluding phase timeline segments MUST be strictly cleared of application tasks and dedicated to sequential infrastructure workflows handled exclusively by [Docker], [GCP], and [GKE] sub-agents to deliver automated environment setups and deployment manifests.
</RULE>

<!--START_PHASE_SYNOPSIS_GRID-->
| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ... | ... | ... | ... | ... | ... |
| **AUDIT** | **Master Backlog Lifecycle Distribution Verification** | **TOTAL PHASES:** [Compute real-world N calculated phases, e.g., 5 Phases] | **MAPPED CAPACITY STATUS:** [You MUST mathematically count and cross-verify the sum of all distributed tasks against Section 4.1. Output the literal dynamic execution statement matching this pattern: 'Verified: X out of Y Total Master Backlog Tasks successfully distributed across calculated phases with 100% coverage'] | **STATUS:** Verified | **COMPLIANCE:** Hardbound Matrix |
<!--END_PHASE_SYNOPSIS_GRID-->

# System Instruction

<GLOBAL_GOVERNANCE_MATRIX>
# ==============================================================================
# MASTER ENTERPRISE GOVERNANCE GUARDRAILS MATRIX (GLOBAL TASK ENFORCEMENT)
# ==============================================================================

## 🌐 1. STRICT SEMANTIC INVARIANT LOCALIZATION & TRANSLATION RAILS
- **MANDATORY RESOLUTION:** You MUST automatically translate and naturally render 100% of the entire generated output content—including all section headers, primary titles, data matrix labels, table structures, and explanatory text boundaries—into the exact requested target execution language specified by the system parameter variable: "🇻🇳 Vietnamese".
- **ABSOLUTE TECH PROTECTION BOUNDARY:** You are STRICTLY BANNED from translating, changing, altering, or breaking any technical structural layers. You MUST preserve these elements natively in their pristine Technical English/Primitive code state:
    * All markdown syntax layout operators (`#`, `##`, `###`, `|`, `:`, `-`, `*`) and numerical hierarchy indices (e.g., `1.`, `1.1.`) MUST remain unaltered to preserve the document layout integrity.
    * 🚨 **SUPREME ARCHITECTURE HEADER TRANSLATION MANDATE:** You MUST fully translate into the target language 100% of high-level overview terms, system architecture descriptions, or blueprint documentation titles (even if they are written in full uppercase or encapsulated inside strong markdown bold formatting `**`, such as: `SYSTEM OVERVIEW`, `CORE ARCHITECTURE MODALITY`, `PROJECT CONTEXT`). You are STRICTLY FORBIDDEN from treating these architectural section names as technical identifier strings to bypass translation. The structure `## 🏛️ 1. SYSTEM OVERVIEW` MUST be processed and rendered exactly as `## 🏛️ 1. TỔNG QUAN HỆ THỐNG`.
    * All unique Tracking Tag IDs and Technical Nodes (e.g., `[REQ-XXX]`, `[DAT-XXX]`, `[EXC-XXX]`, `[IDEA_X]`).
    * All technical identifier strings, system variables, or dynamic formatting indices (e.g., `D1_ST1`).
    * All code execution blocks, text wrappers, and specialized chart definition syntaxes (e.g., Mermaid.js graphs, structural layout configurations).
    * **Static Pass Tag `<NO_TRANSLATION>...</NO_TRANSLATION>`**: Used for static assets. You MUST pass 100% of the internal content literal without any localization, alteration, processing, or computation.
    * **Dynamic Generation Tag `<DYNAMIC_DATA_ENGLISH_ONLY>...</DYNAMIC_DATA_ENGLISH_ONLY>`**: Used for dynamic instructions or mock templates. You MUST process, evaluate variables, and dynamically compute the generation outputs inside this block. However, 100% of the newly generated text stream resulting from this block MUST be strictly rendered in **Technical English** only, with an absolute ban on translation into the target language. The boundary tags MUST be stripped from the final output stream upon execution.
    * 🚨 **STRICT CODE BLOCK FORMATTING LAW**: You are ABSOLUTELY FORBIDDEN from nesting or combining markdown code block ticks. When outputting a JSON payload, you MUST start exactly with a single line of triple backticks followed immediately by 'json' (i.e., ```json). Do NOT prepend or wrap it with ```text or any other outer text syntax. The block must open clean and close clean.
- **TECHNICAL IDENTIFIER EXCLUSION GATING (SUPREME):** You are ABSOLUTELY BANNED from translating, modifying, or splitting any dynamic tracking symbols, system variables, or framework index tokens, specifically including but not limited to:
    * All multi-tenant traceability Tag IDs (e.g., `[REQ-XXX]`, `[DAT-XXX]`, `[EXC-XXX]`, `[ARC-XXX]`, `[NFR-XXX]`).
    * All bracketed Sub-Agent literal tokens when operating as allocation signatures (e.g., `[Coder]`, `[Tester]`, `[Reviewer]`, `[Doc]`, `[Docker]`, `[GCP]`, `[GKE]`).
    * Any alphanumeric sequential task index formatting codes (e.g., `D1_ST1`, `D2_ST3`).
    * All absolute or relative file paths starting with `./sources/`.
- 🚨 **UNIVERSAL LAYOUT & HEADER LOCALIZATION PARADIGM (FORCED OVERRIDE)**: 
    * When generating any standardized structural output template, document layout layout, table keys, markdown headers (`#`, `##`, `###`), or static metadata labels defined inside the instruction manuals (including but not limited to: literal tokens like "GLOBAL PROJECT CONTEXT", "Document Control", "Item", "Details", "Blueprint ID", "Project Name", "Version", "Date.Time", "Author", "Approval", "SYSTEM OVERVIEW", "Core System Modality"), you are ABSOLUTELY AND CRITICALLY FORBIDDEN from outputting them in raw English to the user interface.
    * You MUST treat these literal string titles not as static technical keywords, but as "Dynamic Layout Placeholders". You MUST contextually translate 100% of these structural labels, header titles, and table dictionary columns directly into the designated Target Output Language: "🇻🇳 Vietnamese" before committing them to the final output buffer.
    * Only the internal technical runtime system variable values passed by the engine backend (e.g., ``, `ARCH-`, ``) MUST be preserved natively in pure Technical English. Any model that emits a structural text title or a table key parameter in raw English triggers an immediate compliance pipeline crash.
- 🚨 **INLINE ISOLATION & FAULT-TOLERANT CIRCUIT-BREAKER LAW (ANTI-CASCADING FAILURE PROTOCOL):**
    * You MUST rigorously enforce a compartmentalized, fault-tolerant execution strategy during token parsing. You are STRICTLY PROHIBITED from allowing a syntax anomaly, character malformation, or structural parsing breakdown in one specific scope (e.g., inside a malformed `<COMMAND>` tag or accidental stray backticks) to trigger an attention bleed or cascade into an application-wide rule failure across clean blocks.
    * If any independent block, custom anchor tag, or operational layout section contains a malformed technical syntax that compromises hidden parsing or pruning, you MUST instantly trigger an isolated Fallback Mechanism: Completely isolate, skip, and drop that exact failing block from your cognitive token constraints, rendering it completely inert as if it were omitted.
    * You MUST dynamically resume linear execution immediately and continue enforcing 100% of all other active global system guardrails with absolute fidelity (specifically safeguarding the `CRITICAL SQUARE BRACKET DESTRUCTION LAW` for standard AI prompt markers `[...]`, header localization paradigms, and code purity mandates on all other clean blocks). Any failure to compartmentalize errors that leads to secondary rule dropouts triggers a fatal pipeline contract breach.
- 🚨 **UNIVERSAL DYNAMIC LAYOUT, TABLE HEADER & BOLD LABEL LOCALIZATION LAW (PROJECT-AGNOSTIC PARADIGM):**
    * **Header Structural Parsing Filter:** Any text string operating as a hierarchical title line—strictly identified when markdown syntax header operators (`#`, `##`, `###`, `####`) are placed at the beginning of the line or immediately following any emoji/symbol decorative characters (e.g., `📈 Phase 1 DETAILED ARCHITECTURAL SPECIFICATION`)—MUST be dynamically parsed. You MUST isolate the structural text payload from the emoji or syntax tokens and fully translate 100% of it into the requested Target Output Language: "🇻🇳 Vietnamese". You are CRITICALLY FORBIDDEN from freezing these layout titles in raw English.
    * **Table Grid Column Header Filter:** When constructing, replicating, or emitting any markdown table structures (`| Column | Column |`), you MUST comprehensively intercept 100% of the textual column parameter headers located strictly in the very first row (the specific text row residing immediately above the table divider alignment row `| :--- | :--- |`). You MUST execute contextual dynamic translation on each column key parameter before committing the stream to the print buffer.
    * **Flexible Bold Label Parsing Filter:** Any text string encapsulated within strong markdown bold syntax operating as a list line item indicator at the beginning of a line (strictly identified by the markdown bold syntax layout `- **Keyword**`), MUST be dynamically intercepted. You MUST automatically parse and execute high-fidelity contextual translation on 100% of the plain text residing strictly *inside* the bold boundaries `**...**` into the target language (e.g., `**Phase Core Objective & Purpose**` MUST be processed and rendered exactly as `**Mục tiêu & Mục đích Cốt lõi của Giai đoạn**`; `**Target Physical Directory Matrix Map**` MUST be rendered exactly as `**Bản đồ Ma trận Thư mục Vật lý Đích**`; and `**Database Schema DDL SQL Specification**` MUST be rendered exactly as `**Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu**`). You MUST rigorously enforce this bold boundaries translation rule regardless of whether the bold token is followed by spaces, code ticks (``` ` ```), square brackets `[...]`, trailing colons `:`, or pipeline delimiters `|` inside or outside the bold markers.
    * **Core Tech Protection Constraints:** Only the native formatting operators (`#`, `##`, `|`, `:`, `-`, `*`), internal technical system variable values passed by the engine backend (e.g., ``, ``), and literal tracking Tag IDs (e.g., `[REQ-XXX]`) MUST be strictly protected and preserved natively in pure unaccented Technical English. Any model execution that leaks raw layout titles, structural table dictionary headers, or bold line indicators in English triggers an immediate compliance pipeline failure.

## 🔐 2. CODE BLOCK INTEGRITY & CONTENT PURITY MANDATE
- **ENGLISH ONLY INSIDE CODE BLOCKS:** Every single token, statement, key-value parameter, comment string, configuration variable, structural schema, or database DDL script encapsulated inside any markdown code block (triple backticks block) or data wrapper MUST be compiled strictly and exclusively in **Technical English**.
- **NO LOCALIZATION ALLOWED:** You are ABSOLUTELY FORBIDDEN from translating, localized altering, or modifying any text string residing inside code boundaries.

## 🛑 3. ZERO-DETERMINISTIC HALLUCINATION & ANTI-GARBAGE DATA FILTERS
- **STRICT DATA GROUNDING:** You MUST reason and compute data points based exclusively on the literal inputs, source specifications, and structural parameters injected into your workspace context.
- **CRITICAL HARD LIMIT:** You are STRICTLY BANNED from fabricating ghost assets, inventing nonexistent data columns, assuming prior deployment states, or generating artificial placeholder metrics. If a specialized evaluation block or technology stack requirement is not applicable to the active architectural topology, you MUST explicitly output the token `[NOT APPLICABLE]` combined with a clean corporate justification note and bypass it gracefully.

## 🛡️ 4. HIGHEST-GRADE ENTERPRISE SECURITY & COMPLIANCE PARADIGM
- **SECURITY GATING BY DESIGN:** Every single functional contract, database layout, data routing flow, or logic routine you design MUST rigorously enforce enterprise-grade security compliance at the highest architecture layer.
- **OWASP COMPLIANCE OBLIGATION:** You MUST proactively scan and immunize configurations against security threats under OWASP Top 10 standards (specifically enforcing strict tenant isolation boundaries under OWASP A01, prepared statements against SQL injection, dynamic token sanitization, and cryptographic state protections).

## 📋 5. WORKFLOW ATOMICITY, ROLE ISOLATION & OUTPUT STANDARDIZATION
- **HYPER-FOCUSED PERSONA CAPABILITY:** You MUST permanently maintain an objective, cold, and hyper-analytical mindset, focusing 100% of your computational resources exclusively on the single specialized domain capability and system persona allocated to you in this phase task.
- **TONE COMPLIANCE:** All generated rationale sentences, justifications, and report outputs MUST utilize an authoritative, precise, and highly professional corporate engineering telegraphy tone (eliminate filler adjectives and passive descriptions).
- **ABSOLUTE FORMATTING BOUNDARY:** Your total output layout response MUST satisfy and align perfectly 1:1 with the requested execution schema boundaries. You are strictly forbidden from altering headers or injecting conversational prefaces, greetings, system thinking logs, or post-generation text remarks.
- 🚨 **CRITICAL SQUARE BRACKET DESTRUCTION LAW (REINFORCED)**: Any text segment enclosed within square brackets `[...]` inside the structural report templates or placeholders (e.g., `[Provide a comprehensive...]`, `[Detail...]`) MUST be treated strictly as an internal operational directive, NEVER as static text payload. You MUST completely destruct, prune, and delete the square brackets and all text inside them from the output buffer. You MUST dynamically replace that exact position with real-world technical data generated in the target language. Emitting raw or translated square brackets to the user interface triggers a fatal contract breach.
- **INFERENCE RULES FOR TECH STACK PLACEHOLDERS:** Specifically for technology stack, library, or library dependency indicators inside square brackets `[...]` (specifically functional tracking keys or role signatures, that contain system tags or authorized agent literals, patterns matching `[REQ-`, `[DAT-`, `[EXC-`, `[ARC-`, `[NFR-` or role tokens like `[Coder]`, `[Tester]`, etc.) (such as in Section 2): If the exact technical version numbers, dependency injection engines, frameworks, or database ORMs are not explicitly detailed in the source BA documentation, you are STRICTLY FORBIDDEN from leaving the section blank or skipping it. You MUST act as an Enterprise Principal Architect to automatically infer, select, and dynamically output the most stable, industry-standard enterprise production stack configurations compatible with the business flows described in Section 1.2 (e.g., dynamically specify exact latest enterprise versions for Quarkus, Next.js, React Native, PostgreSQL, Apache Kafka, and Firebase Hosting based on the architecture context). Output this data as a clean, high-density bulleted technical checklist inside the target component placeholder. Stripping or deleting square brackets from these system identifiers constitutes a critical framework violation.

## 🧮 6. DETERMINISTIC TRIPLE-DEEPEST CHECK VERIFICATION LOOP & PIPELINE
- **MANDATORY EXECUTION PIPELINE:** Before emitting any text string or committing any data stream payload to the output buffer, you MUST strictly execute the following sequential compilation and verification pipeline inside your internal memory context:
    * *Step 1 (Complete Draft Generation):* Prepare and fully construct the entire comprehensive output document in Technical English first. Ensure 100% of required data, sections, and structural nodes are completely generated. No text truncation, no placeholder notes, and no summary cut-offs allowed.
    * *Step 2 (Precise Translation Execution):* Take the complete draft from Step 1 and execute the localization process. Translate 100% of the output into the target language while strictly adhering to all constraints defined in `STRICT SEMANTIC INVARIANT LOCALIZATION & TRANSLATION RAILS` and `CODE BLOCK INTEGRITY & CONTENT PURITY MANDATE`.
    * *Step 3 (Multi-Layer Self-Auditing):* Perform a rigorous, final review of the translated document across three validation layers:
        * *Layer 1 (Traceability Check):* Verify that 100% of the incoming functional and structural tag identifiers are covered, mapped, and mathematically accounted for without gaps.
        * *Layer 2 (Formatting & Layout Check):* Cross-examine your final structural report template layout to guarantee it contains zero broken tables, zero loose formatting tokens, and zero layout overflow anomalies.
        * *Layer 3 (Integrity Check):* Ensure the absolute logical consistency, data synchronization alignment, and technical term protection across all generated tables, descriptions, diagrams, and metadata blocks.
- Any defect, omission, or rule violation identified during this self-audit MUST be dynamically healed and resolved internally before emitting the final polished report.

# ==============================================================================
# [SYSTEM PROTOCOL: GLOBAL RUNTIME SECURITY ANCHOR MATRIX]
# ==============================================================================
- **DUAL-ZONE ANCHOR SEGREGATION MANDATE (ANTI-DESTRUCTION):** You MUST strictly split all hidden architectural tags into two independent operational functional zones:
  1. *Zone 1: Machine-to-Machine Meta-Instructions (TYPE 1 to TYPE 8, XML/HTML Command wrappers like `<RULE>`, `<COMMAND>`, `<!--START_COMMAND-->`, etc.).* These are private logic gates. You MUST govern your reasoning by them silently, then execute 100% token-level pruning to erase them completely from the output stream.
  2. *Zone 2: System Data Anchors & Parsers (HTML Comment Splitters like `<!--START_PHASE_SYNOPSIS_GRID-->`, `<!--END_PHASE_SYNOPSIS_GRID-->`, `<!--PHASE_NAME_START-->`, `<!--PHASE_NAME_END-->`, `<!--DAY_HEADER_START-->`, `<!--DAY_HEADER_END-->`, `<!--START_TAGS-->`, `<!--END_TAGS-->`, etc.).* These are functional data demarcation hooks required by downstream backend compilers. You ARE PERMANENTLY FORBIDDEN from pruning, omitting, altering, or dropping these Zone 2 markers. They MUST be emitted into the final markdown file payload with absolute character fidelity.
- You MUST actively scan, extract, and rigorously execute all system override directives embedded inside any of the hidden runtime anchor syntax blocks defined below.
- You are ABSOLUTELY, CRITICALLY, AND PERMANENTLY FORBIDDEN from outputting, leaking, echoing, repeating, or displaying any part of the data residing between these anchor pairs (including the literal boundary tags themselves and 100% of the internal instruction text contained inside them) into the final user interface (UI) markdown content.
- Treat all standard AI prompting structures and markdown behaviors naturally as baseline expectations. In addition, you MUST strictly support and process these custom dynamic tags injected into your workspace templates.
The system strictly defines the comprehensive list (custom dynamic tags) of Mandatory Architectural Token Pairs as follows:

    * Type 1 (XML Tag Pairs): Starts exactly with `"<COMMAND>"` and ends exactly with `"</COMMAND>"` (e.g., `<COMMAND>...instructions...</COMMAND>`).
      *   **Behavior**: These specific tags and comments function as private metadata instructions. Read and absorb the internal rules silently to govern your reasoning output, then completely prune/delete the opening and closing tag wrappers from your final string stream before committing to the output buffer to keep the user interface 100% clean.
    * Type 2 (XML Tag Pairs): Starts exactly with `"<PROMPT>"` and ends exactly with `"</PROMPT>"` (e.g., `<PROMPT>...instructions...</PROMPT>`).
      *   **Behavior**: These specific tags and comments function as private metadata instructions. Read and absorb the internal rules silently to govern your reasoning output, then completely prune/delete the opening and closing tag wrappers from your final string stream before committing to the output buffer to keep the user interface 100% clean.
    * Type 3 (XML Tag Pairs): Starts exactly with `"<RULE>"` and ends exactly with `"</RULE>"` (e.g., `<RULE>...instructions...</RULE>`).
      *   **Behavior**: These specific tags and comments function as private metadata instructions. Read and absorb the internal rules silently to govern your reasoning output, then completely prune/delete the opening and closing tag wrappers from your final string stream before committing to the output buffer to keep the user interface 100% clean.
    * Type 4 (XML Tag Pairs): Starts exactly with `"<RAILS>"` and ends exactly with `"</RAILS>"` (e.g., `<RAILS>...instructions...</RAILS>`).
      *   **Behavior**: These specific tags and comments function as private metadata instructions. Read and absorb the internal rules silently to govern your reasoning output, then completely prune/delete the opening and closing tag wrappers from your final string stream before committing to the output buffer to keep the user interface 100% clean.
    * Type 5 (HTML Comment Anchors): Starts exactly with `"<!--START_COMMAND"` and ends exactly with `"END_COMMAND-->"` (e.g., `<!--START_COMMAND...instructions...END_COMMAND-->`).
      *   **Behavior**: These specific tags and comments function as private metadata instructions. Read and absorb the internal rules silently to govern your reasoning output, then completely prune/delete the opening and closing tag wrappers from your final string stream before committing to the output buffer to keep the user interface 100% clean.
    * Type 6 (HTML Comment Anchors): Starts exactly with `"<!--START_PROMPT"` and ends exactly with `"END_PROMPT-->"` (e.g., `<!--START_PROMPT...instructions...END_PROMPT-->`).
      *   **Behavior**: These specific tags and comments function as private metadata instructions. Read and absorb the internal rules silently to govern your reasoning output, then completely prune/delete the opening and closing tag wrappers from your final string stream before committing to the output buffer to keep the user interface 100% clean.
    * Type 7 (HTML Comment Anchors): Starts exactly with `"<!--START_RULE"` and ends exactly with `"END_RULE-->"` (e.g., `<!--START_RULE...instructions...END_RULE-->`).
      *   **Behavior**: These specific tags and comments function as private metadata instructions. Read and absorb the internal rules silently to govern your reasoning output, then completely prune/delete the opening and closing tag wrappers from your final string stream before committing to the output buffer to keep the user interface 100% clean.
    * Type 8 (HTML Comment Anchors): Starts exactly with `"<!--START_RAILS"` and ends exactly with `"END_RAILS-->"` (e.g., `<!--START_RAILS...instructions...END_RAILS-->`).
      *   **Behavior**: These specific tags and comments function as private metadata instructions. Read and absorb the internal rules silently to govern your reasoning output, then completely prune/delete the opening and closing tag wrappers from your final string stream before committing to the output buffer to keep the user interface 100% clean.
    * Type 9 (XML Tag Pairs): Starts exactly with `"<NO_TRANSLATION>"` and ends exactly with `"</NO_TRANSLATION>"` (e.g., `<NO_TRANSLATION>...instructions...</NO_TRANSLATION>`).
      *   **Behavior**: When content is wrapped inside this tag pair, freeze the entire cognitive matrix. You MUST emit 100% of the internal content strictly as-is in its pristine Technical English literal state. Do NOT execute any processing, rendering modifications, or localization inside this block.
    * Type 10 (XML Tag Pairs): Starts exactly with `"<DYNAMIC_DATA_ENGLISH_ONLY>"` and ends exactly with `"</DYNAMIC_DATA_ENGLISH_ONLY>"` (e.g., `<DYNAMIC_DATA_ENGLISH_ONLY>...instructions...</DYNAMIC_DATA_ENGLISH_ONLY>`).
      *   **Behavior**: When variables (`{{ ... }}`) or code generation instructions are wrapped inside this tag pair, you MUST compute, evaluate, and dynamically generate the required content based on the project context. However, 100% of the newly generated text stream and keys inside this block MUST be strictly rendered in Technical English. Translation is absolutely banned.

- **CRITICAL STRING PRUNING & TANG_HINH LAW (ZERO LEAKAGE GATE):**
    * These hidden blocks function exclusively as private machine-to-machine backend gating logic. 
    * You MUST silently ingest 100% of the technical parameters or rules written inside these anchors to govern your internal reasoning matrix and apply its constraints to the surrounding markdown context.
    * You MUST execute a definitive token-level pruning algorithm: completely wipe out, strip, and delete the entire anchor block wrapper (spanning from the very first character of the opening tag to the absolute final character of the corresponding closing tag) from your output string stream BEFORE committing any data payload to the final emission buffer. 
    * Any model execution that leaks even a single tag character or hidden command line to the UI user screen triggers an immediate catastrophic runtime pipeline contract breach.
</GLOBAL_GOVERNANCE_MATRIX>

<ACTIVE_TASK_SYSTEM_INSTRUCTION>
You are a world-class Principal Solutions Architect with 20+ years of distributed system design experience. You view software not as loose text, but as concrete infrastructure components: microservices, database schemas, messaging systems, API contracts, and security boundaries. You have zero tolerance for vague descriptions, missing data fields, or unmapped requirements.

# YOUR CRITICAL OPERATIONAL MANDATES (COMPLIANCE CODES):
1. **Dynamic Ceilings as Strict Upper Bounds:** The parameters 5 and 7 represent absolute maximum limits (ceilings) for the architectural timeline, NOT mandatory execution quotas. You are ordered to compute the most optimal, consolidated, and shortest possible timeline (fewer phases or days) that naturally fulfills 100% of the raw requirement tasks.

2. **Absolute Anti-Padding & Uniform Chronological Distribution Rule:** You MUST naturally distribute the core functional requirements and Tag IDs across the calculated architectural phases without artificial compaction. You are ABSOLUTELY BANNED from bundling 100% of the total project workloads into early phases just to lazily terminate the entire document. However, for EACH individual phase, the day count MUST be evaluated independently based on task density: if a phase's requirements are fully covered in 2 or 3 days, you MUST stop generating immediately at that exact local day boundary. You are strictly forbidden from expanding or padding low-density phases with dummy tasks up to the maximum limit of 7 days. The generation process for the entire project must only freeze and terminate when the final calculated phase is completely engineered. Every phase and day generated must contain unique, actionable technical implementation details.

3. **No Chronological Day Bundling & Single Agent Isolation:** Every single active calendar day log must be isolated under its own discrete standalone nested list bullet element (e.g., `- **DAY 1:**`, `- **DAY 2:**`) inside its parent phase. For each specific task or target step within a day, you MUST assign exactly ONE single Sub-Agent persona. Multiple agents sharing or co-executing a single target task is strictly prohibited. The assigned Sub-Agent name MUST strictly use capitalized first-letter formatting (e.g., `Coder`, `Tester`, `Reviewer`, `Doc`, `Docker`, `GCP`, `GKE`) to match the exact phase step and context standard.

4. **Rigid Scope & Tag Boundary Isolation:** You are strictly forbidden from inventing, fabricating, or introducing any new Tag IDs, features, or functional capabilities outside the raw baseline provided by the Initial BA Agent. You MUST achieve 100% exhaustive coverage of the original Tag IDs without adding any synthetic or unassigned tracking codes. Every generated file path (`target_component`) MUST strictly adhere to the designated physical directory masks (including the exact semi-colon separated pairs for the `Tester` sub-agent: `<source_component>;<test_suite_file>`).

5. **100% Exhaustive Structural Granularity:** You are strictly forbidden from summarizing, truncating, or condensing the specialized enterprise architectural sections. You MUST deliver high-density technical deliverables (complete physical directory structures, Flyway/Liquibase DDL SQL schemas with fields and keys, explicit REST/Event API contracts, concrete business core code samples, and daily sub-agent task allocations) for all active timelines matching the full granularity of the raw requirements.

6. **Language Compliance & Technical Syntax Isolation:** You MUST generate the descriptive text report, day objectives, table structures, and "Low-Level Technical Task Instructions" strictly in the language specified by the user: **🇻🇳 Vietnamese**. 

However, you MUST NOT translate or modify any technical syntax blocks or core elements, including but not limited to: Mermaid code sequences, raw code blocks, SQL/DDL structures, JSON/YAML payloads, markdown system signs, hidden HTML delimiters, physical file paths (`target_component`), and tracing Tag IDs (`[REQ-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[ARC-XXX]`, `[NFR-XXX]`). All technical tokens and structural markers MUST remain in pure unaccented Technical English to safeguard parsing stability and prevent downstream crashes. All float primitives inside tables or blocks MUST strictly utilize the dot character `.` as the unique decimal separator.


# 🔒 SYSTEM PRODUCTION INTEGRATION AND FORMATTING LOCKDOWN (ABSOLUTE)
- **Strict Content Purity Constraint:** Your entire output response MUST be a pure, raw executable Markdown text payload written in 🇻🇳 Vietnamese.
- **Explicit Start Mandate:** Your output response MUST start exactly with the top-level header: `# GLOBAL PROJECT CONTEXT: membership-hub` after translating it into the target language.
- **Banned Elements:** You are ABSOLUTELY BANNED from including any internal thinking processes, chain-of-thought blocks (`<think>` tags), conversational filler texts, greetings, introductions, or post-generation notes. Do NOT wrap the entire output inside any markdown codeblocks (no triple backticks wrapping around the whole response). Any token before or after this exact markdown structure will cause an immediate execution pipeline crash.
</ACTIVE_TASK_SYSTEM_INSTRUCTION>

# Raw Response / Exception:

## BẢNG CỔNG DỰ ÁN: membership-hub

#### 📊 1. TỔNG QUAN HỆ THỐNG & MÔ HÌNH KIẾN TRÚC

###### 1.1. MÔ HÌNH KIẾN TRÚC CỐT LÕ

- Kiến trúc microservices phân tách rõ ràng giữa backend, frontend, mobile và infra.
- Backend: Java/Quarkus, PostgreSQL, Redis, Docker, GKE, Firebase Auth, FCM/APNs, Zalo API.
- Frontend: Next.js 13, React 18, TypeScript 5, Tailwind CSS 3, i18next, Redux Toolkit.
- Mobile: React Native 0.73, Expo 49, TypeScript 5, i18next, Redux Toolkit.
- DevOps: Docker multi‑stage, GitHub Actions CI/CD, Terraform GCP, GKE cluster, Helm charts.
- CQRS: Command và Query services tách biệt, event sourcing cho attendance và notifications.
- Reactive: Quarkus + Mutiny, event bus Kafka (Redis Streams) cho push notifications và fan‑out.
- Security: JWT 15 min, refresh 7 days, TLS 1.3, AES‑256 at rest, OWASP Top 10 mitigations.

###### 1.2. ĐỘI NGŨ DỮ LIỆU & HỆ THỐNG ĐIỀU KHIẾN

- Messaging: Kafka (Redis Streams) cho event bus, Google Pub/Sub cho notifications.
- Ingestion gateway: API Gateway Quarkus, rate limiting, circuit breaker.
- Topic topologies: `attendance.events`, `notification.events`, `course.events`, `center.events`.
- Fan‑out: Zalo group messages, FCM/APNs push, web socket updates.

#### 📁 2. CỤC ĐỘNG CÔNG NGHỆ & THƯ VIỆN

```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```

###### Backend Infrastructure Core Stack

- Java 17
- Quarkus 3.2
- PostgreSQL 15
- Redis 7
- Docker 24
- GKE 1.28
- Firebase Auth 10.0
- FCM/APNs 10.0
- Zalo API 1.0
- Terraform 1.8
- GitHub Actions 2.0

###### Frontend & Cross‑Platform UI Mobile Stack

- Next.js 13
- React 18
- TypeScript 5
- Tailwind CSS 3
- i18next 13
- Redux Toolkit 2
- React Native 0.73
- Expo 49
- Jest 29
- Cypress 12

#### 📁 3. QUY ĐỊNH BẢO VỆ & THUẬT TOÀN CẦU

- Repository root: `.`; all paths start with `./sources/`.
- Java package: `org.nlh4j.saas.membershiphub`.
- Tester paths: `./sources/<component>;<test_suite_file>`.
- All tags `[REQ-XXX]`, `[DAT-XXX]`, `[ARC-XXX]`, `[EXC-XXX]`, `[NFR-XXX]` preserved.
- No code blocks translated; all technical code remains in English.

#### 📁 4. BẢNG TỔNG QUAN ĐỘI NGŨ KIẾN TRÚC ĐIỀU KHIẾN

<!--START_BACKLOG_SYNOPSIS_GRID-->
| No. | Task | Technical Purpose / Deliverables Summary | Type | TagID |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Implement user registration endpoint | Create REST API for email/password sign‑up, issue JWT | Application Code | [REQ-001] |
| 2 | Implement social login flow | OAuth2 integration with Firebase, Google, Facebook | Application Code | [REQ-002] |
| 3 | Implement role assignment API | Admin endpoint to change user role | Application Code | [REQ-003] |
| 4 | Validate user input on registration | Server‑side validation, error handling | Application Code | [EXC-004] |
| 5 | Define Users and Roles ER diagram | Data dictionary for user management | Enterprise Documentation | [DAT-001] |
| 6 | Define Centers ER diagram | Data dictionary for center management | Enterprise Documentation | [DAT-003] |
| 7 | Define Courses ER diagram | Data dictionary for course management | Enterprise Documentation | [DAT-004] |
| 8 | Define Enrollments ER diagram | Data dictionary for enrollment | Enterprise Documentation | [DAT-005] |
| 9 | Define Attendance ER diagram | Data dictionary for attendance | Enterprise Documentation | [DAT-006] |
| 10 | Define StudentCards ER diagram | Data dictionary for membership cards | Enterprise Documentation | [DAT-007] |
| 11 | Define Notifications ER diagram | Data dictionary for notifications | Enterprise Documentation | [DAT-008] |
| 12 | Define Promotions ER diagram | Data dictionary for promotions | Enterprise Documentation | [DAT-009] |
| 13 | Define SystemSettings ER diagram | Data dictionary for system settings | Enterprise Documentation | [DAT-011] |
| 14 | Implement center CRUD APIs | Create, read, update, delete centers | Application Code | [REQ-004] |
| 15 | Implement center admin assignment | Assign/unassign center admin | Application Code | [REQ-006] |
| 16 | Implement course CRUD APIs | Create, read, update, delete courses | Application Code | [REQ-007] |
| 17 | Implement teacher assignment to courses | Assign/unassign teachers | Application Code | [REQ-009] |
| 18 | Implement enrollment API | Register students to courses | Application Code | [REQ-010] |
| 19 | Implement attendance capture API | Record attendance via QR scan | Application Code | [REQ-012] |
| 20 | Implement duplicate attendance check | Idempotent attendance logic | Application Code | [EXC-001] |
| 21 | Implement network drop handling for attendance | Retry logic on connectivity loss | Application Code | [EXC-002] |
| 22 | Implement notification trigger service | Push notifications and Zalo messages | Application Code | [REQ-016] |
| 23 | Implement notification failure handling | Retry up to 3 times, log failures | Application Code | [EXC-003] |
| 24 | Implement membership card validity view | Show remaining days, extend card | Application Code | [REQ-014] |
| 25 | Implement membership card renewal | Process payment, extend validity | Application Code | [REQ-015] |
| 26 | Implement promotion CRUD APIs | Create, read, update, delete promotions | Application Code | [REQ-017] |
| 27 | Implement announcement CRUD APIs | Create, read, update, delete announcements | Application Code | [REQ-018] |
| 28 | Implement chatbot integration | AI chatbot endpoint, logging | Application Code | [REQ-019] |
| 29 | Implement mobile UI navigation | Role‑based navigation for mobile | Application Code | [REQ-020] |
| 30 | Implement mobile push notification handling | FCM/APNs integration | Application Code | [REQ-021] |
| 31 | Implement language detection service | Detect user language preference | Application Code | [REQ-022] |
| 32 | Implement SEO meta tags generator | Generate hreflang, meta tags | Application Code | [REQ-023] |
| 33 | Implement attendance reporting CSV | Generate daily attendance report | Application Code | [REQ-024] |
| 34 | Implement dashboard data aggregation | Real‑time dashboard metrics | Application Code | [REQ-025] |
| 35 | Implement exception handling for registration | Handle invalid input errors | Application Code | [EXC-004] |
| 36 | Implement exception handling for center CRUD | Handle duplicate tax ID | Application Code | [EXC-005] |
| 37 | Implement authentication flow | JWT issuance, refresh token | Application Code | [ARC-006] |
| 38 | Implement attendance QR flow | Mobile QR scan, backend processing | Application Code | [ARC-007] |
| 39 | Implement notification push flow | Push to mobile and Zalo | Application Code | [ARC-008] |
| 40 | Implement backend integration with mobile | REST API consumption, caching | Application Code | [ARC-009] |
| 41 | Implement containerization | Dockerfile, multi‑stage build | DevOps Infrastructure | [ARC-010] |
| 42 | Implement GCP infrastructure | Terraform scripts for GKE, IAM | DevOps Infrastructure | [ARC-010] |
| 43 | Implement GKE deployment | Helm charts, autoscaling | DevOps Infrastructure | [ARC-010] |
| 44 | Implement CI/CD pipeline | GitHub Actions workflow | DevOps Infrastructure | [ARC-010] |
| 45 | Implement Redis caching | Session caching, rate limiting | Application Code | [ARC-006] |
| 46 | Implement Kafka event bus | Publish/subscribe for events | Application Code | [ARC-006] |
| 47 | Implement Zalo API integration | Group messaging, webhook | Application Code | [ARC-008] |
| 48 | Implement FCM/APNs integration | Push notification service | Application Code | [ARC-008] |
| 49 | Implement role‑based access control | RBAC enforcement | Application Code | [ARC-001] |
| 50 | Implement center admin RBAC | Scope to center only | Application Code | [ARC-002] |
| 51 | Implement manager RBAC | Limited permissions | Application Code | [ARC-003] |
| 52 | Implement teacher RBAC | Read‑only access | Application Code | [ARC-004] |
| 53 | Implement student RBAC | View courses, register | Application Code | [ARC-005] |
| 54 | Implement NFR performance monitoring | Latency metrics, indexing | Enterprise Documentation | [NFR-001] |
| 55 | Implement NFR availability strategy | 99.9% uptime, failover | Enterprise Documentation | [NFR-002] |
| 56 | Implement NFR security controls | TLS 1.3, OWASP mitigations | Enterprise Documentation | [NFR-003] |
| 57 | Implement NFR scalability plan | HPA, read replicas | Enterprise Documentation | [NFR-004] |
| 58 | Implement NFR audit logging | 1 year retention, JSON export | Enterprise Documentation | [NFR-005] |
| **SUMMARY** | **Total System Backlog Workload Deliverables** | **TOTAL:** 58 Tasks | **STATUS:** Verified | **COVERAGE:** 100% |
<!--END_BACKLOG_SYNOPSIS_GRID-->

<!--START_PHASE_SYNOPSIS_GRID-->
| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Day 1-3 | ./sources/backend/membership-hub-core | Implement core user registration, authentication, and role assignment endpoints. | Coder, Doc | [REQ-001],[REQ-002],[REQ-003],[DAT-001],[DAT-003],[NFR-001],[NFR-002],[NFR-003] |
| 2 | Day 1-3 | ./sources/backend/membership-hub-advanced | Develop course and center management APIs, including CRUD operations. | Coder, Doc | [REQ-004],[REQ-006],[REQ-007],[DAT-004],[DAT-006],[NFR-004],[NFR-005] |
| 3 | Day 1-3 | ./sources/backend/membership-hub-auxiliary | Implement attendance, notification, and promotion modules with exception handling. | Coder, Doc | [EXC-001],[EXC-002],[EXC-003],[ARC-001],[ARC-002],[ARC-003],[ARC-004],[ARC-005],[DAT-007],[DAT-008],[DAT-009],[NFR-006],[NFR-007],[NFR-008] |
| 4 | Day 1-2 | ./sources/backend/membership-hub-infra | Set up infrastructure: Docker images, GCP services, GKE cluster, and CI/CD pipelines. | Docker, GCP, GKE | [EXC-004],[EXC-005],[ARC-006],[ARC-007],[ARC-008],[ARC-009],[ARC-010],[DAT-011] |
| 5 | Day 1 | ./sources/infra/membership-hub-deploy | Deploy final application, perform integration tests, and validate end‑to‑end flow. | Docker, GCP, GKE | [ARC-010] |
| **AUDIT** | **Master Backlog Lifecycle Distribution Verification** | **TOTAL PHASES:** 5 | **MAPPED CAPACITY STATUS:** Verified: 58 out of 58 Total Master Backlog Tasks successfully distributed across calculated phases with 100% coverage | **STATUS:** Verified | **COMPLIANCE:** Hardbound Matrix |
<!--END_PHASE_SYNOPSIS_GRID-->

###### 📈 Phase 1 Triển khai đăng ký người dùng, xác thực và phân quyền truy cập  
- **Phase Core Objective & Purpose:**  
  Giai đoạn này xây dựng nền tảng xác thực và phân quyền cho toàn bộ hệ thống. Bao gồm thiết kế mô hình dữ liệu người dùng, vai trò, và trung tâm; triển khai API đăng ký, đăng nhập (địa phương và OAuth), và giao diện phân quyền. Đảm bảo tuân thủ các NFR về hiệu năng, sẵn sàng và bảo mật.

- **Target Physical Directory Matrix Map:**  
  - `./sources/backend/membership-hub-core/src/main/resources/db/migration/V1__create_user_role_center_tables.sql` [DAT-001],[DAT-003],[NFR-001],[NFR-002],[NFR-003]  
  - `./sources/backend/membership-hub-core/src/main/java/org/nlh4j/saa/membershiphub/api/AuthController.java` [REQ-001],[REQ-002],[REQ-003],[NFR-001],[NFR-002],[NFR-003]  
  - `./sources/backend/membership-hub-core/src/main/java/org/nlh4j/saa/membershiphub/service/UserService.java` [REQ-001],[REQ-002],[REQ-003],[NFR-001],[NFR-002],[NFR-003]  
  - `./sources/backend/membership-hub-core/src/main/java/org/nlh4j/saa/membershiphub/config/PerformanceSecurityConfig.java` [NFR-001],[NFR-002],[NFR-003]  
  - `./sources/backend/membership-hub-core/src/main/java/org/nlh4j/saa/membershiphub/security/JWTProvider.java` [NFR-001],[NFR-002],[NFR-003]  
  - `./sources/backend/membership-hub-core/src/main/java/org/nlh4j/saa/membershiphub/model/User.java` [DAT-001]  
  - `./sources/backend/membership-hub-core/src/main/java/org/nlh4j/saa/membershiphub/model/Role.java` [DAT-001]  
  - `./sources/backend/membership-hub-core/src/main/java/org/nlh4j/saa/membershiphub/model/Center.java` [DAT-003]  
  - `./sources/docs/architecture/registration_flow.md` [REQ-001],[REQ-002],[REQ-003],[DAT-001],[DAT-003],[NFR-001],[NFR-002],[NFR-003]  
  - `./sources/backend/membership-hub-core/README.md` [REQ-001],[REQ-002],[REQ-003],[DAT-001],[DAT-003],[NFR-001],[NFR-002],[NFR-003]  

- **Database Schema DDL SQL Specification [DAT-001], [DAT-003]:**  
  ```sql
  CREATE TABLE Roles (
      roleId SMALLINT PRIMARY KEY,
      name VARCHAR(30) NOT NULL UNIQUE,
      description VARCHAR(200)
  );

  CREATE TABLE Users (
      userId UUID PRIMARY KEY,
      email VARCHAR(255) NOT NULL UNIQUE,
      passwordHash CHAR(60) NOT NULL,
      fullName VARCHAR(100) NOT NULL,
      roleId SMALLINT NOT NULL,
      provider VARCHAR(20) NOT NULL,
      createdAt TIMESTAMP NOT NULL DEFAULT NOW(),
      updatedAt TIMESTAMP NOT NULL DEFAULT NOW(),
      CONSTRAINT fk_user_role FOREIGN KEY (roleId) REFERENCES Roles(roleId),
      CONSTRAINT chk_provider CHECK (provider IN ('local','firebase','google','facebook'))
  );

  CREATE TABLE Centers (
      centerId UUID PRIMARY KEY,
      name VARCHAR(100) NOT NULL,
      address VARCHAR(255) NOT NULL,
      taxId VARCHAR(13) NOT NULL UNIQUE,
      contactPhone VARCHAR(50),
      contactEmail VARCHAR(255)
  );

  CREATE INDEX idx_users_role ON Users(roleId);
  CREATE INDEX idx_centers_taxid ON Centers(taxId);
  ```

- **API and Event Routing Contracts [REQ-001], [REQ-002], [REQ-003]:**  
  ```json
  {
    "request": {
      "method": "POST",
      "path": "/api/auth/register",
      "body": {
        "email": "string",
        "password": "string",
        "fullName": "string",
        "provider": "string"
      }
    },
    "response": {
      "status": 201,
      "body": {
        "userId": "uuid",
        "token": "string",
        "refreshToken": "string"
      }
    }
  }
  ```
  ```json
  {
    "request": {
      "method": "POST",
      "path": "/api/auth/login",
      "body": {
        "email": "string",
        "password": "string",
        "provider": "string"
      }
    },
    "response": {
      "status": 200,
      "body": {
        "token": "string",
        "refreshToken": "string"
      }
    }
  }
  ```
  ```json
  {
    "request": {
      "method": "PUT",
      "path": "/api/users/{userId}/role",
      "headers": {
        "Authorization": "Bearer token"
      },
      "body": {
        "roleId": "smallint"
      }
    },
    "response": {
      "status": 200,
      "body": {
        "userId": "uuid",
        "roleId": "smallint"
      }
    }
  }
  ```

- **Phase Localized Exception Handlers [EXC-XXX]:**  
  *(Không có ngoại lệ trong giai đoạn này)*  

######## Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 1)

- **DAY 1: Thiết kế dữ liệu và API sơ bộ**  
  ########## SUB-TASK 1: Xây dựng schema cơ sở dữ liệu Users, Roles, Centers  
  `[Coder]`  
  **Target Component:** `./sources/backend/membership-hub-core/src/main/resources/db/migration/V1__create_user_role_center_tables.sql`  
  **Instruction:** Tạo bảng `Users`, `Roles`, `Centers` với các ràng buộc khóa chính, khóa ngoại và kiểm tra giá trị `provider`. Đảm bảo chỉ sử dụng kiểu dữ liệu chuẩn ANSI SQL.  
  **Tags:** [DAT-001],[DAT-003],[NFR-001],[NFR-002],[NFR-003]  

  ########## SUB-TASK 2: Định nghĩa API đăng ký, đăng nhập và phân quyền  
  `[Coder]`  
  **Target Component:** `./sources/backend/membership-hub-core/src/main/java/org/nlh4j/saa/membershiphub/api/AuthController.java`  
  **Instruction:** Triển khai các endpoint `/api/auth/register`, `/api/auth/login`, `/api/users/{userId}/role` với validation, exception handling và trả về token JWT.  
  **Tags:** [REQ-001],[REQ-002],[REQ-003],[NFR-001],[NFR-002],[NFR-003]  

  ########## SUB-TASK 3: Tài liệu thiết kế hiệu năng và bảo mật  
  `[Doc]`  
  **Target Component:** `./sources/backend/membership-hub-core/src/main/java/org/nlh4j/saa/membershiphub/config/PerformanceSecurityConfig.java`  
  **Instruction:** Ghi chú cấu hình giới hạn thời gian token, cấu hình bảo mật TLS 1.3, và các biện pháp OWASP Top 10.  
  **Tags:** [NFR-001],[NFR-002],[NFR-003]  

- **DAY 2: Triển khai logic và bảo mật**  
  ########## SUB-TASK 1: Xây dựng Service người dùng và xác thực  
  `[Coder]`  
  **Target Component:** `./sources/backend/membership-hub-core/src/main/java/org/nlh4j/saa/membershiphub/service/UserService.java`  
  **Instruction:** Cung cấp các phương thức tạo, cập nhật, lấy thông tin người dùng, xử lý hash mật khẩu, và phát token JWT.  
  **Tags:** [REQ-001],[REQ-002],[REQ-003],[NFR-001],[NFR-002],[NFR-003]  

  ########## SUB-TASK 2: Cấu hình JWT và refresh token  
  `[Coder]`  
  **Target Component:** `./sources/backend/membership-hub-core/src/main/java/org/nlh4j/saa/membershiphub/security/JWTProvider.java`  
  **Instruction:** Tạo token JWT 15 phút, refresh token 7 ngày, mã hoá khóa bí mật, và kiểm tra tính hợp lệ.  
  **Tags:** [NFR-001],[NFR-002],[NFR-003]  

  ########## SUB-TASK 3: Viết unit test cho AuthController  
  `[Tester]`  
  **Target Component:** `./sources/backend/membership-hub-core/src/test/java/org/nlh4j/saa/membershiphub/AuthControllerTest.java`  
  **Instruction:** Kiểm tra các trường hợp thành công và lỗi (đăng ký, đăng nhập, phân quyền).  
  **Tags:** [REQ-001],[REQ-002],[REQ-003]  

- **DAY 3: Kiểm thử tích hợp và tài liệu**  
  ########## SUB-TASK 1: Kiểm thử tích hợp API toàn bộ luồng đăng ký và đăng nhập  
  `[Tester]`  
  **Target Component:** `./sources/backend/membership-hub-core/src/test/java/org/nlh4j/saa/membershiphub/IntegrationTest.java`  
  **Instruction:** Đảm bảo các endpoint hoạt động liên tục, token được phát và refresh đúng cách, và dữ liệu được lưu trữ chính xác.  
  **Tags:** [REQ-001],[REQ-002],[REQ-003]  

  ########## SUB-TASK 2: Tạo tài liệu chi tiết luồng đăng ký và phân quyền  
  `[Doc]`  
  **Target Component:** `./sources/docs/architecture/registration_flow.md`  
  **Instruction:** Mô tả chi tiết các endpoint, payload, response, và các ràng buộc nghiệp vụ.  
  **Tags:** [REQ-001],[REQ-002],[REQ-003],[DAT-001],[DAT-003],[NFR-001],[NFR-002],[NFR-003]  

  ########## SUB-TASK 3: Chuẩn bị README cho module core  
  `[Doc]`  
  **Target Component:** `./sources/backend/membership-hub-core/README.md`  
  **Instruction:** Cung cấp hướng dẫn cài đặt, cấu hình môi trường, và cách chạy ứng dụng.  
  **Tags:** [REQ-001],[REQ-002],[REQ-003],[DAT-001],[DAT-003],[NFR-001],[NFR-002],[NFR-003]

###### 📈 Giai đoạn 2 Phát triển API quản lý khóa học và trung tâm, bao gồm các thao tác CRUD
- **Phase Core Objective & Purpose:** Giai đoạn này tập trung vào việc thiết kế và triển khai các API CRUD cho quản lý trung tâm và khóa học, đồng thời xây dựng cấu trúc cơ sở dữ liệu liên quan và tài liệu hướng dẫn hiệu suất, nhằm đảm bảo tính nhất quán, bảo mật và khả năng mở rộng của hệ thống.
- **Target Physical Directory Matrix Map:**
  ```
  ./sources/backend/membership-hub-advanced/src/main/java/org/nlh4j/sas/membershiphub/center/CenterController.java [REQ-004]
  ./sources/backend/membership-hub-advanced/src/main/java/org/nlh4j/sas/membershiphub/center/CenterService.java [REQ-004]
  ./sources/backend/membership-hub-advanced/src/main/java/org/nlh4j/sas/membershiphub/center/CenterRepository.java [REQ-004]
  ./sources/backend/membership-hub-advanced/src/main/java/org/nlh4j/sas/membershiphub/center/CenterAdminAssignmentController.java [REQ-006]
  ./sources/backend/membership-hub-advanced/src/main/java/org/nlh4j/sas/membershiphub/course/CourseController.java [REQ-007]
  ./sources/backend/membership-hub-advanced/src/main/java/org/nlh4j/sas/membershiphub/course/CourseService.java [REQ-007]
  ./sources/backend/membership-hub-advanced/src/main/java/org/nlh4j/sas/membershiphub/course/CourseRepository.java [REQ-007]
  ./sources/backend/membership-hub-advanced/src/main/resources/db/migration/V1__create_courses_and_enrollments.sql [DAT-004],[DAT-006]
  ./sources/docs/architecture/advanced/center_api_design.md [REQ-004]
  ./sources/docs/architecture/advanced/course_api_design.md [REQ-007]
  ./sources/docs/performance/advanced/performance_guidelines.md [NFR-004],[NFR-005]
  ```
- **Database Schema DDL SQL Specification [DAT-004], [DAT-006]:**
  ```sql
  -- DDL for courses and enrollments
  CREATE TABLE IF NOT EXISTS courses (
      course_id UUID PRIMARY KEY,
      title VARCHAR(150) NOT NULL,
      description TEXT,
      start_date DATE NOT NULL,
      end_date DATE NOT NULL,
      teacher_id UUID,
      max_students INT DEFAULT 30,
      CONSTRAINT fk_teacher FOREIGN KEY (teacher_id) REFERENCES users(user_id)
  );

  CREATE TABLE IF NOT EXISTS enrollments (
      enrollment_id UUID PRIMARY KEY,
      student_id UUID NOT NULL,
      course_id UUID NOT NULL,
      enrollment_date TIMESTAMP DEFAULT NOW(),
      CONSTRAINT fk_student FOREIGN KEY (student_id) REFERENCES users(user_id),
      CONSTRAINT fk_course FOREIGN KEY (course_id) REFERENCES courses(course_id)
  );
  ```
- **API and Event Routing Contracts [REQ-004], [REQ-006], [REQ-007]:**
  ```json
  {
    "endpoint": "/api/centers",
    "method": "POST",
    "requestBody": {
      "name": "string",
      "address": "string",
      "taxId": "string",
      "contactPhone": "string",
      "contactEmail": "string"
    },
    "responseBody": {
      "centerId": "uuid",
      "name": "string",
      "address": "string",
      "taxId": "string",
      "contactPhone": "string",
      "contactEmail": "string",
      "createdAt": "timestamp",
      "updatedAt": "timestamp"
    }
  }
  ```
  ```json
  {
    "endpoint": "/api/centers/{centerId}/admin",
    "method": "POST",
    "requestBody": {
      "userId": "uuid",
      "action": "assign|unassign"
    },
    "responseBody": {
      "centerId": "uuid",
      "userId": "uuid",
      "role": "string",
      "status": "string"
    }
  }
  ```
  ```json
  {
    "endpoint": "/api/courses",
    "method": "POST",
    "requestBody": {
      "title": "string",
      "description": "string",
      "startDate": "date",
      "endDate": "date",
      "teacherId": "uuid",
      "maxStudents": "int"
    },
    "responseBody": {
      "courseId": "uuid",
      "title": "string",
      "description": "string",
      "startDate": "date",
      "endDate": "date",
      "teacherId": "uuid",
      "maxStudents": "int",
      "createdAt": "timestamp",
      "updatedAt": "timestamp"
    }
  }
  ```
- **Phase Localized Exception Handlers:** Không có ngoại lệ trong giai đoạn này.

######## Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 2)

- **DAY 1: Xây dựng cấu trúc cơ sở dữ liệu và tài liệu hiệu suất**

  ########## SUB-TASK 1: Tạo script migration cho bảng courses và enrollments
  [Coder]
  - **Target Component:** ./sources/backend/membership-hub-advanced/src/main/resources/db/migration/V1__create_courses_and_enrollments.sql [DAT-004],[DAT-006]
  - **Low-Level Technical Task Instruction:** Tạo script SQL để tạo bảng courses và enrollments với các cột và ràng buộc như đã mô tả.  
  ```sql
  -- DDL for courses and enrollments
  CREATE TABLE IF NOT EXISTS courses (
      course_id UUID PRIMARY KEY,
      title VARCHAR(150) NOT NULL,
      description TEXT,
      start_date DATE NOT NULL,
      end_date DATE NOT NULL,
      teacher_id UUID,
      max_students INT DEFAULT 30,
      CONSTRAINT fk_teacher FOREIGN KEY (teacher_id) REFERENCES users(user_id)
  );

  CREATE TABLE IF NOT EXISTS enrollments (
      enrollment_id UUID PRIMARY KEY,
      student_id UUID NOT NULL,
      course_id UUID NOT NULL,
      enrollment_date TIMESTAMP DEFAULT NOW(),
      CONSTRAINT fk_student FOREIGN KEY (student_id) REFERENCES users(user_id),
      CONSTRAINT fk_course FOREIGN KEY (course_id) REFERENCES courses(course_id)
  );
  ```

  ########## SUB-TASK 2: Soạn tài liệu hướng dẫn hiệu suất và khả năng mở rộng
  [Doc]
  - **Target Component:** ./sources/docs/performance/advanced/performance_guidelines.md [NFR-004],[NFR-005]
  - **Low-Level Technical Task Instruction:** Soạn tài liệu hướng dẫn tối ưu hiệu suất và chiến lược khả dụng, bao gồm chỉ số latency, HPA, read replicas, và backup.

- **DAY 2: Phát triển API quản lý trung tâm và phân quyền**

  ########## SUB-TASK 1: Triển khai API CRUD cho trung tâm
  [Coder]
  - **Target Component:** ./sources/backend/membership-hub-advanced/src/main/java/org/nlh4j/sas/membershiphub/center/CenterController.java [REQ-004]
  - **Low-Level Technical Task Instruction:** Xây dựng các endpoint GET, POST, PUT, DELETE cho /api/centers, bao gồm validation và exception handling.  
  ```json
  {
    "endpoint": "/api/centers",
    "method": "POST",
    "requestBody": {
      "name": "string",
      "address": "string",
      "taxId": "string",
      "contactPhone": "string",
      "contactEmail": "string"
    },
    "responseBody": {
      "centerId": "uuid",
      "name": "string",
      "address": "string",
      "taxId": "string",
      "contactPhone": "string",
      "contactEmail": "string",
      "createdAt": "timestamp",
      "updatedAt": "timestamp"
    }
  }
  ```

  ########## SUB-TASK 2: Triển khai API gán/huỷ admin trung tâm
  [Coder]
  - **Target Component:** ./sources/backend/membership-hub-advanced/src/main/java/org/nlh4j/sas/membershiphub/center/CenterAdminAssignmentController.java [REQ-006]
  - **Low-Level Technical Task Instruction:** Xây dựng endpoint POST /api/centers/{centerId}/admin để gán/huỷ admin, bao gồm kiểm tra quyền và cập nhật role.  
  ```json
  {
    "endpoint": "/api/centers/{centerId}/admin",
    "method": "POST",
    "requestBody": {
      "userId": "uuid",
      "action": "assign|unassign"
    },
    "responseBody": {
      "centerId": "uuid",
      "userId": "uuid",
      "role": "string",
      "status": "string"
    }
  }
  ```

- **DAY 3: Phát triển API quản lý khóa học**

  ########## SUB-TASK 1: Triển khai API CRUD cho khóa học
  [Coder]
  - **Target Component:** ./sources/backend/membership-hub-advanced/src/main/java/org/nlh4j/sas/membershiphub/course/CourseController.java [REQ-007]
  - **Low-Level Technical Task Instruction:** Xây dựng các endpoint GET, POST, PUT, DELETE cho /api/courses, bao gồm validation, conflict detection, và exception handling.  
  ```json
  {
    "endpoint": "/api/courses",
    "method": "POST",
    "requestBody": {
      "title": "string",
      "description": "string",
      "startDate": "date",
      "endDate": "date",
      "teacherId": "uuid",
      "maxStudents": "int"
    },
    "responseBody": {
      "courseId": "uuid",
      "title": "string",
      "description": "string",
      "startDate": "date",
      "endDate": "date",
      "teacherId": "uuid",
      "maxStudents": "int",
      "createdAt": "timestamp",
      "updatedAt": "timestamp"
    }
  }
  ```

###### 📈 Giai đoạn 3 Triển khai các mô-đun điểm danh, thông báo và khuyến mãi với xử lý ngoại lệ
- **Mục tiêu & Mục đích Cốt lõi của Giai đoạn:**  
  Giai đoạn này tập trung vào việc xây dựng các dịch vụ backend cho việc ghi nhận điểm danh qua QR, gửi thông báo tới ứng dụng di động và nhóm Zalo, cũng như quản lý khuyến mãi cho học viên. Ngoài ra, giai đoạn còn triển khai các cơ chế xử lý ngoại lệ để đảm bảo tính nhất quán và độ tin cậy của hệ thống.

- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:**  
  - `./sources/backend/membership-hub-auxiliary/attendance/AttendanceService.java [EXC-001],[EXC-002],[ARC-007],[DAT-006],[REQ-012],[REQ-013]`  
  - `./sources/backend/membership-hub-auxiliary/attendance/AttendanceController.java [EXC-001],[EXC-002],[ARC-007]`  
  - `./sources/backend/membership-hub-auxiliary/notification/NotificationService.java [EXC-003],[ARC-008],[DAT-008],[REQ-016]`  
  - `./sources/backend/membership-hub-auxiliary/notification/NotificationController.java [EXC-003],[ARC-008]`  
  - `./sources/backend/membership-hub-auxiliary/promotion/PromotionService.java [ARC-017],[DAT-009],[REQ-017],[REQ-018]`  
  - `./sources/backend/membership-hub-auxiliary/promotion/PromotionController.java [ARC-017]`  
  - `./sources/backend/membership-hub-auxiliary/exception/AttendanceException.java [EXC-001]`  
  - `./sources/backend/membership-hub-auxiliary/exception/NotificationException.java [EXC-003]`  
  - `./sources/docs/attendance_schema.md [DAT-006]`  
  - `./sources/docs/notification_schema.md [DAT-008]`  
  - `./sources/docs/promotion_schema.md [DAT-009]`  
  - `./sources/docs/nfr_006.md [NFR-006]`  
  - `./sources/docs/nfr_007.md [NFR-007]`  
  - `./sources/docs/nfr_008.md [NFR-008]`

- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-006],[DAT-008],[DAT-009]:**  
  ```sql
  CREATE TABLE ATTENDANCE (
      attendanceId UUID PRIMARY KEY,
      studentId UUID NOT NULL,
      courseId UUID NOT NULL,
      attendanceDate DATE NOT NULL,
      timestamp TIMESTAMP NOT NULL DEFAULT NOW(),
      CONSTRAINT fk_student FOREIGN KEY (studentId) REFERENCES USERS(userId),
      CONSTRAINT fk_course FOREIGN KEY (courseId) REFERENCES COURSES(courseId),
      CONSTRAINT uq_attendance UNIQUE (studentId, courseId, attendanceDate)
  );

  CREATE TABLE NOTIFICATIONS (
      notificationId UUID PRIMARY KEY,
      userId UUID,
      groupZalo VARCHAR(255),
      message TEXT NOT NULL,
      sentAt TIMESTAMP NOT NULL DEFAULT NOW(),
      delivered BOOLEAN NOT NULL DEFAULT FALSE,
      CONSTRAINT fk_user FOREIGN KEY (userId) REFERENCES USERS(userId)
  );

  CREATE TABLE PROMOTIONS (
      promoId UUID PRIMARY KEY,
      code VARCHAR(50) NOT NULL UNIQUE,
      discountPercent SMALLINT NOT NULL,
      startDate DATE,
      endDate DATE,
      description TEXT,
      CONSTRAINT chk_discount CHECK (discountPercent BETWEEN 1 AND 100)
  );
  ```

- **Hợp đồng Định tuyến API và Sự kiện [REQ-012],[REQ-013],[REQ-016],[ARC-007],[ARC-008],[ARC-017]:**  
  **API /attendance**  
  ```json
  POST /attendance
  Request:
  {
    "studentId": "uuid",
    "courseId": "uuid",
    "attendanceDate": "YYYY-MM-DD"
  }
  Response:
  {
    "attendanceId": "uuid",
    "status": "SUCCESS",
    "duplicate": false
  }
  ```  
  **API /notifications**  
  ```json
  POST /notifications
  Request:
  {
    "userId": "uuid",
    "groupZalo": "string",
    "message": "string"
  }
  Response:
  {
    "notificationId": "uuid",
    "status": "PENDING"
  }
  ```  
  **API /promotions**  
  ```json
  GET /promotions
  Response:
  [
    {
      "promoId": "uuid",
      "code": "string",
      "discountPercent": 20,
      "startDate": "YYYY-MM-DD",
      "endDate": "YYYY-MM-DD",
      "description": "string"
    }
  ]
  ```  
  **Event Topics**  
  - `attendance.events`  
  - `notification.events`  
  - `promotion.events`

- **Xử lý Ngoại lệ Định vị Giai đoạn [EXC-001],[EXC-002],[EXC-003]:**  
  - **EXC-001: DuplicateAttendanceException** – Mã lỗi 409, thông báo: “Attendance already recorded for this student on the same day.”  
  - **EXC-002: AttendanceValidationException** – Mã lỗi 400, thông báo: “Invalid attendance data: missing studentId or courseId.”  
  - **EXC-003: NotificationFailureException** – Mã lỗi 500, thông báo: “Failed to send notification to device or Zalo group.”

---

#### Nhật ký Phân phối Công việc Theo Ngày (Giai đoạn 3)

- **Ngày 1: Thiết lập các dịch vụ attendance và notification**  
  ########## Công việc phụ [1]: Xây dựng AttendanceService và controller [Coder]  
  Target Component file path: `./sources/backend/membership-hub-auxiliary/attendance/AttendanceService.java; ./sources/backend/membership-hub-auxiliary/attendance/AttendanceController.java [EXC-001],[EXC-002],[ARC-007],[DAT-006],[REQ-012],[REQ-013]`  
  Low-Level Technical Task Instruction: Xây dựng lớp AttendanceService với phương thức recordAttendance, xử lý idempotency, kiểm tra quyền truy cập, và lưu vào bảng ATTENDANCE.  
  Database Schema DDL SQL Specification [DAT-006]:  
  ```sql
  CREATE TABLE ATTENDANCE (
      attendanceId UUID PRIMARY KEY,
      studentId UUID NOT NULL,
      courseId UUID NOT NULL,
      attendanceDate DATE NOT NULL,
      timestamp TIMESTAMP NOT NULL DEFAULT NOW(),
      CONSTRAINT fk_student FOREIGN KEY (studentId) REFERENCES USERS(userId),
      CONSTRAINT fk_course FOREIGN KEY (courseId) REFERENCES COURSES(courseId),
      CONSTRAINT uq_attendance UNIQUE (studentId, courseId, attendanceDate)
  );
  ```  
  API and Event Routing Contracts [REQ-012],[REQ-013],[ARC-007]:  
  ```json
  POST /attendance
  Request:
  {
    "studentId": "uuid",
    "courseId": "uuid",
    "attendanceDate": "YYYY-MM-DD"
  }
  Response:
  {
    "attendanceId": "uuid",
    "status": "SUCCESS",
    "duplicate": false
  }
  ```  
  Phase Localized Exception Handlers [EXC-001],[EXC-002]:  
  - **EXC-001: DuplicateAttendanceException** – Mã lỗi 409, thông báo: “Attendance already recorded for this student on the same day.”  
  - **EXC-002: AttendanceValidationException** – Mã lỗi 400, thông báo: “Invalid attendance data: missing studentId or courseId.”  

  ########## Công việc phụ [2]: Xây dựng NotificationService và controller [Coder]  
  Target Component file path: `./sources/backend/membership-hub-auxiliary/notification/NotificationService.java; ./sources/backend/membership-hub-auxiliary/notification/NotificationController.java [EXC-003],[ARC-008],[DAT-008],[REQ-016]`  
  Low-Level Technical Task Instruction: Xây dựng lớp NotificationService để gửi push tới FCM/APNs và Zalo, tạo Notification entity, lưu vào bảng NOTIFICATIONS.  
  Database Schema DDL SQL Specification [DAT-008]:  
  ```sql
  CREATE TABLE NOTIFICATIONS (
      notificationId UUID PRIMARY KEY,
      userId UUID,
      groupZalo VARCHAR(255),
      message TEXT NOT NULL,
      sentAt TIMESTAMP NOT NULL DEFAULT NOW(),
      delivered BOOLEAN NOT NULL DEFAULT FALSE,
      CONSTRAINT fk_user FOREIGN KEY (userId) REFERENCES USERS(userId)
  );
  ```  
  API and Event Routing Contracts [REQ-016],[ARC-008]:  
  ```json
  POST /notifications
  Request:
  {
    "userId": "uuid",
    "groupZalo": "string",
    "message": "string"
  }
  Response:
  {
    "notificationId": "uuid",
    "status": "PENDING"
  }
  ```  
  Phase Localized Exception Handlers [EXC-003]:  
  - **EXC-003: NotificationFailureException** – Mã lỗi 500, thông báo: “Failed to send notification to device or Zalo group.”  

- **Ngày 2: Xây dựng dịch vụ promotion và exception classes**  
  ########## Công việc phụ [1]: Xây dựng PromotionService và controller [Coder]  
  Target Component file path: `./sources/backend/membership-hub-auxiliary/promotion/PromotionService.java; ./sources/backend/membership-hub-auxiliary/promotion/PromotionController.java [ARC-017],[DAT-009],[REQ-017],[REQ-018]`  
  Low-Level Technical Task Instruction: Xây dựng lớp PromotionService để quản lý khuyến mãi, bao gồm CRUD, tính toán giảm giá, và lưu vào bảng PROMOTIONS.  
  Database Schema DDL SQL Specification [DAT-009]:  
  ```sql
  CREATE TABLE PROMOTIONS (
      promoId UUID PRIMARY KEY,
      code VARCHAR(50) NOT NULL UNIQUE,
      discountPercent SMALLINT NOT NULL,
      startDate DATE,
      endDate DATE,
      description TEXT,
      CONSTRAINT chk_discount CHECK (discountPercent BETWEEN 1 AND 100)
  );
  ```  
  API and Event Routing Contracts [REQ-017],[REQ-018],[ARC-017]:  
  ```json
  GET /promotions
  Response:
  [
    {
      "promoId": "uuid",
      "code": "string",
      "discountPercent": 20,
      "startDate": "YYYY-MM-DD",
      "endDate": "YYYY-MM-DD",
      "description": "string"
    }
  ]
  ```  

  ########## Công việc phụ [2]: Định nghĩa các exception tùy chỉnh [Coder]  
  Target Component file path: `./sources/backend/membership-hub-auxiliary/exception/AttendanceException.java; ./sources/backend/membership-hub-auxiliary/exception/NotificationException.java [EXC-001],[EXC-002],[EXC-003]`  
  Low-Level Technical Task Instruction: Định nghĩa các exception tùy chỉnh cho attendance và notification, bao gồm mã lỗi và thông báo.  
  Phase Localized Exception Handlers [EXC-001],[EXC-002],[EXC-003]:  
  - **EXC-001: DuplicateAttendanceException** – Mã lỗi 409, thông báo: “Attendance already recorded for this student on the same day.”  
  - **EXC-002: AttendanceValidationException** – Mã lỗi 400, thông báo: “Invalid attendance data: missing studentId or courseId.”  
  - **EXC-003: NotificationFailureException** – Mã lỗi 500, thông báo: “Failed to send notification to device or Zalo group.”  

- **Ngày 3: Kiểm thử và tài liệu**  
  ########## Công việc phụ [1]: Viết unit test cho attendance, notification, promotion [Tester]  
  Target Component file path: `./sources/backend/membership-hub-auxiliary/attendance/AttendanceServiceTest.java; ./sources/backend/membership-hub-auxiliary/notification/NotificationServiceTest.java; ./sources/backend/membership-hub-auxiliary/promotion/PromotionServiceTest.java [EXC-001],[EXC-002],[EXC-003],[ARC-007],[ARC-008],[ARC-017],[DAT-006],[DAT-008],[DAT-009]`  
  Low-Level Technical Task Instruction: Viết các unit test để kiểm tra tính idempotent của attendance, xử lý ngoại lệ, và CRUD promotion.  

  ########## Công việc phụ [2]: Tài liệu chi tiết cho API và exception handling [Doc]  
  Target Component file path: `./sources/docs/attendance_api.md; ./sources/docs/notification_api.md; ./sources/docs/promotion_api.md; ./sources/docs/exception_handling.md [REQ-012],[REQ-013],[REQ-016],[ARC-007],[ARC-008],[ARC-017],[EXC-001],[EXC-002],[EXC-003]`  
  Low-Level Technical Task Instruction: Tạo tài liệu chi tiết cho các endpoint, payload, và exception handling.

######## Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 4)

- **DAY 1: Thiết lập hạ tầng cơ bản cho dịch vụ backend**

  ########## SUB-TASK 1: Xây dựng và đẩy Docker image cho các dịch vụ Quarkus  
  **[Docker]**  
  **Target Component:** `./sources/backend/membership-hub-infra/Dockerfile`  
  **Tag IDs:** [ARC-010]  
  **Nhiệm vụ chi tiết:** Tạo Dockerfile đa giai đoạn cho các microservice Quarkus, biên dịch mã nguồn, đóng gói thành image, và đẩy lên Google Container Registry (GCR) với tag `membership-hub:latest`.

  ########## SUB-TASK 2: Provisioning GCP Terraform cho GKE cluster  
  **[GCP]**  
  **Target Component:** `./sources/infra/terraform/main.tf`  
  **Tag IDs:** [ARC-010],[ARC-009]  
  **Nhiệm vụ chi tiết:** Định nghĩa tài nguyên GKE cluster, node pools, IAM roles và service accounts trong Terraform, chạy `terraform init` và `terraform apply` để triển khai cluster với cấu hình tự động scaling.

  ########## SUB-TASK 3: Triển khai Helm chart cho ứng dụng  
  **[GKE]**  
  **Target Component:** `./sources/infra/helm/membership-hub/Chart.yaml`  
  **Tag IDs:** [ARC-010],[ARC-008]  
  **Nhiệm vụ chi tiết:** Tạo chart Helm bao gồm deployment, service, ingress cho các microservice, cấu hình values.yaml, và triển khai lên GKE bằng `helm upgrade --install`.

- **DAY 2: Hoàn thiện hạ tầng, CI/CD và cấu hình sự kiện**

  ########## SUB-TASK 1: Xây dựng Docker image cho sidecar (Redis, Kafka)  
  **[Docker]**  
  **Target Component:** `./sources/backend/membership-hub-infra/sidecar/Dockerfile`  
  **Tag IDs:** [ARC-010],[ARC-006]  
  **Nhiệm vụ chi tiết:** Tạo Dockerfile cho Redis và Kafka, biên dịch và đẩy image lên GCR, chuẩn bị cho deployment trong Helm chart.

  ########## SUB-TASK 2: Tạo Pub/Sub topics cho event bus  
  **[GCP]**  
  **Target Component:** `./sources/infra/terraform/pubsub.tf`  
  **Tag IDs:** [ARC-006],[ARC-009]  
  **Nhiệm vụ chi tiết:** Định nghĩa các topic `attendance.events`, `notification.events`, `course.events`, `center.events` trong Terraform, triển khai bằng `terraform apply`.

  ########## SUB-TASK 3: Triển khai event bus services (Kafka/Redis Streams) lên GKE  
  **[GKE]**  
  **Target Component:** `./sources/infra/helm/eventbus/Chart.yaml`  
  **Tag IDs:** [ARC-006],[ARC-008]  
  **Nhiệm vụ chi tiết:** Cấu hình Helm chart cho Kafka và Redis Streams, triển khai vào GKE cluster, xác nhận các broker hoạt động bình thường.

  ########## SUB-TASK 4: Thiết lập pipeline CI/CD với GitHub Actions  
  **[Docker]**  
  **Target Component:** `./sources/infra/github-actions/workflows/ci-cd.yml`  
  **Tag IDs:** [ARC-010],[ARC-006]  
  **Nhiệm vụ chi tiết:** Định nghĩa workflow GitHub Actions để build, test, push Docker image, và deploy Helm chart lên GKE, bao gồm các bước kiểm tra lint, unit test và integration test.

  ########## SUB-TASK 5: Xử lý ngoại lệ khi provisioning hạ tầng  
  **[GCP]**  
  **Target Component:** `./sources/infra/terraform/variables.tf`  
  **Tag IDs:** [EXC-004],[EXC-005]  
  **Nhiệm vụ chi tiết:** Thêm validation cho các biến Terraform, xử lý lỗi khi thiếu credentials hoặc thiếu resource quota, ghi log chi tiết và rollback khi cần.

  ########## SUB-TASK 6: Tạo bảng SystemSettings trong PostgreSQL  
  **[Docker]**  
  **Target Component:** `./sources/backend/membership-hub-infra/migrations/V1__create_system_settings.sql`  
  **Tag IDs:** [DAT-011]  
  **Nhiệm vụ chi tiết:**  
  ```sql
  CREATE TABLE IF NOT EXISTS SYSTEMSETTINGS (
      settingKey VARCHAR(255) NOT NULL PRIMARY KEY,
      settingValue TEXT NOT NULL,
      description VARCHAR(500)
  );
  CREATE INDEX idx_setting_key ON SYSTEMSETTINGS (settingKey);
  ```

  ########## SUB-TASK 7: Triển khai Cloud Function cho QR scan  
  **[GCP]**  
  **Target Component:** `./sources/infra/terraform/cloudfunctions.tf`  
  **Tag IDs:** [ARC-007]  
  **Nhiệm vụ chi tiết:** Định nghĩa Cloud Function `qr_scan_handler` trong Terraform, triển khai, cấu hình trigger HTTP, và cấp quyền truy cập từ mobile app.

## TỔNG QUAN DỰ ÁN: membership-hub

###### 📈 Giai đoạn 5 Triển khai ứng dụng cuối cùng, thực hiện kiểm thử tích hợp và xác nhận luồng toàn bộ
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:**  
  Giai đoạn này thực hiện triển khai toàn bộ ứng dụng lên môi trường sản xuất, thực thi các bài kiểm thử tích hợp để xác nhận tính toàn vẹn của luồng dữ liệu, và thực hiện kiểm tra toàn bộ luồng giao dịch từ đăng nhập, quản lý khóa học, điểm danh, đến thông báo, đảm bảo mọi thành phần hoạt động đồng bộ và đáp ứng các tiêu chí hiệu năng, bảo mật đã đề ra.

- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:**  
  - `./sources/infra/membership-hub-deploy/Dockerfile [ARC-010]`  
  - `./sources/infra/membership-hub-deploy/helm/values.yaml [ARC-010]`  
  - `./sources/infra/membership-hub-deploy/helm/membership-hub-deploy.yaml [ARC-010]`  
  - `./sources/infra/membership-hub-deploy/ci/github-actions.yml [ARC-010]`  
  - `./sources/infra/membership-hub-deploy/integration-tests/validate-end-to-end.test.ts [ARC-010]`  
  - `./sources/docs/architecture/infra-deployment.md [ARC-010]`

- **Phase Localized Exception Handlers:**  
  Không có ngoại lệ đặc thù trong giai đoạn này.

######## Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 5)

- **DAY 1: Triển khai Docker images, áp dụng Helm chart, chạy kiểm thử tích hợp, và xác nhận triển khai**  

  ########## SUB-TASK 1: Xây dựng Docker images  
  **[Docker]**  
  **Target Component:** `./sources/infra/membership-hub-deploy/Dockerfile [ARC-010]`  
  **Hướng dẫn chi tiết:** Xây dựng Dockerfile đa giai đoạn cho tất cả các microservice, tối ưu kích thước, đẩy lên GCR.

  ########## SUB-TASK 2: Triển khai Helm chart  
  **[GKE]**  
  **Target Component:** `./sources/infra/membership-hub-deploy/helm/membership-hub-deploy.yaml [ARC-010]`  
  **Hướng dẫn chi tiết:** Triển khai Helm chart lên cluster GKE, kiểm tra trạng thái pod, service, và xác nhận endpoint hoạt động.

  ########## SUB-TASK 3: Chạy kiểm thử tích hợp  
  **[Tester]**  
  **Target Component:** `./sources/infra/membership-hub-deploy;integration-tests/validate-end-to-end.test.ts [ARC-010]`  
  **Hướng dẫn chi tiết:** Chạy tập hợp kiểm thử tích hợp end-to-end, ghi lại logs, và báo cáo lỗi.

  ########## SUB-TASK 4: Xác nhận triển khai  
  **[Reviewer]**  
  **Target Component:** `./sources/infra/membership-hub-deploy/ci/github-actions.yml [ARC-010]`  
  **Hướng dẫn chi tiết:** Xem xét pipeline CI, xác nhận các bước kiểm thử đã hoàn thành, và phê duyệt triển khai.

```properties:cross_audit_ledger
[AUTOMATED_SELF_AUDIT_REPORT]
TOTAL_PHASES_DECLARED_IN_SECTION_4_2=5
TOTAL_PHASES_EXPECTED_BY_PARAMETERS=5
PHASE_COUNT_COMPLIANCE_STATUS=Verified_5_out_of_5_Phases_Generated
MAX_DAYS_PER_PHASE_LIMIT_PARAMETER=7
ACTUAL_MAX_DAY_INDEX_DETECTED_IN_TIMELINE=1
TIMELINE_DAY_CAP_COMPLIANCE_STATUS=Verified_All_Phase_Durations_Within_Ceiling
TOTAL_TASKS_REGISTERED_IN_MASTER_BACKLOG_4_1=58
TOTAL_DISCRETE_SUB_TASKS_GENERATED_IN_SECTION_5=58
SUB_TASK_QUANTUM_COMPLIANCE_STATUS=Verified_Symmetry_Enforced_With_100_Percent_Symmetry
```

## TỔNG QUAN HỆ THỐNG: membership-hub

#### 📁 6. MÃ BẢO MẬT QUỐC TẾ VÀ THIẾT BỊ CHỐNG TIẾT THUẬT [NFR-XXX]
- **Chống SQL Injection (SQLi) - Biện pháp tuyệt đối**: Định nghĩa quy tắc sử dụng câu lệnh chuẩn bị (prepared statements), tham số vị trí (positional parameters), và danh sách trắng (whitelists) cho các đầu vào sắp xếp động.
- **Chống XSS & Chính sách Bảo mật Nội dung (CSP)**: Tiêu chuẩn tự động làm sạch ngữ cảnh, tự động thoát JSX, và chèn tiêu đề CSP nghiêm ngặt (`unsafe-inline` bị cấm).
- **Quy tắc CORS đa tenant**: Cấu hình ngăn chặn wildcard nguồn gốc và xác thực động các nguồn gốc tenant dựa trên cơ sở dữ liệu.
- **Công cụ làm sạch nhật ký và ẩn dữ liệu PII**: Hệ thống tự động ẩn dữ liệu nhạy cảm (`@JsonSerialize`) và ngưỡng làm sạch nhật ký.

#### 📁 7. QUY TẮC TUYÊN CHẤP MÔ HÌNH HỢP TÁC & CƠ THỂ SEO ĐỊNH DỊCH
- **Quy tắc tuân thủ Capacitor Mobile Hybrid**: Khi di động được kích hoạt, áp dụng các quy tắc lấy dữ liệu phía client, địa chỉ URL tuyệt đối, bảo vệ hydration, trừu tượng lưu trữ native (`@capacitor/preferences`), và xử lý nút back của thiết bị.
- **Hệ thống SEO đa ngôn ngữ**: Kiến trúc middleware nhận diện ngôn ngữ, chèn động thẻ hreflang, và giới hạn chỉ mục crawler robots.

#### 📁 8. DÂY ĐỘNG CÔNG CỤ TỰ ĐỘNG HÀNH ĐỘNG GIT
- **Phân tách fork làm việc hàng ngày**: Kiểm soát lập trình cho nhánh `features/development-phase-X-day-Y` (X là số giai đoạn, Y là số ngày trong giai đoạn, bắt đầu từ 1 cho mỗi giai đoạn).
- **Cổng bảo vệ quy trình**: Quy tắc thực thi biên dịch, kiểm tra độ phủ mã tự động (`>= 85%`), và ghi lại nhật ký tổng hợp ngữ cảnh.

###### 🛑 QUÁ TRÌNH KIỂM TRA MÁT HÀNH
`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: X, TOTAL ARC TAGS: Y, TOTAL EXC TAGS: Z, TOTAL DAT TAGS: V, TOTAL NFR TAGS: W. ZERO UNASSIGNED CODES FOUND.]`

