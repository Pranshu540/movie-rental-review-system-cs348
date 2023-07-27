from ..util.util import find_user_id, find_movie_id
from datetime import date
from MySQLdb import Error


def create_review(username, moviename, rating, comment, mydb):
    userid = find_user_id(username, mydb)
    movieid = find_movie_id(moviename, mydb)
    query = "INSERT INTO Review VALUES(%s, %s, %s, %s, %s)"
    create_review_cursor = mydb.cursor()
    try:
        args = (userid, movieid, date.today(), rating, comment)
        create_review_cursor.execute(query, args)
        mydb.commit()
        return "Review successfully created!"
    except Exception as error:
        return Error('There was an error in adding the review to the database:', error)
    finally:
        create_review_cursor.close()


def remove_review(username, moviename, mydb):
    userid = find_user_id(username, mydb)
    movieid = find_movie_id(moviename, mydb)
    query = "DELETE FROM Review WHERE uid = %s AND mid = %s"
    remove_review_cursor = mydb.cursor()
    try:
        remove_review_cursor.execute(query, (userid, movieid))
        mydb.connection.commit()
        return "Review successfully removed!"
    except Exception as error:
        return Error('There was an error in removing the review from the database:', error)
    finally:
        remove_review_cursor.close()


def modify_review(username, moviename, rating, comment, mydb):
    userid = find_user_id(username, mydb)
    movieid = find_movie_id(moviename, mydb)
    query = "UPDATE Review SET review_date = %s, rating = %s, comment = %s WHERE uid = %s AND mid = %s"
    update_review_cursor = mydb.cursor()
    try:
        args = (date.today(), rating, comment, userid, movieid)
        update_review_cursor.execute(query, args)
        mydb.connection.commit()
        return "Review successfully modified."
    except Exception as error:
        return Error('There was an error in updating the review in the database:', error)
    finally:
        update_review_cursor.close()


def check_single_review(username, moviename, mydb):
    userid = find_user_id(username, mydb)
    movieid = find_movie_id(moviename, mydb)
    query = "SELECT rating, comment FROM Review WHERE uid = %s AND mid = %s;"
    check_review_cursor = mydb.cursor()
    try:
        args = (userid, movieid)
        check_review_cursor.execute(query, args)
        result = check_review_cursor.fetchone()
        return result
    except Exception as error:
        return Error(f"An error occurred: {error}")
    finally:
        check_review_cursor.close()


def get_movie_reviews(moviename, mydb):
    movieid = find_movie_id(moviename, mydb)
    query = "SELECT * FROM Review WHERE mid = %s"
    try:
        cursor = mydb.cursor()
        cursor.execute(query, [movieid])
        result = cursor.fetchall()
        return result
    except Exception as e:
        return Error(f"An error occurred: {e}")
    finally:
        cursor.close()
