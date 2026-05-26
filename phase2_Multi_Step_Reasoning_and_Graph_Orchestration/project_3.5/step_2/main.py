from graph.graph import build_graph
from state import AgentState

def run(query):

    """Run the Langgraph Agent"""
    graph = build_graph()

    initial_state = AgentState(user_query=query)

    final_state = graph.invoke(initial_state)

    print("\n" + "="*60)
    print("FINAL ANSWER")
    print("="*60)
    print(f"Thought: {final_state.get('current_thought', 'No thought recorded')}")
    print(f"Tool Output: {final_state.get('tool_output', 'No tool output')}")
    print(f"Final Answer: {final_state.get('final_answer') or final_state.get('tool_output', 'No answer')}")

    return final_state

if __name__ == "__main__":
    query = input("Ask any reasonable math or normal question to this HITL workflow - \n> ")
    run(query=query)