# This is your first:

# autonomous execution loop

# Major milestone.

from logger import log_section
from prompt import PLANNER_PROMPT, EXECUTION_PROMPT, FINAL_SUMMARY_PROMPT
from validator import parse_plan
from task_executor import TaskExecutor
from state import PlanningState

class PlanningAgent:

    def __init__(self, llm):
        self.llm = llm
        self.state = PlanningState()
        self.executor = TaskExecutor(llm)
    
    def create_plan(self):

        log_section(
            "STEP 1 — PLAN GENERATION",
            "Creating execution plan...")
        
        raw_plan = self.llm.chat(system_prompt = PLANNER_PROMPT,
                                 user_prompt = self.state.goal,
                                 temperature = 0.3)
        
        log_section(
            "RAW AGENT PLAN",
            raw_plan)
        
        parsed_tasks = parse_plan(raw_plan)
        self.state.plan = parsed_tasks

        log_section(
            "Parsed Tasks",
            str(parsed_tasks))
    

    def execute_plan(self):

        log_section(
            "STEP 2 — PLAN EXECUTION",
            "Executing parsed plan...")
        
        for index, task in enumerate(self.state.plan):

            log_section(
            f"Executing task {index +1}",
            task)

            result = self.executor.execute_task(task=task,
                                                goal=self.state.goal)
            self.state.completed_tasks.append({
                "task": task,
                "result": result
            })

            log_section(
            "Task Result",
            result)
    
    def generate_final_output(self):

        combined_results = ""
        for item in self.state.completed_tasks:
            
            combined_results += f"""

TASK: {item["task"]}
RESULT: {item["result"]}
"""
        final_output = self.llm.chat(system_prompt = FINAL_SUMMARY_PROMPT,
                                         user_prompt = combined_results,
                                         temperature = 0.4)
            
        self.state.final_output.append(str(final_output))
        
    
    def run(self, goal):

        self.state.goal = goal
        self.create_plan()
        self.execute_plan()
        self.generate_final_output()

        return self.state.final_output

            
