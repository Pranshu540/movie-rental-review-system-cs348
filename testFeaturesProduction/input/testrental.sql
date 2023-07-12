# User 'batman' (uID = 2) wants to rent out 'Avatar' (mID = 9)
SELECT rental_price FROM Movie WHERE mid = 9

UPDATE Movie SET rental_quantity = rental_quantity - 1 WHERE mid = 9

UPDATE User SET wallet = wallet - {rental_price} WHERE uid = 2

INSERT INTO Rental (uid, mid, rent_date, due_date, is_active) VALUES (2, 9, date.today(), date.today() + timedelta(weeks=2), 1)"

