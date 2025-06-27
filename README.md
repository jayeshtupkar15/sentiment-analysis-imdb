# Sentiment Analysis – IMDB Movie Reviews 🎬

A machine learning web application that classifies IMDB movie reviews as **positive** or **negative** using a trained logistic regression model and TF-IDF vectorization. Built using Flask, this project provides a simple UI for real-time sentiment prediction.

---

## 🔍 Features

- ✅ Clean and responsive Flask-based web interface
- ✅ Text vectorization using TF-IDF (max 5000 features)
- ✅ Logistic Regression for binary sentiment classification
- ✅ Supports real-time input and prediction
- ✅ Pre-trained model and vectorizer for instant use

---

## 🗂️ Project Structure

📦 sentiment-analysis-imdb
app.py # Flask backend \n
IMDB Review.ipynb # Model training notebook
Test.csv # Sample dataset
sentiment_model.pkl # Trained logistic regression model
tfidf_vectorizer.pkl # TF-IDF vectorizer
templates/index.html # Web UI for user input
