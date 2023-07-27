from datetime import date, timedelta
from ..util.util import find_user_id, find_movie_id
from MySQLdb import Error


def rent_movie(username, movie_id, mydb):
    cursor = mydb.cursor()
    user_id = find_user_id(username, mydb)

    # Check if the user and movie exists and the movie is available for rent
    cursor.execute(f"SELECT rental_quantity FROM Movie WHERE mid = {movie_id}")
    movie_result = cursor.fetchone()
    if not movie_result:
        return Error("Movie does not exist")
    elif movie_result[0] <= 0:
        return Error("There are no more copies of this movie available to rent.")

    cursor.execute(f"SELECT wallet FROM User WHERE uid = {user_id}")
    user_result = cursor.fetchone()
    if not user_result:
        return Error("User does not exist")

    # Check if the user has enough balance in the wallet to rent the movie
    cursor.execute(f"SELECT rental_price FROM Movie WHERE mid = {movie_id}")
    rental_price = cursor.fetchone()[0]
    if user_result[0] < rental_price:
        return Error("User does not have enough balance to rent the movie.")

    # Start transaction
    cursor.execute("START TRANSACTION")

    try:
        # Decrement the quantity of the movie and deduct the price from the user's wallet
        cursor.execute(f"UPDATE Movie SET rental_quantity = rental_quantity - 1 WHERE mid = {movie_id}")
        cursor.execute(f"UPDATE User SET wallet = wallet - {rental_price} WHERE uid = {user_id}")

        # Insert a new rental record
        rent_date = date.today()
        due_date = date.today() + timedelta(weeks=2)
        cursor.execute(
            f"INSERT INTO Rental (uid, mid, rent_date, due_date, is_active) VALUES ({user_id}, {movie_id}, '{rent_date}', '{due_date}', 1)")

        # Commit the transaction
        mydb.commit()
        return "Movie rented successfully"

    except Exception as e:
        # If an error occurred, rollback the transaction
        mydb.rollback()
        return Error(f"An error occurred: {e}")

    finally:
        cursor.close()


def get_user_rentals(username, mydb):
    cursor = mydb.cursor()
    try:
        user_id = find_user_id(username, mydb)
        cursor.execute(f"SELECT * FROM Rental WHERE uid={user_id}")
        result = cursor.fetchall()
        return result
    except Exception as e:
        return Error(f"An error occurred: {e}")
    finally:
        cursor.close()


def get_user_wallet(username, mydb):
    cursor = mydb.cursor()
    try:
        user_id = find_user_id(username, mydb)
        cursor.execute(f"SELECT wallet FROM User WHERE uid={user_id}")
        result = cursor.fetchall()
        return result
    except Exception as e:
        return Error(f"An error occurred: {e}")
    finally:
        cursor.close()
