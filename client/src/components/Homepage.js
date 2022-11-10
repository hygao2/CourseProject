import React, { useEffect, useState } from "react";
import "./Homepage.css";

function Homepage() {
  const [name, setName] = useState("");
  const [result, setResult] = useState({
    movie_name: "",
    movie_sentiment: 0,
    rating: 0,
  });
  const [isSearchSuccessful, setIsSearchSuccessful] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  const searchHandler = (event) => {
    event.preventDefault();
    setIsLoading(true);
    setIsSearchSuccessful(false);

    fetch(`/movie/` + name).then((res) =>
      res.json().then((data) => {
        console.log(data);

        // Setting a data from api
        setIsLoading(false);
        setResult({
          movie_name: data.movie_name,
          movie_sentiment: data.movie_sentiment,
          rating: data.rating,
        });
        setIsSearchSuccessful(true);
      })
    );
  };

  return (
    <div className="wrapper">
      <div className="header">Movie Sentiment Analysis</div>
      <form>
        <label htmlFor="name_input">Enter a movie name: </label>
        <input
          type="text"
          id="name_input"
          onChange={(e) => setName(e.target.value)}
        ></input>
        <button type="button" onClick={searchHandler}>
          Search
        </button>
      </form>

      {isLoading && <div>Loading...</div>}

      {isSearchSuccessful && (
        <div className="results">
          <p>You searched for: {result.movie_name}</p>
          <p>This movie has an IMDB rating of: {result.rating}</p>
          <p>This movie has an average sentiment of: {result.movie_sentiment}</p>
        </div>
      )}
    </div>
  );
}

export default Homepage;
