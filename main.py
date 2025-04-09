import requests
import pandas as pd
from textblob import TextBlob
from utils import clean_text, get_comments

# Parameters
BASE_URL = "http://127.0.0.1:8080"  # Localhost API URL

SUBFEDDIT = 2  # ID of the subfeddit to analyze
LIMIT = 100  # Number of comments per API request
TOTAL_COMMENTS = 500  # Total number of comments to fetch

# Function to calculate the sentiment polarity of a text
def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity  # Returns a float between -1 (negative) and 1 (positive)

def main():
    print(f"Downloading comments from subfeddit: {SUBFEDDIT}")
    
    # Get comments using the custom get_comments function
    comments = get_comments(BASE_URL, SUBFEDDIT, TOTAL_COMMENTS, LIMIT)

    # Check if any comments were retrieved
    if not comments:
        print("No comments found. Please check the subfeddit ID or the API endpoint.")
        return
    
    # Convert comments list to DataFrame for easier manipulation
    df = pd.DataFrame(comments)

    # Clean the text of each comment
    df['clean_text'] = df['text'].apply(clean_text)

    # Analyze the sentiment of each cleaned comment
    df['sentiment'] = df['clean_text'].apply(analyze_sentiment)

    # Print first 5 rows of the resulting DataFrame
    print(df.head())

    # Export the results to a CSV file
    df.to_csv(f"{SUBFEDDIT}_sentiment.csv", index=False)
    print(f"Results saved to {SUBFEDDIT}_sentiment.csv")

# Entry point of the script
if __name__ == "__main__":
    main()
