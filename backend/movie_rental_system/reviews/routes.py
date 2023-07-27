from flask import current_app, request, jsonify
from .models import *
from . import reviews


@reviews.route('/upsert_review/<string:username>/<int:movie_id>', methods=['POST'])
def upsert_review(username, movie_id):
    try:
        data = request.get_json()
        rating = data['rating']
        comment = data['comment']
        mydb = current_app.config['mysql']
        # check if the review is in the table
        exists = does_review_exist(username, movie_id, mydb.connection)
        if exists:
            modify_review(username, movie_id, rating, comment, mydb.connection)
            return jsonify({"message": "Review updated successfully."}), 200
        else:
            create_review(username, movie_id, rating, comment, mydb.connection)
            return jsonify({"message": "Review added successfully."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@reviews.route('/delete_review/<string:username>/<int:movie_id>', methods=['DELETE'])
def delete_review(username, movie_id):
    try:
        mydb = current_app.config['mysql']
        remove_review(username, movie_id, mydb.connection)
        return jsonify({"message": "Review deleted successfully."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@reviews.route('/get_single_review/<string:username>/<int:movie_id>', methods=['GET'])
def get_single_review(username, movie_id):
    try:
        mydb = current_app.config['mysql']
        review = check_single_review(username, movie_id, mydb.connection)
        return jsonify(review), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@reviews.route('/get_movie_reviews/<int:movie_id>', methods=['GET'])
def get_movie_reviews(movie_id):
    try:
        mydb = current_app.config['mysql']
        reviews = get_movie_reviews(movie_id, mydb.connection)
        return jsonify(reviews), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
