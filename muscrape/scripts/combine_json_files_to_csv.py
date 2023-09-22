import pandas as pd
import glob

# Step 1: Define the folder path containing JSON files
folder_path = 'muscrape/data/*.json'

# Step 2: Initialize an empty list to store DataFrames
dfs = []

# Step 3: Loop through JSON files and load them into DataFrames
for file in glob.glob(folder_path):
    with open(file, 'r') as json_file:
        data = pd.read_json(json_file)
        dfs.append(data)

# Step 4: Concatenate DataFrames into one
combined_df = pd.concat(dfs, ignore_index=True)

# Step 5: Remove duplicates based on 'video_id' field
combined_df.drop_duplicates(subset='video_id', keep='first', inplace=True)

CSV_PATH = "muscrape/dataset/indian_music_dataset_combined.csv"

# Convert the combined DataFrame to CSV
combined_df.to_csv(CSV_PATH, index=False)

print("CSV file "+ CSV_PATH +" created successfully.")
