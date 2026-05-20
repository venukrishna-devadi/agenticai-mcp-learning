from graph_agent import GraphAgent
from local_llm import LocalLLM

def main():

    llm = LocalLLM()
    agent = GraphAgent(llm)

    query = input("\nThis is a Calculator Agent. Ask a math problem or anything in general:\n> ")

    result = agent.run(query)
    print("\n")

    print("=" * 70)
    print(f"The resulted State is -  {result}")
    print("\n")
    print("=" * 70)
    print("FINAL ANSWER")
    print("=" * 70)
    print(result["final_answer"])

if __name__ == "__main__":
    main()