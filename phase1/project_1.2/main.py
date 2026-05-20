from local_llm import LocalLLM
from agent import CalculatorAgent
from tools import AgentTools

def main():

    llm = LocalLLM()

    tools = AgentTools()
    calulcator_agent = CalculatorAgent(llm, tools)

    while True:

        user_query = input("\nThis is a Math solving agent. Ask any Math questions: \n")

        if user_query.lower() == "end":
            break

        result = calulcator_agent.run(user_query)

        print("Final Result:\n")
        print(result)


if __name__ == "__main__":
    main()