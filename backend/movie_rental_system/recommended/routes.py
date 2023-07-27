from flask import jsonify, current_app
from . import models
from . import recommended


@recommended.route('/username', methods=['GET'])
def get_recommended_movies(username):
    mydb = current_app.config['mysql']
    try:
        result = models.create_recommended(username, mydb)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

