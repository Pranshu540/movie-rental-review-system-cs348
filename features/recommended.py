from util.util import *
import pandas as pd
import mysql.connector


def choose_genre(userid, genre_list, mydb):
    query = (
        "SELECT m.genre FROM Rental r NATURAL JOIN Movie m WHERE r.uid = %s "
        "GROUP BY m.genre ORDER BY count(m.genre) DESC LIMIT 1;"
    )
    choose_genre_cursor = mydb.cursor()
    genre = ""
    try:
        choose_genre_cursor.execute(query, (userid,))
        genre = choose_genre_cursor.fetchall()
        if choose_genre_cursor.rowcount == 0:
            while True:
                genre = input(
                    "Please enter your desired genre to see a recommended list of movies for:"
                )
                if genre not in genre_list:
                    print("Invalid genre. Please check your spelling of the genre.")
                    continue
                break
    except mysql.connector.Error as error:
        print("There was an error in finding the most rented genre from the database:")
        print(error)
    finally:
        choose_genre_cursor.close()
        return genre


def create_recommended(username, mydb):
    userid = find_user_id(username, mydb)
    genre_list = list_genres(mydb)
    genre_list = [s.lower() for s in genre_list]
    genre = choose_genre(userid, genre_list, mydb)
    query = (
        "CREATE VIEW Recommended AS "
        "SELECT mid, title, rental_price, duration FROM Movie"
        " WHERE rental_quantity > 0 "
        "AND genre = %s ORDER BY RAND(100)"
        "LIMIT 200;"
    )
    create_recommended_cursor = mydb.cursor()
    try:
        args = (genre,)
        create_recommended_cursor.execute(query, args)
    except mysql.connector.Error as error:
        print("There was an error in creating the Recommended view:")
        print(error)
    finally:
        create_recommended_cursor.close()

    query2 = "SELECT * FROM Recommended ORDER BY RAND() LIMIT 5"
    cursor = mydb.cursor()
    try:
        cursor.execute(query2)
        result_list = cursor.fetchall()
        df = pd.DataFrame(result_list, columns=["title", "rental_price", "duration"])
    except mysql.connector.Error as error:
        print("There was an error in selecting from the view:")
        print(error)
    finally:
        cursor.close()

    print(f"Recommended movies of genre {genre} for {username}:")
    count = 1

    print("Title Rental_Price Duration")

    for val in df.values:
        print(f"{count}. {val[0]} {val[1]} {val[2]}")
        count += 1

    # Ask the user if they want to remove any movies from the recommended list
    while True:
        subset_wanted = []
        subset_unwanted = []
        print(
            "Please enter the number of the movie you would like to remove from the list, or enter 0 to continue:"
        )
        remove = input()
        if remove == "0":
            break
        elif remove.isdigit() and int(remove) > 0 and int(remove) <= 5:
            # Add mid of the unwanted movie to the subset_unwanted list
            subset_unwanted.append(df.iloc[int(remove) - 1]["mid"])
            # Add mids of the other movies to the subset_wanted list
            for i in range(5):
                if i != int(remove) - 1:
                    subset_wanted.append(df.iloc[i]["mid"])

        query3 = """
        SELECT * FROM Recommended WHERE mid IN %s)
        UNION
        (SELECT * FROM Recommended WHERE mid NOT IN %s
        ORDER BY RAND() 
        LIMIT 1);
        """

        cursor = mydb.cursor()
        try:
            args = (tuple(subset_wanted), tuple(subset_unwanted))
            cursor.execute(query3, args)
            result_list = cursor.fetchall()
            df = pd.DataFrame(
                result_list, columns=["title", "rental_price", "duration"]
            )
        except mysql.connector.Error as error:
            print("There was an error in selecting from the view:")
            print(error)
        finally:
            cursor.close()

        print(f"Recommended movies of genre {genre} for {username}:")
        count = 1

        print("Title Rental_Price Duration")

        for val in df.values:
            print(f"{count}. {val[0]} {val[1]} {val[2]}")
            count += 1

    # Drop the view
    query4 = "DROP VIEW Recommended;"
    cursor = mydb.cursor()
    try:
        cursor.execute(query4)
    except mysql.connector.Error as error:
        print("There was an error in dropping the Recommended view:")
        print(error)
    finally:
        cursor.close()
