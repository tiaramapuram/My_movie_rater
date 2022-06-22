from flask import jsonify, request, Blueprint, abort
from db import mydb

ratings = Blueprint('ratings', __name__, url_prefix="/ratings")

# Need to:
# Clean up so there is one endpoint for this
# Add endpoint to connect movies with ratings

@ratings.route('/', methods = ['GET', 'POST'])
def get_ratings():
    cursor = mydb.cursor(dictionary=True)
    if request.method == 'GET':
        query = 'select * from Ratings;'
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        
        return jsonify(result)

    elif request.method == 'POST':
        info = request.get_json()
        id = info.get('Rating_ID')
        rating = info.get('Ratings')
        description = info.get('Rating_desc')
        
        if not id or not rating or not description:
            abort(400, 'Invalid request, missing field')

        query = 'INSERT INTO Ratings(Rating_ID, Ratings, Rating_desc) values ' + \
            f"({id}, {rating}, '{description}')"
        
        cursor.execute(query)
        cursor.close()

        return 'Posted data successfully!', 201

