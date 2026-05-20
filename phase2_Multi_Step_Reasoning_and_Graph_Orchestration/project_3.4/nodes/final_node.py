from llm.local_llm import LocalLLM

def final_node(state):
    print("\n" + "="*60)
    print("FINAL NODE")
    print("="*60)

    llm = LocalLLM()

    system_prompt = f"""
You are a helpful assistant. Generate a clean, concise final answer.
Use the reasoning history to provide an accurate response.
"""
    
    history_text = ""
    for step in state.history:
        history_text += f"\nStep {step['step']}:"
        history_text += f"\n  Thought: {step['thought']}"
        history_text += f"\n  Tool: {step['tool']}({step['tool_input']})"
        history_text += f"\n  Result: {step['observation']}\n"


    user_prompt = f"""
User Question: {state.user_query}
Reasoning History: {state.history}
Please provide the final answer to the user's question.
"""
    
    response = llm.chat(system_prompt= system_prompt,
                        user_prompt= user_prompt,
                        temperature= 0.3)
    
    state.final_answer = response
    print(f"\nFinal answer generated")
    return state
    