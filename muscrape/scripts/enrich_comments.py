import pandas as pd
import emoji
import asyncio
from googletrans import Translator
from transformers import pipeline

translator = Translator()
sentiment_pipeline = pipeline("sentiment-analysis")

async def analyze_sentiment(index, row):
    try:
        review_text = row["comment"]
        clean_text = emoji.replace_emoji(review_text)
        translated_text = translator.translate(clean_text).text
        result = sentiment_pipeline([translated_text])[0]
        label, score = result['label'], result['score']
        return index, label, score
    except Exception as ex:
        print(f"Exception at index {index}: {ex}")
        return index, None, None

async def main():
    df = pd.read_csv("/Users/aditya.karnam/Personal/muscrape/muscrape/scripts/combined_comments.csv")  # Load your input DataFrame
    total_reviews = len(df)
    
    tasks = []
    results = []

    print("Started sentiment analysis")

    for index, row in df.iterrows():
        task = asyncio.ensure_future(analyze_sentiment(index, row))
        tasks.append(task)

        if (index + 1) % 250 == 0:
            print(f"Completed Reviews: {index + 1}")
            print(f"Completed Percentage: {round((index / total_reviews) * 100, 2)}")
            break

    for task in asyncio.as_completed(tasks):
        index, label, score = await task
        print("Completed task", index)
        if label is not None and score is not None:
            results.append((index, label, score))

    # Update the DataFrame with sentiment results
    for index, label, score in results:
        df.at[index, "sentiment_label"] = label
        df.at[index, "sentiment_score"] = score

    df.to_csv("your_output_file_enriched.csv")  # Save the enriched DataFrame

if __name__ == "__main__":
    asyncio.run(main())
