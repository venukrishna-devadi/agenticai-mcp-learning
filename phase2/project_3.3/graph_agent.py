# — graph_agent.py
# Now the graph becomes a REAL agent.

from langgraph.graph import StateGraph, END
from nodes import think_node, tool_node, final_node
from state import AgentState
from router import tool_router

class GraphAgent:

    def __init__(self, llm):
        self.llm = llm
        workflow = StateGraph(AgentState)

        # Now we will add nodes to the workflow
        
        workflow.add_node(
            "think_node",
            lambda state: think_node(state, self.llm)
        )

        workflow.add_node(
            "tool_node",
            lambda state: tool_node(state)
        )

        workflow.add_node(
            "final_node",
            lambda state: final_node(state, self.llm)
        )

        #Now we will set an entry point
        workflow.set_entry_point("think_node")

        # conditional routing
        workflow.add_conditional_edges(
            "think_node",
            tool_router,
            {
                "tool_node": "tool_node",
                "final_node": "final_node"
            }
        )

        workflow.add_edge("tool_node", "final_node")
        workflow.add_edge("final_node", END)

        self.graph = workflow.compile()


    def run(self, user_query):

        initial_state = AgentState(user_query=user_query)

        result = self.graph.invoke(initial_state)

        return result
    