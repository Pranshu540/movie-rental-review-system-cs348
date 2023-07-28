#=====Test Filters=====
SELECT * FROM Movie WHERE title LIKE "%The%" AND rental_quantity >= 1 AND genre = 'Drama';
SELECT * FROM Movie WHERE rental_quantity >= 10 AND genre = "Sci-Fi";

#=====Test Rentals=====
SELECT rental_price FROM Movie WHERE mid = 9;

UPDATE Movie SET rental_quantity = rental_quantity - 1 WHERE mid = 9;

UPDATE User SET wallet = wallet - 10 WHERE uid = 2;

INSERT INTO Rental (uid, mid, rent_date, due_date, is_active) VALUES (2, 9, '2023-07-27', '2023-08-10', 1);

SELECT * FROM Rental;
SELECT * FROM User;
SELECT * FROM Movie;

#=====Test Review=====
# Print the review table
SELECT * FROM Review;

# Add a review from George for The Book Thief:
INSERT INTO Review VALUES(4, 10, '2023-06-22', 4, 'Teaches me how to steal books!');

# Print the updated review table
SELECT * FROM Review WHERE mid = 10;

# Modify the review on INSERT MOVIE HERE
UPDATE Review SET review_date = '2023-06-22', rating = 5, comment = 'This movie was absolutely amazing I wish I could live in it XD' WHERE uid = 4 AND mid = 10;

# Print the updated review table
SELECT * FROM Review WHERE mid = 10;

# Remove george's review on the book thief:
DELETE FROM Review WHERE uid = 4 AND mid = 10;

# Print the updated review table
SELECT * FROM Review WHERE mid = 10;

#=====Test User Auth=====
SELECT EXISTS(SELECT 1 FROM User WHERE username='HumbleGoat456' AND password='xKODPhDD');
SELECT EXISTS(SELECT 1 FROM User WHERE username='userName' AND password='userPassword');
INSERT INTO User(username, password) VALUES ('userName', 'userPassword');
SELECT EXISTS(SELECT 1 FROM User WHERE username='userName' AND password='userPassword');

#=====Test User Deletion=====
DELETE FROM User WHERE uid=4;

SELECT * FROM User;


#=====Test Recommended List Feature=====
SELECT m.genre FROM Rental r NATURAL JOIN Movie m WHERE r.uid = 1 GROUP BY m.genre ORDER BY count(m.genre) DESC LIMIT 1;

CREATE VIEW Recommended AS
    SELECT mid, title, rental_price, duration
    FROM Movie
    WHERE rental_quantity > 0
      AND genre = 'drama'
    ORDER BY RAND(100)
    LIMIT 200;

SELECT * FROM Recommended LIMIT 5;
