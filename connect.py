import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="abcde12345"
)

print(mydb)

mycursor = mydb.cursor()
mycursor.execute("use sys")
mycursor.execute("SELECT * FROM movie")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)