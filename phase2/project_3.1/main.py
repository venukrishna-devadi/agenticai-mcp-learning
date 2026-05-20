from local_llm import LocalLLM
from graph_agent import GraphAgent

def main():

    llm = LocalLLM()

    agent = GraphAgent(llm)

    user_query = input("\nAsk something which you want to know\n> ")

    result = agent.run(user_query)

    print("\n")
    print("=" * 70)
    print("FINAL ANSWER")
    print("=" * 70)
    print(result)
    print(result["final_answer"])

if __name__ == "__main__":
    main()