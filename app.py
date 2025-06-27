from flask import Flask, request, render_template
import pickle

# Load model and vectorizer
model = pickle.load(open('sentiment_model.pkl', 'rb'))
vectorizer = pickle.load(open('tfidf_vectorizer.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        review = request.form['review']
        review_vector = vectorizer.transform([review])
        prediction = model.predict(review_vector)[0]
        result = "Positive Review 😊" if prediction == 1 else "Negative Review 😠"
        return render_template('index.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True)
