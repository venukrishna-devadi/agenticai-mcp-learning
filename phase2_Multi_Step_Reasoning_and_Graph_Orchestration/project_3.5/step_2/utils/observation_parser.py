import re

def extract_numbers(text: str):
    """
    Extract numbers from human or tool response.
    """
    numbers = re.findall(r"-?\d+\.?\d*", text)
    return [float(n) for n in numbers] if numbers else []


def is_math_expression(text: str):
    return any(op in text for op in ["/", "*", "+", "-"])