# Movie Recommender System

A content-based movie recommendation system built with Flask and React. The system uses TF-IDF vectorization and cosine similarity to find movies similar to a user's input.

## Overview

Enter a movie title to receive recommendations based on content similarity. The backend processes movie titles using TF-IDF vectorization and returns the top 10 most similar movies from a dataset of over 85,000 films.

## Tech Stack

**Backend:**
- Flask
- scikit-learn (TF-IDF vectorization, cosine similarity)
- pandas
- joblib (model persistence)

**Frontend:**
- React
- Material-UI

## Prerequisites

- Python 3.7+
- Node.js 14+
- npm or yarn

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd "movie-recommender-system"
```

2. Install Python dependencies:
```bash
pip install flask flask-cors scikit-learn pandas joblib numpy
```

3. Install frontend dependencies:
```bash
cd frontend
npm install
```

## Required Files

Ensure the following files are present in the project root:
- `movies_clean.csv` - Processed movie dataset
- `vectorizer.joblib` - Trained TF-IDF vectorizer
- `tfidf.joblib` - TF-IDF matrix

These files should be generated from the `Movie_Recommendation_System.ipynb` notebook if they're not already included.

## Running the Application

1. Start the Flask backend:
```bash
python app.py
```
The API will run on `http://127.0.0.1:5000`

2. Start the React frontend (in a separate terminal):
```bash
cd frontend
npm start
```
The frontend will run on `http://localhost:3000`

## API Endpoint

**POST** `/recommend`

Request body:
```json
{
  "title": "The Matrix"
}
```

Response:
```json
[
  {
    "movieId": 1234,
    "title": "The Matrix Reloaded",
    "genres": "Action|Sci-Fi|Thriller"
  },
  ...
]
```

## How It Works

1. User enters a movie title in the frontend
2. The title is cleaned (special characters removed) and sent to the backend
3. The backend vectorizes the input using the pre-trained TF-IDF vectorizer
4. Cosine similarity is computed against all movies in the dataset
5. Top 10 most similar movies are returned and displayed

## Project Structure

```
.
├── app.py                          # Flask backend API
├── movies_clean.csv                # Processed movie dataset
├── vectorizer.joblib               # TF-IDF vectorizer model
├── tfidf.joblib                    # TF-IDF matrix
├── Movie_Recommendation_System.ipynb  # Model training notebook
├── frontend/
│   ├── src/
│   │   └── App.js                  # React main component
│   └── package.json
└── ml-latest/                      # MovieLens dataset (optional)
```

## License

See LICENSE file for details.

