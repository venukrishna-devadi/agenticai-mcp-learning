from local_llm import LocalLLM
from planner_agent import PlanningAgent

def main():

    llm = LocalLLM()
    agent = PlanningAgent(llm)

    goal = input("\nEnter your goal: \n")

    result = agent.run(goal)

    print("\nFinal Output: \n")
    print(result)

if __name__ =="__main__":
    main()