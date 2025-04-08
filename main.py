import requests
import pandas as pd
from textblob import TextBlob
from utils import clean_text, get_comments

# Parámetros
BASE_URL = "http://0.0.0.0:8080"
SUBFEDDIT = "technology"  # Puedes cambiar a: "sports", "politics"
LIMIT = 100
TOTAL_COMMENTS = 500  # Cambiar según necesidad

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

def main():
    print(f"Descargando comentarios del subfeddit: {SUBFEDDIT}")
    comments = get_comments(BASE_URL, SUBFEDDIT, TOTAL_COMMENTS, LIMIT)

    df = pd.DataFrame(comments)
    df['clean_text'] = df['text'].apply(clean_text)
    df['sentiment'] = df['clean_text'].apply(analyze_sentiment)

    print(df.head())

    df.to_csv(f"{SUBFEDDIT}_sentiment.csv", index=False)
    print(f"Resultados guardados en {SUBFEDDIT}_sentiment.csv")

if __name__ == "__main__":
    main()
