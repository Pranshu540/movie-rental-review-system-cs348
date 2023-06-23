from dotenv import load_dotenv
import os
from features.userauth import *
from features.review import *
from features.rental import *

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

def main():
    # We create a terminal interface for the user to interact with the database
    print("Welcome to the Movie Rental Database!")
    option = input("Are you a new user? (y/n): ")
    while option != "y" and option != "n":
        option = input("Please enter y or n: ")
    if option == "y":
        # If the user is new, we ask them to create an account
        print("Please create an account")
        username = input("Username: ")
        password = input("Password: ")
        while(signup(username, password, mydb) is False):
            print("Signup failed. Please try again.")
            username = input("Username: ")
            password = input("Password: ")
        # after sign up is successful we try logging in
        while(signin(username, password, mydb) is False):
            pass
            # continue trying to login until successful
    elif option == "n":
        # If the user is not new, we ask them to login
        print("Please login")
        username = input("Username: ")
        password = input("Password: ")
        while(signin(username, password, mydb) is False):
            print("Login failed. Please try again.")
            username = input("Username: ")
            password = input("Password: ")
    # Once the user is logged in, we display the menu
    while True:
        print("Menu:")
        print("1. See all movies")
        print("2. See all reviews")
        print("3. See all rentals")
        print("4. Rent a movie")
        print("5. Add a review")
        print("6. Remove a review")
        print("7. Modify a review")

if __name__ = "__main__":
    main()