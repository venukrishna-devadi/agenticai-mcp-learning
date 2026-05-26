from utils.observation_parser import extract_numbers

def human_node(state):

    print("\n============================================================")
    print("HUMAN NODE")
    print("============================================================")

    print("\nAgent Question:")
    print(state.human_question)

    human_input = input("\nPlease give your response: ")

    # store response
    state.human_response = human_input
    state.need_human = False  # reset flag, we got the human input

    # update observation
    state.last_observation = {
        "type": "human_response",
        "content": human_input,
        "success": True
    }

    # history tracking
    state.history.append({
        "type": "human",
        "question": state.human_question,
        "response": human_input
    })

    # IMPORTANT: move forward
    state.step_count += 1

    # IMPORTANT FIX (prevents re-asking same question)
    state.need_human = False

    return state