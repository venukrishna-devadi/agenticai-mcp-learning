def router(state):

    if state.need_human:
        return "human"
    
    if state.need_tool:
        return "tool"
    
    return "final"