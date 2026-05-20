from local_llm import LocalLLM
from reliable_llm import ReliableLLM
from prompts import JSON_SYSTEM_PROMPT

def main():

    llm = LocalLLM()

    reliable_llm = ReliableLLM(llm)
    required_keys = ["name", "topic", "difficulty", "author"]

    user_prompt = """
Generate a beginner LLM Course Object."""

    response = reliable_llm.generate_json(
        system_prompt= JSON_SYSTEM_PROMPT,
        user_prompt= user_prompt,
        temperature= 0.0,
        max_retries =3,
        required_keys=required_keys
    )

    print("\nFinal Result")
    print(response)

if __name__ == "__main__":
    main()