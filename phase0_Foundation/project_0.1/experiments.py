from logger import log_section
from output_prser import try_parse_json

class PlaygroundExperiments:

    def __init__(self, llm):
        self.llm = llm
    
    def basic_chat(
            self,
            system_prompt,
            user_prompt,
            temperature = 0.0
    ):
        
        log_section("System Prompt", system_prompt)
        log_section("User Prompt", user_prompt)

        response = self.llm.chat(
            system_prompt =  system_prompt,
            user_prompt = user_prompt,
            temperature = temperature
        )

        log_section("Model Response", response)

        return response
    

    def json_experiment(
            self,
            system_prompt,
            user_prompt,
            temperature = 0.0
    ):
        
        response = self.basic_chat(system_prompt=system_prompt,
                                   user_prompt= user_prompt,
                                   temperature= temperature)
        
        result = try_parse_json(response)

        log_section("json parse result", result)

        return result