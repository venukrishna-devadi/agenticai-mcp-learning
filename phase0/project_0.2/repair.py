def basic_json_repair(text: str):

    text = text.replace("```json", "")
    text = text.replace("```", "")

    return text
