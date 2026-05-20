def parse_plan(plan_text):

    lines = plan_text.split("\n")
    tasks = []

    for line in lines:

        line = line.strip()
        if not line:
            continue

        if line[0].isdigit():
            cleaned = line.split(".", 1)[-1]

            tasks.append(cleaned.strip())
    
    return tasks