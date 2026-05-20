from pydantic import BaseModel

class AgentState(BaseModel):

    user_query: str

    route: str = ""
    reasoning: str = ""

    final_response: str = ""