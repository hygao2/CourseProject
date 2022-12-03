from flask import Flask
from flask import jsonify
from flask import request
import pandas as pd
from data import *
from preprocess import *

app = Flask(__name__)

# Get rating from IMDB
@app.route('/movie/<string:name>/rating', methods=['GET'])
def returnRating(name):
    df = pd.read_csv("IMDbRating.csv")
    return {"rating": df.loc[df['Title'] == name]['Rating'].to_string()[-3:]}
  
# Preprocess movie comments and return movie data
@app.route('/movie/<name>')
def get_movie(name):
    comments = movie_comments(name)
    df = pd.DataFrame(comments, columns=['title', 'id', 'body', 'score', 'created'])
    df.to_csv('../reddit_data/reddit_scraped_movie_comments.csv')
    
    # Sentiment Calculation
    preprocess()
    avg_sentiment = calculate_avg_sentiment()
    sentiment_classification = "neutral"
    if avg_sentiment <-0.03:
        sentiment_classification = "negative"
    elif avg_sentiment < 0.03:
        sentiment_classification = "neutral"
    else:
        sentiment_classification = "positive"

    # Top five sentiment comments
    cleaned_df = pd.read_csv('../reddit_data/cleaned_reddit_comments.csv')
    sorted_df = cleaned_df.sort_values(by=['compound'], ascending=False)
    top_five_indices = sorted_df.head(5)['Unnamed: 0']
    top_five_comments = []
    for index in top_five_indices:
        top_five_comments.append(df.iloc[int(index)]['body'])

    # IMDB rating
    imdb_df = pd.read_csv("IMDbRating.csv")
    rating = imdb_df.loc[imdb_df['Title'] == name]['Rating'].to_string()[-3:]

    # Graph data
    compound = cleaned_df['compound'].tolist()
    created = cleaned_df['created'].tolist()
    created.sort()

    # Returning an api for showing in  reactjs
    return {"movie_name" : name, 
            "movie_sentiment" : avg_sentiment, 
            "rating" : rating,
            "top_five_comments" : top_five_comments,
            "sentiment_classification" : sentiment_classification,
            "created_at": created,
            "compound_score": compound,}
  
# Running app
if __name__ == '__main__':
    app.run(debug=True)
