import json

VALID_TOOLS = [
    "summarize",
    "breakdown"
]

# {
#   "tool": "summarize"
# }

def validate_tool_decision(text: str):

    try:

        parsed = json.loads(text)
        tool = parsed.get("tool")

        if tool not in VALID_TOOLS:

            return {
                "valid": False,
                "error": f"Invalid tool: {tool}"
            }
        
        return {
            "valid": True,
            "tool": tool
        }
    
    except Exception as e:
        return {
            "valid": False,
            "error": str(e)
        }