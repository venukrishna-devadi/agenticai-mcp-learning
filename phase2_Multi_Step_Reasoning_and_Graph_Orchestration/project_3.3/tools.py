# Now we create actual executable tools.

def calculator(expression: str):

    try:
        result = eval(expression)
        return str(result)
    
    except Exception as e:
        return f"Calculation Error - {str(e)}"
    

# In production:
# NEVER use raw eval()

# Later you’ll replace this with:

# * sympy
# * numexpr
# * restricted parsers
# * sandboxed execution

# For learning:
# this is okay.