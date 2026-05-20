# Never trust raw LLM output directly.

# Always:

# * validate
# * parse
# * sanitize

class TaskExecutor:

    def __init__(self, llm):
        self.llm = llm
    
    def execute_task(self,
                     task,
                     goal):
        
        prompt = f"""

Goal: {goal}

Current Task: {task}
"""
        result = self.llm.chat(
            system_prompt = """
You are an execution agent.
Focus only on the current task.
""",
            user_prompt = prompt,
            temperature = 0.3
        )

        return result
    

# You now have:

# specialized execution units

# This is proto-agent architecture.