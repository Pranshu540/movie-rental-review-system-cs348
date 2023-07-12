from util.util import *
import pandas as pd

def choose_genre(userid, genre_list, mydb):
    query = "SELECT m.genre FROM Rental r NATURAL JOIN Movie m WHERE r.uid = %s "\
    "GROUP BY m.genre ORDER BY count(m.genre) DESC LIMIT 1;"
    choose_genre_cursor = mydb.cursor()
    genre = ""
    try:
        choose_genre_cursor.execute(query, (userid, ))
        genre = choose_genre_cursor.fetchall()
        if choose_genre_cursor.rowcount == 0:
            while True:
                genre = input("Please enter your desired genre to see a recommended list of movies for:")
                if genre not in genre_list:
                    print("Invalid genre. Please check your spelling of the genre.")
                    continue
                break
    except mysql.connector.Error as error:
        print('There was an error in finding the most rented genre from the database:')
        print(error)
    finally:
        choose_genre_cursor.close()
        return genre
def create_recommended(username, mydb):
    userid = find_user_id(username, mydb)
    genre_list = list_genres(mydb)
    genre_list = [s.lower() for s in genre_list]
    genre = choose_genre(userid, genre_list, mydb)
    query = "CREATE VIEW Recommended AS " \
    "SELECT mid, title, rental_price, duration FROM Movie" \
    " WHERE rental_quantity > 0 " \
    "AND genre = %s ORDER BY RAND(100)" \
    "LIMIT 200;"
    create_recommended_cursor = mydb.cursor()
    try:
        args = (genre,)
        create_recommended_cursor.execute(query, args)
    except mysql.connector.Error as error:
        print('There was an error in creating the Recommended view:')
        print(error)
    finally:
        create_recommended_cursor.close()

    query2 = "SELECT * FROM Recommended ORDER BY RAND() LIMIT 5"
    cursor = mydb.cursor()
    try:
        cursor.execute(query2)
        result_list = cursor.fetchall()
        df = pd.DataFrame(result_list, columns=['title', 'rental_price', 'duration'])
    except mysql.connector.Error as error:
        print('There was an error in selecting from the view:')
        print(error)
    finally:
        cursor.close()

    print(f"Recommended movies of genre {genre} for {username}:")
    count = 1

    for val in result_list:
        print(f"{count}. {val}")
