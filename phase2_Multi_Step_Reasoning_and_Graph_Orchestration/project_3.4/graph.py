from langgraph.graph import StateGraph, END
from state import AgentState
from nodes.think_node import think_node
from nodes.tool_node import tool_node
from nodes.final_node import final_node

def route_after_think(state):
    """Conditional routing: tool or final"""
    if state.need_tool:
        return "tool_node"
    return "final_node"

class ReactAgent:

    def __init__(self):

        workflow = StateGraph(AgentState)
        
        # add nodes
        workflow.add_node("think_node", think_node)
        workflow.add_node("tool_node", tool_node)
        workflow.add_node("final_node", final_node)

        # set entry point
        workflow.set_entry_point("think_node")
        workflow.add_conditional_edges(
            "think_node",
            route_after_think,
            {
                "tool_node": "tool_node",
                "final_node": "final_node"
            }
        )

        # Important- after tool node, go back again to think node
        workflow.add_edge("tool_node", "think_node")

        # add final edge
        workflow.add_edge("final_node", END)

        self.graph = workflow.compile()

    def run(self, user_query: str):

        initial_state = AgentState(
            user_query=user_query,
            history= [],
            step_count=0,
            max_steps = 5
        )

        result = self.graph.invoke(initial_state)

        return result