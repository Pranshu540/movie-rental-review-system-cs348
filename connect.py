import mysql.connector
from datetime import date

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password"
)


def find_user_id(user):
    query = "SELECT userid FROM User WHERE username=%s"
    user_id = -1
    try:
        user_id_cursor = mydb.cursor()
        user_id_cursor.execute("use sys")

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
    try:
        mid_cursor = mydb.cursor()
        mid_cursor.execute("use sys")

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
    try:
        create_review_cursor = mydb.cursor()
        create_review_cursor.execute("use sys")

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
    try:
        remove_review_cursor = mydb.cursor()
        remove_review_cursor.execute("use sys")

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
    try:
        update_review_cursor = mydb.cursor()
        update_review_cursor.execute("use sys")

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

# Testing out the review feature:
#
# print('This is before adding a review')
# cursor = mydb.cursor()
# cursor.execute("use sys")
# cursor.execute("SELECT * FROM Review")
# result = cursor.fetchall()
# for x in result:
#     print(x)
# cursor.close()
#
# create_review('george', 'The Book Thief', 4, 'Teaches people how to steal, great for a broke person like myself')
#
# print('\nThis is after adding a review')
# cursor = mydb.cursor()
# cursor.execute("use sys")
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
