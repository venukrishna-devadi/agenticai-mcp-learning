# STEP 2 — state.py
# VERY important.

# This introduces:
# execution tracking

class PlanningState:

    def __init__(self):

        self.goal = ""
        self.plan = []
        self.completed_tasks = []
        self.final_output = []

    def show(self):

        return {
            "goal": self.goal,
            "plan": self.plan,
            "completed_tasks": self.completed_tasks,
            "final_outputs": self.final_output
        }
    
# You are building:

# execution memory

# The agent now remembers:

# * what was planned
# * what was executed
# * what remains

# This is foundational for:

# * autonomous agents
# * workflow engines
# * LangGraph state