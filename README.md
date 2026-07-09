# IMDB-Sentiment-Analysis
# 🎬 SentiScope AI by Anubhav Singh

An NLP-powered web application that analyzes movie reviews and predicts whether the sentiment is **Positive 😊** or **Negative 😞** using Machine Learning.

## 🚀 Live Demo

Add your Streamlit deployment link here:

[Live Demo](YOUR_STREAMLIT_LINK)

---

## 📌 Project Overview

This project uses Natural Language Processing (NLP) techniques and Machine Learning to classify IMDb movie reviews into positive or negative sentiments.

The application takes a user review as input, preprocesses the text, converts it into numerical features using TF-IDF Vectorization, and predicts sentiment using a trained Logistic Regression model.

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- NLTK
- Scikit-learn
- Streamlit
- Joblib

---

## 📂 Dataset

IMDb Movie Reviews Dataset

- Movie reviews labeled as Positive or Negative
- Text classification problem
- Approximately 4,000 reviews used for training

---

## 🔄 NLP Pipeline

### 1. Text Cleaning
- Convert text to lowercase
- Remove HTML tags
- Remove special characters

### 2. Stopword Removal
Removed common words such as:
- the
- is
- are
- was

### 3. Stemming
Examples:

```text
watching → watch
loved → love
movies → movi
```

### 4. TF-IDF Vectorization

Converted text reviews into numerical features for machine learning.

```python
TfidfVectorizer(max_features=5000)
```

---

## 🤖 Machine Learning Model

### Logistic Regression

Used Logistic Regression for sentiment classification.

```python
LogisticRegression(max_iter=1000)
```

---

## 📊 Results

| Metric | Score |
|----------|----------|
| Accuracy | 86.68% |
| NLP Technique | TF-IDF |
| Model | Logistic Regression |

---

## 🖥️ Application Features

✅ Predict Positive Reviews

✅ Predict Negative Reviews

✅ Real-Time Predictions

✅ Interactive Streamlit Interface

---

## 📸 Screenshots

### Home Page

Add screenshot here

### Positive Prediction

Add screenshot here

### Negative Prediction

Add screenshot here

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/anubhavsingh23906-code/IMDB-Sentiment-Analysis.git
```

Move into the project directory:

```bash
cd IMDB-Sentiment-Analysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```text
IMDB-Sentiment-Analysis
│
├── app.py
├── sentiment_model.pkl
├── tfidf_vectorizer.pkl
├── requirements.txt
├── README.md
```

---

## 👨‍💻 Author

### Anubhav Singh

B.Tech CSE Student | Machine Learning Enthusiast

GitHub:
https://github.com/anubhavsingh23906-code

LinkedIn:
(Add your LinkedIn profile)

---

## ⭐ Future Improvements

- Deploy using Docker
- Add confidence score
- Support multi-class sentiment analysis
- Use advanced NLP models (BERT, DistilBERT)
- Improve UI/UX

---

### If you found this project useful, consider giving it a ⭐ on GitHub.
