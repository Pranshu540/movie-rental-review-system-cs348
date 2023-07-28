from backend.movie_rental_system.util.util import *
from datetime import date


def create_review(userid, movieid, rating, comment, mydb):
    query = "INSERT INTO Review VALUES(%s, %s, %s, %s, %s)"
    create_review_cursor = mydb.cursor()
    try:
        args = (userid, movieid, date.today(), rating, comment)
        create_review_cursor.execute(query, args)

        mydb.commit()
    except mysql.connector.Error as error:
        print('There was an error in adding the review to the database:')
        print(error)
    finally:
        create_review_cursor.close()


def remove_review(userid, movieid, mydb):
    query = "DELETE FROM Review WHERE uid = %s AND mid = %s"
    remove_review_cursor = mydb.cursor()
    try:
        remove_review_cursor.execute(query, (userid, movieid))
        mydb.commit()
    except mysql.connector.Error as error:
        print('There was an error in removing the review from the database:')
        print(error)
    finally:
        remove_review_cursor.close()


def modify_review(userid, movieid, rating, comment, mydb):
    query = "UPDATE Review SET review_date = %s, rating = %s, comment = %s WHERE uid = %s AND mid = %s"
    update_review_cursor = mydb.cursor()
    try:
        args = (date.today(), rating, comment, userid, movieid)
        update_review_cursor.execute(query, args)

        mydb.commit()
    except mysql.connector.Error as error:
        print('There was an error in updating the review in the database:')
        print(error)
    finally:
        update_review_cursor.close()


def check_single_review(userid, movieid, mydb):
    query = "SELECT rating, comment FROM Review WHERE uid = %s AND mid = %s;"
    check_review_cursor = mydb.cursor()
    try:
        args = (userid, movieid)
        check_review_cursor.execute(query, args)
        result = check_review_cursor.fetchone()
        print("Printing review:")
        print(result)
    except Exception as error:
        print(f"An error occurred: {error}")
    finally:
        check_review_cursor.close()


def check_all_reviews(mydb):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Review")
    result = cursor.fetchall()
    for x in result:
        print(x)
    cursor.close()
