# CourseProject - MGH-SentimentAnalysis

Our team consists of Helena Gao (hygao2), Grace Jia (gracejj2), and Minjoong Kim (msk6). Our captain is Helena.

We will perform a sentiment analysis on a given movie by scraping Reddit. Our project will be based off of a project created in Spring 2019 by Jiawei Tang. In Jiawei’s project, users are able to search for a movie, receive a movie sentiment score, and the top 6 comments. However, in our project, users will be able to search for a movie and receive a general movie sentiment score, a graph showing sentiment over a time period, and a comparison between the user sentiment score and ratings for the movie from IMDb. Through this analysis, we think that it will be interesting to compare the perception towards the movie over time, as well as the difference between reviews made by critics and by the general public. Because we believe that comments and posts on Reddit are a good representation of the opinions of the general public, we think that our sentiment analysis will find interesting contrasts between how critics think about and evaluate a movie versus how the general population views the same movie.

Our approach consists of first scraping reddit for all posts/comments related to a particular movie and storing that in a dataset. The next step consists of preparing the data to run sentiment analysis which includes cleaning/preprocessing the data (ie. removing stopwords, punctuations, changing all words to lowercase), and lemmatization/tokenization. Next we will run sentiment analysis on each of the posts/comments to calculate an average sentiment score for the movie. Finally we will build out a frontend component where users can search for movies from the data available in our dataset and see the calculated average sentiment score, along with the imdb ratings, and a chart displaying the sentiment over time. 

Our team will utilize NLTK specifically with regards to data cleaning, tokenizing/lemmatizing, and optimizing the usability of our dataset. Our team will also use NLTK or a different library that has sentiment analysis tools, which we will utilize to extract sentiment from Reddit posts and comments. To access posts/comments from Reddit, our project will use PRAW, which will allow us to develop our own dataset of comments and posts from Reddit users about various movies. To access critic reviews from IMDb, we will use one of IMDb’s datasets to extract the information.Our team will use React to develop a visual component to our project which will allow users to search/see the various visualizations comparing sentiment analysis for a number of movies. 

We expect our app to complete all the goals and objectives we have outlined in this proposal, such as successfully preparing our data, performing the sentiment analysis, and the proposed frontend data visuals. We will evaluate our work based on how well we have accomplished these goals.

We plan to use Python for the data scraping, preprocessing, and sentiment analysis. We plan to use React for the frontend component for the user to interact with. 

20 * 3 = 60 Hours:
Scraping Reddit posts/comments for relevant data: 6 Hours
Scraping IMDb for corresponding movie data: 6 Hours
Preprocessing of data (cleaning, lemmatization, tokenization) - 6 Hours
Calculate sentiment analysis for each comment - 6 Hours
Calculate average sentiment analysis for a movie - 6 Hours
Store sentiment analysis for each comment into csv files to be displayed in frontend - 4 Hours
Connect React frontend to the project - 3 Hours
React
Allow users to search for movies and display a list of movies with matching titles from dataset - 6 Hours
Display calculated average sentiment score - 6 Hours
Display comparison with IMDb ratings - 6 Hours
Display chart showing sentiment over time - 6 Hours


