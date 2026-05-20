from pydantic import BaseModel

class AgentState(BaseModel):

    user_query: str
    need_tool: bool = False
    selected_tool: str = ""
    tool_input: str = ""
    tool_output: str = ""
    final_answer: str = ""


# STEP 1 — state.py

# We now track:

# * tool decisions
# * tool outputs
# * reasoning traces