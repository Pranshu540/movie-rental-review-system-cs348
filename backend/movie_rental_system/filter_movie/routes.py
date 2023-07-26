from flask import request, jsonify, current_app
from . import models
from . import filter_movie


@filter_movie.route('/filter_movie', methods=['GET'])
def filter_movies_route():
    # Retrieve the GET parameters
    title_filter = request.args.get('title', default=None, type=str)
    count_filter = request.args.get('count', default=0, type=int)
    genre_filter = request.args.get('genre', default=None, type=str)

    # Access your mysql object from the application context
    mysql = current_app.config['mysql']
    mydb = mysql.connection

    # Call the filter_movies function
    result = models.filter_movies(title_filter, count_filter, genre_filter, mydb)

    return jsonify(result)