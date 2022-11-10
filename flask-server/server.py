from flask import Flask
from flask import jsonify
from flask import request
import pandas as pd
from data import *
from preprocess import *

app = Flask(__name__)


@app.route('/movie/<string:name>/rating', methods=['GET'])
def returnRating(name):
    df = pd.read_csv("IMDbRating.csv")
    return {"rating": df.loc[df['Title'] == name]['Rating'].to_string()[-3:]}
  
# Route for seeing a data
@app.route('/movie/<name>')
def get_movie(name):
    comments = movie_comments(name)
    df = pd.DataFrame(comments, columns=['title', 'id', 'body', 'score', 'created'])
    df.to_csv('../reddit_data/reddit_scraped_movie_comments.csv')
    preprocess()
    # Returning an api for showing in  reactjs
    return {"movie_name" : name}

  
      
# Running app
if __name__ == '__main__':
    app.run(debug=True)
