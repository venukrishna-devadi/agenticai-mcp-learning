from langgraph.graph import StateGraph, END
from state import AgentState
from nodes.think_node import think_node
from nodes.tool_node import tool_node
from nodes.human_node import human_node
from router import router

def build_graph():
    """ Build the Graph workflow"""

    workflow = StateGraph(AgentState)

    workflow.add_node("think", think_node)
    workflow.add_node("tool", tool_node)
    workflow.add_node("human", human_node)

    workflow.set_entry_point("think")

    workflow.add_conditional_edges(
        "think",
        router,
        {
            "human": "human",
            "tool": "tool",
            "final": END
        }
    )
    workflow.add_edge("tool", "think")
    workflow.add_edge("human", "think")
    graph = workflow.compile()

    return graph
