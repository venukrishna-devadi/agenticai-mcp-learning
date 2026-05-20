from langgraph.graph import StateGraph, END
from state import AgentState
from nodes import router_node, math_node, science_node, final_node, history_node
from router import route_decision


class GraphAgent:
    def __init__(self, llm):
        self.llm = llm
        workflow = StateGraph(AgentState)

        # now we will add nodes
        workflow.add_node(
            "router",
            lambda state: router_node(state, self.llm)
        )

        workflow.add_node(
            "math_node",
            lambda state: math_node(state, self.llm)
        )

        workflow.add_node(
            "science_node",
            lambda state: science_node(state, self.llm)
        )

        workflow.add_node(
            "history_node",
            lambda state: history_node(state, self.llm)
        )
        
        workflow.add_node(
            "final_node",
            lambda state: final_node(state, self.llm)
        )


        # now we will add the entry point
        workflow.set_entry_point("router")

        # now we will add conditional routing
        workflow.add_conditional_edges(
            "router",
            route_decision,
            {
                "math_node": "math_node",
                "science_node": "science_node",
                "history_node": "history_node"
            }
        )

        # now we will add final transitions
        workflow.add_edge("math_node", "final_node")
        workflow.add_edge("science_node", "final_node")
        workflow.add_edge("history_node", "final_node")
        workflow.add_edge("final_node", END)

        self.graph = workflow.compile()

    def run(self, user_query):

        initial_state = AgentState(user_query=user_query)

        result = self.graph.invoke(initial_state)

        return result
    
#workflow.add_conditional_edges()
# is the beginning of:

# autonomous decision workflows

# This is where LangGraph becomes powerful.