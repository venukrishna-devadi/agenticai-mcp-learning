# STEP 5 — agent.py

# This is the brain.

# This is where:

# * reasoning
# * validation
# * retries
# * execution
# all connect together.

from logger import logger
from prompts import ROUTER_SYSTEM_PROMPT
from validators import validate_tool_decision



class IntentAgent:

    def __init__(self, llm, tools):
        self.llm = llm
        self.tools = tools

    def decide_tool(self,
                    user_query,
                    max_retries = 3):
        attempt = 1

        while attempt <= max_retries:

            logger(title="Routing Attempt",
                   content=f"Attempt {attempt}")
            
            response = self.llm.chat(system_prompt = ROUTER_SYSTEM_PROMPT,
                                     user_prompt = user_query,
                                     temperature = 0.0)
            
            logger("RAW AGENT DECISION",
                   response)
            
            validation = validate_tool_decision(response)

            if validation["valid"]:
                tool = validation["tool"]

                logger("Valid Tool",
                       tool)
                
                return tool
            
            else:
                logger("Validation Failed",
                       validation["error"])
                
                attempt += 1
            
        return "summarize"
    
    def execute_tool(self,
                     tool_name,
                     document):
        
        if tool_name == "summarize":
            return self.tools.summarize(document)
        
        elif tool_name == "breakdown":
            return self.tools.breakdown(document)
        
        else:
            return "Unknown tool"
        
    def run(
            self,
            user_query,
            document):
        
        logger("User Query",
               user_query)
        
        tool_name = self.decide_tool(user_query)

        logger("Final tool selection",
               tool_name)
        
        result = self.execute_tool(tool_name,
                                   document)
        
        logger("Final result from tool",
               str(result))
        
        return result