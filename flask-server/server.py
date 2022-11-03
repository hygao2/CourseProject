from flask import Flask, jsonify
  
  
# Initializing flask app
app = Flask(__name__)
  
  
# Route for seeing a data
@app.route('/movie/<name>')
def get_movie(name):

    # Returning an api for showing in  reactjs
    return {"movie_name" : name}
  
      
# Running app
if __name__ == '__main__':
    app.run(debug=True)