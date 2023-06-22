from flask import jsonify
from datetime import date
from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()  # load variables from .env file

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

mydb = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

# def get_db_connection():
#     return mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="password",
#         database="movie_rental_proj"
#     )


def find_user_id(user):
    query = "SELECT userid FROM User WHERE username=%s"
    user_id = -1
    try:
        user_id_cursor = mydb.cursor()
        user_id_cursor.execute("use sys")

        user_id_cursor.execute(query, (user,))
        user_id = user_id_cursor.fetchone()[0]
    except mysql.connector.Error as error:
        print('There was an error in fetching user id:')
        print(error)
    finally:
        user_id_cursor.close()
        return user_id


def find_movie_id(movie):
    query = "SELECT mid FROM Movie WHERE title=%s"
    mid = -1
    try:
        mid_cursor = mydb.cursor()
        mid_cursor.execute("use sys")

        mid_cursor.execute(query, (movie,))
        mid = mid_cursor.fetchone()[0]
    except mysql.connector.Error as error:
        print('There was an error in fetching movie id:')
        print(error)
    finally:
        mid_cursor.close()
        return mid


def create_review(user, movie, rating, comment):
    query = "INSERT INTO Review VALUES(%s, %s, %s, %s, %s)"
    try:
        create_review_cursor = mydb.cursor()
        create_review_cursor.execute("use sys")

        userid = find_user_id(user)
        # print(f'User ID has been acquired. ', userid)

        mid = find_movie_id(movie)
        # print(f'Movie ID has been acquired. ', mid)

        args = (userid, mid, date.today(), rating, comment)
        create_review_cursor.execute(query, args)

        mydb.commit()
    except mysql.connector.Error as error:
        print('There was an error in adding the review to the database:')
        print(error)
    finally:
        create_review_cursor.close()


def remove_review(user, movie):
    query = "DELETE FROM Review WHERE uid = %s AND mid = %s"
    try:
        remove_review_cursor = mydb.cursor()
        remove_review_cursor.execute("use sys")

        userid = find_user_id(user)
        # print(f'User ID has been acquired. ', userid)

        mid = find_movie_id(movie)
        # print(f'Movie ID has been acquired. ', mid)

        remove_review_cursor.execute(query, (userid, mid))

        mydb.commit()
    except mysql.connector.Error as error:
        print('There was an error in removing the review from the database:')
        print(error)
    finally:
        remove_review_cursor.close()


def modify_review(user, movie, rating, comment):
    query = "UPDATE Review SET review_date = %s, rating = %s, comment = %s WHERE uid = %s AND mid = %s"
    try:
        update_review_cursor = mydb.cursor()
        update_review_cursor.execute("use sys")

        userid = find_user_id(user)
        # print(f'User ID has been acquired. ', userid)

        mid = find_movie_id(movie)
        # print(f'Movie ID has been acquired. ', mid)

        args = (date.today(), rating, comment, userid, mid)
        update_review_cursor.execute(query, args)

        mydb.commit()
    except mysql.connector.Error as error:
        print('There was an error in updating the review in the database:')
        print(error)
    finally:
        update_review_cursor.close()


def rent_movie(uid, mid):
    cursor = mydb.cursor()

    # Proceed with the rental operation: update the User's wallet, decrease the Movie's quantity and insert a new Rental
    mydb.start_transaction()

    try:
        sql = """
        UPDATE User, Movie SET User.wallet = User.wallet - Movie.rental_price, 
        Movie.rental_quantity = Movie.rental_quantity - 1 
        WHERE User.uid = %s AND Movie.mid = %s AND Movie.rental_quantity > 0 AND User.wallet >= Movie.rental_price
        """
        cursor.execute(sql, (uid, mid))

        if cursor.rowcount == 0:
            mydb.rollback()
            return jsonify({'message': 'Movie not available or insufficient funds'}), 400

        sql = """
        INSERT INTO Rental (uid, mid, rent_date, due_date, is_active) 
        VALUES (%s, %s, date.today(), date.today() + timedelta(weeks=2), 1)
        """
        cursor.execute(sql, (uid, mid))

        mydb.commit()

    except mysql.connector.Error:
        mydb.rollback()
        return jsonify({'message': 'Error occurred during rental process'}), 500

    return jsonify({'message': 'Movie rented successfully'})

# Testing out the review feature:
#
# print('This is before adding a review')
# cursor = mydb.cursor()
# cursor.execute("SELECT * FROM Review")
# result = cursor.fetchall()
# for x in result:
#     print(x)
# cursor.close()
#
# create_review('george', 'The Book Thief', 4, 'Teaches people how to steal, great for a broke person like myself')
#
# print('\nThis is after adding a review')
# cursor = mydb.cursor()
# cursor.execute("use sys")
# cursor.execute("SELECT * FROM Review")
# result = cursor.fetchall()
# for x in result:
#     print(x)
# cursor.close()

# print('Removing the review.')
# remove_review('george', 'The Book Thief')
# cursor = mydb.cursor()
# cursor.execute("use sys")
# cursor.execute("SELECT * FROM Review")
# result = cursor.fetchall()
# for x in result:
#     print(x)
# cursor.close()

# print('Updating harold\'s review on The Shawshank Redemption')
# modify_review('harold', 'The Shawshank Redemption', 3, 'test-change')
# cursor = mydb.cursor()
# cursor.execute("use sys")
# cursor.execute("SELECT * FROM Review")
# result = cursor.fetchall()
# for x in result:
#     print(x)
# cursor.close()
