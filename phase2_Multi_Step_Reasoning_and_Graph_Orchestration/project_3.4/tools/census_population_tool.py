import os
import requests

from dotenv import load_dotenv
load_dotenv()

CENSUS_API_KEY = os.getenv("CENSUS_API_KEY")
print("key loaded:", bool(CENSUS_API_KEY))

def census_population_tool(state_name: str):

    try:

        base = "https://api.census.gov/data/2021/pep/population"

        params = {
            "get": "NAME,POP_2021",
            "for": "state:*",
            "key": CENSUS_API_KEY
        }

        response = requests.get(url=base,
                                params=params,
                                timeout=20)
        response.raise_for_status()
        data = response.json()
        print(data)

        headers = data[0]
        rows = data[1:]

        name_i = headers.index("NAME")
        pop_i = headers.index("POP_2021")

        populations = {}
        for row in rows:
            state = row[name_i]
            pop = int(row[pop_i])
            populations[state.lower()] = pop

        state_name = state_name.lower()

        if state_name not in populations:
            for key in populations:
                if state_name in key or key in state_name:
                    return str(populations[key])
            return f"Population data not found for {state_name}"
        
        pop_value = populations[state_name]
        print(f"{state_name}: {pop_value:,}")
        
        return str(pop_value)
    
    except Exception as e:
        return f"Census Tool Error: {str(e)}"

# Your tool now:

# * calls internet
# * parses JSON
# * validates data
# * transforms output
# * handles exceptions