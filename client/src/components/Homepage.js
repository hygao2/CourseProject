import React, { useEffect, useState } from "react";

function Homepage() {
  const [name, setName] = useState("");
  const [returnVal, setReturnVal] = useState({
    movie_name: "",
  });

  const searchHandler = () => {
    fetch(`/movie/` + name).then((res) =>
      res.json().then((data) => {
        console.log(data);
        
        // Setting a data from api
        setReturnVal({ movie_name: data.movie_name });
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
        <button type="button" onClick={searchHandler}>
          Search
        </button>
      </form>

      <p>You searched for: {returnVal.movie_name}</p>
    </div>
  );
}

export default Homepage;
