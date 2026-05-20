import os
import requests
from dotenv import load_dotenv

load_dotenv()
CENSUS_API_KEY = os.getenv("CENSUS_API_KEY")
print("key loaded:", bool(CENSUS_API_KEY))
def get_tx_ca_pop():
    base = "https://api.census.gov/data/2021/pep/population"
    params = {
        "get": "NAME,POP_2021",
        "for": "state:*",
        "key": CENSUS_API_KEY
    }

    print(f"📡 Requesting {base}")
    r = requests.get(base, params=params, timeout=15)
    r.raise_for_status() # will raise if key is bad

    data = r.json() # now it's real JSON, not HTML
    headers, rows = data[0], data[1:]

    name_i = headers.index("NAME")
    pop_i = headers.index("POP_2021")

    pops = {row[name_i]: int(row[pop_i]) for row in rows
            if row[name_i] in ("Texas", "California")}

    tx = pops["Texas"]
    ca = pops["California"]

    print(f"Texas (2021 est): {tx:,}")
    print(f"California (2021 est): {ca:,}")
    print(f"Ratio TX/CA = {tx/ca:.4f}")

if __name__ == "__main__":
    get_tx_ca_pop()