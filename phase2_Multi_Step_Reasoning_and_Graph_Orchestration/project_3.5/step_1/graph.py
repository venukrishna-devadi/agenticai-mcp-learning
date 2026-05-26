from langgraph.graph import StateGraph, END
from state import AgentState
from nodes.think_node import think_node
from nodes.human_node import human_node
from nodes.tool_node import tool_node
from nodes.final_node import final_node

def router(state):

    if state.step_count >= state.max_steps:
        print(f"\n⚠️ Max steps ({state.max_steps}) reached. Forcing final answer.")
        return "final"

    if state.need_human:
        return "human"
    if state.need_tool:
        return "tool"
    return "final"


builder = StateGraph(AgentState)

builder.add_node("think", think_node)
builder.add_node("tool", tool_node)
builder.add_node("human", human_node)
builder.add_node("final", final_node)


builder.set_entry_point("think")

builder.add_conditional_edges(
    "think",
    router,
    {
        "human": "human",
        "tool": "tool",
        "final": "final" 
    }
)

builder.add_edge("tool", "think")
builder.add_edge("human", "think")
builder.add_edge("final", END)
graph = builder.compile()

# builder.add_edge("human", "think")
# builder.add_edge("tool", "think")
# mean BOTH:

# * tool observations
# * human observations

# flow back into reasoning.