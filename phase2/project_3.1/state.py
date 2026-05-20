# STEP 1 — state.py

# This is the MOST IMPORTANT file.

# Why State Exists
# Traditional code: variables passed manually

# Graph systems: shared evolving state
# The ENTIRE graph reads/writes this state.

from typing import TypedDict

class AgentState(TypedDict):

    user_query: str
    thought: str
    final_answer: str

# This AgentState
# is your:
# agent memory schema

# Every node:
# * receives it
# * modifies it
# * returns updated state

# That’s how graphs coordinate cognition.