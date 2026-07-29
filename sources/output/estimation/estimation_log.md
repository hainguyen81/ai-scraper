# Exception:

expected token 'end of print statement', got ':': ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/agent_super.py", line 275, in __execute__
    user_prompt = self.build_user_prompt(**kwargs)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/agent_super.py", line 197, in build_user_prompt
    return render_prompt(self.user_prompt_template(), user_prompt_context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/agent_helper.py", line 170, in render_prompt
    tmpl = JinjaTemplate(template_content)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/jinja2/environment.py", line 1214, in __new__
    return env.from_string(source, template_class=cls)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/jinja2/environment.py", line 1111, in from_string
    return cls.from_code(self, self.compile(source), gs, None)
                               ^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/jinja2/environment.py", line 771, in compile
    self.handle_exception(source=source_hint)
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/jinja2/environment.py", line 942, in handle_exception
    raise rewrite_traceback_stack(source=source)
', '  File "<unknown>", line 98, in template
', "jinja2.exceptions.TemplateSyntaxError: expected token 'end of print statement', got ':'
"]: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/agent_super.py", line 328, in execute
    return self.__do_execute__(**safe_kwargs) or {}
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/agent_super.py", line 315, in __do_execute__
    raise RuntimeError(exception) # response is exception stack-trace from `__execute__`
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', 'RuntimeError: expected token \'end of print statement\', got \':\': [\'Traceback (most recent call last):\
\', \'  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/agent_super.py", line 275, in __execute__\
    user_prompt = self.build_user_prompt(**kwargs)\
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\
\', \'  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/agent_super.py", line 197, in build_user_prompt\
    return render_prompt(self.user_prompt_template(), user_prompt_context)\
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\
\', \'  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/agent_helper.py", line 170, in render_prompt\
    tmpl = JinjaTemplate(template_content)\
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\
\', \'  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/jinja2/environment.py", line 1214, in __new__\
    return env.from_string(source, template_class=cls)\
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\
\', \'  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/jinja2/environment.py", line 1111, in from_string\
    return cls.from_code(self, self.compile(source), gs, None)\
                               ^^^^^^^^^^^^^^^^^^^^\
\', \'  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/jinja2/environment.py", line 771, in compile\
    self.handle_exception(source=source_hint)\
\', \'  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/jinja2/environment.py", line 942, in handle_exception\
    raise rewrite_traceback_stack(source=source)\
\', \'  File "<unknown>", line 98, in template\
\', "jinja2.exceptions.TemplateSyntaxError: expected token \'end of print statement\', got \':\'\
"]
']

---

