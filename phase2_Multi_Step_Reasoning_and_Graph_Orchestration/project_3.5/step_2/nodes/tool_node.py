from tools.calculator_tool import calculator_tool
from tools.search_tool import search_tool

def tool_node(state):

    tool = state.selected_tool
    tool_input = state.tool_input

    cache_key = f"{tool}:{tool_input}"

    # cache check
    if cache_key in state.tool_cache:
        output = state.tool_cache[cache_key]
    
    else:
        if tool =="calculator_tool":
            output = calculator_tool(expression= tool_input)
        elif tool == "search_tool":
            output = search_tool(query=tool_input)
        else:
            output = "unknown_tool"
        
        state.tool_cache[cache_key] = output
    
    state.tool_output = output

    is_error = output.lower().startswith("error") or "failed" in output.lower()
    if is_error:
        state.retry_count += 1
    else:
        state.retry_count = 0

    # observation layer
    state.last_observation = {
        "type" : "tool_output",
        "content": output,
        "success": not output.lower().startswith("error"),
        "retry_needed": output.lower().startswith("error")
    }

    # update history
    state.history.append(
        {
            "type":"tool",
            "tool": tool,
            "input": tool_input,
            "output": output
        }
    )

    return state