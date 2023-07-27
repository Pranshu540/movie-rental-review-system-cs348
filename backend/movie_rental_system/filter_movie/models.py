from decimal import Decimal


def filter_movies(title_filter, count_filter, genre_filter, mydb):
    filter_params = []
    cmd = "SELECT * FROM Movie"

    if title_filter:
        cmd += " WHERE title LIKE %s"
        filter_params.append("%" + title_filter + "%")

    if count_filter > 0:
        if title_filter:
            cmd += " AND"
        else:
            cmd += " WHERE"
        cmd += " rental_quantity >= %s"
        filter_params.append(count_filter)

    if genre_filter:
        if title_filter or count_filter:
            cmd += " AND"
        else:
            cmd += " WHERE"
        cmd += "  genre=%s"
        filter_params.append(genre_filter)

    try:
        cursor = mydb.cursor()
        cursor.execute(cmd, filter_params)

        rows = cursor.fetchall()
        col_names = [desc[0] for desc in cursor.description]

        my_result = [dict(zip(col_names, row)) for row in rows]
    except Exception as err:
        return "Something went wrong: {}".format(err)
    finally:
        cursor.close()
        return my_result
