import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password"
)

titleFilter = input("Enter Filter for Title: ")
while(True):
  countFilter = input("Enter Filter for Count: ")
  try:
    countFilter = int(countFilter)
    break
  except:
    print("Please enter a number.\n")

genreFilter = input("Enter Filter for Genre: ")
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
  mycursor = mydb.cursor()
  mycursor.execute("use sys")
  mycursor.execute(cmd, filterParams)

  myresult = mycursor.fetchall()
except mysql.connector.Error as err:
  print("Something went wrong: {}".format(err))


for x in myresult:
  print(x)