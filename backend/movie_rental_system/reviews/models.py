from ..util.util import find_user_id, find_movie_id
from datetime import date
from MySQLdb import Error


def create_review(username, movie_id, rating, comment, mydb):
    userid = find_user_id(username, mydb)
    query = "INSERT INTO Review VALUES(%s, %s, %s, %s, %s)"
    create_review_cursor = mydb.cursor()
    try:
        args = (userid, movie_id, date.today(), rating, comment)
        create_review_cursor.execute(query, args)
        mydb.commit()
        return "Review successfully created!"
    except Exception as error:
        return Error('There was an error in adding the review to the database:', error)
    finally:
        create_review_cursor.close()


def remove_review(username, movie_id, mydb):
    userid = find_user_id(username, mydb)
    query = "DELETE FROM Review WHERE uid = %s AND mid = %s"
    remove_review_cursor = mydb.cursor()
    try:
        remove_review_cursor.execute(query, (userid, movie_id))
        mydb.connection.commit()
        return "Review successfully removed!"
    except Exception as error:
        return Error('There was an error in removing the review from the database:', error)
    finally:
        remove_review_cursor.close()


def modify_review(username, movie_id, rating, comment, mydb):
    userid = find_user_id(username, mydb)
    query = "UPDATE Review SET review_date = %s, rating = %s, comment = %s WHERE uid = %s AND mid = %s"
    update_review_cursor = mydb.cursor()
    try:
        args = (date.today(), rating, comment, userid, movie_id)
        update_review_cursor.execute(query, args)
        mydb.connection.commit()
    except Exception as error:
        return Error('There was an error in updating the review in the database:', error)
    finally:
        update_review_cursor.close()
        return "Review successfully modified."


def check_single_review(username, movie_id, mydb):
    userid = find_user_id(username, mydb)
    query = "SELECT rating, comment FROM Review WHERE uid = %s AND mid = %s;"
    check_review_cursor = mydb.cursor()
    try:
        args = (userid, movie_id)
        check_review_cursor.execute(query, args)
        result = check_review_cursor.fetchone()
        return result
    except Exception as error:
        return Error(f"An error occurred: {error}")
    finally:
        check_review_cursor.close()


def get_movie_reviews(movie_id, mydb):
    query = "SELECT * FROM Review WHERE mid = %s"
    try:
        cursor = mydb.cursor()
        cursor.execute(query, [movie_id])
        result = cursor.fetchall()
        return result
    except Exception as e:
        return Error(f"An error occurred: {e}")
    finally:
        cursor.close()


def does_review_exist(username, movie_id, mydb):
    user_id = find_user_id(username)
    query = "SELECT * FROM Review WHERE uid = %s AND mid = %s"
    try:
        cursor = mydb.cursor()
        cursor.execute(query, [user_id, movie_id])
        result = cursor.fetchall()
        return True if result else False
    except Exception as e:
        return Error(f"An error occurred: {e}")
    finally:
        cursor.close()
