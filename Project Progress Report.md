1) Which tasks have been completed?
The tasks that have been completed so far are being able to extract/scrape reddit posts/ IMDb critics rating. We have also finished cleaning the data and can run the prepreocessed data through sentiment analysis. We also connected our react frontend to flask backend. 

**scraping**
- We are able to connect with reddit and scrape for reddit posts/comments for a particular movie title
- We scraped IMDb for corresponding movie data / critics rating
**cleaning/preprocessing**
- Finished preprocessing of data (cleaning, removing punctuations, stopwords, links, lemmatization)
**sentiment analysis**
- Calculated a compound sentiment analysis score for each post/comment
- Able to store the sentiment analysis for each post/comment into csv files to be displayed in Frontend
**frontend**
- Able to successfully connect our flask backend to react frontend
- Added a search functionality that allow users to search for movies 
- Display the calculated average sentiment of the movie on frontend
- Add a loading functionality after user submits movie title request

2) Which tasks are pending? 
Most of the work remaining is on the frontend part of the application, dealing with pulling data from the backend and being able to display it on the frontend in certain ways and making the ui cleaner/intuitive. 

- Display comparison with IMDb ratings
- Display an analysis of the calculated average sentiment
- Display chart that plots the sentiment of the movie over time based on posts/comments
- Making the UI more user friendly/intuitive
- Display top 5 posts/comments with the strongest sentiment score

3) Are you facing any challenges? 
- there is a limit to how many comments we can pull at one time with the praw api, and with extracting comments form reddit posts as well, it takes a very long time to retrieve the data. 
- some of the posts/comments scraped are very irrelevant to the movies itself, sometimes its someone promoting a youtube channel etc.
- there is a lot of gen z slang in reddit posts that sentiment analysis isn't able to account for
