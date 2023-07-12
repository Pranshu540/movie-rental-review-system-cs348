#=====Movie filter=====
SELECT * FROM Movie WHERE title LIKE ‘%The%’ AND rental_quantity >= 1 AND genre = ‘Drama’
SELECT * FROM Movie WHERE rental_quantity >= 10 AND genre = ‘Sci-Fi’

#=====Movie rental=====
SELECT rental_price FROM Movie WHERE mid = 9;

UPDATE Movie SET rental_quantity = rental_quantity - 1 WHERE mid = 9;

UPDATE User SET wallet = wallet - {rental_price} WHERE uid = 2;

INSERT INTO Rental (uid, mid, rent_date, due_date, is_active) VALUES (2, 9, date.today(), date.today() + timedelta(weeks=2), 1);

#=====Movie review=====
# Print the review table
SELECT * FROM Review;

# Add a review from George for The Book Thief:
INSERT INTO Review VALUES(4, 10, '2023-06-22', 4, 'Teaches me how to steal books!');

# Print the updated review table
SELECT * FROM Review;

# Modify the review from Batman on The Amazing Spider-Man:
UPDATE Review SET review_date = '2023-06-22', rating = 5, comment = 'Across the Spiderverse changed my mind' WHERE uid = 2 AND mid = 3;

# Print the updated review table
SELECT * FROM Review;

# Remove george's review on the book thief:
DELETE FROM Review WHERE uid = 4 AND mid = 10;

# Print the updated review table
SELECT * FROM Review;

#=====Test User Auth=====
SELECT EXISTS(SELECT 1 FROM User WHERE username='movielover123' AND password=’Secret48!’);
SELECT EXISTS(SELECT 1 FROM User WHERE username='userName' AND password=’userPassword’);
INSERT INTO Users(username, password) VALUES ('userName', 'userPassword');
SELECT EXISTS(SELECT 1 FROM User WHERE username='userName' AND password=’userPassword’);

