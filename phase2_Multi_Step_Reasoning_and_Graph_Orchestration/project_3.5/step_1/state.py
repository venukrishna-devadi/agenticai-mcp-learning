from pydantic import BaseModel, Field
from typing import List, Any

class AgentState(BaseModel):

    user_query: str

    current_thought: str = Any

    need_tool: bool = False
    selected_tool: str = ""
    tool_input: str = ""
    tool_output: str = ""

    # Human fields
    need_human: bool = False
    human_question: str = ""
    human_response: str = ""

    confidence: float = 0.0

    step_count: int = 0
    max_steps: int = 10
    history: List[dict] = Field(default_factory=list)

    final_answer: str = ""