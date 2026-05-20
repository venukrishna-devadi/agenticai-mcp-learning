from tools.calculator_tool import calculator_tool
from tools.census_population_tool import census_population_tool

def tool_node(state):

    print("\n" + "="*60)
    print("TOOL NODE")
    print("="*60)

    tool_name = state.selected_tool
    tool_input = state.tool_input

    print(f"Executing Tool: {tool_name}")
    print(f"Tool Input: {tool_input}")

    if tool_name == "calculator_tool":
        result = calculator_tool(tool_input)
    elif tool_name == "census_population_tool":
        result = census_population_tool(tool_input)

    else:

        result = "Unknown Tool"
    
    print(f"\nTool Output: {result}")
    state.tool_output = result

    state.step_count += 1

    state.history.append(
        # memory persistence
        {
            "step": state.step_count,
            "thought": state.current_thought,
            "tool": tool_name,
            "tool_input": tool_input,
            "observation": result
        }
    )

    return state