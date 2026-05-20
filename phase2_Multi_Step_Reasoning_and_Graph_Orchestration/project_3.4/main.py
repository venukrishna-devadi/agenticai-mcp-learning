from graph import ReactAgent
from dotenv import load_dotenv

load_dotenv()

def main():

    agent = ReactAgent()
    print("\n" + "="*60)
    print("ReAct AGENT - Iterative Reasoning + Tools")
    print("="*60)
    print("\nAvailable tools:")
    print("  • census_population_tool - Get state population")
    print("  • calculator_tool - Perform calculations")
    print("\nExample: What is the population of Texas divided by California?")

    user_query = input("\n❓ Ask something: ")

    result = agent.run(user_query=user_query)

    print("\n" + "="*60)
    print("FINAL ANSWER")
    print("="*60)
    print(result["final_answer"])

    print("\n" + "="*60)
    print("REASONING TRACE")
    print("="*60)
    for step in result["history"]:
        print(f"\n📌 Step {step['step']}:")
        print(f"   Thought: {step['thought']}")
        print(f"   Action: {step['tool']}({step['tool_input']})")
        print(f"   Observation: {step['observation']}")


if __name__ == "__main__":
    main()



# LLMs are NOT the agent

# The:
# * graph
# * memory
# * tools
# * routing
# * observations
# * state transitions

# TOGETHER form the agent.

# The LLM is only: one cognitive component.