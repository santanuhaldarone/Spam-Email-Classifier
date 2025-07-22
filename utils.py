import pickle
import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"\W+", " ", text)
    text = re.sub(r"\d+", "", text)
    return text.strip()

def load_model():
    with open("model/vectorizer.pkl" , "rb") as vf:
        vectorizer = pickle.load(vf)
    with open("model/spam_classifier.pkl","rb") as mf:
        model = pickle.load(mf)
    return vectorizer , model

def predict_spam(text, vectorizer, model):
    cleaned = clean_text(text)
    vector = vectorizer.transform([cleaned])
    label = model.predict(vector)[0]
    prob = model.predict_proba(vector)[0][label]
    return ("Spam" if label == 1 else "Not Spam", round(prob * 100, 2))
