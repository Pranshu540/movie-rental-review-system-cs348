from flask import jsonify, current_app
from .models import delete_user
from . import delete_user


@delete_user.route('/delete_user/<userid>', methods=['DELETE'])
def remove_user(userid):
    try:
        mydb = current_app.config['mysql']
        result = delete_user(userid, mydb)
        if result:
            return jsonify({"message": "Account deletion successful."}), 200
        else:
            return jsonify({"message": "Account deletion unsuccessful. Please try again later."}), 500
    except Exception as e:
        return jsonify({"message": str(e)}), 500
