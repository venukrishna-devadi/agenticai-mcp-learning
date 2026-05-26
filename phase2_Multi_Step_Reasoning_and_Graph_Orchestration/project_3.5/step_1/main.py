from graph import graph
from state import AgentState

query = input("\nAsk Something - \n>")
print(type(query))

initial_state = AgentState(user_query = query)
print(type(initial_state))
print(initial_state)


result = graph.invoke(
    initial_state, 
    config={"recursion_limit": 20} 
)
print("\n" + "="*60)
print("FINAL RESULT IS - ")
print(result)
print("\n" + "="*60)
print("FINAL ANSWER")

print("="*60)

print(result["final_answer"])