# A node:
# receives state
# → modifies state
# → returns state
# That’s the entire graph model.

from logger import log_section
from prompts import THINK_PROMPT, ACTION_PROMPT

# Think Node
def think_node(state, llm):

    log_section("Think Node")
    user_query = state["user_query"]
    print("Analyzing user query ...")

    thought = llm.chat(system_prompt = THINK_PROMPT,
                       user_prompt = user_query,
                       temperature = 0.5)
    
    print(thought)
    state["thought"] = thought
    return state

# Action Node
def action_node(state, llm):

    log_section("Action Node")
    user_query = state["user_query"]
    thought = state["thought"]

    prompt = f"""
USER QUESTION: {user_query}

AGENT REASONING: {thought}
"""
    final_answer = llm.chat(system_prompt = ACTION_PROMPT,
                            user_prompt = prompt,
                            temperature = 0.5)
    
    print(final_answer)
    state["final_answer"] = final_answer
    return state

# Nodes:
# * do NOT directly call each other
# * do NOT control flow

# graph controls flow
# This is VERY different architecture.