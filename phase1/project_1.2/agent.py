# STEP 6 — agent.py

# This is where:

# * routing
# * validation
# * execution
# * orchestration

# all come together.

from tools import AgentTools
from validators import validate_tool_decision
from prompts import ROUTER_SYSTEM_PROMPT
from logger import log_section

class CalculatorAgent:

    def __init__(self, llm, tools):
        self.llm = llm
        self.tools = tools

    def decision_agent(self,
                       user_query,
                       max_retries = 3):
        
        attempt = 1

        while attempt<= max_retries:

            log_section("Routing Agent",
                        f"Attempt {attempt}")
            
            response = self.llm.chat(system_prompt = ROUTER_SYSTEM_PROMPT,
                                    user_prompt = user_query,
                                    temperature = 0.0)
            
            log_section(
                "RAW AGENT DECISION",
                response
            )

            validation_response = validate_tool_decision(response)

            if validation_response["valid"]:
                log_section(
                    "Validated Action",
                    str(validation_response["data"])
                )

                return validation_response["data"]
            
            else:
                log_section(
                    "Validated Failed",
                    validation_response["error"])
            
            attempt +=1
        
        return{
            "tool": "normal_response"
        }
    

    def execute_decision(self,
                    decision,
                    user_query):
        
        tool = decision["tool"]

        if tool == "calculator":
            expression = decision["expression"]

            result = self.tools.calculator(expression)

            return f"Calculation result: {result}"
        
        else:

            return self.llm.chat(
                    system_prompt = "You are a helpful assistant",
                    user_prompt = user_query,
                    temperature = 0.5
                )
        
    def run(self, user_query):

        log_section("User_Query",
                    user_query)
        
        action = self.decision_agent(user_query)

        log_section("Agent Action",
                    action)

        execution = self.execute_decision(decision=action,
                                          user_query=user_query)
        
        log_section("Final Execution",
                    str(execution))
        
        return execution
        

                
            
        


