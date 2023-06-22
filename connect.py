from datetime import date, timedelta
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


def connect_to_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

# instance_user is a dictionary that stores the current user's username and uid
instance_user = {'username': '', 'uid': ''}

####
# Function: isLogged
# Description: Checks if the user is logged in
# Parameters: None
# Returns true if the user is logged in, false otherwise
# Author: Nicholas Jiang
####

def isLogged():
    return instance_user['username'] != '' and instance_user['uid'] != ''

####
# Function: Authenticate
# Description: Checks if the username and password are valid
# Parameters: username, password
# Returns true if there exists a user with the given username and password, false otherwise
# Author: Nicholas Jiang
####
def authenticate(username, password):
    db = mydb
    cursor = db.cursor()
    # SELECT EXISTS(SELECT 1 FROM Users WHERE username='givenUsername' AND password='givenPassword')
    query = f"SELECT EXISTS(SELECT 1 FROM Users WHERE username='{username}' AND password='{password}')"
    cursor.execute(query)
    result = cursor.fetchone()[0]
    return result == 1

####
# Function: Signin
# Description: Signs in the user with the given username and password
# Parameters: username, password
# Returns true if the user was successfully signed in, false otherwise
# Author: Nicholas Jiang
####
def signin(username, password):
    if (authenticate(username, password)):
        # login successful
        print("Login successful.")
        print("Welcome, " + username + "!")
        instance_user['username'] = username
        instance_user['uid'] = find_user_id(username)
        return True
    else:
        # login failed
        print("Login failed. Please try again.")
        return False

####
# Function: Signup
# Description: Creates a new user with the given username and password if the username is not taken
# Parameters: username, password
# Returns true if the user was successfully created, false otherwise
# Author: Nicholas Jiang
####
def signup(username, password):
    try:
        db = mydb
        cursor = db.cursor()
        query = f"INSERT INTO Users(username, password) VALUES ('{username}', '{password}')"
        cursor.execute(query)
        db.commit()
        print("User created successfully.")
        return True

    except mysql.connector.Error as error:
        print("Error creating user: {}".format(error))
        return False

def find_user_id(user):
    query = "SELECT userid FROM User WHERE username=%s"
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


def find_movie_id(movie):
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


def create_review(user, movie, rating, comment):
    query = "INSERT INTO Review VALUES(%s, %s, %s, %s, %s)"
    create_review_cursor = mydb.cursor()
    try:
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
    remove_review_cursor = mydb.cursor()
    try:
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
    update_review_cursor = mydb.cursor()
    try:
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


def rent_movie(user_id, movie_id):
    db = connect_to_db()
    cursor = db.cursor()

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
        cursor.execute(f"INSERT INTO Rental (uid, mid, rent_date, due_date, is_active) VALUES ({user_id}, {movie_id}, '{rent_date}', '{due_date}', 1)")

        # Commit the transaction
        db.commit()
        print("Movie rented successfully")

    except Exception as e:
        # If an error occurred, rollback the transaction
        db.rollback()
        print(f"An error occurred: {e}")

    finally:
        cursor.close()
        db.close()


def check_rentals():
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Rental")
    result = cursor.fetchall()
    for x in result:
        print(x)
    cursor.close()
    db.close()

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
# #
# # print('\nThis is after adding a review')
# cursor = mydb.cursor()
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

# Testing out the rental feature:


print('This is before renting movie')
check_rentals()

print('Harold renting movie')
rent_movie(2, 2)

print('This is after renting movie')
check_rentals()


def main():
    # We create a terminal interface for the user to interact with the database
    print("Welcome to the Movie Rental Database!")
    option = input("Are you a new user? (y/n): ")
    if option == "y":
        # If the user is new, we ask them to create an account
        print("Please create an account")
        username = input("Username: ")
        password = input("Password: ")
        while(signup(username, password) is False):
            print("Signup failed. Please try again.")
            username = input("Username: ")
            password = input("Password: ")
        # after sign up is successful we try logging in
        while(signin(username, password) is False):
            pass
            # continue trying to login until successful
    elif option == "n":
        # If the user is not new, we ask them to login
        print("Please login")
        username = input("Username: ")
        password = input("Password: ")
        while(signin(username, password) is False):
            print("Login failed. Please try again.")
            username = input("Username: ")
            password = input("Password: ")
    # Once the user is logged in, we display the menu
    print("Menu:")
    print("1. See all movies")
    print("3. See all rentals")
    print("4. Rent a movie")
    print("5. Add a review")
    print("6. Remove a review")
