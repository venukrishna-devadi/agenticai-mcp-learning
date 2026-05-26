import json
from prompts.think_prompt import THINK_PROMPT
from local_llm import LocalLLM

def think_node(state):

    print("\n" + "="*60)
    print("THINK NODE")
    print("="*60)

    llm = LocalLLM()

    state.step_count += 1

    # Loop Gaurd
    if state.step_count >= state.max_steps:
        state.final_answer = f"Max reasoning steps ({state.max_steps}) reached."
        state.need_tool = False
        state.need_human = False
        return state
    
    prompt = f"""
User Query: {state.user_query}

Previous Human Response: {state.human_response if state.human_response else 'None yet'}

History of interactions: {state.history[-3:] if state.history else 'None'}

Current step: {state.step_count} of {state.max_steps}
"""
    
    response = llm.chat(
        system_prompt=THINK_PROMPT,
        user_prompt = prompt,
        temperature= 0.2
    )
    print("\nRaw Think Response:\n")
    print(response)

    try:
        parsed = json.loads(response)

        state.current_thought = parsed.get("thought", "")
        state.confidence = parsed.get("confidence", 0.0)
        
        state.need_tool = parsed.get("need_tool", False)
        state.need_human = parsed.get("need_human", False)

        state.selected_tool = parsed.get("tool_name", "")
        state.tool_input = parsed.get("tool_input", "")

        state.human_question = parsed.get("human_question", "")

    except Exception as e:
        print("Json Parsing Error", e)
        state.final_answer = "Failed to parse from reasoning agent."
    
    return state


# future reasoning uses human clarification.

# This is EXACTLY how HITL works.