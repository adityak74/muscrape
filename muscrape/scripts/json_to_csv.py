"""JSON to CSV converter for muscrape."""

import json
import pandas as pd

JSON_PATH = "muscrape/data/search_results.json"
CSV_PATH = "muscrape/data/search_results.csv"

with open(JSON_PATH, "r") as f:
    data = json.load(f)

df = pd.DataFrame(data)

df.to_csv(CSV_PATH, index=False)

print("Done!")