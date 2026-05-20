from local_llm import LocalLLM
from agent import IntentAgent
from tools import AgentTools

DOCUMENT = """
Transformers are neural network architectures
that use self-attention mechanisms to process
sequential data efficiently.
They revolutionized natural language processing
by enabling parallel computation and better
long-range dependency handling.

"""

def main():
    llm = LocalLLM()

    tools = AgentTools(llm)
    agent = IntentAgent(llm,tools)

    while True:

        user_query = input("\n What do you want? \n>")

        if user_query.lower() == "exit":
            break

        result = agent.run(user_query=user_query,
                           document=DOCUMENT)
        print("\nResult:\n")
        print(result)

if __name__ =="__main__":
    main()