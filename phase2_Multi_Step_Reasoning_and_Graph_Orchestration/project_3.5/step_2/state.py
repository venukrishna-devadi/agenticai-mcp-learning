from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

class AgentState(BaseModel):

    user_query: str

    #reasoning
    current_thought: str = ""
    confidence: float = 0.0

    #tool control
    need_tool: bool = False
    selected_tool: str = ""
    tool_input: str = ""
    tool_output: str = ""

    # human loop
    need_human: bool = False
    human_question: str = ""
    human_response: str = ""
    human_response_consumed: bool = False

    # observation layer
    observation: Dict[str, Any] = Field(default_factory= dict)
    last_observation: Dict[str, Any] = Field(default_factory= dict)

    # control
    step_count: int = 0
    max_steps: int = 8
    retry_count: int = 0

    # memory
    history: List[Dict[str, Any]] = Field(default_factory= list)

    #cache
    tool_cache: Dict[str, Any] = Field(default_factory= dict)

    final_answer: str = ""