from prompts import GENERATOR_PROMPT, CRITIC_PROMPT, IMPROVEMENT_PROMPT
from logger import log_section
from local_llm import LocalLLM

class ReflectionAgent:

    def __init__(self, llm):
        self.llm = llm

        
    ####################################################################
    # STEP 1 — GENERATE INITIAL ANSWER
    ####################################################################

    def generate_initial_answer(self, user_query):

        log_section("STEP 1 — INITIAL GENERATION")
        print("Generating Initial Answer......\n")

        response = self.llm.chat(system_prompt = GENERATOR_PROMPT,
                                 user_prompt = user_query,
                                 temperature = 0.5)
        print(response)

        return response
    
    ####################################################################
    # STEP 2 — CRITIQUE ANSWER
    ####################################################################

    def critique_answer(self,
                        user_query,
                        generated_answer):
        
        log_section("STEP 2 — SELF CRITIQUE")

        critique_prompt = f"""

USER QUESTION IS {user_query}

GENERATED ANSWER IS {generated_answer}
"""
        
        response = self.llm.chat(system_prompt = CRITIC_PROMPT,
                                 user_prompt = critique_prompt,
                                 temperature = 0.3)
        
        print(response)
        return response
    
    ####################################################################
    # STEP 3 — IMPROVE ANSWER
    ####################################################################

    def improve_answer(self,
                      user_query,
                      critique_answer,
                      generated_answer):
        
        log_section("STEP 3 — ANSWER IMPROVEMENT")

        improv_prompt = f"""
USER QUERY - {user_query}

INITIAL ANSWER - {generated_answer}

CRITIQUE ANSWER - {critique_answer}
"""
        
        response = self.llm.chat(system_prompt = IMPROVEMENT_PROMPT,
                                 user_prompt = improv_prompt,
                                 temperature = 0.5)
        
        print(response)
        return response
    

    def run(self, user_query):

        initial_answer = self.generate_initial_answer(user_query)

        critique = self.critique_answer(user_query, initial_answer)

        final_answer = self.improve_answer(user_query,
                                           critique,
                                           initial_answer)
        
        return {
            "initial_answer": initial_answer,
            "critique_response": critique,
            "final_answer": final_answer
        }


        
    

        
        


    


