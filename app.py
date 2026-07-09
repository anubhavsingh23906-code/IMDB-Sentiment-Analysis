import streamlit as st
import joblib

model = joblib.load("sentiment_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")

st.title("IMDb Sentiment Analysis")

review = st.text_area("Enter a movie review")

if st.button("Predict"):

    review_tfidf = tfidf.transform([review])

    prediction = model.predict(review_tfidf)[0]

    if prediction == "positive":
        st.success("😊 Positive Review")
    else:
        st.error("😞 Negative Review")
