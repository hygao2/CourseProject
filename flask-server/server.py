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
  
# Preprocess movie comments and return movie name
@app.route('/movie/<name>')
def get_movie(name):
    comments = movie_comments(name)
    df = pd.DataFrame(comments, columns=['title', 'id', 'body', 'score', 'created'])
    df.to_csv('../reddit_data/reddit_scraped_movie_comments.csv')
    preprocess()
    avg_sentiment = calculate_avg_sentiment()

    imdb_df = pd.read_csv("IMDbRating.csv")
    rating = imdb_df.loc[imdb_df['Title'] == name]['Rating'].to_string()[-3:]

    # Returning an api for showing in  reactjs
    return {"movie_name" : name, "movie_sentiment" : avg_sentiment, "rating" : rating}

  
# Running app
if __name__ == '__main__':
    app.run(debug=True)
