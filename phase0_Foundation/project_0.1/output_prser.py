import json

def try_parse_json(text: str):

    try:
        parsed = json.loads(text)

        return{
            "success": True,
            "data": parsed
        }
    
    except Exception as e:

        return{
            "success": False,
            "error": str(e)
        }