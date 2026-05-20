from local_llm import LocalLLM
from reflection_agent import ReflectionAgent

def main():

    llm = LocalLLM()
    reflection_agent = ReflectionAgent(llm)

    user_query = input("\nAsk a question which you want to learn\n>")
    result = reflection_agent.run(user_query = user_query)

    print("\n")
    print("=" * 70)
    print("FINAL IMPROVED ANSWER")
    print("=" * 70)
    print(result["final_answer"])

if __name__ =="__main__":
    main()