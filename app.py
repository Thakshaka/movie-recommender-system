from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load datasets
movies = pd.read_csv('ml-25m/movies.csv')  # Load movies dataset
# ratings = pd.read_csv('ratings.csv')  # Load ratings dataset
ratings = pd.read_csv('ml-25m/ratings.csv', nrows=100000)  # Load ratings dataset (100000 rows)

# Function to recommend movies
def recommend_movies(movie_title):
    # Find the movie
    movie = movies[movies['title'].str.contains(movie_title, case=False, na=False)]
    if movie.empty:
        return []

    # Collaborative filtering logic
    movie_id = movie.iloc[0]['movieId']
    similar_users = ratings[ratings['movieId'] == movie_id]['userId']
    similar_ratings = ratings[ratings['userId'].isin(similar_users)]
    similar_ratings = similar_ratings.groupby('movieId').mean()['rating'].reset_index()
    recommended_movies = pd.merge(similar_ratings, movies, on='movieId').sort_values('rating', ascending=False).head(10)
    
    return recommended_movies[['title', 'genres']].to_dict(orient='records')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    movie_title = data.get('title')
    recommendations = recommend_movies(movie_title)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
