# This is your FIRST real graph orchestration.
# state = a Python dict that travels through the graph. Every node can read from it and write to it.
# node = just a function f(state) -> state. It takes the current state, does something, returns the (updated) state.
# workflow = the graph where you register those functions by name.

#LangGraph's add_node wants a function that takes only state. 
# But your think_node needs two arguments: state and llm.

from langgraph.graph import StateGraph, END
from state import AgentState
from nodes import think_node, action_node

class GraphAgent:

    def __init__(self, llm):
        self.llm = llm

        # create graph
        workflow = StateGraph(AgentState)

        # now we will add nodes
        workflow.add_node(
            "think",
            lambda state: think_node(state, self.llm)
        )

        workflow.add_node(
            "action",
            lambda state: action_node(state, self.llm)
        )

        # now we will define the flow
        workflow.set_entry_point("think")
        workflow.add_edge("think", "action")
        workflow.add_edge("action", END)

        # now we will compile the graph
        self.graph = workflow.compile()

### Now we will run the graph
    def run(self, user_query):

        initial_state = {
            "user_query": user_query,
            "thought": "",
            "final_answer": ""
        }

        result = self.graph.invoke(initial_state)
        return result

# In LangGraph, graph.invoke(initial_state) always returns the final state dict,
#  not just one value.

# workflow.add_edge("think", "act")
# cognitive routing
# This becomes:

# * branching
# * loops
# * retries
# * conditional execution