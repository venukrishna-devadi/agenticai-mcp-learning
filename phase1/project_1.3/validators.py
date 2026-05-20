import json

VALID_TOOLS = [
    "read_statement",
    "normal_response"
]

def validate_tool(text: str):

    try:

        parsed = json.loads(text)
        tool = parsed.get("tool")

        if tool not in VALID_TOOLS:
            return {
                "valid": False,
                "error": f"Invalid tool {tool}"
            }
        
        return {
            "valid": True,
            "tool": tool
        }
    
    except Exception as e:

        return{
            "valid": False,
            "error": str(e)
        }