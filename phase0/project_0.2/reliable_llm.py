# This is the core learning.

# We build:

# * retries
# * validation
# * repair attempts
# * defensive loops

from logger import logger
from validators import validate_json
from repair import basic_json_repair

class ReliableLLM:

    def __init__(self, llm):
        self.llm = llm
    
    def generate_json(
            self,
            system_prompt,
            user_prompt,
            temperature = 0.9,
            max_retries = 3,
            required_keys = None
    ):
        
        attempt = 1

        while attempt <= max_retries:

            logger("Attempt", f"attempt: {attempt}")

            response = self.llm.chat(
                system_prompt = system_prompt,
                user_prompt = user_prompt,
                temperature = temperature
            )

            logger("Raw Response", response)

            repaired_response = basic_json_repair(response)

            logger("Repaired Response", repaired_response)

            validation = validate_json(repaired_response, required_keys)

            if validation["valid"]:
                logger("Valid Json",
                       str(validation["data"]))
                
                return validation["data"]
            
            else:
                logger("Validation Failed",
                       validation["error"])
            
            attempt +=1
        
        return {
            "error": "Failed after retries"
        }