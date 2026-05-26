def route_by_confidence(confidence: float):

    """ confidence routing logic"""

    if confidence < 0.3:
        return "HUMAN_REQUIRED"
    if confidence < 0.6:
        return "TRY_TOOL"
    if confidence < 0.8:
        return "TOOL_PREFERRED"
    
    return "DIRECT_ANSWER"