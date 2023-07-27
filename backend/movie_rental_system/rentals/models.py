from datetime import date, timedelta


def rent_movie(user_id, movie_id, mydb):
    cursor = mydb.connect.cursor()

    # Check if the user and movie exists and the movie is available for rent
    cursor.execute(f"SELECT rental_quantity FROM Movie WHERE mid = {movie_id}")
    movie_result = cursor.fetchone()
    if not movie_result:
        print("Movie does not exist")
        return
    elif movie_result[0] <= 0:
        print("Movie is not available for rent")
        return

    cursor.execute(f"SELECT wallet FROM User WHERE uid = {user_id}")
    user_result = cursor.fetchone()
    if not user_result:
        print("User does not exist")
        return

    # Check if the user has enough balance in the wallet to rent the movie
    cursor.execute(f"SELECT rental_price FROM Movie WHERE mid = {movie_id}")
    rental_price = cursor.fetchone()[0]
    if user_result[0] < rental_price:
        print("User does not have enough balance to rent the movie")
        return

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
        print("Movie rented successfully")

    except Exception as e:
        # If an error occurred, rollback the transaction
        mydb.rollback()
        print(f"An error occurred: {e}")

    finally:
        cursor.close()


def check_rentals(mydb):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Rental")
    result = cursor.fetchall()
    for x in result:
        print(x)
    cursor.close()
