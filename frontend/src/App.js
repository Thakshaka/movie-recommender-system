import React, { useState } from 'react';
import './App.css';

function App() {
  const [movieTitle, setMovieTitle] = useState('');
  const [recommendations, setRecommendations] = useState([]);
  const [error, setError] = useState('');

  const getRecommendations = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/recommend', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ title: movieTitle }),
      });

      const data = await response.json();
      
      if (data.length > 0) {
        setRecommendations(data);
        setError('');
      } else {
        setRecommendations([]);
        setError('No recommendations found.');
      }
    } catch (err) {
      console.error('Error fetching recommendations:', err);
      setRecommendations([]);
      setError('An error occurred. Please try again.');
    }
  };

  return (
    <div className="App">
      <h1>Movie Recommender System</h1>
      <div className="search-container">
        <input
          type="text"
          value={movieTitle}
          onChange={(e) => setMovieTitle(e.target.value)}
          placeholder="Enter movie title"
        />
        <button onClick={getRecommendations}>Recommend</button>
      </div>
      <div id="recommendations">
        {error && <p>{error}</p>}
        {recommendations.map((movie, index) => (
          <p key={index}>{movie.title} - {movie.genres}</p>
        ))}
      </div>
    </div>
  );
}

export default App;
