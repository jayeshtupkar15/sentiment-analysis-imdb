# Sentiment Analysis – IMDB Movie Reviews

A machine learning web application that classifies IMDB movie reviews as **positive** or **negative** using a trained logistic regression model and TF-IDF vectorization.

## Features
- Clean Flask web interface for entering custom reviews.
- Uses pre-trained ML model (`sentiment_model.pkl`) and vectorizer (`tfidf_vectorizer.pkl`).
- Includes sample data and notebook for reference.

## Tech Stack
- Python, Flask
- Scikit-learn, Pandas
- HTML (Jinja2 templating)

## How to Run
```bash
python app.py
