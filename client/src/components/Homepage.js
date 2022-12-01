import React, { useState } from "react";
import Chart from "react-apexcharts";

import "./Homepage.css";

function Homepage() {
  const [name, setName] = useState("");
  const [result, setResult] = useState({
    movie_name: "",
    movie_sentiment: 0,
    rating: 0,
    top_five_comments: [],
    sentiment_classification: "",
  });
  const [isSearchSuccessful, setIsSearchSuccessful] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [options, setOptions] = useState({
    series: [
      {
        name: "sentiment",
        data: [30, 40, 45, 50, 49],
      },
    ],
    xaxis: {
      categories: [
        "mon aug 6",
        1668863278.0,
        1668865268.0,
        1668866268.0,
        1668963268.0,
      ],
    },
  });

  const searchHandler = (event) => {
    event.preventDefault();
    setIsLoading(true);
    setIsSearchSuccessful(false);

    fetch(`/movie/` + name).then((res) =>
      res.json().then((data) => {
        console.log(data);

        setIsLoading(false);
        setResult({
          movie_name: data.movie_name,
          movie_sentiment: data.movie_sentiment,
          rating: data.rating,
          top_five_comments: data.top_five_comments,
          sentiment_classification: data.sentiment_classification,
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

      {isLoading && <div className="loading">Loading...</div>}

      {isSearchSuccessful && (
        <div className="results">
          <p>You searched for: {result.movie_name}</p>
          <p>This movie has an IMDB rating of: {result.rating}</p>
          <p>
            This movie has an average sentiment of: {result.movie_sentiment}{" "}
            which is a mostly {result.sentiment_classification} reaction.
          </p>

          <h3>Top 5 Sentiment Comments from Reddit:</h3>
          {result.top_five_comments.map((comment, index) => (
            <p>
              {index + 1}. {comment}
            </p>
          ))}

          <h3>Sentiment Chart Over Time</h3>
          <Chart
            className="chart"
            options={options}
            series={options.series}
            type="line"
            width="500"
          />
        </div>
      )}
    </div>
  );
}

export default Homepage;
