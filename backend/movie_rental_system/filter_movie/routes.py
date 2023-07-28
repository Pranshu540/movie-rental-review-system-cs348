from flask import request, jsonify, current_app
from . import models
from . import filter_movie
from decimal import Decimal


def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError


@filter_movie.route('/', methods=['GET'])
def filter_movies_route():
    # Retrieve the GET parameters
    title_filter = request.args.get('title', default=None, type=str)
    count_filter = request.args.get('count', default=0, type=int)
    genre_filter = request.args.get('genre', default=None, type=str)

    # Access your mysql object from the application context
    mydb = current_app.config['mysql']
    try:
        # Call the filter_movies function
        result = models.filter_movies(title_filter, count_filter, genre_filter, mydb.connection)
        result = [{k: decimal_default(v) if isinstance(v, Decimal) else v for k, v in row.items()} for row in result]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
