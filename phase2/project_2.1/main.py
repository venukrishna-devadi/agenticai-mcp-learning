from local_llm import LocalLLM
from agent import ResearchAssistantAgent

def load_abstract():

    with open("phase2/project_2.1/sample_data/QLoRA.txt", "r") as f:
        abstract = f.read()
    
    return abstract

def main():

    llm= LocalLLM()

    agent = ResearchAssistantAgent(llm)

    abstract = load_abstract()

    agent.load_abstract(abstract)

    final_report = agent.run()

    print(final_report)


if __name__ == "__main__":
    main()