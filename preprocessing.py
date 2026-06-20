import string
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

def preprocess(text):
    if not isinstance(text, str):
        return ""

    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))

    tokens = text.split()
    tokens = [token for token in tokens if token not in stop_words]

    return " ".join(tokens)