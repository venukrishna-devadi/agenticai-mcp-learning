from local_llm import LocalLLM
from agent import FileReaderAgent
from tools import AgentTools

def main():

    llm = LocalLLM()
    tools = AgentTools()

    agent = FileReaderAgent(llm = llm,
                            tools = tools)
    
    while True:

        user_query = input("\nAsk about your bofa bank statement -\n")

        if user_query.lower() == "exit":
            break

        result = agent.run(user_query)

        print("Final Result is - \n")
        print(result)


if __name__ =="__main__":
    main()
    