from local_llm import LocalLLM
def final_node(state):

    print("\n" + "="*60)
    print("FINAL NODE")
    print("="*60)
    llm = LocalLLM()

    synthesis_prompt = f"""
    User asked: {state.user_query}
    
    Reasoning history: {state.history}
    
    Tool output (if any): {state.tool_output}
    Human clarification (if any): {state.human_response}
    
    Generate a clear, concise final answer.
    """

    state.final_answer = llm.chat(
        system_prompt = "You are a helpful assistant that provides final answers based on reasoning and tool outputs.",
        user_prompt = synthesis_prompt,
        temperature = 0.0
    )
    
    return state