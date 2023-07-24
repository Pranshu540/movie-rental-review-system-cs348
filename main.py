from dotenv import load_dotenv
import os
from features.userauth import *
from features.review import *
from features.rental import *
from features.movie_filter import *
from features.delete_user import *
from features.recommended import *

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
    user_id = instance_user['uid']
    username = instance_user['username']
    # Once the user is logged in, we display the menu
    while True:
        print("Menu:")
        print("0. (ADMIN) See all users")
        print("1. See list of movies")
        print("2. See all reviews")
        print("3. See all rentals")
        print("4. Rent a movie")
        print("5. Add a review")
        print("6. Remove a review")
        print("7. Modify a review")
        print("8. Delete your account")
        print("9. See recommended movies")
        print("10. Quit")
        try:
            choice = int(input("Please enter your selection: "))
        except:
            print("Please input a valid choice.")
            continue
        if choice == 0:
            print("Printing all users in the database:")
            print_users(mydb)
        if choice == 1:
            title_filter = input("Please enter the title of the movie you want to filter: ")
            try:
                count_filter = int(input("Please enter the quantity of the movie you want to filter: "))
            except:
                print("Invalid count, needs to be a number >= 0. Try again")
                continue
            genre_filter = input("Please enter the genre of movie you want to filter: ")
            print("Here is the list of the movies with the filters applied: ")
            filter_movies(title_filter, count_filter, genre_filter, mydb)
        elif choice == 2:
            check_all_reviews(mydb)
        elif choice == 3:
            check_rentals(mydb)
        elif choice == 4:
            title = input("Please enter the name of the movie you'd like to rent: ")
            movie_id = find_movie_id(title, mydb)
            wallet = find_user_wallet(user_id, mydb)
            cost = find_movie_cost(movie_id, mydb)
            if cost == -1:
                print("Requested movie does not exist in the database.")
                continue
            print(f"The price of the movie requested is {cost}.")
            print(f"Your available funds are {wallet}.")
            option = input("Would you like to proceed with the rental? (y/n): ")
            while option != "y" and option != "n":
                option = input("Please enter y or n: ")
            if option == "y":
                rent_movie(user_id, movie_id, mydb)
            continue
        elif choice == 5:
            title = input("Please enter the name of the movie you'd like to review: ")
            rating = int(input("Please enter the rating of the movie you'd like to review: "))
            comment = input("Please enter your review: ")
            movie_id = find_movie_id(title, mydb)
            create_review(user_id, movie_id, rating, comment, mydb)
            print("Review has been added successfully.")
        elif choice == 6:
            title = input("Please enter the name of the movie you'd like to remove your review from: ")
            movie_id = find_movie_id(title, mydb)
            remove_review(user_id, movie_id, mydb)
            print("Review has been removed successfully.")
        elif choice == 7:
            title = input("Please enter the name of the movie that you reviewed: ")
            rating = int(input("Please enter the rating of the movie that you reviewed: "))
            comment = input("Please enter your new review comment: ")
            movie_id = find_movie_id(title, mydb)
            modify_review(user_id, movie_id, rating, comment, mydb)
            print("Review has been modified successfully.")
        elif choice == 8:
            confirm = input('Are you sure you wish to continue? (y/n): ')
            while confirm != "y" and confirm != "n":
                confirm = input("Please enter y or n: ")
            if(confirm == "y"):
                delete_user(user_id, mydb)
                break
            else:
                continue
        elif choice == 9:
            create_recommended(username, mydb)
            continue
        elif choice == 10:
            print(f"Thank you so much for using our system! See you again {username}!")
            break
        else:
            continue

if __name__ == "__main__":
    main()
