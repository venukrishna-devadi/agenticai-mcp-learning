def calculator_tool(expression: str):

    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Calculation error - {str(e)}"