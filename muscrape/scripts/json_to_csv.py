"""JSON to CSV converter for muscrape."""

import json
import pandas as pd
import kaggle
from dotenv import load_dotenv

load_dotenv()

JSON_PATH = "muscrape/data/search_results.json"
CSV_FOLDER_PATH = "muscrape/dataset"
CSV_PATH = "muscrape/dataset/hindi_music_dataset.csv"

with open(JSON_PATH, "r") as f:
    data = json.load(f)

df = pd.DataFrame(data)
df.to_csv(CSV_PATH, index=False)
print("Done converting to CSV!")

print("Upload to kaggle:")
kaggle.api.authenticate()
kaggle.api.dataset_create_version(CSV_FOLDER_PATH, "Updated dataset.")
print("Done!")
