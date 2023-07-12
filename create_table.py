import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()  # load variables from .env file

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")


# Connect to the database
cnx = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

cursor = cnx.cursor()

# If tables exist, drop them
cursor.execute('DROP TABLE IF EXISTS Rental;')
cursor.execute('DROP TABLE IF EXISTS Review;')
cursor.execute('DROP TABLE IF EXISTS User;')
cursor.execute('DROP TABLE IF EXISTS Movie;')

# Create new tables
cursor.execute('''
    CREATE TABLE Movie (
        mid INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        title VARCHAR(250) NOT NULL,
        genre VARCHAR(30) NOT NULL,
        release_year INT NOT NULL, /* YYYY */
        duration INT NOT NULL, /* minutes */
        rental_price DECIMAL(5, 2) NOT NULL DEFAULT 9.99, /* Default price is $9.99 */
        rental_quantity INT NOT NULL DEFAULT 10,
        CONSTRAINT chk_rental_quantity CHECK (rental_quantity >= 0)
    );
''')

cursor.execute('''
    CREATE TABLE User (
        uid INT NOT NULL AUTO_INCREMENT,
        username VARCHAR(50) UNIQUE NOT NULL,
        password VARCHAR(30) NOT NULL,
        wallet DECIMAL(7, 2) NOT NULL DEFAULT 500.00,
        CONSTRAINT chk_wallet CHECK (wallet >= 0),
        PRIMARY KEY (uid)
    );
''')

cursor.execute('''
    CREATE TABLE Review (
        uid INT NOT NULL REFERENCES User(uid),
        mid INT NOT NULL REFERENCES Movie(mid),
        review_date DATE NOT NULL,
        rating INT NOT NULL CHECK(rating BETWEEN 1 and 5),
        comment VARCHAR(500),
        PRIMARY KEY(uid, mid)
    );
''')

cursor.execute('''
    CREATE TABLE Rental (
        uid INT NOT NULL REFERENCES User(uid),
        mid INT NOT NULL REFERENCES Movie(mid),
        rent_date DATE NOT NULL, /* 'YYYY-MM-DD' */
        due_date DATE NOT NULL, /* Standard rent period is 2 weeks */
        is_active INT NOT NULL, /* 1 if rental is currently active, otherwise 0 */
        PRIMARY KEY(uid, mid)
    );
''')

# Triggers
cursor.execute('''
    CREATE TRIGGER DelUserReview AFTER DELETE ON user FOR EACH ROW DELETE FROM review WHERE uid = OLD.uid;
''')
cursor.execute('''
    CREATE TRIGGER DelUserRental AFTER DELETE ON user FOR EACH ROW DELETE FROM rental WHERE uid = OLD.uid;
''')
cursor.execute('''
    CREATE TRIGGER UpdateRentalQuantity AFTER DELETE ON rental FOR EACH ROW UPDATE movie SET rental_quantity = rental_quantity + 1 WHERE mid = OLD.mid AND OLD.is_active = 1;
''')

# Commit changes and close connection
cnx.commit()
cursor.close()
cnx.close()
