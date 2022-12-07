# CourseProject - MGH-SentimentAnalysis

Our team consists of Helena Gao (hygao2), Grace Jia (gracejj2), and Minjoong Kim (msk6). Our captain is Helena.

We will perform a sentiment analysis on a given movie by scraping Reddit. Our project will be based off of a project created in Spring 2019 by Jiawei Tang. In Jiawei’s project, users are able to search for a movie, receive a movie sentiment score, and the top 6 comments. However, in our project, users will be able to search for a movie and receive a general movie sentiment score, a graph showing sentiment over a time period, and a comparison between the user sentiment score and ratings for the movie from IMDb. Through this analysis, we think that it will be interesting to compare the perception towards the movie over time, as well as the difference between reviews made by critics and by the general public. Because we believe that comments and posts on Reddit are a good representation of the opinions of the general public, we think that our sentiment analysis will find interesting contrasts between how critics think about and evaluate a movie versus how the general population views the same movie.

Our approach consists of first scraping reddit for all posts/comments related to a particular movie and storing that in a dataset. The next step consists of preparing the data to run sentiment analysis which includes cleaning/preprocessing the data (ie. removing stopwords, punctuations, changing all words to lowercase), and lemmatization/tokenization. Next we will run sentiment analysis on each of the posts/comments to calculate an average sentiment score for the movie. Finally we will build out a frontend component where users can search for movies from the data available in our dataset and see the calculated average sentiment score, along with the imdb ratings, and a chart displaying the sentiment over time. 

Our team will utilize NLTK specifically with regards to data cleaning, tokenizing/lemmatizing, and optimizing the usability of our dataset. Our team will also use NLTK or a different library that has sentiment analysis tools, which we will utilize to extract sentiment from Reddit posts and comments. To access posts/comments from Reddit, our project will use PRAW, which will allow us to develop our own dataset of comments and posts from Reddit users about various movies. To access critic reviews from IMDb, we will use one of IMDb’s datasets to extract the information.Our team will use React to develop a visual component to our project which will allow users to search/see the various visualizations comparing sentiment analysis for a number of movies. 

We expect our app to complete all the goals and objectives we have outlined in this proposal, such as successfully preparing our data, performing the sentiment analysis, and the proposed frontend data visuals. We will evaluate our work based on how well we have accomplished these goals.

We plan to use Python for the data scraping, preprocessing, and sentiment analysis. We plan to use React for the frontend component for the user to interact with. 

20 * 3 = 60 Hours:
- Scraping Reddit posts/comments for relevant data: 6 Hours
- Scraping IMDb for corresponding movie data: 6 Hours
- Preprocessing of data (cleaning, lemmatization, tokenization) - 6 Hours
- Calculate sentiment analysis for each comment - 6 Hours
- Calculate average sentiment analysis for a movie - 6 Hours
- Store sentiment analysis for each comment into csv files to be displayed in frontend - 4 Hours
- Connect React frontend to the project - 3 Hours
- React
  - Allow users to search for movies and display a list of movies with matching titles from dataset - 6 Hours
  - Display calculated average sentiment score - 6 Hours
  - Display comparison with IMDb ratings - 6 Hours
  - Display chart showing sentiment over time - 6 Hours


---------------------------------documentation-------------------------------------------------------------------

1) An overview of the function of the code (i.e., what it does and what it can be used for). 
Our project allows a user to input a movie title they are interested in to understand people’s average sentiments of the movie (reddit). 

Once users search for a particular movie, we then scrape the Reddit movie subreddit ‘movies’ and ‘MovieDetails’ using Praw (a Python Reddit API wrapper) for posts/comments regarding the searched movie title. We also scraped IMDb to retrieve a list of common movies along with the IMDb scores to be compared to the calculated average sentiment of the reddit posts/comments. We also cleaned/preprocessed the data by removing punctuation, numbers, special characters, lowercasing, lemmatizing, removing stop words to then calculate a compounded sentiment score. Using these scores, we also provide a chart to display the sentiment over time.


 (2) team member contributions

Msk6: 
Used PRAW to scrape relevant comments from Reddit relating to movie threads
Created csv files for IMDB data and scraped comments based on PRAW scraping
Created API endpoints using flask to retrieve IMDB rating based on movie name
 Added sentiment classification on frontend, based on sentiment score calculated from backend

Gracejj2:
Did the initial connection between flask backend/react frontend
Created search bar/search function, loading
Created API endpoint to retrieve relevant information from inputted movie title
Retrieved top 5 most significant post/comment for each movie to display on frontend

Hygao2 
Did the initial preprocessing for the retrieved reddit comments/posts
Cleaned data by removing punctuation, numbers, special characters, stopwords, lowercasing, lemmatizing
Calculated sentiment scores for the comments/posts using NLTK libraries
Calculated average sentiment for movies
Created the chart mapping out sentiment analysis trends over time


(3) related work and used libraries/models/previous projects, if any, 


Our project consists of a backend and frontend component that allows the user to view information about various movies. The frontend is built in React using Javascript and CSS, while the backend is written entirely in Python. The backend uses the Flask framework to run a server and create API’s that calculate the movie rating, sentiment score, and sentiment classification of a movie based on the name of the movie. These attributes are calculated by analyzing a large amount of reddit comments, which are scraped from Reddit threads through use of the PRAW library, and saved to a CSV file. These comments are then cleaned, lemmatized, and evaluated for sentiment using NLTK. The UI features a textbox that allows the user to search for a given movie, from which the search query is stored and used to call the API on the backend, which allows the UI to display the information retrieved from the API call to the user, allowing them to see various evaluations and ratings of the movie they searched for. 



(4) code structure or architecture diagram

Backend
data.py - authenticating/configuring PRAW to pull information from reddit, retrieves posts/comments from reddit movie subreddits for a specific movie

Imdb_scores.py - scraped imdb to get a list of movies and it's imdb rating

preprocess.py - cleans/preprocesses the reddit comments/posts and calculates a compounded sentiment score for each comment/post

server.py - the backend server that connects with the frontend, contains endpoints that the frontend calls and returns relevant posts/comments/sentiments related to the movie name

frontend
Homepage.js - bulk of frontend logic, consists of all the components displayed on the UI (search bar, chart, loading, etc)


(5) detailed instructions for reviewers to set up and run code, including possible errors or blockers.

How to run:
Clone the repo
Ensure that Python and Node.js are installed
Navigate to CourseProject/flask-server
Run ‘python server.py’
If there are any missing dependencies, use ‘pip install <package>’ to install them
Run ‘python server.py’ again if needed
Navigate to CourseProject/client
Run ‘npm install’ to install necessary dependencies
Run ‘npm start’



