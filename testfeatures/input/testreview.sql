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