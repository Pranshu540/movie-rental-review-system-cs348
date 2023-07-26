from flask import current_app, jsonify
from .models import rent_movie, check_rentals
from . import rentals


@rentals.route('/<int:user_id>/rent_movie/<int:movie_id>', methods=['POST'])
def rent_movie_route(user_id, movie_id):
    try:
        mydb = current_app.config['mysql']
        response = rent_movie(user_id, movie_id, mydb)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@rentals.route('/rentals', methods=['GET'])
def check_rentals_route():
    try:
        mydb = current_app.config['mysql']
        response = check_rentals(mydb)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
