from textblob import TextBlob
from utils import clean_text


def analyze_sentiment(comment):
    """
    Analiza el sentimiento de un comentario limpio.
    Devuelve: positivo / negativo / neutro
    """
    cleaned = clean_text(comment)
    polarity = TextBlob(cleaned).sentiment.polarity

    if polarity > 0:
        return 'positive'
    elif polarity < 0:
        return 'negative'
    else:
        return 'neutral'


def get_sentiment_summary(comments):
    """
    Aplica el análisis de sentimiento a una lista de comentarios.
    Devuelve un diccionario resumen con el conteo de cada categoría.
    """
    summary = {'positive': 0, 'negative': 0, 'neutral': 0}

    for comment in comments:
        sentiment = analyze_sentiment(comment['text'])
        summary[sentiment] += 1

    return summary
