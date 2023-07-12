import mysql.connector


def print_users(mydb):
    query = "SELECT * FROM User"
    user_cursor = mydb.cursor()
    try:
        user_cursor.execute(query)
        result = user_cursor.fetchall()
    except mysql.connector.Error as error:
        print('There was an error in fetching users:')
        print(error)
    finally:
        user_cursor.close()
        for x in result:
            print(x)


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


def find_user_wallet(userid, mydb):
    query = "SELECT wallet FROM User WHERE uid=%s"
    wallet = -1
    wallet_cursor = mydb.cursor()
    try:
        wallet_cursor.execute(query, (userid,))
        wallet = wallet_cursor.fetchone()[0]
    except mysql.connector.Error as error:
        print('There was an error in fetching wallet:')
        print(error)
    finally:
        wallet_cursor.close()
        return wallet


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


def find_movie_cost(movieid, mydb):
    query = "SELECT rental_price FROM Movie WHERE mid=%s"
    cost = -1
    price_cursor = mydb.cursor()
    try:
        price_cursor.execute(query, (movieid,))
        cost = price_cursor.fetchone()[0]
    except mysql.connector.Error as error:
        print('There was an error in fetching movie price:')
        print(error)
    finally:
        price_cursor.close()
        return cost


def list_genres(mydb):
    query = "SELECT DISTINCT genre FROM Movie;"
    cursor = mydb.cursor()
    genre_list = list()
    try:
        cursor.execute(query)
        genre_list = cursor.fetchall()
    except mysql.connector.Error as error:
        print('There was an error in fetching list of genres:')
        print(error)
    finally:
        cursor.close()
        return list(genre_list)
