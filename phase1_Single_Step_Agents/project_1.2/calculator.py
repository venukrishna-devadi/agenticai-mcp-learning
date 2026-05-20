# STEP 4 — calculator.py

# Now we build:

# deterministic execution

def calculator(expression: str):

    try:

        # safe restricted eval
        result = eval(expression,
                      {"__builtins__": None},
                      {})
        
        return{
            "success": True,
            "result": result
        }
    
    except Exception as e:
        return{
            "success": False,
            "error": str(e)
        }