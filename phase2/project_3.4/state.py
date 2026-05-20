from pydantic import BaseModel, Field
from typing import List, Dict, Any

class AgentState(BaseModel):
    user_query: str
    current_thought: str = ""
    need_tool: bool = False
    selected_tool: str = ""
    tool_input: str = ""
    tool_output: str = ""
    final_answer: str = ""
    step_count: int = 0
    max_steps: int = 5
    history: List[Dict] = Field(default_factory= list)

# history is now our working memory