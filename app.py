from flask import Flask, request, jsonify
from flask_cors import CORS
from joblib import load
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import re
import numpy as np

app = Flask(__name__)
CORS(app)

# Load exported artifacts
vectorizer = load("vectorizer.joblib")
tfidf = load("tfidf.joblib")
movies = pd.read_csv("movies_clean.csv")

def clean_title(title):
    return re.sub("[^a-zA-Z0-9 ]", "", title)

@app.route("/recommend", methods=["POST"])
def search():
    title = request.json["title"]
    title = clean_title(title)

    query_vec = vectorizer.transform([title])
    similarity = cosine_similarity(query_vec, tfidf).flatten()

    indices = np.argpartition(similarity, -10)[-10:]
    results = movies.iloc[indices].iloc[::-1]

    return jsonify(
        results[["movieId", "title", "genres"]].to_dict(orient="records")
    )

if __name__ == "__main__":
    app.run(debug=True)
