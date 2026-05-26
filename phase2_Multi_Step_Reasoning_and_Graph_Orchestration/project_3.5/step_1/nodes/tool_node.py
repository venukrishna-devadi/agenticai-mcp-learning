from tools.calculator_tool import calculator_tool
from tools.search_tool import search_tool

AVAILABLE_TOOLS = {
    "calculator_tool": calculator_tool,
    "search_tool": search_tool,
}


def tool_node(state):

    print("\n" + "="*60)
    print("TOOL NODE")
    print("="*60)

    print(f"Selected Tool: {state.selected_tool}")
    print(f"Tool Input: {state.tool_input} ")

    # check if tool exists
    if state.selected_tool not in AVAILABLE_TOOLS:
        state.tool_output = f"Tool selected '{state.selected_tool}' not in available tools"
        state.need_tool = False
        print(f"\n Tool not found: {state.selected_tool}")
        return state
    
    # now we will execute the tool
    tool_func = AVAILABLE_TOOLS[state.selected_tool]
    try:

        result = tool_func(state.tool_input)
        state.tool_output = result
        print(f"\nTool Output: {state.tool_output[:300]}")

    except Exception as e:
        state.tool_output = f"Tool Execution Error - {str(e)}"
        print(f"\n Error - {state.tool_output}")

    # Record in history
    state.history.append({
        "step": state.step_count,
        "type": "tool_usage",
        "tool": state.selected_tool,
        "input": state.tool_input,
        "output": state.tool_output
    })

    state.step_count += 1
    return state