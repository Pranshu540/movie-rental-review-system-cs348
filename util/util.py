import mysql.connector


def find_user_id(user, mydb):
    query = "SELECT uid FROM User WHERE username=%s"
    user_id = -1
    user_id_cursor = mydb.cursor()
    try:
        user_id_cursor.execute(query, (user,))
        user_id = user_id_cursor.fetchone()[0]
    except mysql.connector.Error as error:
        print('There was an error in fetching user id:')
        print(error)
    finally:
        user_id_cursor.close()
        return user_id


def find_movie_id(movie, mydb):
    query = "SELECT mid FROM Movie WHERE title=%s"
    mid = -1
    mid_cursor = mydb.cursor()
    try:
        mid_cursor.execute(query, (movie,))
        mid = mid_cursor.fetchone()[0]
    except mysql.connector.Error as error:
        print('There was an error in fetching movie id:')
        print(error)
    finally:
        mid_cursor.close()
        return mid
