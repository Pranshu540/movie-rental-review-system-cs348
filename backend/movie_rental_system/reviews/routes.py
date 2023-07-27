from flask import current_app, request, jsonify
from .models import *
from . import reviews


@reviews.route('/create_review/<string:username>/<string:moviename>', methods=['POST'])
def add_review(username, moviename):
    try:
        data = request.get_json()
        rating = data['rating']
        comment = data['comment']
        mydb = current_app.config['mysql']
        create_review(username, moviename, rating, comment, mydb.connection)
        return jsonify({"message": "Review added successfully."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@reviews.route('/delete_review/<string:username>/<string:moviename>', methods=['DELETE'])
def delete_review(username, moviename):
    try:
        mydb = current_app.config['mysql']
        remove_review(username, moviename, mydb.connection)
        return jsonify({"message": "Review deleted successfully."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@reviews.route('/edit_review/<string:username>/<string:moviename>', methods=['PUT'])
def edit_review(username, moviename):
    try:
        data = request.get_json()
        rating = data['rating']
        comment = data['comment']
        mydb = current_app.config['mysql']
        modify_review(username, moviename, rating, comment, mydb.connection)
        return jsonify({"message": "Review updated successfully."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@reviews.route('/get_single_review/<string:username>/<string:moviename>', methods=['GET'])
def get_single_review(username, moviename):
    try:
        mydb = current_app.config['mysql']
        review = check_single_review(username, moviename, mydb.connection)
        return jsonify(review), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@reviews.route('/get_movie_review/<string:moviename>', methods=['GET'])
def get_movie_review(moviename):
    try:
        mydb = current_app.config['mysql']
        reviews = get_movie_reviews(moviename, mydb.connection)
        return jsonify(reviews), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
