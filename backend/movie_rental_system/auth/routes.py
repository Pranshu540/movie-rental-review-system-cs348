from flask import request, jsonify, current_app
from . import auth
from . import models


@auth.route('/signin', methods=['POST'])
def signin():
    username = request.json.get('username')
    password = request.json.get('password')
    if not username or not password:
        return jsonify({'error': 'Username and Password required'}), 400
    mydb = current_app.config['mysql']
    success = models.signin(username, password, mydb.connection)
    if success:
        return jsonify({'status': 'success'}), 200
    else:
        return jsonify({'error': 'Login failed'}), 400


@auth.route('/signup', methods=['POST'])
def signup():
    username = request.json.get('username')
    password = request.json.get('password')
    if not username or not password:
        return jsonify({'error': 'Username and Password required'}), 400
    mydb = current_app.config['mysql']
    success = models.signup(username, password, mydb.connection)
    if success:
        return jsonify({'status': 'success'}), 200
    else:
        return jsonify({'error': 'Signup failed'}), 400
