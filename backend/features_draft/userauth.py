import mysql.connector
from backend.movie_rental_system.util import util

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
def authenticate(username, password, mydb):
    db = mydb
    cursor = db.cursor()
    # SELECT EXISTS(SELECT 1 FROM User WHERE username='givenUsername' AND password='givenPassword')
    query = f"SELECT EXISTS(SELECT 1 FROM User WHERE username='{username}' AND password='{password}')"
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
def signin(username, password, mydb):
    if authenticate(username, password, mydb):
        # login successful
        print("Login successful.")
        print("Welcome, " + username + "!")
        instance_user['username'] = username
        instance_user['uid'] = util.find_user_id(username, mydb)
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
def signup(username, password, mydb):
    try:
        db = mydb
        cursor = db.cursor()
        query = f"INSERT INTO User(username, password) VALUES ('{username}', '{password}')"
        cursor.execute(query)
        db.commit()
        print("User created successfully.")
        return True

    except mysql.connector.Error as error:
        print("Error creating user: {}".format(error))
        return False
