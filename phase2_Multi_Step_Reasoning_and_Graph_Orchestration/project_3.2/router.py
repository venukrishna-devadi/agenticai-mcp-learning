# This file controls:
# conditional graph transitions
# VERY important concept.

def route_decision(state):

    if state.route == "math":
        return "math_node"
    elif state.route == "science":
        return "science_node"
    
    return "history_node"

# controls:
# graph intelligence

# This becomes:

# * tool selection
# * retries
# * planner execution
# * memory retrieval
# * RAG routing
# * multi-agent delegation