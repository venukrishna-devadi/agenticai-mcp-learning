def get_retry_action(retry_count: int):

    """Determines retry strategy"""
    if retry_count == 0:
        return "RETRY_SAME_TOOL"
    if retry_count == 1:
        return "SEARCH_TOOL"
    if retry_count == 2:
        return "MODIFY_INPUT"
    
    return "ASK_HUMAN"
