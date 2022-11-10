import React, { useEffect, useState } from "react";

function Homepage() {
  const [name, setName] = useState("");
  const [rating, setRating] = useState(0);

  const getImdbScore = () => {
    fetch(`/movie/` + name + `/rating`).then((res) =>
      res.json().then((data) => {
        console.log(data);

        // Setting a data from api
        setRating(data.rating);
      })
    );
  };

  const searchHandler = () => {
    fetch(`/movie/` + name).then((res) =>
      res.json().then((data) => {
        console.log(data);

        // Setting a data from api
        setName(data.movie_name);
      })
    );
  };

  return (
    <div>
      <h1>Movie Sentiment Analysis</h1>

      <form>
        <label htmlFor="name_input">Enter a movie name: </label>
        <input
          type="text"
          id="name_input"
          onChange={(e) => setName(e.target.value)}
        ></input>
        <button type="button" onClick={getImdbScore}>
          Search
        </button>
      </form>

      <p>You searched for:</p>
      <p>{name}</p>
      <p>With IMDB rating: {rating}</p>
    </div>
  );
}

export default Homepage;
