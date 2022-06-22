from flask import Flask, jsonify, request, abort
from ratings import ratings
from myratings import myr
from db import mydb

app = Flask(__name__)
app.register_blueprint(ratings)
app.register_blueprint(myr)

# Need to:
# Figure out how to get moves in without having to insert each row. Webscrape?
# Get movies by ID, but this is somewhat covered in ratings


# Endpoint to GET all movies
# Endpoint to POST or add a movie to the database
@app.route('/movies', methods = ['GET', 'POST'])
def get_movies():
    cursor = mydb.cursor(dictionary=True)
    if request.method == 'GET':
        query = 'select * from Movies;'
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()

        return jsonify(result)

    elif request.method == 'POST':
        info = request.get_json()
        id = info.get('Movie_ID')
        name = info.get('Movie_name')
        language = info.get('Movie_language')
        series = info.get('Movie_series')
        mactor = info.get('MActor')
        factor = info.get('FActor')
        director = info.get('Movie_director')
        
        if not id or not name or not language or not series or not mactor or not factor or not director:
            abort(400, 'Invalid request, missing field')

        query = 'INSERT INTO Movies(Movie_ID, Movie_name, Movie_language, Movie_series, MActor, FActor, Movie_director) VALUES ' + \
            f"({id}, '{name}', '{language}', '{series}', '{mactor}', '{factor}', '{director}')"
        cursor.execute(query)
        cursor.close()
        
        return 'Posted data successfully!',201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)