import json
from prompts.think_prompt import THINK_PROMPT
from llm.local_llm import LocalLLM

def think_node(state):

    print("\n" + "="*60)
    print("THINK NODE")
    print("="*60)
    llm = LocalLLM()

    if state.step_count >= state.max_steps:
        state.need_tool = False
        state.final_answer = "Max reasoning steps reached."

        return state
    
    full_prompt = f"""
USER_QUESTION: {state.user_query}

HISTORY: {state.history}
"""
    
    response = llm.chat(system_prompt = THINK_PROMPT,
                        user_prompt = full_prompt,
                        temperature = 0.1)
    
    print("\nRaw Think Response\n> ")
    print(response)

    parsed = json.loads(response)
    state.current_thought = parsed["thought"]
    state.need_tool = parsed["need_tool"]
    
    if state.need_tool:

        state.selected_tool = parsed["tool_name"]
        state.tool_input = parsed["tool_input"]
    
    return state