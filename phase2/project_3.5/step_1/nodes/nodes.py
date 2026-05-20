import json
from prompts.think_prompt import THINK_PROMPT
from local_llm import LocalLLM

def think_node(state):

    print("\n" + "="*60)
    print("THINK NODE")
    print("="*60)

    # Loop Gaurd
    