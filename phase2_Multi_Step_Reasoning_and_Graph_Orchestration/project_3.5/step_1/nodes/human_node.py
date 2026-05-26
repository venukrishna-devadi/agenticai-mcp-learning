def human_node(state):

    print("\n" + "="*60)
    print("HUMAN NODE")
    print("="*60)

    print(f"\nAgent Asks - \n{state.human_question}")

    response = input("\nHuman Response:\n>")
    state.human_response = response

    state.step_count += 1

    state.history.append({
        "step": state.step_count,
        "type": "human_interaction",
        "question": state.human_question,
        "response": response
    })

    return state

# the graph PAUSES and WAITS.

# This is:
# interruptible execution.