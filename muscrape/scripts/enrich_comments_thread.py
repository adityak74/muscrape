import pandas as pd
import emoji
import multiprocessing
from googletrans import Translator
from transformers import pipeline

translator = Translator()
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(index, row):
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

def process_chunk(df_chunk, output_filename):
    results = []
    for index, row in df_chunk.iterrows():
        result = analyze_sentiment(index, row)
        if result[1] is not None and result[2] is not None:
            results.append(result)
    
    # Update the DataFrame with sentiment results
    for index, label, score in results:
        df_chunk.at[index, "sentiment_label"] = label
        df_chunk.at[index, "sentiment_score"] = score
    
    df_chunk.to_csv(output_filename, index=False)  # Save the chunk-specific output file

def main():
    df = pd.read_csv("/Users/aditya.karnam/Personal/muscrape/muscrape/scripts/combined_comments.csv")  # Load your input DataFrame
    total_reviews = len(df)
    
    print("Started sentiment analysis")

    chunk_size = 250
    num_processes = multiprocessing.cpu_count()
    
    pool = multiprocessing.Pool(processes=num_processes)
    
    for chunk_start in range(0, total_reviews, chunk_size):
        chunk_end = min(chunk_start + chunk_size, total_reviews)
        df_chunk = df.iloc[chunk_start:chunk_end]
        
        output_filename = f"/Users/aditya.karnam/Personal/muscrape/enriched_comments/output_chunk_{chunk_start}_{chunk_end}.csv"
        
        # Use multiprocessing to process each chunk in parallel
        pool.apply_async(process_chunk, args=(df_chunk, output_filename))
    
    pool.close()
    pool.join()

if __name__ == "__main__":
    main()
