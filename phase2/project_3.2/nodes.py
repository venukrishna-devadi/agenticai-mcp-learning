from logger import log_section
from prompts import ROUTER_PROMPT, SCIENCE_PROMPT, MATH_PROMPT, FINAL_PROMPT, HISTORY_PROMPT


# Router Node
def router_node(state, llm):
    
    log_section("Router Node --")
    print("Determining Query Type ---")

    route = llm.chat(system_prompt = ROUTER_PROMPT,
                     user_prompt = state.user_query,
                     temperature = 0.1)
    
    route = route.strip().lower()

    print(f"Detected Route: {route}")

    state.route = route

    return state

def math_node(state, llm):

    log_section("MATH NODE")

    response = llm.chat(system_prompt = MATH_PROMPT,
                        user_prompt = state.user_query,
                        temperature = 0)
    
    state.reasoning = response
    print(response)

    return state

def science_node(state, llm):
    log_section("SCIENCE NODE")

    response = llm.chat(system_prompt = SCIENCE_PROMPT,
                        user_prompt = state.user_query,
                        temperature = 0.5)
    
    state.reasoning = response
    print(response)

    return state

def history_node(state, llm):
    log_section("HISTORY NODE")

    response = llm.chat(
        system_prompt = HISTORY_PROMPT,
        user_prompt = state.user_query,
        temperature = 0.5
    )

    state.reasoning = response
    print(response)
    return state

def final_node(state, llm):
    log_section("FINAL NODE")

    final_response = llm.chat(system_prompt = FINAL_PROMPT,
                        user_prompt = state.reasoning,
                        temperature = 0.5)
    
    state.final_response = final_response
    print(final_response)

    return state