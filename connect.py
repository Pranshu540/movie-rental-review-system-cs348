import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password"
)

def filter_movies(titleFilter, countFilter, genreFilter):
  filterParams = []
  cmd = "SELECT * FROM Movie"

  if titleFilter: 
   cmd += " WHERE title LIKE %s"
   filterParams.append("%" + titleFilter + "%")

  if countFilter > 0:
    if titleFilter:
      cmd += " AND"
    else:
      cmd += " WHERE"
    cmd += " rental_quantity >= %s"
    filterParams.append(countFilter)

  if genreFilter:
    if titleFilter or countFilter:
      cmd += " AND"
    else:
      cmd += " WHERE"
    cmd += "  genre=%s"
    filterParams.append(genreFilter)

  try: 
    cursor = mydb.cursor()
    cursor.execute("use sys")
    cursor.execute(cmd, filterParams)

    myresult = cursor.fetchall()
  except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))
  finally:
    cursor.close()
    return myresult