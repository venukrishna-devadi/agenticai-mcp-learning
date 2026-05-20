from local_llm import LocalLLM
from experiments import PlaygroundExperiments
from prompts import SYSTEM_PROMPTS

def main():

    print("\nInitializing Local LLM")

    llm = LocalLLM()

    experiments = PlaygroundExperiments(llm=llm)

    while True:

        print("Choose Experiments:\n")

        print("1. Basic Chat")
        print("2. JSON Reliability")
        print("3. Exit")

        choice = input("\n Enter Choice: ")

        if choice == "1":

            user_input = input("\n Ask Something: ")

            experiments.basic_chat(system_prompt=SYSTEM_PROMPTS["assistant"],
                                   user_prompt=user_input,
                                   temperature=0.0)
        elif choice == "2":

            user_prompt = """
            Generate JSON with:
            - name
            - topic
            - difficulty
            """

            experiments.json_experiment(
                system_prompt=SYSTEM_PROMPTS["strict_json"],
                user_prompt=user_input,
                temperature=0.0
            )
        elif choice == "3":

            print("\nExiting Playground...\n")

            break

        else:

            print("\nInvalid choice.\n")

if __name__ == "__main__":

    main()

