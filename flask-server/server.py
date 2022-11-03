from flask import Flask
from flask import jsonify
from flask import request
import pandas as pd
app = Flask(__name__)


@app.route('/movies/<string:name>', methods=['GET'])
def returnRating(name):
    df = pd.read_csv("IMDbRating.csv")
    return df.loc[df['Title'] == name]['Rating'].to_string()[-3:]
    



app = Flask(__name__)
  
  
# Route for seeing a data
@app.route('/movie/<name>')
def get_movie(name):

    # Returning an api for showing in  reactjs
    return {"movie_name" : name}
  
      
# Running app
if __name__ == '__main__':
    app.run(debug=True)
