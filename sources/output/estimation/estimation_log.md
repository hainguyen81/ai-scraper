# Exception:

expected str, bytes or os.PathLike object, not NoneType: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/agent_super.py", line 285, in __execute__
    kwargs = self.__ai_execute__(**kwargs) or {}
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/agent_super.py", line 260, in __ai_execute__
    kwargs = self.process_communication(**kwargs) or {}
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/estimation/agent_estimator.py", line 382, in process_communication
    output_image_path=self.__storage_path__(storage_name="output_estimation", file=EST_CHART_FILE),
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/subagent_super.py", line 52, in __storage_path__
    return os.path.join(self.storage.get(storage_name), file)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "<frozen posixpath>", line 76, in join
', 'TypeError: expected str, bytes or os.PathLike object, not NoneType
']: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/agent_super.py", line 328, in execute
    return self.__do_execute__(**safe_kwargs) or {}
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/agent_super.py", line 315, in __do_execute__
    raise RuntimeError(exception) # response is exception stack-trace from `__execute__`
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', 'RuntimeError: expected str, bytes or os.PathLike object, not NoneType: [\'Traceback (most recent call last):\
\', \'  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/agent_super.py", line 285, in __execute__\
    kwargs = self.__ai_execute__(**kwargs) or {}\
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\
\', \'  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/agent_super.py", line 260, in __ai_execute__\
    kwargs = self.process_communication(**kwargs) or {}\
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\
\', \'  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/estimation/agent_estimator.py", line 382, in process_communication\
    output_image_path=self.__storage_path__(storage_name="output_estimation", file=EST_CHART_FILE),\
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\
\', \'  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/subagent_super.py", line 52, in __storage_path__\
    return os.path.join(self.storage.get(storage_name), file)\
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\
\', \'  File "<frozen posixpath>", line 76, in join\
\', \'TypeError: expected str, bytes or os.PathLike object, not NoneType\
\']
']

---

