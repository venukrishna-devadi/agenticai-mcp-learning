# This is where everything becomes REAL.
# THINK NODE

# This node:

# * reasons
# * decides if tool needed
# * chooses tool
# * prepares tool arguments

import json
from logger import log_section
from prompts import TOOL_DECISION_PROMPT, FINAL_RESPONSE_PROMPT
from schemas import ToolDecision
from tools import calculator

def think_node(state, llm):

    log_section("Think Node")
    print("Analyzing whether tool is needed ..")
    response = llm.chat(system_prompt = TOOL_DECISION_PROMPT,
                        user_prompt = state.user_query,
                        temperature = 0.1)
    
    print("RAW LLM RESPONSE")
    print(response)

    # parse json
    parsed = json.loads(response)

    decision = ToolDecision(**parsed)

    # update state
    state.need_tool = decision.need_tool
    state.selected_tool = decision.tool_name
    state.tool_input = decision.tool_input

    print("State Updated")
    print("\nParsed Decision:\n")
    return state


# TOOL NODE

# This node:
# executes real tools

# tool node
def tool_node(state):

    log_section("TOOL NODE")
    print(f"Executing Tool: {state.selected_tool}")

    if state.selected_tool == "calculator":
        result = calculator(state.tool_input)

        state.tool_output = result

        print(f"\nTool Output: \n> {result}")
    
    return state

# FINAL NODE

# This node synthesizes:

# * tool outputs
# * reasoning
# * user request

# into polished response.

def final_node(state, llm):

    log_section("FINAL NODE")

    if state.need_tool:

        context = f"""

User Question: {state.user_query}
Tool Used: {state.selected_tool}
Tool Input: {state.tool_input}
Tool Output: {state.tool_output}
"""
        
    else:
        context = f"""
User Question: {state.user_query}

No tool was needed.
"""
        
    response = llm.chat(
        system_prompt = FINAL_RESPONSE_PROMPT,
        user_prompt = context,
        temperature = 0.4
    )

    state.final_answer = response
    print(response)

    return state