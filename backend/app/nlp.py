import re
import unicodedata
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer

STOP_WORDS = set(stopwords.words("portuguese"))
STEMMER = RSLPStemmer()

def preprocess_text(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = text.lower()
    text = re.sub(r"[^a-zà-ú0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    tokens = [
        STEMMER.stem(word)
        for word in text.split()
        if word not in STOP_WORDS
    ]

    return " ".join(tokens)
