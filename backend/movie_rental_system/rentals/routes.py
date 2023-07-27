from flask import current_app, jsonify
from .models import rent_movie, get_user_rentals
from . import rentals


@rentals.route('/<string:username>/rent_movie/<string:moviename>', methods=['POST'])
def rent_movie_route(username, moviename):
    try:
        mydb = current_app.config['mysql']
        response = rent_movie(username, moviename, mydb.connection)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@rentals.route('/rentals/<string:username>', methods=['GET'])
def get_user_rentals(username):
    try:
        mydb = current_app.config['mysql']
        response = get_user_rentals(username, mydb.connection)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
