import json

def validate_json(text: str, required_keys: list = None):

    try:
        parsed = json.loads(text)

        # schema validation
        if required_keys:
            missing_keys = [key for key in required_keys if key not in parsed]
            if missing_keys:
                return{
                    "valid": False,
                    "data": None,
                    "error": f"Missing Keys : {missing_keys}"
                }

        return{
            "valid": True,
            "data": text,
            "error": None
        }
    
    except Exception as e:
        return{
            "valid": False,
            "data": None,
            "error": str(e)
        }