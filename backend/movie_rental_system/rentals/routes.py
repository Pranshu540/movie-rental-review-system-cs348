from flask import current_app, jsonify
from .models import rent_movie, get_user_rentals
from . import rentals


@rentals.route('/<string:username>/rent_movie_by_name/<int:movie_id>', methods=['POST'])
def rent_movie_route(username, movie_id):
    try:
        mydb = current_app.config['mysql']
        response = rent_movie(username, movie_id, mydb.connection)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@rentals.route('/get_user_rentals/<string:username>', methods=['GET'])
def get_user_rentals(username):
    try:
        mydb = current_app.config['mysql']
        response = get_user_rentals(username, mydb.connection)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@rentals.route('/get_user_wallet/<string:username>', methods=['GET'])
def get_user_wallet(username):
    try:
        mydb = current_app.config['mysql']
        response = get_user_wallet(username, mydb.connection)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
