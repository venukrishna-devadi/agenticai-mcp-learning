# This decides:
# whether to execute tool node

def tool_router(state):
    if state.need_tool:
        return "tool_node"
    
    return "final_node"

# this if state.need_tool
# is now:
# graph-controlled cognition
# Not hardcoded application logic.