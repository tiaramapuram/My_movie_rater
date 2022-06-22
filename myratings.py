from flask import jsonify, request, Blueprint, abort
from db import mydb

myr = Blueprint('myr',__name__, url_prefix="/myratings")

# Need to:
# Combine this is regular ratings. Should find a way to make it so theres one URL based on ID

# GET endpoint - retrieve all of my  movie ratings.
# POST endpoint - insert my rating preferences.
@myr.route('/', methods = ['GET', 'POST'])
def get_myr():
    cursor = mydb.cursor(dictionary=True)
    if request.method == 'GET':
        query = 'select * from My_movie_ratings;'
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()

        return jsonify(result)

    elif request.method == 'POST':
        info = request.get_json()
        ratingid = info.get('Rating_ID')
        movieid = info.get('Movie_ID')

        if not ratingid or not movieid:
            abort(400, 'Invalid request, missing field')

        query = 'INSERT INTO My_movie_ratings(Movie_ID, Rating_ID) values ' + \
            f"({ratingid}, {movieid})"
        
        cursor.execute(query)
        cursor.close()

        return 'Posted data successfully!', 201

@myr.route('/all', methods = ['GET'])
def get_all():
    cursor = mydb.cursor(dictionary=True)
    if request.method == 'GET':
        query = 'SELECT * FROM ((My_movie_ratings mr INNER JOIN Movies m ON mr.Movie_ID = m.Movie_ID) INNER JOIN Ratings r ON mr.Rating_ID = r.Rating_ID);'
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()

        return jsonify(result)
