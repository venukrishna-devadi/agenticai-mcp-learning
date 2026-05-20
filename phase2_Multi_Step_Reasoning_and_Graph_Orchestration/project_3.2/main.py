from graph import GraphAgent
from local_llm import LocalLLM

def main():

    llm = LocalLLM()
    agent = GraphAgent(llm)

    user_query = input("\nAsk Anything on Math, Science and History question:\n> ")

    result = agent.run(user_query)
    print("\n")
    print("=" * 70)
    print("FINAL ANSWER")
    print("=" * 70)
    print(f"Final Result State: {result}\n")
    print(result["final_response"])

if __name__ == "__main__":
    main()