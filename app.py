import streamlit as st
import joblib
import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords')

model = joblib.load("sentiment_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")

stop_words = set(stopwords.words('english'))
ps = PorterStemmer()

def clean_text(text):
    text = text.lower()
    text = re.sub('<.*?>', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text

def remove_stopwords(text):
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)

def stem_text(text):
    words = text.split()
    words = [ps.stem(word) for word in words]
    return " ".join(words)

st.title("IMDb Sentiment Analysis")

review = st.text_area("Enter a movie review")

if st.button("Predict"):

    review = clean_text(review)
    review = remove_stopwords(review)
    review = stem_text(review)

    review_tfidf = tfidf.transform([review])

    prediction = model.predict(review_tfidf)[0]

    if prediction == "positive":
        st.success("😊 Positive Review")
    else:
        st.error("😞 Negative Review")
