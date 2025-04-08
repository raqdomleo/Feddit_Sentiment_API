import requests
import re

def get_comments(base_url, subfeddit, total_comments, limit):
    comments = []
    skip = 0

    while skip < total_comments:
        url = f"{base_url}/subfeddits/{subfeddit}/comments?skip={skip}&limit={limit}"
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Error en la petición: {response.status_code}")
            break

        data = response.json()
        comments.extend(data)

        skip += limit

    return comments[:total_comments]


def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+', '', text)  # eliminar links
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # eliminar caracteres especiales
    text = re.sub(r'\s+', ' ', text).strip()  # eliminar espacios múltiples
    return text
