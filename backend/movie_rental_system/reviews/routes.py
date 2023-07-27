from flask import current_app, request, jsonify
from .models import create_review, remove_review, modify_review, check_single_review, check_all_reviews
from . import reviews


@reviews.route('/create_review/<userid>/<movieid>', methods=['POST'])
def add_review(userid, movieid):
    try:
        data = request.get_json()
        rating = data['rating']
        comment = data['comment']
        mydb = current_app.config['mysql']
        create_review(userid, movieid, rating, comment, mydb)
        return jsonify({"message": "Review added successfully."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@reviews.route('/remove_review/<userid>/<movieid>', methods=['DELETE'])
def delete_review(userid, movieid):
    try:
        mydb = current_app.config['mysql']
        remove_review(userid, movieid, mydb)
        return jsonify({"message": "Review deleted successfully."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@reviews.route('/modify_review/<userid>/<movieid>', methods=['PUT'])
def edit_review(userid, movieid):
    try:
        data = request.get_json()
        rating = data['rating']
        comment = data['comment']
        mydb = current_app.config['mysql']
        modify_review(userid, movieid, rating, comment, mydb)
        return jsonify({"message": "Review updated successfully."}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@reviews.route('/check_review/<userid>/<movieid>', methods=['GET'])
def get_single_review(userid, movieid):
    try:
        mydb = current_app.config['mysql']
        review = check_single_review(userid, movieid, mydb)
        return jsonify(review), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@reviews.route('/check_all_reviews/<movieid>', methods=['GET'])
def get_all_reviews(movieid):
    try:
        mydb = current_app.config['mysql']
        reviews = check_all_reviews(movieid, mydb)
        return jsonify(reviews), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
