# STEP 3 — validators.py

# We validate:

# * tool names
# * required parameters
# * safe expressions

# IMPORTANT LEARNING

# This is your first:

# Tool Safety Layer

# Very important.

# Real agent systems require:

# * sanitization
# * validation
# * access control

import json
import re

VALID_TOOLS = [
    "calculator",
    "normal_response"
]

def validate_tool_decision(text: str):

    try:
        parsed = json.loads(text)
        tool = parsed.get("tool")

        if tool not in VALID_TOOLS:
            return {
                "valid": False,
                "error": f"Invalid tool name: {tool}"
            }
        
        if tool == VALID_TOOLS[0]:
            expression = parsed.get("expression")

            if not expression:
                return{
                    "valid": False,
                    "error": "Missing Expression"
                }
            
            # we will only allow safe math characters
            pattern = r'^[0-9+\-*/(). ]+$'

            if not re.match(pattern, expression):
                return{
                    "valid": False,
                    "error": "Invalid and unsafe Math expression"
                }
        
        return{
            "valid": True,
            "data": parsed
        }
    
    except Exception as e:

        return {
            "valid": False,
            "error": str(e)
        }