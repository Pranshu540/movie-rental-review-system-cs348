from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os
from features.review import *
from loguru import logger

app = Flask(__name__)

load_dotenv()  # load variables from .env file

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

app.config['MYSQL_HOST'] = db_host
app.config['MYSQL_USER'] = db_user
app.config['MYSQL_PASSWORD'] = db_password
app.config['MYSQL_DB'] = db_name

mysql = MySQL(app)

@app.route('/get_reviews', methods=['GET'])
def get_reviews():


    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO info_table VALUES(%s,%s)''', (name, age))
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"


app.run(host='localhost', port=5000)
